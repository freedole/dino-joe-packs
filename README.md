# Dino Joe - Packs 🦖📦

Community content for **[Dino Joe - Desktop Pet](https://github.com/freedole/dino-joe)**: joke packs, skins and personalities.

**EN** | [SR](#sr)

## Structure

```
jokes/<language>/<pack-id>/
  pack.ini        # id, name, lang, author, version, license, description, tags
                  # optional per category: weight.<category>=10, keywords.<category>=word1,word2
  jokes/*.txt     # one joke per line; file name = category; lines starting with # are ignored
  keywords.ini    # optional: <category>=word1,word2 (keywords for offline chat)
skins/            # coming soon
personalities/    # coming soon
```

Languages: `sr-ijek`, `sr-ekav`, `bs`, `hr`, `en`.

Special categories (not picked at random): `food.txt` (when fed), `poke.txt` (when clicked), `glasses.txt` (glasses on), `chick.txt` (chick visits).

## Male / female

ODjordje has a female version (ODjordjina). Write gendered words as `{male|female}` and the app picks the right one:

```
{Rekao|Rekla} sam meteoru "biće to sutra".
```

## Rules

- One joke per line, max ~200 characters (it is shown in a speech bubble).
- UTF-8 text only. No scripts, no executables, no links.
- **No politics, nationality, religion or swearing.** Balkan humor goes through mentality (coffee, neighbors, mom, "it'll be done tomorrow"), not identity.
- No real private people. Your own work jokes are welcome if they make sense to others in that profession.

## Contributing

See **[CONTRIBUTING.md](CONTRIBUTING.md)**. Short version: suggest a joke via an issue (no Git needed), or copy an existing pack, write jokes and open a Pull Request. CI checks UTF-8, line length and forbidden words, and rebuilds the in-app catalog.

---

<a id="sr"></a>
## SR

Sadržaj zajednice za **Dino Joe**: paketi fora, skinovi i ličnosti.

- Jedna fora po liniji, najviše ~200 znakova.
- Samo UTF-8 tekst, bez skripti i linkova.
- **Bez politike, nacije, vjere i psovki.** Balkanski humor ide preko mentaliteta (kafa, komšija, mama, "biće sutra").
- Predloži foru preko issue-a (bez Git-a) ili napravi paket i otvori Pull Request: vidi **[CONTRIBUTING.md](CONTRIBUTING.md)**.

Licenca: CC BY-SA 4.0.
