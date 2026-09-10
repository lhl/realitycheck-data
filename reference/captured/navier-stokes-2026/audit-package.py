"""Read-only integrity checks for the Navier–Stokes research package.

Run with a Python environment containing lancedb and PyYAML:
  /home/lhl/github/lhl/realitycheck/.venv/bin/python reference/captured/navier-stokes-2026/audit-package.py
"""
from pathlib import Path
import hashlib
import json
import re
import lancedb
import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
plan = json.loads((HERE / 'analysis-plan.json').read_text())
registration = json.loads((HERE / 'registration.json').read_text())
connection = lancedb.connect(str(ROOT / 'data/realitycheck.lance'))
claims = {r['id']: r for r in connection.open_table('claims').to_arrow().to_pylist()}
sources = {r['id']: r for r in connection.open_table('sources').to_arrow().to_pylist()}
evidence = connection.open_table('evidence_links').to_arrow().to_pylist()
reasoning = connection.open_table('reasoning_trails').to_arrow().to_pylist()
logs = {r['id']: r for r in connection.open_table('analysis_logs').to_arrow().to_pylist()}
checks = []
for wanted in registration['claims']:
    claim = claims[wanted['id']]
    for key in ['text', 'type', 'domain', 'evidence_level', 'source_ids', 'falsifiers', 'operationalization']:
        assert claim[key] == wanted[key], (wanted['id'], key)
    assert abs(claim['credence'] - wanted['credence']) < 1e-5
    assert claim['embedding'] and len(claim['embedding']) == 384
    assert any(row['claim_id'] == claim['id'] for row in evidence)
    assert any(row['claim_id'] == claim['id'] for row in reasoning)
    for source_id in claim['source_ids']:
        assert claim['id'] in sources[source_id]['claims_extracted']
    checks.append(claim['id'])
required_sections = ['## Metadata', '## Stage 1:', '## Stage 2:', '## Stage 3:',
                     '### Key Claims', '### Key Factual Claims Verified',
                     '### Disconfirming Evidence Search', '### Corrections & Updates',
                     '### Claim Summary', '### Claims to Register', '## Analysis Log']
files = []
for source in plan:
    filename = ROOT / 'analysis/sources' / (source['id'] + '.md')
    text = filename.read_text()
    assert all(section in text for section in required_sections), source['id']
    assert '| **Rigor Level** | DRAFT |' in text
    assert all(c['id'] in text for c in source['claims'])
    assert sources[source['id']]['embedding']
    exported = yaml.safe_load(filename.with_suffix('.yaml').read_text())
    assert exported['sources'][0]['type'] == sources[source['id']]['type']
    assert len(exported['claims']) == len(source['claims'])
    files.append(filename)
files.append(ROOT / 'analysis/syntheses/navier-stokes-2026-research-credit-data-value-chain.md')
for filename in files:
    for target in re.findall(r'\]\(([^)]+)\)', filename.read_text()):
        if target.startswith(('https:', 'http:', '#', 'mailto:')):
            continue
        assert (filename.parent / target.split('#')[0]).exists(), (filename, target)
for row in json.loads((HERE / 'claim-verification-searches.json').read_text()):
    assert len({q['query'] for q in row['queries']}) >= 2, row['claim']
for log_id in json.loads((HERE / 'lifecycle.json').read_text()).values():
    assert logs[log_id]['status'] == 'completed', log_id
expected = {
    'openai-proof-20260908-172948.pdf': '8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81',
    'openai-proof-20260908-200449.pdf': '0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f',
    'openai-proof-pdf.pdf': '0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f',
}
for filename, digest in expected.items():
    assert hashlib.sha256((HERE / filename).read_bytes()).hexdigest() == digest, filename
print(json.dumps({'ok': True, 'source_analyses': len(plan), 'claims_checked': len(checks),
                  'completed_lifecycles': len(json.loads((HERE / 'lifecycle.json').read_text())),
                  'pdf_hashes_checked': len(expected), 'local_links': 'pass',
                  'embeddings': 'present', 'provenance': 'present'}, indent=2))
