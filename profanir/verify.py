#!/usr/bin/env python3
"""Check narrow invariants in stored outputs. Does not generate or semantically grade text."""
import json, re, sys
from collections import Counter
from pathlib import Path
base=Path(__file__).resolve().parent
cases=[json.loads(x) for x in (base/'corpus.jsonl').read_text().splitlines()]
results=[json.loads(x) for x in (base/'nidurstodur.jsonl').read_text().splitlines()]
assert len({c['id'] for c in cases})==len(cases)
assert len({r['id'] for r in results})==len(results)
assert {c['id'] for c in cases}=={r['id'] for r in results}
by_id={c['id']:c for c in cases}
def numbers(text):
    return Counter(re.findall(r'\d+(?:[.,]\d+)*',text))
def check(case,after):
    errors=[]
    if numbers(case['before'])!=numbers(after): errors.append('numeric_tokens_changed')
    for text in case['protected']:
        if case['before'].count(text)!=after.count(text): errors.append('protected_span_changed: '+text)
    return errors
checks=[]
for r in results:
    c=by_id[r['id']]
    assert {x['id'] for x in c['invariants']}=={x['id'] for x in r['semantic_review']}
    checks.append({'id':r['id'],'errors':check(c,r['after']),'semantic_review':'recorded self-review; not verified by script'})
controls=json.loads((base/'neikvaed-vidmid.json').read_text())
negative=[]
for n in controls:
    errors=check(by_id[n['case']],n['candidate'])
    negative.append({'id':n['id'],'mechanically_detected':bool(errors),'errors':errors,'semantic_self_review':'reject','reason':n['reason']})
metrics={}
for dim in ('clarity','naturalness','voice'):
    metrics[dim]={side:round(sum(r['scores_'+side][dim] for r in results)/len(results),2) for side in ('before','after')}
report={'date':'2026-10-27','case_count':len(cases),'invariant_count':sum(len(c['invariants']) for c in cases),'mechanical_pass_count':sum(not x['errors'] for x in checks),'checks':checks,'negative_controls':negative,'subjective_self_review_means':metrics,'limitations':'Checks do not establish semantic equivalence. Negative controls are deliberately seeded; outputs and scores were authored by the same assistant.'}
(base/'velraent-mat.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('checks','negative_controls')},ensure_ascii=False,indent=2))
print('Seeded corruptions detected mechanically:',sum(n['mechanically_detected'] for n in negative),'/',len(negative))
sys.exit(0 if all(not c['errors'] for c in checks) else 1)
