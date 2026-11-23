"""Engine checks that run offline on Python 3.9+: python -m unittest discover tests"""
import json, shutil, socket, subprocess, sys, tempfile, time, unittest, urllib.error
from pathlib import Path
from unittest import mock

ENGINE = Path(__file__).resolve().parent.parent / 'engine'
sys.path.insert(0, str(ENGINE))
import core
from server import FileStore

LINK_LIVE = core._link_live  # the real check; the tests below replace core._link_live so nothing goes online
PRODUCT = 'https://example.com/'
POST = 'https://www.threads.com/@yourbrand/post/C0ffee123'


class EngineTest(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.mkdtemp(prefix='nuluno-test-')
        self.store = FileStore(self.folder)
        patcher = mock.patch.object(core, '_link_live', lambda url: True)  # no network unless a test says so
        patcher.start(); self.addCleanup(patcher.stop)
        self.addCleanup(shutil.rmtree, self.folder, True)

    def call(self, tool, **args):
        return core.TOOLS[tool](self.store, 'test', PRODUCT, args)

    def submit(self, step, **extra):
        args = {'step_id': step['step_id'], 'output': {key: 'x ' + key for key in step['deliver']}}
        if step.get('publishes'): args['links'] = [POST]
        args.update(extra)
        return self.call('submit_step', **args)

    def walk(self, until, values=None):
        """Hand in steps until until(step) is true; numbers steps get values (or ones)."""
        step = self.call('next_step')
        for _ in range(80):
            if until(step): return step
            if step.get('call'):
                answer = self.call('record_numbers', values=values or {p: 1 for p in step['values_needed']}, source='test')
            else:
                answer = self.submit(step)
            self.assertTrue(answer['accepted'], answer)
            step = answer['next']
        self.fail('the playbook never reached the wanted step')

    def end_window(self):
        state = self.store.load('test'); state['wait_until'] = time.time() - 1; self.store.save('test', state)

    def miss_round(self):
        self.walk(lambda s: s['state'] == 'waiting_for_results', {'link_clicks': 1, 'views': 100})
        self.end_window()
        answer = self.call('record_numbers', values={'link_clicks': 1, 'views': 100}, source='test')
        self.assertFalse(answer['reached'])
        return answer['next']

    # ---- steps ----

    def test_missing_field_refused(self):
        step = self.call('set_goal', goal_id='G-TH-LINK-RATE')['next']
        answer = self.call('submit_step', step_id=step['step_id'], output={step['deliver'][0]: 'facts'})
        self.assertFalse(answer['accepted'])
        self.assertIn('Deliverables missing', answer['error'])
        answer = self.call('submit_step', step_id=step['step_id'], output={key: '' for key in step['deliver']})
        self.assertFalse(answer['accepted'])

    def test_out_of_order_step_refused(self):
        step = self.call('set_goal', goal_id='G-TH-LINK-RATE')['next']
        answer = self.call('submit_step', step_id='some-later-step:r1', output={'anything': 'x'})
        self.assertFalse(answer['accepted'])
        self.assertEqual(answer['next']['step_id'], step['step_id'])

    def test_missed_round_opens_round_two(self):
        self.call('set_goal', goal_id='G-TH-LINK-RATE', target=0.5)
        step = self.miss_round()
        self.assertEqual(step['state'], 'target_missed_choose_one_change')
        answer = self.call('submit_step', step_id=step['step_id'], output={'bottleneck': 'angle', 'reason': 'views held, clicks fell', 'one_change': 'Lead with the price'})
        self.assertTrue(answer['accepted'], answer)
        self.assertEqual(self.store.load('test')['round'], 2)
        self.assertIn('round 2', answer['next']['progress'])

    def test_repeated_change_refused_and_listed(self):
        self.call('set_goal', goal_id='G-TH-LINK-RATE', target=0.5)
        step = self.miss_round()
        self.call('submit_step', step_id=step['step_id'], output={'bottleneck': 'angle', 'reason': 'r', 'one_change': 'Lead with the price'})
        step = self.miss_round()
        self.assertEqual(step['already_tried'], ['Lead with the price'])
        answer = self.call('submit_step', step_id=step['step_id'], output={'bottleneck': 'angle', 'reason': 'r', 'one_change': 'lead with  the PRICE.'})
        self.assertFalse(answer['accepted'])
        self.assertIn('already tried', answer['error'])
        answer = self.call('submit_step', step_id=step['step_id'], output={'bottleneck': 'message', 'reason': 'r', 'one_change': 'Shorter first line'})
        self.assertTrue(answer['accepted'])

    # ---- publishing ----

    def publish_step(self):
        self.call('set_goal', goal_id='G-TH-LINK-RATE')
        return self.walk(lambda s: s.get('publishes'))

    def test_profile_link_refused_for_threads_post(self):
        step = self.publish_step()
        with mock.patch.object(core, '_link_live', side_effect=AssertionError('a profile is refused before any request')):
            for link in ('https://www.threads.com/@yourbrand', 'https://www.threads.net/', 'https://www.threads.com/search?q=x'):
                answer = self.submit(step, links=[link])
                self.assertFalse(answer['accepted'], link)
                self.assertIn('not a single post', answer['error'])

    def test_link_that_does_not_exist_refused(self):
        step = self.publish_step()
        with mock.patch.object(core, '_link_live', lambda url: False):
            answer = self.submit(step)
        self.assertFalse(answer['accepted'])
        self.assertIn('does not exist', answer['error'])

    def test_robot_blocked_link_accepted(self):
        step = self.publish_step()
        with mock.patch.object(core, '_link_live', lambda url: 'blocked'):
            answer = self.submit(step)
        self.assertTrue(answer['accepted'], answer)
        self.assertEqual(answer['link_read_back'], 'blocked')

    def test_post_patterns(self):
        posts = ['https://x.com/a/status/1', 'https://www.reddit.com/r/a/comments/abc/t/', 'https://www.instagram.com/reel/Cx1/',
                 'https://www.tiktok.com/@a/video/1', 'https://www.youtube.com/watch?v=abc', 'https://youtu.be/dQw4w9WgXcQ',
                 'https://www.linkedin.com/posts/jane_x-activity-1', 'https://www.pinterest.com/pin/1/', 'https://www.facebook.com/groups/g/posts/1/',
                 'https://www.producthunt.com/products/x', 'https://example.com/blog/launch', 'https://www.reddit.com/r/x/s/AbCd123',
                 'https://www.tiktok.com/t/ZT8abc/', 'https://www.facebook.com/share/p/1AbCdEf/', 'https://www.facebook.com/reel/123',
                 'https://www.youtube.com/live/abcDEF', 'https://youtu.be/abc', 'https://fb.watch/abc/', 'https://www.threads.com/@notavue/post/Df_xw73E3F1']
        pages = ['https://x.com/a', 'https://old.reddit.com/r/a/', 'https://www.instagram.com/a/', 'https://www.tiktok.com/@a',
                 'https://www.youtube.com/@a', 'https://www.linkedin.com/company/a/posts/', 'https://www.pinterest.com/a/',
                 'https://www.facebook.com/a', 'https://www.producthunt.com/']
        for url in posts: self.assertIsNone(core._not_a_post(url), url)
        for url in pages: self.assertIsNotNone(core._not_a_post(url), url)

    def test_link_live_outcomes(self):
        public = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('93.184.215.14', 443))]
        page = b'<html><title>Post</title><body><p>' + b'words ' * 100 + b'</p></body></html>'
        cases = [((200, 'text/html', page, POST), True), ((404, '', b'', POST), False), ((410, '', b'', POST), False),
                 ((403, '', b'', POST), 'blocked'), ((429, '', b'', POST), 'blocked'), ((999, '', b'', POST), 'blocked'),
                 ((200, 'text/html', b'<html><title>Threads</title></html>', POST), 'blocked'),
                 ((200, 'text/html', page, 'https://www.threads.com/login?next=x'), 'blocked')]
        with mock.patch.object(socket, 'getaddrinfo', return_value=public):
            for answer, expected in cases:
                with mock.patch.object(core, 'fetch_public', return_value=answer):
                    self.assertEqual(LINK_LIVE(POST), expected, answer[:2])
            refused = urllib.error.URLError(ConnectionRefusedError(61, 'refused'))
            with mock.patch.object(core, 'fetch_public', side_effect=refused): self.assertIs(LINK_LIVE(POST), False)
            with mock.patch.object(core, 'fetch_public', side_effect=urllib.error.URLError(socket.timeout('timed out'))):
                self.assertEqual(LINK_LIVE(POST), 'blocked')
        with mock.patch.object(socket, 'getaddrinfo', side_effect=socket.gaierror(8, 'nodename nor servname provided')):
            self.assertIs(LINK_LIVE(POST), False)

    # ---- waiting on the owner ----

    def test_blocked_numbers_step_waits_on_owner(self):
        self.call('set_goal', goal_id='G-TH-LINK-RATE')
        step = self.walk(lambda s: s.get('call') == 'record_numbers')
        self.assertIn('other_numbers', step)
        answer = self.call('submit_step', step_id=step['step_id'], status='blocked', needs='Read link clicks and views for the last 6 posts in Threads Insights.')
        self.assertTrue(answer['accepted'], answer)
        self.assertEqual(answer['next']['state'], 'waiting_on_owner')
        status = self.call('where_are_we')
        self.assertEqual(status['state'], 'waiting_on_owner')
        self.assertIn('Threads Insights', status['tell_the_owner'])
        self.assertIsNotNone(status['waiting_on_owner'])
        nxt = self.call('next_step')
        self.assertEqual(nxt['state'], 'waiting_on_owner')
        self.assertEqual(nxt['step_id'], step['step_id'])
        self.call('record_numbers', values={'link_clicks': 3, 'views': 90}, source='owner read Threads Insights')
        self.assertEqual(self.call('where_are_we')['state'], 'working')

    def test_blocked_without_needs_still_says_next(self):
        step = self.call('set_goal', goal_id='G-TH-LINK-RATE')['next']
        answer = self.call('submit_step', step_id=step['step_id'], status='blocked', needs='  ')
        self.assertFalse(answer['accepted'])
        self.assertIn('next', answer)

    # ---- reading ----

    def test_read_page_refuses_private_addresses(self):
        for url in ('https://127.0.0.1/', 'https://10.0.0.1/admin', 'http://example.com/', 'https://user@example.com/'):
            answer = self.call('read_page', url=url)
            self.assertFalse(answer['read'], url)

    def test_read_page_little_text(self):
        page = b'<!DOCTYPE html><html><head><title>Log in</title></head><body><div id="root"></div></body></html>'
        with mock.patch.object(core, 'fetch_public', return_value=(200, 'text/html', page, 'https://example.com/login')):
            answer = self.call('read_page', url='https://example.com/login')
        self.assertTrue(answer['read'])
        self.assertTrue(answer['little_text'])
        self.assertNotIn('DOCTYPE', answer['text'])
        self.assertIn('paste', answer['note'])

    def test_goal_status_label(self):
        self.assertIn(core.goal_status('G-TH-LINK-RATE'), ('tried_on_a_live_product', 'english', 'english_and_chinese'))
        self.assertNotIn('running_on_a_live_product', json.dumps(self.call('where_are_we')))


class HookStore(FileStore):
    """A store with the optional month target hooks, answering what each test sets."""
    limit = None; paid = None; clicks = None; lane_clicks = {}
    def lane_limit(self, owner): return self.limit if self.limit is not None else 5
    def paid_since(self, owner, start): return self.paid
    def clicks_since(self, owner, start):
        if '#lane:' in owner: return self.lane_clicks.get(owner.split('#lane:')[1])
        return self.clicks


LANES = ['G-TH-LINK-RATE', 'G-RD-PURCHASES', 'G-META-PURCHASE-CPA']


class MonthTargetTest(EngineTest):
    def setUp(self):
        super().setUp()
        self.store = HookStore(self.folder)

    def start(self, lanes=LANES, **target):
        answer = self.call('set_month_target', **dict({'amount': 100, 'days': 30}, **target))
        self.assertTrue(answer['accepted'], answer)
        plan = self.call('plan_month', lanes=lanes)
        self.assertTrue(plan['accepted'], plan)
        return plan

    def walk_lane(self, lane, until, values=None):
        step = self.call('next_step', lane=lane)
        for _ in range(80):
            if until(step): return step
            if step.get('call'): answer = self.call('record_numbers', lane=lane, values=values or {p: 1 for p in step['values_needed']}, source='test')
            elif step.get('publishing'): answer = self.publish_approved(lane, step)
            else: answer = self.submit(step, lane=lane)
            self.assertTrue(answer['accepted'], answer)
            step = answer['next']
        self.fail('the lane never reached the wanted step')

    def publish_approved(self, lane, step):
        """A lane step that publishes or sends: the owner approves the exact text in a batch, then it is published with approved_item."""
        text = 'Approved text for %s' % step['step_id']
        batch_id, item = self.batch(text, lane)
        self.assertTrue(core.approve_batch(self.store, 'test', batch_id, [item], 'test owner')['approved'])
        output = {key: 'x ' + key for key in step['deliver']}; output[step['deliver'][0]] = text
        return self.submit(step, lane=lane, output=output, approved_item=item)

    def end_lane_window(self, lane):
        key = core.lane_owner('test', lane); state = self.store.load(key); state['wait_until'] = time.time() - 1; self.store.save(key, state)

    def test_target_refusals(self):
        for bad in ({'amount': 0}, {'amount': -5}, {'amount': 100, 'days': 6}, {'amount': 100, 'days': 91}, {'amount': 100, 'days': 30.5},
                    {'amount': 390000, 'kind': 'revenue_minor'}, {'amount': 100, 'kind': 'visits'}):
            self.assertFalse(self.call('set_month_target', **bad)['accepted'], bad)
        self.assertFalse(self.call('plan_month', lanes=LANES)['accepted'])  # no target yet
        self.assertTrue(self.call('set_month_target', amount=100)['accepted'])
        self.assertFalse(self.call('set_month_target', amount=50)['accepted'])  # one is already open
        self.assertTrue(self.call('set_month_target', amount=50, replace=True)['accepted'])
        self.assertFalse(self.call('plan_month', lanes=['G-NOPE'])['accepted'])
        self.assertFalse(self.call('plan_month', lanes=LANES + LANES[:1])['accepted'])

    def test_funnel_math(self):
        plan = self.start()
        need = plan['plan']['needed_per_day']
        self.assertEqual(need['visits_per_day'], 167)  # 100 paid / 30 days at 2% of visits
        self.assertAlmostEqual(need['paid_per_day'], 3.33, places=2)
        self.assertEqual(plan['plan']['funnel']['visit_to_paid']['basis'], 'assumed')
        quotas = plan['plan']['daily_visit_quota_per_lane']
        self.assertEqual(sum(quotas.values()), 167); self.assertEqual(sorted(quotas.values()), [55, 56, 56])
        self.assertIn('167 visits a day', plan['tell_the_owner'])
        for lane in LANES: self.assertEqual(self.call('where_are_we', lane=lane)['goal']['goal_id'], lane)
        self.assertEqual(self.call('set_month_target', amount=100, current_paid=10, replace=True)['month_target']['status'], 'planning')
        plan = self.call('plan_month', lanes=LANES)
        self.assertEqual(plan['plan']['needed_per_day']['visits_per_day'], 150)  # 90 left / 30 days at 2%
        self.call('set_month_target', amount=100, replace=True)
        plan = self.call('plan_month', lanes=LANES, funnel={'visit_to_signup': 0.1, 'signup_to_paid': {'value': 0.2, 'source': 'Stripe: 20 of 100 trials paid'}})
        self.assertEqual(plan['plan']['needed_per_day']['visits_per_day'], 167)
        self.assertEqual(plan['plan']['needed_per_day']['signups_per_day'], 17)
        self.assertEqual(plan['plan']['funnel']['signup_to_paid']['basis'], 'measured')
        self.assertEqual(plan['plan']['funnel']['visit_to_paid']['basis'], 'assumed')  # one of the two layers is assumed
        self.store.paid, self.store.clicks = {'count': 10, 'revenue_minor': 39000, 'source': 'Stripe'}, 1000
        status = self.call('month_status')
        self.assertEqual(status['paid']['total'], 10); self.assertEqual(status['paid']['source'], 'Stripe')
        self.assertEqual(status['funnel']['visit_to_paid']['basis'], 'measured'); self.assertAlmostEqual(status['funnel']['visit_to_paid']['value'], 0.01)
        self.assertEqual(status['needed_per_day']['visits_per_day'], 300)  # 90 left / 30 days at the measured 1%
        self.assertFalse(self.call('plan_month', lanes=LANES, funnel={'visit_to_paid': 2})['accepted'])

    def test_revenue_target(self):
        self.call('set_month_target', amount=390000, kind='revenue_minor', price=39, currency='USD')
        plan = self.call('plan_month', lanes=LANES[:1])
        self.assertEqual(plan['plan']['remaining_customers'], 100)
        self.assertEqual(plan['plan']['needed_per_day']['visits_per_day'], 167)

    def test_lanes_are_separate(self):
        self.call('set_goal', goal_id='G-X-LINK-RATE')  # the goal without lanes keeps working on its own
        self.start()
        step = self.call('next_step', lane=LANES[0])
        self.assertTrue(self.submit(step, lane=LANES[0])['accepted'])
        self.assertEqual(self.store.load(core.lane_owner('test', LANES[0]))['cursor'], 1)
        self.assertEqual(self.store.load(core.lane_owner('test', LANES[1]))['cursor'], 0)
        plain = self.call('where_are_we')
        self.assertEqual(plain['goal']['goal_id'], 'G-X-LINK-RATE'); self.assertEqual(self.store.load('test')['cursor'], 0)
        self.assertEqual(plain['month_target']['call'], 'month_status')
        self.assertIn('lane', self.call('next_step', lane='G-X-LINK-RATE')['error'])  # not a lane of this month target
        self.assertFalse(self.call('set_goal', lane=LANES[0], goal_id='G-X-LINK-RATE')['accepted'])
        status = self.call('month_status')
        self.assertEqual(status['next']['lane'], LANES[1])  # lanes not worked on yet come first
        self.assertEqual(status['next']['arguments'], {'lane': LANES[1]})
        self.assertEqual([v['lane'] for v in status['lanes']], LANES)

    def test_lane_limit_hook(self):
        self.store.limit = 1
        self.call('set_month_target', amount=100)
        answer = self.call('plan_month', lanes=LANES)
        self.assertFalse(answer['accepted']); self.assertEqual(answer['lane_limit'], 1)
        self.assertTrue(self.call('plan_month', lanes=LANES[:1])['accepted'])
        self.store = FileStore(tempfile.mkdtemp(dir=self.folder))  # a store without any hook: the default is 5 lanes
        self.call('set_month_target', amount=10)
        self.assertTrue(self.call('plan_month', lanes=LANES + ['G-EM-PURCHASE', 'G-X-LINK-RATE'])['accepted'])
        self.assertEqual(self.call('month_status')['paid']['since_start'], 0)
        self.assertFalse(self.call('plan_month', lanes=LANES + ['G-EM-PURCHASE', 'G-X-LINK-RATE', 'G-IG-LINK-RATE'])['accepted'])

    def test_daily_window(self):
        goal = core.goals()[LANES[0]]
        self.assertGreater(goal.get('observation_seconds', 172800), 86400)
        self.start()
        self.walk_lane(LANES[0], lambda s: s['state'] == 'waiting_for_results')
        state = self.store.load(core.lane_owner('test', LANES[0]))
        self.assertAlmostEqual(state['wait_until'] - state['published_at'], 86400, delta=1)
        self.call('set_goal', goal_id=LANES[0])  # the same goal outside the month target keeps its own window
        self.walk(lambda s: s['state'] == 'waiting_for_results')
        state = self.store.load('test')
        self.assertAlmostEqual(state['wait_until'] - state['published_at'], goal.get('observation_seconds', 172800), delta=1)

    def batch(self, text='Our new pricing page is live: https://example.com/', lane=LANES[0]):
        answer = self.call('submit_batch', items=[{'lane': lane, 'kind': 'post', 'channel': 'threads', 'text': text, 'when': 'Mon 09:00'}])
        self.assertTrue(answer['accepted'], answer)
        return answer['batch_id'], answer['batch_id'] + '-1'

    def test_batch_only_the_owner_approves(self):
        self.start()
        self.assertFalse(self.call('submit_batch', items=[{'lane': 'G-X-LINK-RATE', 'kind': 'post', 'channel': 'x', 'text': 't'}])['accepted'])
        self.assertFalse(self.call('submit_batch', items=[{'lane': LANES[0], 'kind': 'post', 'channel': 'threads', 'text': 't'}] * 51)['accepted'])
        batch_id, item = self.batch()
        self.assertIn('cannot approve', self.call('submit_batch', items=[{'lane': LANES[0], 'kind': 'post', 'channel': 'threads', 'text': 'x'}])['approval_needed']['rule'])
        self.assertEqual(self.call('batch_status')['batches'][-1]['items'][0]['state'], 'awaiting_owner')
        self.assertFalse([name for name in core.TOOLS if 'approve' in name])
        self.assertFalse([spec['name'] for spec in core.TOOL_SPECS if 'approve' in spec['name']])
        self.assertEqual(self.call('month_status')['pending_approvals'][0]['batch_id'], batch_id)
        self.assertFalse(core.approve_batch(self.store, 'test', 'B99', 'all', 'owner')['approved'])
        answer = core.approve_batch(self.store, 'test', batch_id, 'all', 'owner page')
        self.assertTrue(answer['approved']); self.assertEqual(answer['approved_items'], [item])
        self.assertEqual(self.call('batch_status')['batches'][-1]['items'][0]['state'], 'approved')

    def test_approved_item_counts_as_owner_approval(self):
        self.start()
        text = 'Our new pricing page is live: https://example.com/'
        batch_id, item = self.batch(text)
        step = self.walk_lane(LANES[0], lambda s: s.get('publishes'))
        self.assertIn('approved_item', step['batch_approval'])
        output = {key: 'x ' + key for key in step['deliver']}; output[step['deliver'][0]] = text
        answer = self.submit(step, lane=LANES[0], output=output, approved_item=item)
        self.assertFalse(answer['accepted']); self.assertIn('not approved', answer['error'])  # still waiting for the owner
        core.approve_batch(self.store, 'test', batch_id, [item], 'owner page')
        self.assertEqual(self.call('next_step', lane=LANES[0])['approved_items'][0]['id'], item)
        answer = self.submit(step, lane=LANES[0], output=dict(output, **{step['deliver'][0]: text + ' Buy now!'}), approved_item=item)
        self.assertFalse(answer['accepted']); self.assertIn('word for word', answer['error'])  # changed text
        answer = self.submit(step, lane=LANES[1], output=output, approved_item=item)
        self.assertFalse(answer['accepted'])  # another lane
        answer = self.submit(step, lane=LANES[0], output=dict(output, **{step['deliver'][0]: '  Our new pricing page is live:\n https://example.com/ '}), approved_item=item)
        self.assertTrue(answer['accepted'], answer); self.assertIn(batch_id, answer['owner_approval'])
        logged = self.store.outputs(core.lane_owner('test', LANES[0]), 1)[0]['content']
        self.assertEqual(logged['owner_approved_item']['id'], item)
        self.assertEqual(self.call('batch_status')['batches'][-1]['items'][0]['state'], 'used')
        self.assertFalse(self.call('submit_step', step_id='x', approved_item=item)['accepted'])  # needs lane

    def test_lane_publishing_requires_approved_item(self):
        self.start()
        step = self.walk_lane(LANES[0], lambda s: s.get('publishes'))
        self.assertIn('Required on a month target lane', step['batch_approval']); self.assertIn('nuluno.py approve', step['batch_approval'])
        self.assertNotIn('Show the owner the exact text first', step['publishing'])
        self.assertEqual(step['approved_items'], [])
        self.assertFalse(self.submit(step, lane=LANES[0], approved_item='B1-1')['accepted'])
        answer = self.submit(step, lane=LANES[0])  # published without an approved item: refused, nothing recorded
        self.assertFalse(answer['accepted']); self.assertTrue(answer['approved_item_required'])
        for words in ('submit_batch', 'owner page', 'nuluno.py approve', 'approved_item', 'blocked'): self.assertIn(words, answer['error'])
        self.assertEqual(answer['next']['step_id'], step['step_id']); self.assertIn('batch_approval', answer['next'])
        cursor = self.store.load(core.lane_owner('test', LANES[0]))['cursor']
        blocked = self.submit(step, lane=LANES[0], status='blocked', needs='Approve batch B1 on your owner page.')
        self.assertTrue(blocked['accepted'], blocked); self.assertEqual(blocked['state'], 'waiting_on_owner')  # blocked is still allowed
        self.assertEqual(self.store.load(core.lane_owner('test', LANES[0]))['cursor'], cursor)
        answer = self.publish_approved(LANES[0], step)
        self.assertTrue(answer['accepted'], answer)
        self.assertIn('owner_approval', answer)
        self.assertEqual(self.store.outputs(core.lane_owner('test', LANES[0]), 1)[-1]['content']['owner_approved_item']['approved_by'], 'test owner')

    def test_sending_step_requires_approved_item(self):
        lane = 'G-TH-INTENT'  # its reply step sends something without a post link
        self.start(lanes=[lane])
        step = self.walk_lane(lane, lambda s: s.get('publishing') and not s.get('publishes'))
        answer = self.submit(step, lane=lane)
        self.assertFalse(answer['accepted']); self.assertTrue(answer['approved_item_required'])
        self.assertTrue(self.publish_approved(lane, step)['accepted'])

    def test_outside_a_month_target_publishing_is_unchanged(self):
        self.call('set_goal', goal_id=LANES[0])
        step = self.walk(lambda s: s.get('publishes'))
        self.assertNotIn('batch_approval', step)
        self.assertTrue(self.submit(step)['accepted'])

    def test_ad_budget_cap_flag(self):
        ads = LANES[2]
        self.start()
        self.assertIn('request_ad_budget', self.call('next_step', lane=ads)['ad_budget']['rule'])
        self.assertFalse(self.call('request_ad_budget', daily_cap=0, currency='USD', channels=['meta_ads'])['accepted'])
        self.assertEqual(self.call('request_ad_budget', daily_cap=10, currency='usd', channels=['meta_ads'])['status'], 'awaiting_owner')
        self.assertFalse(self.call('next_step', lane=ads)['ad_budget']['approved'])
        self.assertTrue(core.approve_ad_budget(self.store, 'test', 'owner page')['approved'])
        self.assertEqual(self.call('next_step', lane=ads)['ad_budget']['daily_cap'], 10)
        self.walk_lane(ads, lambda s: s['state'] == 'waiting_for_results', {'spend_minor': 500, 'external_purchases': 1})
        self.end_lane_window(ads)
        answer = self.call('record_numbers', lane=ads, values={'spend_minor': 900, 'external_purchases': 1}, source='Ads Manager')
        self.assertTrue(answer['accepted']); self.assertNotIn('over_budget', answer)  # 9.00 within 1 day x 10.00
        self.walk_lane(ads, lambda s: s['state'] in ('waiting_for_results', 'target_missed_choose_one_change', 'goal_reached'))
        self.assertEqual(self.store.load(core.lane_owner('test', ads))['status'], 'diagnose')  # 9.00 per purchase is worse than 5.00
        self.assertTrue(self.call('submit_step', lane=ads, step_id='diagnose:r1', output={'bottleneck': list(core.goals()[ads]['bottleneck_routes'])[0], 'reason': 'r', 'one_change': 'c'})['accepted'])
        self.walk_lane(ads, lambda s: s['state'] == 'waiting_for_results')
        self.end_lane_window(ads)
        answer = self.call('record_numbers', lane=ads, values={'spend_minor': 5000, 'external_purchases': 1}, source='Ads Manager')
        self.assertTrue(answer['accepted']); self.assertTrue(answer['over_budget'])  # accepted, and flagged
        status = self.call('month_status')
        self.assertEqual(list(status)[0], 'alerts'); self.assertEqual(status['alerts'][0]['lane'], ads)

    def test_month_numbers_and_end(self):
        self.start()
        step = self.walk_lane(LANES[0], lambda s: s.get('call'))
        answer = self.call('record_numbers', lane=LANES[0], values=dict({p: 1 for p in step['values_needed']}, paid_customers=4, visits=300), source='Stripe dashboard 23 Nov')
        self.assertEqual(answer['month_numbers_recorded'], ['paid_customers', 'visits'])
        status = self.call('month_status')
        self.assertEqual(status['paid']['total'], 4); self.assertIn('Stripe dashboard', status['paid']['source'])
        self.assertEqual(status['visits']['count'], 300)
        self.store.paid = {'count': 100, 'revenue_minor': 0, 'source': 'Stripe'}
        status = self.call('month_status')
        self.assertEqual(status['state'], 'reached'); self.assertTrue(status['result']['reached']); self.assertIsNone(status['next']['lane'])
        self.assertEqual(len(status['result']['per_lane']), 3)
        self.store.paid = None
        self.call('set_month_target', amount=100, replace=True)  # a reached target can be followed by a new one
        self.call('plan_month', lanes=LANES[:1])
        record = self.store.load('test#campaign'); record['target']['end'] = time.time() - 1; self.store.save('test#campaign', record)
        status = self.call('month_status')
        self.assertEqual(status['state'], 'ended'); self.assertFalse(status['result']['reached'])
        self.assertFalse(self.call('submit_batch', items=[{'lane': LANES[0], 'kind': 'post', 'channel': 't', 'text': 't'}])['accepted'])

    def test_split_follows_clicks_after_three_days(self):
        self.start()
        record = self.store.load('test#campaign'); record['running_since'] -= 4 * 86400; self.store.save('test#campaign', record)
        self.store.lane_clicks = {LANES[0]: 30, LANES[1]: 10, LANES[2]: 0}
        status = self.call('month_status')
        quotas = {v['lane']: v['today_visit_quota'] for v in status['lanes']}
        self.assertEqual(quotas, {LANES[0]: 125, LANES[1]: 42, LANES[2]: 0}); self.assertIn('proportional', status['split'])

    def test_without_lane_nothing_changes(self):
        self.assertNotIn('month_target', self.call('where_are_we'))
        self.assertEqual(self.call('month_status')['state'], 'no_month_target')
        self.assertEqual(self.call('batch_status')['batches'], [])
        names = {spec['name'] for spec in core.TOOL_SPECS}
        self.assertEqual(names, set(core.TOOLS))
        for spec in core.TOOL_SPECS:
            if spec['name'] in core.GOAL_TOOLS: self.assertIn('lane', spec['inputSchema']['properties'])


class CommandLineTest(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.mkdtemp(prefix='nuluno-cli-')
        self.addCleanup(shutil.rmtree, self.folder, True)

    def run_cli(self, *args):
        done = subprocess.run([sys.executable, str(ENGINE / 'nuluno.py')] + list(args), stdin=subprocess.DEVNULL, capture_output=True, text=True, encoding='utf-8', timeout=60)
        return done.returncode, json.loads(done.stdout)

    def run_owner(self, *args, tty=True, typed='yes'):
        """Run the command in this process as if in a terminal (isatty) where the owner types typed."""
        import contextlib, io, nuluno
        out, err = io.StringIO(), io.StringIO()
        stdin = mock.MagicMock(); stdin.isatty.return_value = tty
        with mock.patch.object(sys, 'stdin', stdin), mock.patch('builtins.input', return_value=typed) as asked, contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit) as done: nuluno.main(list(args))
        return done.exception.code, json.loads(out.getvalue()), err.getvalue(), asked.call_count

    def test_smoke(self):
        code, out = self.run_cli('--data', self.folder, 'next')
        self.assertEqual(code, 1); self.assertIn('error', out)
        code, out = self.run_cli('start', PRODUCT, '--data', self.folder)
        self.assertEqual(code, 0); self.assertEqual(out['state'], 'no_goal_yet')
        code, out = self.run_cli('--data', self.folder, 'goal', 'G-TH-LINK-RATE')
        self.assertEqual(code, 0); self.assertTrue(out['accepted'])
        code, step = self.run_cli('next', '--data', self.folder)
        self.assertEqual(code, 0); self.assertIn('submit_step', step['cli_names'])
        code, out = self.run_cli('submit', step['step_id'], '--data', self.folder, '--output', '{"product_facts": "x"}')
        self.assertEqual(code, 1); self.assertIn('Deliverables missing', out['error'])
        code, out = self.run_cli('submit', step['step_id'], '--data', self.folder, '--output', 'not json')
        self.assertEqual(code, 2); self.assertIn('error', out)
        code, out = self.run_cli('--data', self.folder, 'no-such-command')
        self.assertEqual(code, 2); self.assertIn('error', out)
        code, out = self.run_cli('--data', self.folder, 'numbers')
        self.assertEqual(code, 2); self.assertIn('error', out)
        code, out = self.run_cli('start', 'http://not-https.example')
        self.assertEqual(code, 1); self.assertIn('https', out['error'])
        code, out = self.run_cli('tracking', '--data', self.folder)
        self.assertEqual(code, 0); self.assertFalse(out['available'])

    def test_month_commands(self):
        self.run_cli('start', PRODUCT, '--data', self.folder)
        code, out = self.run_cli('--data', self.folder, 'target', '100', '--days', '30')
        self.assertEqual(code, 0); self.assertTrue(out['accepted']); self.assertIn('plan_month', out['cli_names'])
        code, out = self.run_cli('--data', self.folder, 'target', '0')
        self.assertEqual(code, 1); self.assertFalse(out['accepted'])
        code, out = self.run_cli('--data', self.folder, 'plan', *LANES)
        self.assertEqual(code, 0); self.assertEqual(out['plan']['needed_per_day']['visits_per_day'], 167)
        code, step = self.run_cli('--data', self.folder, 'next', '--lane', LANES[0])
        self.assertEqual(code, 0); self.assertEqual(step['lane'], LANES[0]); self.assertIn('lane', step['cli_names'])
        code, out = self.run_cli('--data', self.folder, 'next', '--lane', 'G-NOPE')
        self.assertEqual(code, 1); self.assertIn('lane', out['error'])
        week = Path(self.folder) / 'week.json'
        week.write_text(json.dumps({'items': [{'lane': LANES[0], 'kind': 'post', 'channel': 'threads', 'text': 'Hello'}]}), encoding='utf-8')
        code, out = self.run_cli('--data', self.folder, 'batch', '@' + str(week))
        self.assertEqual(code, 0); self.assertEqual(out['status'], 'awaiting_owner')
        code, out = self.run_cli('--data', self.folder, 'approve', out['batch_id'], '--all')  # no terminal: refused
        self.assertEqual(code, 1); self.assertIn('Only the owner', out['error'])
        code, out = self.run_cli('--data', self.folder, 'approve', 'B1', '--all', '--i-am-the-owner')  # there is no flag that skips the typed yes
        self.assertEqual(code, 2); self.assertIn('error', out)
        code, out, shown, asked = self.run_owner('--data', self.folder, 'approve', 'B1', '--all', tty=False)
        self.assertEqual(code, 1); self.assertIn('Only the owner', out['error']); self.assertEqual(asked, 0)
        code, out, shown, asked = self.run_owner('--data', self.folder, 'approve', 'B1', '--all', typed='y')  # anything but yes
        self.assertEqual(code, 1); self.assertIn('Not approved', out['error']); self.assertEqual(asked, 1); self.assertIn('Hello', shown)
        code, out = self.run_cli('--data', self.folder, 'batches')
        self.assertEqual(out['batches'][0]['items'][0]['state'], 'awaiting_owner')
        code, out, shown, asked = self.run_owner('--data', self.folder, 'approve', 'B1', '--all', typed=' YES ')
        self.assertEqual(code, 0); self.assertEqual(out['approved_items'], ['B1-1'])
        code, out = self.run_cli('--data', self.folder, 'batches')
        self.assertEqual(out['batches'][0]['items'][0]['state'], 'approved')
        code, out = self.run_cli('--data', self.folder, 'ad-budget', '10', '--currency', 'USD', '--channel', 'meta_ads')
        self.assertEqual(code, 0); self.assertEqual(out['status'], 'awaiting_owner')
        code, out = self.run_cli('--data', self.folder, 'approve-budget')
        self.assertEqual(code, 1)
        code, out = self.run_cli('--data', self.folder, 'approve-budget', '--i-am-the-owner')
        self.assertEqual(code, 2)
        code, out, shown, asked = self.run_owner('--data', self.folder, 'approve-budget', typed='no')
        self.assertEqual(code, 1); self.assertIn('USD 10.00', shown)
        code, out, shown, asked = self.run_owner('--data', self.folder, 'approve-budget')
        self.assertEqual(code, 0); self.assertTrue(out['approved'])
        for command in ('approve', 'approve-budget'):
            shown = subprocess.run([sys.executable, str(ENGINE / 'nuluno.py'), command, '--help'], stdin=subprocess.DEVNULL, capture_output=True, text=True, encoding='utf-8', timeout=60).stdout
            self.assertIn('usage', shown); self.assertNotIn('--i-am', shown)
        code, out = self.run_cli('--data', self.folder, 'month')
        self.assertEqual(code, 0); self.assertEqual(out['next']['lane'], LANES[0]); self.assertEqual(out['pending_approvals'], [])


if __name__ == '__main__':
    unittest.main()
