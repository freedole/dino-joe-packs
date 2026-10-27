# Contributing / Doprinos

**EN** | [SR](#sr)

Thanks for helping Dino Joe get funnier! 🦖

## Suggest a joke (no Git needed)
Open an issue: **New issue -> Suggest a joke**. Write the joke, the language and the pack it fits. We add good ones to a pack.

## Add a new pack (Pull Request)
1. Fork this repo.
2. Copy an existing pack as a template, e.g. `jokes/sr-ijek/motoristi-sr`, to `jokes/<language>/<your-pack-id>/`.
3. Edit `pack.ini`: `id` (same as the folder name), `name`, `lang`, `author` (your GitHub name), `version=1.0.0`, `description`, `tags`.
4. Write jokes in `jokes/<category>.txt`, one per line. The file name is the category.
5. Optional: `keywords.ini` with `<category>=word1,word2` so the offline chat answers with your jokes.
6. Open a Pull Request. CI checks UTF-8, length and forbidden words; `index.json` (the in-app catalog) is rebuilt automatically after merge.

Test locally before the PR: copy your pack folder to `%AppData%\DinoJoe\packs\` and restart Dino Joe (or right-click -> Jokes -> Reload).

## Rules
- One joke per line, max ~200 characters (speech bubble).
- UTF-8 text only. No scripts, no links, no images (yet).
- **No politics, nationality, religion or swearing.** No real private persons.
- Male/female: write `{male|female}`, e.g. `{Rekao|Rekla} sam...`.
- Profession packs: jokes should be understandable to anyone in that profession, not just your office.
- By contributing you agree to license your content under **CC BY-SA 4.0**.

## Languages
`sr-ijek`, `sr-ekav`, `bs`, `hr`, `en`. Packs in other languages are welcome; the app currently shows `en` packs with English and the rest with BCS languages.

---

<a id="sr"></a>
## SR

Hvala što pomažeš da Dino Joe bude smješniji! 🦖

**Predloži foru (bez Git-a):** otvori issue **New issue -> Predloži foru / Suggest a joke**, napiši foru, jezik i paket kojem pripada.

**Novi paket (Pull Request):**
1. Fork repoa.
2. Kopiraj postojeći paket (npr. `jokes/sr-ijek/motoristi-sr`) u `jokes/<jezik>/<id-paketa>/`.
3. U `pack.ini` promijeni `id` (isto kao ime foldera), `name`, `author`, `description`, `tags`.
4. Fore u `jokes/<kategorija>.txt`, jedna po liniji.
5. Otvori Pull Request. CI provjerava UTF-8, dužinu i zabranjene riječi; katalog u aplikaciji se ažurira sam.

Lokalni test: kopiraj folder paketa u `%AppData%\DinoJoe\packs\` i restartuj dinu (ili desni klik -> Fore -> Učitaj ponovo).

**Pravila:** jedna fora po liniji (do ~200 znakova), samo UTF-8 tekst, **bez politike, nacije, vjere, psovki i stvarnih privatnih osoba**, muški/ženski oblik kao `{muški|ženski}`. Sadržaj ide pod licencom CC BY-SA 4.0.
