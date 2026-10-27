# Mannleg íslenska

Íslenskt ritstjórnar-skill með miðlungs yfirferð sem sjálfgefna stillingu. Markmiðið er skýrara og eðlilegra mál með varðveittri merkingu og rödd höfundar. Þetta er þróunarútgáfa 0.3, ekki óháð gæðastaðfest vara.

## Byrja hér

1. Lestu [verkefnastöðu og afhendingu](docs/AFHENDING.md).
2. Notaðu [verkbeiðnina fyrir Claude Code](docs/CLAUDE-CODE-VERKBEIDNI.md) fyrir yfirlestur og stofnun GitHub-kóðahirslu.
3. Skoðaðu [SKILL.md](mannleg-islenska/SKILL.md) og keyrðu prófið hér fyrir neðan.
4. Skilaðu síðar hirsluslóð og nákvæmu commit-auðkenni til Codex með [verkbeiðni fyrir enduryfirlestur](docs/CODEX-YFIRLESTUR.md).

## Skipulag

- `mannleg-islenska/`: sjálfstæð skill-mappa; reglur, heimildir og lýsigögn.
- `profanir/`: 18 tilbúin þróunardæmi, fyrri úttök, sjálfsmat og vélræn próf.
- `docs/`: staða, verkbeiðnir og upphafleg skýrsla.
- `AGENTS.md`: sameiginleg viðmið við vinnu í kóðahirslu.
- `CLAUDE.md`: inngangur fyrir Claude Code.
- `SHA256SUMS.txt`: fingraför afhendingarskráa, ekki ný niðurstaða mats.

## Keyra núverandi próf

Frá rót þessarar möppu:

```sh
python3 profanir/verify.py
```

Þarf Python 3 og aðeins staðalsafnið. Prófið endurskrifar `profanir/velraent-mat.json`. Vænt niðurstaða við afhendingu: 18/18 varðveislupróf standast; 5/7 vísvitandi gallaðar útgáfur greinast vélrænt. Prófið keyrir ekki líkan og staðfestir ekki merkingarjafngildi.

## Uppsetning

Skill-ið er ekki sjálfvirkt sett upp með því að afþjappa möppunni. Claude Code þarf að staðfesta viðeigandi staðsetningu og hleðslu skills samkvæmt því umhverfi sem er í notkun. Varðveitið `mannleg-islenska/` sem sameiginlega frumútgáfu; ekki láta afrit fyrir ólík verkfæri reka í sundur.

`agents/openai.yaml` er lýsigagnaskrá fyrir viðeigandi OpenAI-umhverfi, ekki forsenda ritstjórnarreglnanna. Ekki gera ráð fyrir að önnur verkfæri lesi hana. Engin einkavefþjónusta, API-lykill eða tiltekin vefviðbót er nauðsynleg forsenda skillsins.

## Útgáfur

Útgáfum er stýrt með [release-please](https://github.com/googleapis/release-please). Commit-skilaboð fylgja [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:` o.s.frv.). Eftir hverja sameiningu í `main` uppfærir release-please útgáfu-PR með `CHANGELOG.md` og `version.txt`. Útgáfa og tag (`vX.Y.Z`) verða til þegar sá PR er sameinaður. Fyrir 1.0 hækkar `feat:` minni útgáfutöluna (0.3 → 0.4) og `fix:` plásturstöluna.

## Réttindi og uppruni

Sjá [upprunaskrá prófunarsafns](profanir/UPPRUNI-OG-NOTKUN.md) og [heimildir](mannleg-islenska/references/heimildir.md). Heimildatextar eru ekki endurbirtir í pakkanum. Notandi hefur ekki valið opið hugbúnaðarleyfi; ekki bæta slíku við að eigin frumkvæði eða merkja verkefnið sem opinn hugbúnað án ákvörðunar hans.
