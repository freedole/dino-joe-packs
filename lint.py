#!/usr/bin/env python3
"""Dino Joe packs lint: UTF-8, duzina fore, zabranjene rijeci, dozvoljeni fajlovi."""
import os, re, sys
MAX = 220
ALLOWED = {'.txt', '.ini', '.gitkeep', '.md'}
BAD = re.compile(r'https?://|<script|\b(kurac|pička|picka|jebem|jebo|govno|fuck|shit)\b', re.I)
errors = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.github' in root: continue
    for f in files:
        p = os.path.join(root, f)
        if root == '.': continue
        ext = os.path.splitext(f)[1] or f
        if ext not in ALLOWED:
            print(f'{p}: nedozvoljen tip fajla'); errors += 1; continue
        try:
            text = open(p, encoding='utf-8-sig').read()
        except UnicodeDecodeError:
            print(f'{p}: nije UTF-8'); errors += 1; continue
        if os.path.getsize(p) > 1024 * 1024:
            print(f'{p}: veci od 1 MB'); errors += 1
        if f.endswith('.txt'):
            for i, line in enumerate(text.splitlines(), 1):
                l = line.strip()
                if not l or l.startswith('#'): continue
                if len(l) > MAX: print(f'{p}:{i}: fora duza od {MAX} znakova'); errors += 1
                if BAD.search(l): print(f'{p}:{i}: zabranjen sadrzaj'); errors += 1
print('OK' if errors == 0 else f'{errors} gresaka')
sys.exit(1 if errors else 0)
