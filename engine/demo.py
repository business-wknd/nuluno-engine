#!/usr/bin/env python3
"""See the loop without connecting an agent: python3 engine/demo.py

A scripted "agent" works one goal on a throwaway product. Nothing is published
and nothing is saved outside a temporary folder. Watch what the engine refuses.
"""
import json, sys, tempfile, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import core
from server import FileStore

PRODUCT = 'https://example.com/'
store = FileStore(tempfile.mkdtemp(prefix='nuluno-demo-'))
core._link_live = lambda url: True  # the demo does not touch the network


def call(tool, **args):
    result = core.TOOLS[tool](store, 'demo', PRODUCT, args)
    print('\n> %s(%s)' % (tool, ', '.join('%s=%s' % (k, json.dumps(v, ensure_ascii=False)[:60]) for k, v in args.items())))
    return result


def say(text): print('  engine: ' + text)


def work_until_numbers(step):
    """Hand in every step with placeholder deliverables until the engine asks for numbers or waits."""
    while step.get('state') == 'work' and not step.get('call'):
        args = {'step_id': step['step_id'], 'output': {key: '(what the agent produced for %s)' % key for key in step['deliver']}}
        if step.get('publishes'): args['links'] = [PRODUCT + 'post/1']
        answer = call('submit_step', **args)
        say('accepted "%s", receipt %s' % (step['title'], answer['receipt']))
        step = answer['next']
    return step


first = call('where_are_we')
say('%s. %d playbooks available.' % (first['state'], len(first['all_goals'])))

answer = call('set_goal', goal_id='G-TH-LINK-RATE', target=0.04)
step = answer['next']
say('goal set: %s. Target %.0f%%. First step: "%s" (%s)' % (answer['goal'], answer['target'] * 100, step['title'], step['progress']))

answer = call('submit_step', step_id=step['step_id'], output={'product_facts': 'It sells things.'})
say('REFUSED: ' + answer['error'])

answer = call('submit_step', step_id='some-later-step:r1', output={'anything': 'skipping ahead'})
say('REFUSED: ' + answer['error'])

step = work_until_numbers(step)
say('now wants numbers before anything is published: ' + ', '.join(step['values_needed']))
answer = call('record_numbers', values={'link_clicks': 9, 'views': 262}, source='Threads insights, last 6 posts')
say('baseline recorded: %.2f%%' % (answer['metric'] * 100))

step = work_until_numbers(answer['next'])
say('%s until %s. One change per round, so no new variant yet.' % (step['state'], step['come_back_at_text']))

state = store.load('demo'); state['wait_until'] = time.time() - 1; store.save('demo', state)
print('\n  (two days later)')
step = call('next_step')
answer = call('record_numbers', values={'link_clicks': 7, 'views': 240}, source='Threads insights for the new post')
say('result %.2f%% against a 4%% target: %s' % (answer['metric'] * 100, 'reached' if answer['reached'] else 'MISSED'))
step = answer['next']
say('%s. Bottlenecks to choose from: %s' % (step['state'], ', '.join(step['choose_bottleneck_from'])))

answer = call('submit_step', step_id=step['step_id'], output={'bottleneck': 'angle', 'reason': 'Views held, clicks fell: people saw it and did not care.', 'one_change': 'Lead with selling your own sheet music instead of saving time'})
say(answer['message'])
say('round 2, first step: "%s". Everything from round 1 is still on record: %d steps.' % (answer['next']['title'], store.count_outputs('demo')))
print('\nThat is the whole product: the agent does the work, the engine keeps the goal, the record and the verdict.')
