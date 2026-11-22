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


class CommandLineTest(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.mkdtemp(prefix='nuluno-cli-')
        self.addCleanup(shutil.rmtree, self.folder, True)

    def run_cli(self, *args):
        done = subprocess.run([sys.executable, str(ENGINE / 'nuluno.py')] + list(args), capture_output=True, text=True, encoding='utf-8', timeout=60)
        return done.returncode, json.loads(done.stdout)

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


if __name__ == '__main__':
    unittest.main()
