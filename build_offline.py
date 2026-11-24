# -*- coding: utf-8 -*-
"""offline.html is index.html plus the whole bank baked into the page, so the
file works when there is no network at all.  Rebuilding it from index.html
keeps the two copies from drifting apart."""
import json, io

INDEX = 'index.html'
OUT = 'offline.html'
BANK = 'data/question_bank.json'
MARKER = "const BANK_DATA_URL = new URL('./data/question_bank.json', location.href).href;"

html = io.open(INDEX, encoding='utf-8').read()
bank = json.load(io.open(BANK, encoding='utf-8'))
payload = json.dumps(bank, ensure_ascii=False, separators=(',', ':'))

assert html.count(MARKER) == 1, 'marker not unique'
assert 'window.P4_EMBEDDED_BANK = {' not in html, 'index.html already carries a bank'

out = html.replace(MARKER, 'window.P4_EMBEDDED_BANK = ' + payload + ';\n' + MARKER, 1)
io.open(OUT, 'w', encoding='utf-8').write(out)

# read it back and make sure the data parses
chk = io.open(OUT, encoding='utf-8').read()
i = chk.index('window.P4_EMBEDDED_BANK = ') + len('window.P4_EMBEDDED_BANK = ')
j = chk.index(';\n', i)
data = json.loads(chk[i:j])
print('offline.html rebuilt: %d questions, %.1f MB' % (
    len(data['questions']), len(out) / 1024.0 / 1024.0))
