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


NEW_GOALS = ('G-CREATOR-COLLAB', 'G-BASE-', 'G-B2B-')


def library_without_new_goals():
    """The goals of a library from before the scenario goals existed, to check presets work with either library."""
    return {gid: goal for gid, goal in core.library()['goals'].items() if not gid.startswith(NEW_GOALS)}


def library_with_new_goals():
    """The library with every scenario goal: the real ones when present, otherwise stand-ins copied from an existing goal."""
    lib = dict(core.library()['goals']); base = lib['G-EM-PURCHASE']
    channels = {'G-CREATOR-COLLAB': 'partnerships', 'G-B2B-ALTERNATIVES': 'b2b_search_ads'}
    for gid in ('G-CREATOR-COLLAB', 'G-BASE-REACTIVATE', 'G-BASE-REFERRAL', 'G-BASE-UPGRADE', 'G-B2B-LTD', 'G-B2B-ALTERNATIVES', 'G-B2B-INTENT',
                'G-B2B-TRIAL-CONVERT', 'G-B2B-MARKETPLACE', 'G-B2B-OUTBOUND', 'G-B2B-PARTNERS'):
        lib.setdefault(gid, dict(base, title=gid + ': stand-in', channel=channels.get(gid, 'b2b_saas')))
    return lib


class HostedStore(HookStore):
    """A store that says it is the hosted service (it gives tracked links), with an optional recipient list."""
    recipients = None
    def tracked_link(self, owner, round_number, target): return 'https://engine.example/t/abc'
    def sale_counter(self, owner): return 'https://engine.example/s/abc'


class ListStore(HookStore):
    """A store holding an uploaded list: next_recipients hands out the next rows."""
    rows = [{'email': 'a%d@example.com' % i, 'first_name': 'A%d' % i} for i in range(10)]
    handed = 0
    def list_size(self, owner): return len(self.rows)
    def next_recipients(self, owner, lane, item_id, n):
        out = self.rows[self.handed:self.handed + n]; self.handed += len(out); return out


class PresetTest(MonthTargetTest):
    """The three owner scenarios: a new consumer brand (Notavue), a brand with members (The Weekend Club), B2B SaaS."""

    def plan(self, preset, inputs, lanes=None, **target):
        answer = self.call('set_month_target', **dict({'amount': 100, 'days': 30, 'replace': True}, **target))
        self.assertTrue(answer['accepted'], answer)
        args = {'preset': preset, 'inputs': inputs}
        if lanes: args['lanes'] = lanes
        plan = self.call('plan_month', **args)
        self.assertTrue(plan['accepted'], plan)
        return plan

    def row(self, plan, model):
        return next(r for r in plan['feasibility']['capacity']['lanes'] if r['model'] == model)

    def asks(self, answer, kind): return [a for a in answer['asks'] if a['kind'] == kind]

    def test_notavue_new_brand_100_paid_in_30_days(self):
        for library in (library_with_new_goals(), library_without_new_goals()):
            with mock.patch.object(core, 'goals', lambda: library):
                plan = self.plan('new_brand', {'price': 9.99, 'free_trial': 'yes'}, currency='USD')
                lanes = [lane['lane'] for lane in plan['lanes']]
                self.assertEqual(lanes[1:], ['G-IG-LINK-RATE', 'G-META-PURCHASE-CPA', 'G-RD-PURCHASES'])
                if 'G-CREATOR-COLLAB' in library:
                    self.assertEqual(lanes[0], 'G-CREATOR-COLLAB'); self.assertNotIn('skipped_lanes', plan)
                    self.assertAlmostEqual(self.row(plan, 'creators')['paid_by_end'], 23.0)  # 10 contacted a day x 5% x 100 visits x 2%, from day 7
                else:
                    self.assertEqual(lanes[0], 'G086')
                    self.assertEqual(plan['skipped_lanes'], [{'goal_id': 'G-CREATOR-COLLAB', 'why': 'not in this library version', 'used_instead': 'G086'}])
                feas = plan['feasibility']
                self.assertEqual(feas['needed']['paid_per_day'], 3.33); self.assertEqual(feas['needed']['visits_per_day'], 167)
                self.assertEqual(self.row(plan, 'posts')['paid_by_end'], 6.0)  # 1 post x 10 visits (a new account) x 2% x 30 days
                self.assertEqual(self.row(plan, 'replies')['paid_by_end'], 6.0)  # 5 replies x 2 visits (a new account) x 2% x 30 days
                self.assertEqual(self.row(plan, 'posts')['new_account'], ['visits_per_post']); self.assertIn('assumed for a new account', self.row(plan, 'posts')['basis'])
                self.assertEqual(self.row(plan, 'replies')['new_account'], ['visits_per_reply'])
                self.assertIn('estimates until the first 7 days', feas['summary'])
                # a free trial: visits -> trials -> paying, 8% x 25% (still 2 of 100 visitors paying), with the trial layer to watch
                funnel = plan['plan']['funnel']
                self.assertEqual((funnel['visit_to_signup']['value'], funnel['signup_to_paid']['value'], funnel['visit_to_paid']['value']), (0.08, 0.25, 0.08 * 0.25))
                self.assertEqual(feas['needed']['trials_per_day'], 14); self.assertIn('14 trials a day', plan['tell_the_owner'])
                ads = self.row(plan, 'ads'); self.assertEqual(ads['paid_by_end'], 0); self.assertIn('no ad budget', ads['basis'])
                self.assertEqual(feas['verdict'], 'not_with_current_inputs')  # no budget, nothing measured: honest
                self.assertIn('Not with the current inputs', feas['summary']); self.assertIn(feas['summary'], plan['tell_the_owner'])
                self.assertIn('visit_to_paid', feas['assumed'])
                ad_lever = next(l for l in feas['levers'] if l['ask'] == 'approve_ad_budget')
                self.assertEqual(ad_lever['cost_per_customer'], 50.0); self.assertIn('loses money', ad_lever['warning'])  # US$50 per customer for a US$9.99 product
                self.assertFalse([l for l in feas['closes_gap_with'] if l['ask'] == 'approve_ad_budget'])  # never proposed as the way to close the gap
                self.assertEqual(len([l for l in feas['levers'] if l['ask'] == 'approve_ad_budget']), 1)  # one ad lever, never two different caps
                self.assertTrue(feas['closes_gap_with'])
                self.assertEqual([a['input'] for a in self.asks(plan, 'answer')], ['ad_daily_cap'])  # price and free trial were given
                self.assertFalse(self.asks(plan, 'connect_stripe'))  # local engine: no Stripe connection to offer
                self.assertTrue(all(a['where'] and a['reason'] for a in plan['asks']))
                # the owner says US$50 a day: counted, and the approval is asked for; once approved the ask is gone
                plan = self.call('plan_month', inputs={'ad_daily_cap': 50})
                self.assertAlmostEqual(self.row(plan, 'ads')['paid_by_end'], 29.0)  # 50 visits a day x 2%, from day 1
                ask = self.asks(plan, 'approve_ad_budget')[0]
                self.assertEqual(ask['suggested'], 50); self.assertIn('request_ad_budget', ask['agent_does_first']); self.assertIn('approve-budget', ask['where'])
                self.assertFalse(self.asks(plan, 'answer'))
                self.call('request_ad_budget', daily_cap=50, currency='USD', channels=['meta_ads'])
                core.approve_ad_budget(self.store, 'test', 'owner')
                status = self.call('month_status')
                self.assertIn('approved by the owner', self.row(status, 'ads')['basis']); self.assertFalse(self.asks(status, 'approve_ad_budget'))
                self.assertEqual(status['preset']['id'], 'new_brand')

    def test_measured_rate_replaces_the_assumption(self):
        plan = self.plan('new_brand', {'price': 9.99})
        self.assertIn('visit_to_paid', self.row(plan, 'posts')['assumed'])
        self.store.paid, self.store.clicks = {'count': 5, 'revenue_minor': 0, 'source': 'Stripe'}, 500
        status = self.call('month_status')
        self.assertNotIn('visit_to_paid', self.row(status, 'posts')['assumed'])
        self.assertAlmostEqual(self.row(status, 'posts')['paid_by_end'], 3.0, delta=0.2)  # 10 visits a day (a new account) at the measured 1%

    def test_twc_existing_base_doubling(self):
        for library in (library_with_new_goals(), library_without_new_goals()):
            with mock.patch.object(core, 'goals', lambda: library):
                inputs = {'paid': 400, 'members': 50000, 'capacity_per_week': 120, 'message_channels': 'email, LINE'}
                plan = self.plan('existing_base', inputs, amount=800, current_paid=400, price=750, currency='TWD')
                lanes = [lane['lane'] for lane in plan['lanes']]
                if 'G-BASE-REACTIVATE' in library: self.assertEqual(lanes, ['G-BASE-REACTIVATE', 'G-BASE-REFERRAL', 'G-BASE-UPGRADE', 'G-IG-LINK-RATE'])
                else: self.assertEqual(lanes, ['G088', 'G086', 'G-EM-PURCHASE', 'G-IG-LINK-RATE']); self.assertEqual(len(plan['skipped_lanes']), 3)
                self.assertEqual(plan['preset']['inputs']['message_channels'], ['email', 'LINE'])
                self.assertNotIn('check_target', plan)
                feas = plan['feasibility']
                self.assertEqual(plan['plan']['remaining_customers'], 400)
                self.assertEqual(feas['needed']['paid_per_day'], 13.33)
                self.assertEqual(feas['needed']['messages_per_day_if_all_from_the_list'], 5556)  # 13.33 / (3% click x 8% pay)
                self.assertEqual([r['model'] for r in feas['capacity']['lanes']], ['list', 'referral', 'list', 'posts'])  # a stand-in keeps the job of the missing goal
                for row in feas['capacity']['lanes'][::2][:2]: self.assertEqual(row['paid_by_end'], 0); self.assertIn('no send volume approved', row['basis'])
                self.assertEqual(self.row(plan, 'referral')['paid_by_end'], 18.0)  # 400 x 10% share x 0.5 paid friend, from day 3
                self.assertEqual(feas['verdict'], 'not_with_current_inputs')
                self.assertIn('Even with every lever', feas['summary'])  # doubling 400 in a month: honest that it is out of reach
                volume = [l for l in feas['levers'] if l['ask'] == 'approve_send_volume']
                self.assertEqual({l['suggested'] for l in volume}, {1654})  # 49,600 contacts x 2 messages / 30 days / 2 list lanes
                kinds = [a['kind'] for a in plan['asks']]
                for kind in ('upload_list', 'approve_send_volume', 'verify_sending_domain'): self.assertIn(kind, kinds)
                self.assertEqual(self.asks(plan, 'upload_list')[0]['input'], 'list_size')
                self.assertFalse(self.asks(plan, 'answer'))  # members, paid, channels, capacity and price were given
                # the owner approves a win-back template capped at 1654 a day: that lane now counts, its ask is gone
                win_back = lanes[0]
                batch = self.call('submit_batch', items=[{'lane': win_back, 'kind': 'template', 'channel': 'email', 'text': 'Hi {first_name}, we kept your seat. Book this week: {link}',
                                                          'audience_rule': 'members with no booking in 90 days', 'daily_cap': 1654}])
                self.assertIn('up to 1654 a day', batch['approval_needed']['tell_the_owner'])
                core.approve_batch(self.store, 'test', batch['batch_id'], 'all', 'owner')
                status = self.call('month_status')
                self.assertEqual(status['feasibility']['capacity']['lanes'][0]['paid_by_end'], 119.0)  # 1653.3 a day x 0.24% x 30 days
                self.assertFalse([a for a in self.asks(status, 'approve_send_volume') if a['lane'] == win_back])
                # seats are the limit: 20 more a week caps the month at about 86 whatever the lanes could bring
                plan = self.call('plan_month', inputs={'daily_send_cap': 4000, 'capacity_per_week': 20})
                feas = plan['feasibility']
                self.assertGreater(feas['capacity']['before_limits'], 200)
                self.assertEqual(feas['capacity']['paid_by_end'], 85.7); self.assertTrue(feas['capacity']['limits'][0]['binding'])
                self.assertTrue([l for l in feas['levers'] if l.get('limit') == 'capacity_per_week'])
                self.assertEqual(feas['verdict'], 'not_with_current_inputs')
        # a doubling written as 800 new customers gets a note to count the 400 already paying
        plan = self.plan('existing_base', {'paid': 400, 'members': 50000}, amount=800)
        self.assertIn('current_paid 400', plan['check_target'])

    def test_b2b_self_serve_100_customers(self):
        for library in (library_with_new_goals(), library_without_new_goals()):
            with mock.patch.object(core, 'goals', lambda: library):
                plan = self.plan('b2b_self_serve', {'price': 29, 'trials_per_week': 20, 'competitors': 'Calendly, Doodle'}, currency='USD')
                lanes = [lane['lane'] for lane in plan['lanes']]
                self.assertEqual(len(lanes), 5)
                if 'G-B2B-LTD' in library:
                    self.assertEqual(lanes, ['G-B2B-LTD', 'G-B2B-ALTERNATIVES', 'G-B2B-INTENT', 'G-B2B-TRIAL-CONVERT', 'G-B2B-MARKETPLACE'])
                    self.assertEqual(self.row(plan, 'launch')['paid_by_end'], 9.0)  # the low end, 30 sales a month, live after 21 days
                    self.assertTrue([a for a in self.asks(plan, 'provide_link') if a['input'] == 'ltd_listing_url'])
                else:
                    self.assertEqual(lanes, ['G-PH-LAUNCH-PURCHASE', 'G-GA-PURCHASE-RATE', 'G065', 'G087', 'G084'])
                    self.assertEqual(self.row(plan, 'launch_day')['starts_after_days'], 7)
                feas = plan['feasibility']; funnel = plan['plan']['funnel']
                self.assertEqual(funnel['signup_to_paid']['basis'], 'assumed'); self.assertAlmostEqual(funnel['visit_to_paid']['value'], 0.006)
                self.assertEqual(feas['needed']['trials_per_day'], 23); self.assertEqual(feas['needed']['visits_per_day'], 556)
                self.assertAlmostEqual(self.row(plan, 'trials')['paid_by_end'], 12.9)  # 20 trials a week x 15% x 30 days
                self.assertEqual(feas['verdict'], 'not_with_current_inputs')
                ads = next(l for l in feas['levers'] if l['ask'] == 'approve_ad_budget')
                self.assertEqual(ads['cost_per_customer'], 500.0); self.assertIn('loses money', ads['warning'])
                self.assertIn('only at a loss', feas['summary']); self.assertIn('Even with every lever', feas['summary'])
                self.assertFalse(self.asks(plan, 'approve_ad_budget'))
                self.assertEqual([(a['input'], a['optional']) for a in self.asks(plan, 'answer')], [('trial_to_paid', True)])
                plan = self.call('plan_month', inputs={'trial_to_paid': 0.25})
                self.assertEqual(plan['plan']['funnel']['signup_to_paid']['basis'], 'measured')
                self.assertEqual(plan['feasibility']['needed']['trials_per_day'], 14)
                self.assertFalse(self.asks(plan, 'answer'))

    def test_b2b_sales_cycle_longer_than_the_month(self):
        plan = self.plan('b2b_sales', {'acv': 6000, 'sales_cycle_days': 30, 'demos_per_week': 5, 'has_trial': 'no'}, amount=20)
        feas = plan['feasibility']
        self.assertEqual(len(plan['lanes']), 4)  # no trial: no trial lane
        self.assertEqual(feas['capacity']['paid_by_end'], 0); self.assertEqual(feas['verdict'], 'not_with_current_inputs')
        self.assertIn('close after the end', feas['summary'])
        self.assertTrue([l for l in feas['levers'] if 'pilot' in l['lever']])
        self.assertFalse([l for l in feas['levers'] if l['ask'] == 'approve_ad_budget'])  # ads cannot close deals that close after the end
        self.assertEqual(feas['needed']['demos_per_day'], 3.3)
        self.assertEqual(self.store.load('test#campaign')['price_minor'], 600000)  # acv sets the price when the target had none
        plan = self.call('plan_month', inputs={'has_trial': 'yes', 'sales_cycle_days': 7, 'daily_send_cap': 40})
        self.assertEqual(len(plan['lanes']), 5)
        outbound = self.row(plan, 'outreach')
        self.assertAlmostEqual(outbound['paid_by_end'], 40 * 0.05 * 0.4 * 0.2 * 20, places=1)  # from day 3 + 7
        self.assertTrue([a for a in self.asks(plan, 'verify_sending_domain')])

    def test_b2b_sales_demo_limit_caps_the_levers(self):
        plan = self.plan('b2b_sales', {'acv': 3000, 'sales_cycle_days': 14, 'demos_per_week': 10, 'has_trial': 'yes'}, currency='USD')
        feas = plan['feasibility']; limit = feas['capacity']['limits'][0]
        self.assertEqual(limit['limit'], 'demos_per_week'); self.assertAlmostEqual(limit['most_by_end'], 10 / 7.0 * 0.2 * 16)  # 4.6 by the end
        self.assertFalse(self.asks(plan, 'approve_ad_budget'))  # ads cannot bring customers the team cannot demo
        self.assertFalse([l for l in feas['levers'] if l['ask'] == 'approve_ad_budget'])
        demos = [l for l in feas['closes_gap_with'] if l.get('limit') == 'demos_per_week']
        self.assertEqual(len(demos), 1); self.assertEqual(feas['closes_gap_with'][0], demos[0])  # raising the limit comes first
        self.assertTrue([l for l in feas['closes_gap_with'] if l.get('cycle_days') == 7])  # the paid pilot is in the plan
        self.assertGreater(demos[0]['suggested'], 10); self.assertEqual(demos[0]['for_target'], 153)  # 100 / (20% x 23 days, the pilot's 7-day cycle) x 7
        self.assertIn('counting the 7-day pilot', demos[0]['lever'])
        self.assertLessEqual(feas['reachable_with_levers'], 10 / 7.0 * 0.2 * 23 + demos[0]['adds_by_end'] + 0.1)
        self.assertFalse([l for l in feas['closes_gap_with'] if (l['adds_by_end'] or 0) < 0.5])  # 0.1 more customers is not asked for
        partners = next(l for l in feas['levers'] if 'agencies or consultants a day' in l['lever'])  # still listed as a lever
        self.assertLess(partners['adds_by_end'], 0.5); self.assertNotIn(15, [a.get('suggested') for a in self.asks(plan, 'approve_send_volume')])
        self.assertIn('Even with every lever', feas['summary']); self.assertIn('raise demos_per_week first', feas['summary'])
        mailboxes = next(l for l in feas['levers'] if 'mailboxes' in l['lever'])
        self.assertEqual(mailboxes['limited_by'], ['demos_per_week']); self.assertLess(mailboxes['adds_within_current_limits'], mailboxes['adds_by_end'])
        self.assertIn('demo requests a day', plan['tell_the_owner']); self.assertNotIn('sign-ups', plan['tell_the_owner'])
        # enough demos: then ads count again, within the new limit
        plan = self.call('plan_month', inputs={'demos_per_week': 300})
        self.assertFalse([l for l in plan['feasibility']['levers'] if l.get('limit')])
        self.assertTrue([l for l in plan['feasibility']['closes_gap_with'] if l['ask'] == 'approve_ad_budget'])

    def test_pilot_raises_the_demo_limit(self):
        # a 40-day cycle in a 30-day month: no demo closes by the end, but a 7-day pilot makes the 10 demos a week count
        plan = self.plan('b2b_sales', {'acv': 3000, 'sales_cycle_days': 40, 'demos_per_week': 10, 'has_trial': 'no'}, currency='USD')
        feas = plan['feasibility']
        self.assertEqual(feas['capacity']['limits'][0]['most_by_end'], 0)
        pilot = next(l for l in feas['closes_gap_with'] if l.get('cycle_days') == 7)
        self.assertNotIn('limited_by', pilot)  # 10 a week x 20% x 23 days leaves room for what the pilot adds
        self.assertGreater(feas['reachable_with_levers'], 0); self.assertAlmostEqual(feas['reachable_with_levers'], pilot['adds_by_end'], places=1)
        self.assertNotIn('about 0 of 100', feas['summary'])

    def test_stated_ad_cap_respects_the_limits(self):
        # seats are the limit and the other lanes already fill them: no ad budget is asked for
        plan = self.plan('existing_base', {'paid': 400, 'members': 50000, 'capacity_per_week': 20, 'daily_send_cap': 4000, 'ad_daily_cap': 3000, 'message_channels': 'email'},
                         amount=800, current_paid=400, price=750, currency='TWD')
        feas = plan['feasibility']; ads = self.row(plan, 'ads')
        self.assertFalse(self.asks(plan, 'approve_ad_budget')); self.assertIn('More ad money would not help', feas['summary'])
        self.assertEqual(ads['paid_by_end'], 0); self.assertGreater(ads['paid_by_end_before_limits'], 50); self.assertEqual(ads['limited_by'], ['capacity_per_week'])
        self.assertEqual(feas['capacity']['ad_cap']['useful_daily_cap'], 0)
        # demos are the limit: only the part of the US$500 that brings the about 2 customers the demos leave room for
        plan = self.plan('b2b_sales', {'acv': 3000, 'sales_cycle_days': 14, 'demos_per_week': 10, 'has_trial': 'yes', 'ad_daily_cap': 500}, currency='USD')
        feas = plan['feasibility']; ads = self.row(plan, 'ads'); ask = self.asks(plan, 'approve_ad_budget')[0]
        room = 10 / 7.0 * 0.2 * 16 - self.row(plan, 'replies')['paid_by_end']
        self.assertAlmostEqual(ads['paid_by_end'], room, places=0); self.assertEqual(ads['paid_by_end_before_limits'], 5.0)
        self.assertLess(ask['suggested'], 500); self.assertGreater(ask['suggested'], 150)
        self.assertEqual(ask['suggested'], feas['capacity']['ad_cap']['useful_daily_cap']); self.assertIn('daily_cap %d' % ask['suggested'], ask['agent_does_first'])
        self.assertIn('past that limit', ask['reason']); self.assertIn('demos', ask['reason'])
        # no limit: the stated cap is asked for as given, with the money-losing warning when ads cost more than the price
        plan = self.plan('new_brand', {'price': 9.99, 'free_trial': 'no', 'ad_daily_cap': 50}, currency='USD')
        ask = self.asks(plan, 'approve_ad_budget')[0]
        self.assertEqual(ask['suggested'], 50); self.assertIn('loses money', ask['warning']); self.assertIn('USD 50.00', ask['warning'])
        self.assertAlmostEqual(self.row(plan, 'ads')['paid_by_end'], 29.0); self.assertNotIn('limited_by', self.row(plan, 'ads'))
        plan = self.plan('new_brand', {'price': 99, 'free_trial': 'no', 'ad_daily_cap': 50}, currency='USD')
        self.assertIsNone(self.asks(plan, 'approve_ad_budget')[0]['warning'])  # US$50 a customer for a US$99 product: no warning

    def test_capacity_limit_caps_the_levers(self):
        plan = self.plan('existing_base', {'paid': 400, 'members': 50000, 'capacity_per_week': 20, 'daily_send_cap': 4000, 'message_channels': 'email'},
                         amount=800, current_paid=400, price=750, currency='TWD')
        feas = plan['feasibility']; most = feas['capacity']['limits'][0]['most_by_end']
        self.assertAlmostEqual(feas['capacity']['paid_by_end'], 85.7, places=1)
        room = feas['closes_gap_with'][0]; self.assertEqual(room['limit'], 'capacity_per_week')
        self.assertLessEqual(feas['reachable_with_levers'], most + room['adds_by_end'] + 0.1)
        self.assertLess(feas['reachable_with_levers'], 400); self.assertIn('Even with every lever', feas['summary'])
        # the stated send cap is counted, so each list lane asks for its template approval with that volume
        volume = self.asks(plan, 'approve_send_volume')
        self.assertEqual(sorted(a['lane'] for a in volume), sorted(r['lane'] for r in feas['capacity']['lanes'] if r['model'] == 'list'))
        self.assertTrue(all(a['suggested'] == 1654 and 'daily_cap 1654' in a['agent_does_first'] for a in volume))

    def test_free_trial_changes_the_funnel(self):
        plan = self.plan('new_brand', {'price': 9.99, 'free_trial': 'no'})
        self.assertNotIn('visit_to_signup', plan['plan']['funnel']); self.assertNotIn('trials_per_day', plan['feasibility']['needed'])
        self.assertEqual(plan['plan']['funnel']['visit_to_paid']['value'], 0.02)
        plan = self.call('plan_month', inputs={'free_trial': 'yes', 'trial_to_paid': 0.5})
        self.assertEqual(plan['plan']['funnel']['signup_to_paid']['basis'], 'measured'); self.assertAlmostEqual(plan['plan']['funnel']['visit_to_paid']['value'], 0.04)
        self.assertEqual(plan['feasibility']['needed']['trials_per_day'], 7)
        plan = self.call('plan_month', inputs={'free_trial': 'no'})  # no trial any more: the assumed trial layer goes
        self.assertNotIn('visit_to_signup', plan['plan']['funnel']); self.assertNotIn('signup_to_paid', plan['plan']['funnel'])
        self.assertNotIn('trials a day', plan['tell_the_owner'])
        self.assertNotIn('free_trial', [a.get('input') for a in plan['asks']])

    def test_preset_refusals_and_limits(self):
        self.call('set_month_target', amount=100)
        self.assertFalse(self.call('plan_month', preset='viral')['accepted'])
        self.assertIn('Unknown input', self.call('plan_month', preset='new_brand', inputs={'pricee': 9})['error'])
        self.assertFalse(self.call('plan_month', preset='new_brand', inputs={'trial_to_paid': 2})['accepted'])
        self.assertFalse(self.call('plan_month', preset='new_brand', inputs={'free_trial': 'maybe'})['accepted'])
        self.assertFalse(self.call('plan_month', preset='new_brand', inputs={'organic_channel': 'myspace'})['accepted'])
        self.assertIn('preset', self.call('plan_month')['error'])
        self.assertEqual(self.store.load('test#campaign')['status'], 'planning')  # nothing changed by a refusal
        self.store.limit = 1
        plan = self.call('plan_month', preset='new_brand', inputs={'organic_channel': 'tiktok'})
        self.assertEqual(len(plan['lanes']), 1); self.assertEqual(len(plan['left_out_lanes']['lanes']), 3)
        self.store.limit = None
        plan = self.call('plan_month', preset='new_brand')
        self.assertIn('G-TT-LINK-RATE', [lane['lane'] for lane in plan['lanes']])  # the agent's channel choice is kept
        with mock.patch.object(core, 'goals', lambda: {gid: g for gid, g in library_without_new_goals().items() if gid not in ('G-PH-LAUNCH-PURCHASE', 'G-GA-PURCHASE-RATE', 'G065', 'G087', 'G084')}):
            self.assertIn('None of the b2b_self_serve', self.call('plan_month', preset='b2b_self_serve')['error'])
        plan = self.call('plan_month', preset='new_brand', lanes=['G-TH-LINK-RATE'])  # lanes given: they are used, the preset still asks
        self.assertEqual([lane['lane'] for lane in plan['lanes']], ['G-TH-LINK-RATE'])

    def test_plan_without_preset_has_feasibility(self):
        plan = self.start()
        self.assertNotIn('preset', plan)
        self.assertEqual(plan['feasibility']['verdict'], 'not_with_current_inputs')
        self.assertEqual([r['model'] for r in plan['feasibility']['capacity']['lanes']], ['posts', 'replies', 'ads'])
        self.assertFalse(self.asks(plan, 'answer'))
        self.assertIn('feasibility', self.call('month_status'))

    def test_hosted_asks(self):
        self.store = HostedStore(self.folder)
        plan = self.plan('existing_base', {'paid': 10, 'members': 200})
        stripe = self.asks(plan, 'connect_stripe')[0]; self.assertIn('owner page', stripe['where'])
        self.assertIn('owner page', self.asks(plan, 'upload_list')[0]['where']); self.assertNotIn('input', self.asks(plan, 'upload_list')[0])
        self.store.paid = {'count': 1, 'revenue_minor': 0, 'source': 'Stripe'}
        self.assertFalse(self.asks(self.call('month_status'), 'connect_stripe'))
        store = ListStore(self.folder); self.store = store
        self.assertFalse(self.asks(self.call('month_status'), 'upload_list'))  # the list is uploaded
        self.assertEqual(self.call('month_status')['feasibility']['capacity']['lanes'][0]['basis'].count('the uploaded list'), 1)

    # ---- templates ----

    def test_template_items_are_checked(self):
        self.start(lanes=['G-TH-INTENT'])
        good = {'lane': 'G-TH-INTENT', 'kind': 'template', 'channel': 'threads', 'text': 'Hi {first_name}, saw your post about {topic}.', 'audience_rule': 'people asking for help', 'daily_cap': 20}
        for bad in ({'audience_rule': None}, {'audience_rule': ''}, {'daily_cap': 0}, {'daily_cap': 2001}, {'daily_cap': 2.5}, {'daily_cap': None},
                    {'text': 'Hi {first_name}{last_name}'}, {'text': ' '.join('{p%d}' % i for i in range(11))}, {'text': '{a}'}):
            self.assertFalse(self.call('submit_batch', items=[dict(good, **bad)])['accepted'], bad)
        answer = self.call('submit_batch', items=[good])
        self.assertTrue(answer['accepted'], answer); self.assertIn('up to 20 a day to people asking for help', answer['approval_needed']['tell_the_owner'])
        item = self.call('batch_status')['batches'][0]['items'][0]
        self.assertEqual((item['daily_cap'], item['placeholders'], item['sent_today'], item['remaining_today']), (20, ['first_name', 'topic'], 0, 20))

    def test_template_matching(self):
        template = 'Hi {first_name}, thanks for your post about {topic}. Try it: https://example.com/'
        fills = lambda text: core._fills_template(template, text)
        self.assertTrue(fills('Hi Ann, thanks for your post about piano covers. Try it: https://example.com/'))
        self.assertTrue(fills('Hi  Ann,\nthanks for your post about piano covers.  Try it: https://example.com/'))  # whitespace normalised
        self.assertFalse(fills('Hi Ann, thanks for your post about piano covers. Buy it now: https://example.com/'))  # fixed text changed
        self.assertFalse(fills('Hi , thanks for your post about piano covers. Try it: https://example.com/'))  # an empty value
        self.assertFalse(fills('Hi %s, thanks for your post about x. Try it: https://example.com/' % ('A' * 41)))  # a name over 40 characters
        self.assertTrue(fills('Hi %s, thanks for your post about x. Try it: https://example.com/' % ('A' * 40)))
        self.assertTrue(fills('Hi Ann, thanks for your post about %s. Try it: https://example.com/' % ('b' * 80)))
        self.assertFalse(fills('Hi Ann, thanks for your post about %s. Try it: https://example.com/' % ('b' * 81)))  # other values: 80 by default
        self.assertFalse(fills('Hi Ann, thanks for your post about piano covers. Try it: https://example.com/ PS'))
        self.assertTrue(core._fills_template('Same text for all', ' Same  text for all'))
        started = time.time()
        self.assertFalse(core._fills_template(' '.join('{p%d} x' % i for i in range(10)), 'x ' * 2400))  # an input built to be slow stays fast
        self.assertLess(time.time() - started, 5)

    def test_template_values_cannot_carry_other_text(self):
        template = 'Hi {first_name}, saw your post about {topic}. Try it: https://notavue.com'
        fills = lambda text, links=(): core._fills_template(template, text, links)
        self.assertTrue(fills('Hi Ann, saw your post about piano covers. Try it: https://notavue.com'))
        # the review's abuse example: a link and an offer hidden in a value
        self.assertFalse(fills('Hi Ann, buy crypto now at https://evil.example/x?y=1 , saw your post about piano. Try it: https://notavue.com'))
        for value in ('piano at evil.com', 'piano, see www.example.org', 'piano, mail me at a@b.co', 'piano 10.0.0.1', 'piano. Also join my casino today',
                      'piano\nBuy now', 'piano covers. Try it: https://x.io'):
            self.assertFalse(fills('Hi Ann, saw your post about %s. Try it: https://notavue.com' % value), value)
        for name in ('Ann, buy crypto now', 'Ann! Click', 'Ann Lee Marie Bo Cy Di Ed'):
            self.assertFalse(fills('Hi %s, saw your post about piano. Try it: https://notavue.com' % name), name)
        self.assertTrue(fills('Hi Ann,\nsaw your post about piano.\nTry it: https://notavue.com'))  # a line break in the fixed text is a space
        self.assertTrue(fills('Hi Member 2, saw your post about Op. 9 No. 2 and Node.js. Try it: https://notavue.com'))  # numbers and abbreviations are fine
        # a domain on any top-level domain is a link, not only the common ones; a few dotted words are not domains
        for value in ('piano at evil.lol now', 'piano at evil.zip', 'piano, see x.agency', 'piano at evil.lol', 'piano 看evil.best', 'Node.js.evil.lol'):
            self.assertFalse(fills('Hi Ann, saw your post about %s. Try it: https://notavue.com' % value), value)
        for value in ('Vue.js and Next.js', 'ASP.NET apps', 'scales, e.g, Hanon', 'piano (i.e, covers)'):
            self.assertTrue(fills('Hi Ann, saw your post about %s. Try it: https://notavue.com' % value), value)
        ok, why = core._template_fill(template, 'Hi Ann, saw your post about piano at evil.com. Try it: https://notavue.com')
        self.assertFalse(ok); self.assertIn('link', why)
        # a template may allow a longer value, up to 200
        long = 'Hi {first_name}, here is a tip for you: {tip:200} More at https://notavue.com'
        self.assertTrue(core._fills_template(long, 'Hi Ann, here is a tip for you: %s More at https://notavue.com' % ('slow down the left hand ' * 8).strip()))
        self.assertIsNone(core._template_problem(long))
        self.assertIn('1 to 200', core._template_problem('Hi {first_name}, here is a tip for you: {tip:201} More at https://notavue.com'))
        self.assertIn('at least 20', core._template_problem('{a}. {b}. {c}.'))  # mostly placeholders: refused
        # a {link} placeholder holds only the product link or the round's tracked link
        linked = 'Hi {first_name}, we kept your seat for Friday. Book here: {link}'
        links = core._link_prefixes(HostedStore(self.folder), 'test', 'https://the-wknd.club/', None, 1)
        self.assertTrue(core._fills_template(linked, 'Hi Ann, we kept your seat for Friday. Book here: https://engine.example/t/abc?v=A', links))
        self.assertTrue(core._fills_template(linked, 'Hi Ann, we kept your seat for Friday. Book here: https://the-wknd.club/taipei', links))
        for bad in ('https://evil.example/x', 'https://the-wknd.club.evil.net/', 'https://engine.example/t/abcd', 'https://the-wknd.club/ and more'):
            self.assertFalse(core._fills_template(linked, 'Hi Ann, we kept your seat for Friday. Book here: ' + bad, links), bad)

    def test_library_states_the_placeholder_rule(self):
        # the playbooks tell agents the same limits the engine enforces, so a message written by the book is not refused
        skills = core.library()['skills']
        steps = [step['do'] for skill in skills.values() for step in skill['steps']]
        self.assertFalse([do for do in steps if 'under 200 characters' in do and 'placeholder' in do])
        reply = next(step['do'] for step in skills['C-INT-REPLY']['steps'] if step['id'] == 'C-INT-REPLY.01')
        self.assertIn('{specific_tip:200}', reply); self.assertIn('{fit_line:120}', reply); self.assertIn('80 characters (40 for a name)', reply)
        fills = [do for do in steps if do.startswith(('Fill the placeholders', 'Send once per person', 'Each day, send to the next contacts'))]
        self.assertTrue(fills and all('80 characters (40 for a name)' in do and '{link}' in do for do in fills))
        template = 'Hi {name_or_handle}, I work on Notavue. For {their_problem}, try this: {specific_tip:200} {fit_line:120} https://notavue.com'
        self.assertIsNone(core._template_problem(template))
        self.assertTrue(core._fills_template(template, 'Hi Ann, I work on Notavue. For slow sight-reading, try this: %s %s https://notavue.com'
                                             % ('read one bar ahead while you play, and keep the tempo slow enough that you never stop ' * 2, 'It turns any YouTube piano video into sheet music to practise')))

    def test_template_abuse_refused_in_submit_step(self):
        lane = 'G-TH-INTENT'
        self.start(lanes=[lane])
        template = 'Hi {first_name}, saw your post about {topic}. Try it: https://notavue.com'
        batch = self.call('submit_batch', items=[{'lane': lane, 'kind': 'template', 'channel': 'threads', 'text': template, 'audience_rule': 'people asking', 'daily_cap': 3}])
        self.assertEqual(self.call('batch_status')['batches'][0]['items'][0]['placeholder_limits'], {'first_name': 40, 'topic': 80})
        core.approve_batch(self.store, 'test', batch['batch_id'], 'all', 'owner')
        step = self.walk_lane(lane, lambda s: s.get('publishing') and not s.get('publishes'))
        output = {key: 'x ' + key for key in step['deliver']}
        evil = 'Hi Ann, buy crypto now at https://evil.example/x?y=1 , saw your post about piano. Try it: https://notavue.com'
        answer = self.submit(step, lane=lane, output=dict(output, sent=[evil]), approved_item=batch['batch_id'] + '-1')
        self.assertFalse(answer['accepted']); self.assertIn('Closest refusal', answer['error']); self.assertIn('link', answer['error'])
        self.assertEqual(self.call('batch_status')['batches'][0]['items'][0]['sent_today'], 0)  # nothing counted

    def test_template_sends_count_per_day_under_the_cap(self):
        lane = 'G-TH-INTENT'
        self.start(lanes=[lane])
        template = 'Hi {first_name}, saw your question about {topic}. This may help: https://example.com/'
        batch = self.call('submit_batch', items=[{'lane': lane, 'kind': 'template', 'channel': 'threads', 'text': template, 'audience_rule': 'people asking', 'daily_cap': 3}])
        item = batch['batch_id'] + '-1'
        step = self.walk_lane(lane, lambda s: s.get('publishing') and not s.get('publishes'))
        messages = ['Hi %s, saw your question about sheet music. This may help: https://example.com/' % name for name in ('Ann', 'Bo', 'Cy', 'Di')]
        output = {key: 'x ' + key for key in step['deliver']}
        self.assertIn('not approved', self.submit(step, lane=lane, output=dict(output, sent=messages[:1]), approved_item=item)['error'])
        core.approve_batch(self.store, 'test', batch['batch_id'], 'all', 'owner')
        approved = self.call('next_step', lane=lane)['approved_items'][0]
        self.assertEqual((approved['kind'], approved['remaining_today']), ('template', 3))
        answer = self.submit(step, lane=lane, output=dict(output, sent=messages), approved_item=item)
        self.assertFalse(answer['accepted']); self.assertIn('3 more fit today, not 4', answer['error'])
        answer = self.submit(step, lane=lane, output=dict(output, sent=['Hi Ann, saw your question. Buy now: https://example.com/']), approved_item=item)
        self.assertFalse(answer['accepted']); self.assertIn('built from template', answer['error'])
        answer = self.submit(step, lane=lane, output=dict(output, sent=messages[:2]), approved_item=item)
        self.assertTrue(answer['accepted'], answer); self.assertEqual(answer['template_messages_counted'], 2); self.assertIn('1 left today', answer['owner_approval'])
        logged = self.store.outputs(core.lane_owner('test', lane), 1)[0]['content']['owner_approved_item']
        self.assertEqual((logged['kind'], logged['messages_counted']), ('template', 2))
        view = self.call('batch_status')['batches'][0]['items'][0]
        self.assertEqual((view['state'], view['sent_today'], view['remaining_today']), ('approved', 2, 1))  # a template stays approved
        record = self.store.load('test#campaign')
        self.assertEqual(core._approved(record, lane, item)[0]['remaining_today'], 1)
        entry = record['batches'][0]['items'][0]; entry['sent_by_day'] = {core._day(time.time() - 86400): 3, core._day(): 2}
        self.assertEqual(core._approved(record, lane, item)[0]['remaining_today'], 1)  # yesterday's sends do not count today

    def test_next_recipients(self):
        lane = 'G-TH-INTENT'
        self.start(lanes=[lane])
        items = [{'lane': lane, 'kind': 'template', 'channel': 'email', 'text': 'Hi {first_name}, a seat is free on Friday.', 'audience_rule': 'past guests', 'daily_cap': 4},
                 {'lane': lane, 'kind': 'post', 'channel': 'threads', 'text': 'A post'}]
        batch = self.call('submit_batch', items=items)['batch_id']
        self.assertIn('not approved', self.call('next_recipients', lane=lane, item_id=batch + '-1')['error'])
        core.approve_batch(self.store, 'test', batch, 'all', 'owner')
        self.assertIn('template', self.call('next_recipients', lane=lane, item_id=batch + '-2')['error'])
        self.assertFalse(self.call('next_recipients', lane='G-X-LINK-RATE', item_id=batch + '-1')['accepted'])
        self.assertFalse(self.call('next_recipients', lane=lane, item_id=batch + '-1', n=0)['accepted'])
        local = self.call('next_recipients', lane=lane, item_id=batch + '-1')
        self.assertTrue(local['accepted']); self.assertFalse(local['available']); self.assertEqual(local['remaining_today'], 4); self.assertIn('own list', local['note'])
        self.store = ListStore(self.folder)
        first = self.call('next_recipients', lane=lane, item_id=batch + '-1', n=3)
        self.assertTrue(first['available']); self.assertEqual([r['first_name'] for r in first['recipients']], ['A0', 'A1', 'A2']); self.assertEqual(first['remaining_today'], 1)
        second = self.call('next_recipients', lane=lane, item_id=batch + '-1', n=3)
        self.assertEqual(len(second['recipients']), 1)  # the daily cap, not n
        third = self.call('next_recipients', lane=lane, item_id=batch + '-1')
        self.assertFalse(third['accepted']); self.assertEqual(third['remaining_today'], 0)


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

    def test_preset_commands(self):
        self.run_cli('start', PRODUCT, '--data', self.folder)
        self.run_cli('--data', self.folder, 'target', '100', '--days', '30', '--currency', 'USD')
        code, out = self.run_cli('--data', self.folder, 'plan')
        self.assertEqual(code, 2); self.assertIn('--preset', out['error'])
        code, out = self.run_cli('--data', self.folder, 'plan', '--preset', 'new_brand', '--input', 'price')
        self.assertEqual(code, 2); self.assertIn('key=value', out['error'])
        code, out = self.run_cli('--data', self.folder, 'plan', '--preset', 'new_brand', '--input', 'price=9.99', '--input', 'free_trial=yes', '--input', 'organic_channel=youtube')
        self.assertEqual(code, 0, out); self.assertTrue(out['accepted'])
        self.assertEqual(out['preset']['inputs'], {'price': 9.99, 'free_trial': True, 'organic_channel': 'youtube'})
        self.assertIn('G-YT-SITE-CLICKS', [lane['lane'] for lane in out['lanes']])
        self.assertEqual(out['feasibility']['verdict'], 'not_with_current_inputs'); self.assertIn('inputs', out['cli_names'])
        self.assertEqual([a['input'] for a in out['asks'] if a['kind'] == 'answer'], ['ad_daily_cap'])
        self.assertIn('nuluno.py plan --input ad_daily_cap', out['asks'][0]['where'])
        code, out = self.run_cli('--data', self.folder, 'plan', '--input', 'ad_daily_cap=20')  # the preset is remembered
        self.assertEqual(code, 0, out); self.assertEqual(out['preset']['inputs']['ad_daily_cap'], 20)
        code, out = self.run_cli('--data', self.folder, 'month')
        self.assertEqual(code, 0); self.assertIn('verdict', out['feasibility']); self.assertTrue(any(a['kind'] == 'approve_ad_budget' for a in out['asks']))
        code, out = self.run_cli('--data', self.folder, 'plan', '--input', 'members=many')
        self.assertEqual(code, 1); self.assertIn('members', out['error'])


if __name__ == '__main__':
    unittest.main()
