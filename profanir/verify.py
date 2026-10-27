#!/usr/bin/env python3
"""Check narrow invariants in stored outputs. Does not generate or semantically grade text.

Usage:
  python3 profanir/verify.py                  # check nidurstodur.jsonl, print summary
  python3 profanir/verify.py --write          # also rewrite velraent-mat.json
  python3 profanir/verify.py --results FILE   # check another run (JSONL with id, after)
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

base=Path(__file__).resolve().parent
# Fewer detected seeded corruptions than this means the checks got weaker.
MIN_DETECTED=5

def load_jsonl(path):
    return [json.loads(x) for x in Path(path).read_text(encoding='utf-8').splitlines() if x.strip()]

def numbers(text):
    return Counter(re.findall(r'\d+(?:[.,]\d+)*',text))

def count_span(text,span):
    # Word boundary only at ends that are word characters: „ef“ must not be found
    # inside „eftir“, but a `code span` still counts when glued to the preceding word.
    start=r'(?<!\w)' if re.match(r'\w',span) else ''
    end=r'(?!\w)' if re.search(r'\w$',span) else ''
    return len(re.findall(start+re.escape(span)+end,text))

def check(case,after):
    errors=[]
    if numbers(case['before'])!=numbers(after): errors.append('numeric_tokens_changed')
    for text in case['protected']:
        if count_span(case['before'],text)!=count_span(after,text): errors.append('protected_span_changed: '+text)
    return errors

def build_report(results_path):
    cases=load_jsonl(base/'corpus.jsonl')
    results=load_jsonl(results_path)
    assert len({c['id'] for c in cases})==len(cases)
    assert len({r['id'] for r in results})==len(results)
    assert {c['id'] for c in cases}=={r['id'] for r in results}
    by_id={c['id']:c for c in cases}
    self_reviewed=all('semantic_review' in r for r in results)
    checks=[]
    for r in results:
        c=by_id[r['id']]
        if self_reviewed:
            assert {x['id'] for x in c['invariants']}=={x['id'] for x in r['semantic_review']}
        checks.append({'id':r['id'],'errors':check(c,r['after']),'semantic_review':'recorded self-review; not verified by script' if self_reviewed else 'none recorded'})
    controls=json.loads((base/'neikvaed-vidmid.json').read_text(encoding='utf-8'))
    negative=[]
    for n in controls:
        errors=check(by_id[n['case']],n['candidate'])
        negative.append({'id':n['id'],'mechanically_detected':bool(errors),'errors':errors,'semantic_self_review':'reject','reason':n['reason']})
    report={'date':'2026-10-27','case_count':len(cases),'invariant_count':sum(len(c['invariants']) for c in cases),'mechanical_pass_count':sum(not x['errors'] for x in checks),'checks':checks,'negative_controls':negative}
    if all('scores_before' in r for r in results):
        report['subjective_self_review_means']={dim:{side:round(sum(r['scores_'+side][dim] for r in results)/len(results),2) for side in ('before','after')} for dim in ('clarity','naturalness','voice')}
    report['limitations']='Checks do not establish semantic equivalence. Negative controls are deliberately seeded; outputs and scores were authored by the same assistant.'
    return report

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--results',default=str(base/'nidurstodur.jsonl'),help='JSONL with id and after per case')
    ap.add_argument('--write',action='store_true',help='rewrite velraent-mat.json (only for the stored 0.3 results)')
    args=ap.parse_args(argv)
    if args.write and Path(args.results).resolve()!=(base/'nidurstodur.jsonl').resolve():
        ap.error('--write only applies to the stored 0.3 results; it would overwrite velraent-mat.json')
    report=build_report(args.results)
    if args.write:
        (base/'velraent-mat.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('checks','negative_controls')},ensure_ascii=False,indent=2))
    for c in report['checks']:
        if c['errors']: print('FAIL',c['id'],'; '.join(c['errors']))
    detected=sum(n['mechanically_detected'] for n in report['negative_controls'])
    print('Seeded corruptions detected mechanically:',detected,'/',len(report['negative_controls']))
    ok=all(not c['errors'] for c in report['checks']) and detected>=MIN_DETECTED
    return 0 if ok else 1

if __name__=='__main__':
    sys.exit(main())
