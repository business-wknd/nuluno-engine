#!/usr/bin/env python3
"""Write the readable playbook pages from engine/library.json.

    python3 engine/pages.py [output folder, default: playbooks/ next to engine/]

The engine reads only library.json. Run this after editing it so the pages match.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CJK = re.compile(r'[一-鿿]')


def chinese(value): return bool(CJK.search(json.dumps(value, ensure_ascii=False)))


def language(goal, skills):
    """English when every step of the goal is written in English."""
    texts = [{k: skills[n['skill']].get(k) for k in ('title', 'purpose', 'steps', 'blockers')} for n in goal['plan']]
    if any(chinese(t) for t in texts): return 'English and 繁體中文'
    return 'English · running on a live product' if goal.get('live_test') else 'English'


def metric_line(metric):
    parts = metric['components']
    formula = '`%s` / `%s`' % (parts[0], parts[1]) if metric['formula'] in ('rate', 'ratio', 'cost') and len(parts) > 1 else '`%s`' % parts[0]
    return '`%s` = %s, should %s' % (metric['key'], formula, metric['direction'])


def page(goal_id, goal, skills):
    lang = language(goal, skills)
    out = ['# ' + goal['title'], '']
    if goal.get('title_zh') and lang.startswith('English and'):
        out += [goal['title_zh'], '']
    routes = ', '.join('%s (the next round starts with `%s`)' % (name, skill) for name, skill in goal['bottleneck_routes'].items())
    out += ['- **Goal id:** `%s`' % goal_id, '- **Language:** ' + lang, '- **Channel:** ' + goal['channel'], '- **Metric:** ' + metric_line(goal['metric']),
            '- **Observation window:** %d hours after publishing' % (goal.get('observation_seconds', 172800) // 3600),
            '- **If the target is missed, the agent picks one bottleneck:** ' + routes, '', '## Steps', '']
    for number, node in enumerate(goal['plan'], 1):
        info = skills[node['skill']]
        suffix = {'baseline': ' (baseline numbers)', 'current': ' (result numbers)'}.get(node['measure'], '')
        out += ['### %d. %s%s' % (number, info['title'], suffix), '']
        if info.get('purpose'): out += [info['purpose'], '']
        for step in info['steps']:
            out.append('- **%s** %s  ' % (step['id'], step['do']))
            out.append('  _Done when:_ ' + step.get('evidence', ''))
        out.append('')
        if info.get('deliver') and not node['measure']:
            out += ['**Hand back:** ' + ', '.join('`%s`' % key for key in info['deliver']), '']
        if info.get('blockers'):
            out += ['**If stuck:**'] + ['- `%s`: %s' % (b['code'], b['do']) for b in info['blockers']] + ['']
    return '\n'.join(out).rstrip('\n') + '\n'


def index(library):
    goals, skills = library['goals'], library['skills']
    order = sorted(goals, key=lambda g: (0 if goals[g].get('live_test') else 1 if language(goals[g], skills) == 'English' else 2, goals[g]['channel'], g))
    rows = ['| [%s](%s.md) | %s | %s | %d | %s |' % (goals[g]['title'], g, goals[g]['channel'], goals[g]['metric']['key'], len(goals[g]['plan']), language(goals[g], skills)) for g in order]
    return '\n'.join(['# Playbooks', '',
                      'Each playbook is one sales goal: an ordered list of steps, the number that decides success, and what to change when a round misses.', '',
                      ('Every playbook is written in English.' if all(language(goals[g], skills).startswith('English') and 'and' not in language(goals[g], skills) for g in goals) else 'Playbooks marked English are in English end to end. The others mix steps in English with steps in Traditional Chinese.'), '',
                      'The pages are written from [`engine/library.json`](../engine/library.json) by `python3 engine/pages.py`; edit the library, then run it.', '',
                      '| Goal | Channel | Metric | Steps | Language |', '|---|---|---|---|---|'] + rows) + '\n'


def main():
    library = json.loads((HERE / 'library.json').read_text(encoding='utf-8'))
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / 'playbooks'
    folder.mkdir(parents=True, exist_ok=True)
    for goal_id, goal in library['goals'].items():
        (folder / (goal_id + '.md')).write_text(page(goal_id, goal, library['skills']), encoding='utf-8')
    (folder / 'README.md').write_text(index(library), encoding='utf-8')
    print(len(library['goals']), 'pages ->', folder)


if __name__ == '__main__':
    main()
