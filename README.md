# Atgervill

Skill-ið heitir `yfirlestur` og er kallað fram með `/yfirlestur` í Claude Code. Verkefnið hét „Mannleg íslenska“ til og með útgáfu 0.3; sögulegu skjölin í `docs/` nota það nafn.

Íslenskt ritstjórnar-skill með miðlungs yfirferð sem sjálfgefna stillingu. Markmiðið er skýrara og eðlilegra mál með varðveittri merkingu og rödd höfundar. Þetta er þróunarútgáfa 0.3, ekki óháð gæðastaðfest vara.

## Byrja hér

1. Lestu [verkefnastöðu og afhendingu](docs/AFHENDING.md).
2. Notaðu [verkbeiðnina fyrir Claude Code](docs/CLAUDE-CODE-VERKBEIDNI.md) fyrir yfirlestur og stofnun GitHub-kóðahirslu.
3. Skoðaðu [SKILL.md](yfirlestur/SKILL.md) og keyrðu prófið hér fyrir neðan.
4. Skilaðu síðar hirsluslóð og nákvæmu commit-auðkenni til Codex með [verkbeiðni fyrir enduryfirlestur](docs/CODEX-YFIRLESTUR.md).

## Skipulag

- `yfirlestur/`: sjálfstæð skill-mappa; reglur, heimildir og lýsigögn.
- `profanir/`: 18 tilbúin þróunardæmi, fyrri úttök, sjálfsmat og vélræn próf.
- `docs/`: staða, verkbeiðnir, upphafleg skýrsla og [yfirlestur Claude Code](docs/CLAUDE-YFIRLESTUR.md).
- `AGENTS.md`: sameiginleg viðmið við vinnu í kóðahirslu.
- `CLAUDE.md`: inngangur fyrir Claude Code.
- `SHA256SUMS.txt`: fingraför afhendingarskráa 0.3 eins og Codex skilaði þeim (grunncommit `4848b92`), ekki ný niðurstaða mats. Breyttar skrár standast þau ekki lengur.

## Keyra núverandi próf

Frá rót þessarar möppu:

```sh
python3 profanir/verify.py
python3 -m unittest discover -s profanir
```

Þarf Python 3 og aðeins staðalsafnið. Prófið prentar niðurstöðuna; `--write` endurskrifar `profanir/velraent-mat.json` og `--results <skrá>` athugar aðra keyrslu (sjá `profanir/keyrslur/`). Vænt niðurstaða: 18/18 varðveislupróf standast; 5/7 vísvitandi gallaðar útgáfur greinast vélrænt, og prófið fellur ef færri greinast. Verndaðir strengir eru taldir sem heil orð. Prófið keyrir ekki líkan og staðfestir ekki merkingarjafngildi.

## Uppsetning

Skill-ið er ekki sjálfvirkt sett upp með því að afþjappa möppunni. Í Claude Code verður `/yfirlestur` tiltækt þegar mappan liggur í `~/.claude/skills/yfirlestur/` (öll verkefni) eða `.claude/skills/yfirlestur/` (eitt verkefni), t.d. sem tákntengill: `ln -s "$PWD/yfirlestur" ~/.claude/skills/yfirlestur`. Hleðsla hefur ekki verið prófuð. Varðveitið `yfirlestur/` sem sameiginlega frumútgáfu; ekki láta afrit fyrir ólík verkfæri reka í sundur.

`agents/openai.yaml` er lýsigagnaskrá fyrir viðeigandi OpenAI-umhverfi, ekki forsenda ritstjórnarreglnanna. Ekki gera ráð fyrir að önnur verkfæri lesi hana. Engin einkavefþjónusta, API-lykill eða tiltekin vefviðbót er nauðsynleg forsenda skillsins.

## Réttindi og uppruni

Sjá [upprunaskrá prófunarsafns](profanir/UPPRUNI-OG-NOTKUN.md) og [heimildir](yfirlestur/references/heimildir.md). Heimildatextar eru ekki endurbirtir í pakkanum. Notandi hefur ekki valið opið hugbúnaðarleyfi; ekki bæta slíku við að eigin frumkvæði eða merkja verkefnið sem opinn hugbúnað án ákvörðunar hans.
