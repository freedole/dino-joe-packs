#!/usr/bin/env python3
"""Generise index.json (katalog paketa) za Dino Joe aplikaciju. Pokrece se iz korijena repoa."""
import hashlib, json, os

ROOT = 'jokes'
out = {"format": 1, "base": "https://raw.githubusercontent.com/freedole/dino-joe-packs/main/", "packs": []}

def read_ini(p):
    d = {}
    with open(p, encoding='utf-8-sig') as f:
        for line in f:
            line = line.strip()
            if not line or line[0] in '#;[' or '=' not in line: continue
            k, v = line.split('=', 1)
            d[k.strip()] = v.strip()
    return d

for lang in sorted(os.listdir(ROOT)):
    ld = os.path.join(ROOT, lang)
    if not os.path.isdir(ld): continue
    for pid in sorted(os.listdir(ld)):
        pd = os.path.join(ld, pid)
        ini = os.path.join(pd, 'pack.ini')
        if not os.path.isfile(ini): continue
        meta = read_ini(ini)
        files, jokes = [], 0
        for dp, _, fs in os.walk(pd):
            for fn in sorted(fs):
                if os.path.splitext(fn)[1] not in ('.txt', '.ini'): continue
                fp = os.path.join(dp, fn)
                data = open(fp, 'rb').read()
                rel = os.path.relpath(fp, pd).replace(os.sep, '/')
                files.append({"path": rel, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()})
                if rel.startswith('jokes/'):
                    jokes += sum(1 for l in data.decode('utf-8-sig').splitlines() if l.strip() and not l.strip().startswith('#'))
        out["packs"].append({
            "id": meta.get("id", pid), "name": meta.get("name", pid), "lang": meta.get("lang", lang),
            "version": meta.get("version", "0"), "author": meta.get("author", ""),
            "description": meta.get("description", ""), "personality": meta.get("personality", ""),
            "jokes": jokes, "dir": pd.replace(os.sep, '/'), "files": sorted(files, key=lambda x: x["path"])})

with open('index.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(out["packs"]), "paketa")
