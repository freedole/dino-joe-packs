# Dino Joe - Packs 🦖📦

Community content for **[Dino Joe - Desktop Pet](https://github.com/freedole/dino-joe)**: joke packs, skins and personalities.

**EN** | [SR](#sr)

## Structure

```
jokes/<language>/<pack-id>/
  pack.ini        # id, name, lang, author, version, license, description, tags
                  # optional: weight.<category>=10, keywords.<category>=word1,word2
  jokes/*.txt     # one joke per line; file name = category; lines starting with # are ignored
  keywords.ini    # optional: <category>=word1,word2 (keywords for offline chat)
skins/            # coming soon
personalities/    # coming soon
```

Languages: `sr-ijek`, `sr-ekav`, `bs`, `hr`, `en`.

Special categories (not picked at random): `hrana.txt` (feeding), `bockanje.txt` (click), `naocale.txt` (glasses), `pile.txt` (chick).

## Rules

- One joke per line, max ~200 characters (it is shown in a speech bubble).
- UTF-8 text only. No scripts, no executables, no links.
- **No politics, nationality, religion or swearing.** Balkan humor goes through mentality (coffee, neighbors, mom, "it'll be done tomorrow"), not identity.
- No real private people. Your own work jokes are welcome if they make sense to others in that profession.

## Contributing

1. Fork, copy `jokes/sr-ijek/odjordje-classic` as a template, rename the folder and the `id`.
2. Write jokes, open a Pull Request.
3. CI checks UTF-8, line length and the forbidden-words list.

---

<a id="sr"></a>
## SR

Sadržaj zajednice za **Dino Joe**: paketi fora, skinovi i ličnosti.

- Jedna fora po liniji, najviše ~200 znakova.
- Samo UTF-8 tekst, bez skripti i linkova.
- **Bez politike, nacije, vjere i psovki.** Balkanski humor ide preko mentaliteta (kafa, komšija, mama, "biće sutra").
- Novi paket: kopiraj `jokes/sr-ijek/odjordje-classic`, promijeni ime foldera i `id`, napiši fore i otvori Pull Request.

Licenca: CC BY-SA 4.0.
