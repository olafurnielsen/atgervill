# Atgervill: yfirlestur Claude Code á útgáfu 0.3

27. október 2026. Yfirlestur og lagfæringar: Claude Code (`claude-opus-5-5`). Þetta er annað líkanamat, ekki óháð mat íslensks ritstjóra.

## Hirsla og útgáfur

| | |
|---|---|
| Hirsla | https://github.com/olafurnielsen/atgervill |
| Nafn | Atgervill; skill-ið `yfirlestur` (`/yfirlestur`). Hét „Mannleg íslenska“ til og með 0.3; endurnefnt að ósk notanda. |
| Sýnileiki | Opinber (`PUBLIC`). Verkbeiðnin gerði ráð fyrir lokaðri hirslu; notandi staðfesti opinberan sýnileika 27. október 2026. |
| Leyfi | MIT (`LICENSE`), valið af notanda 27. október 2026. |
| Grunncommit | `4848b92` á `main`: afhending Codex óbreytt, staðfest gegn `SHA256SUMS.txt` |
| Vinnugrein | `claude-yfirlestur`; lokacommit og PR-slóð koma fram í PR-lýsingu |

## Athugasemdir í alvarleikaröð

### A1 — Verndaðir strengir taldir sem hlutstrengir (alvarlegt; lagfært)

- Staður: `profanir/verify.py`, `check()`.
- Dæmi: Í T04 er „ef“ verndað orð, en `str.count('ef')` finnur það líka í „eftir“ og skilar 2. Endurskriftin „Leigjandi má óska eftir framlengingu og hefja ferlið berist umsókn fyrir 1. desember.“ fellir skilyrðið „ef“ brott, en „hefja“ bætir upp talninguna og gamla `check()` skilar engri villu. Á sama hátt finnst „má“ í „málið“.
- Áhrif: Varðveislupróf á stuttum orðum (neitun, skilyrði, heimild/skylda) gat staðist þótt orðið hyrfi.
- Lagfæring: talning með orðmörkum (`(?<!\w)…(?!\w)`). Bæði dæmin eru í `profanir/test_verify.py`. Gamla `check()` úr grunncommiti skilar `[]` fyrir þau bæði, en sú nýja grípur þau. Niðurstaða á geymdum pörum er óbreytt: 18/18 og 5/7.

### A2 — Prófið skrifaði inn í hirsluna við hverja keyrslu (miðlungs; lagfært)

- Staður: `profanir/verify.py`; skjalað í README og `UPPRUNI-OG-NOTKUN.md`.
- Áhrif: Hver keyrsla snerti `velraent-mat.json` með fastri dagsetningu. Prófið féll heldur ekki ef neikvæðu viðmiðin hættu að greinast.
- Lagfæring: Skrif aðeins með `--write` (sem endurskapar skráða skrá nákvæmlega). Prófið fellur ef færri en 5 af 7 skemmdum dæmum greinast. `--results <skrá>` athugar nýjar keyrslur án sjálfsmatsreita.

### A3 — Málvillur í ritstjórnarreglunum (miðlungs; lagfært)

- Staður: `yfirlestur/references/reglur.md`.
- „Stirð nafnorðastíll“ → „Stirður nafnorðastíll“ (stíll er karlkyns). R11 „Halda tölum …“ → „Haltu tölum …“, í samræmi við boðhátt annarra reglna.
- Áhrif: Málvilla í dæmi sem líkanið á að læra af.

### A4 — Skill-ið vísaði í prófunargögn sem fylgja því ekki (lítið; lagfært)

- Staður: `SKILL.md` (Prófun), `references/mat.md` (Endurtekning, liðir 1 og 4).
- Áhrif: Eftir uppsetningu skill-möppunnar einnar vísuðu „fylgiskjöl“ í ekkert.
- Lagfæring: Vísað er í `profanir/` í kóðahirslunni og tekið fram að það fylgi ekki skill-möppunni.

### A5 — Fyrri úttök teygja mörk stillinga (tillaga; ekki breytt)

Geymdu úttökin eru söguleg og voru ekki endurskrifuð.

- T16 (ítarleg): „Við viljum þakka …“ og „Skráning fer fram …“ urðu að „þú“-ávarpi og fyrirmælum („Skráðu þig …“). Það breytir málsniði og viðtakanda, sem R10 varar við. Blinda keyrsla Claude varðveitti „við“-rödd.
- T12: „hjá teymum sem vinna með“ (afmörkun hóps) → „ef þau vinna með“ (skilyrði). Nálægt, en ekki jafngilt.
- T14 (miðlungs): bætti við efnisgreinaskilum þótt SKILL.md segi að varðveita heildarbyggingu.
- Tillaga: Taka fram í SKILL.md að ávarp (við/þú) og upplýsandi/fyrirskipandi háttur haldist líka í ítarlegri yfirferð nema beðið sé um annað. Bæta merkingaratriði um viðtakanda við T16 í corpus.

### A6 — Tegundarheiti ljóstra upp prófunartilgangi (miðlungs; tillaga)

- Staður: `profanir/corpus.jsonl`, reiturinn `genre`.
- Dæmi: „tvíræð tilvísun“, „gildissvið neitunar“, „ótilgreindur gerandi“, „skýr talaðri rödd“.
- Áhrif: Líkan sem fær reitinn veit að hverju er gætt, svo prófið er ekki blint.
- Tillaga: Aðgreina hlutlaust `genre` (t.d. „fundarboð“) frá innri `test_focus`-reit sem ekki er sendur líkani.

### A7 — Verndaðir strengir geta verið of þröngir (lítið; tillaga)

- Dæmi: Í blindri keyrslu Claude varð „Enginn sparnaður er tryggður.“ að „Enginn sparnaður er þó tryggður.“ Það fellur í vélræna prófinu, en neitunin og merkingin haldast og R5 leyfir „þó“.
- Tillaga: Vernda kjarnaorð („Enginn“, „tryggður“) fremur en heila setningu, eða merkja niðurstöðuna sem „þarfnast skoðunar“ í stað villu.

### A8 — Jákvætt viðmið ekki virt í blindri keyrslu (lítið; tillaga)

- T17 átti að standa óbreytt, en Claude sameinaði setningarnar. Merkingin hélst.
- Tillaga: Setja `expect_unchanged: true` á T06 og T17 og láta `verify.py` tilkynna frávik (sem viðvörun, ekki villu).

### A9 — Uppsetning og hleðsla óprófuð (opið)

Skill-ið var ekki sett upp í `~/.claude/skills/` eða `.claude/skills/`: sandkassi þessa umhverfis bannar skrif þar. Blinda keyrslan las skrárnar beint. `agents/openai.yaml` var ekki prófuð í Codex.

## Það sem reyndist vel

Skjölin aðgreina sjálfsmat, vélræn próf og óháð mat á skýran hátt. Varðveislureglurnar eru markvissar (neitun, fyrirvari, heimild/skylda, prósentustig, óþekktur gerandi). Dæmasafnið nær yfir margar gildrur, og bæði úttakasöfnin varðveita merkingu í öllum tilvikum sem skoðuð voru. Réttindaskráning er varfærin og engir heimildatextar eru endurbirtir.

## Prófanir

| Próf | Niðurstaða |
|---|---|
| `sha256sum -c SHA256SUMS.txt` á afhendingu | Allar 21 skrár standast (fyrir breytingar) |
| `python3 profanir/verify.py` (fyrir og eftir lagfæringu) | 18/18 standast; 5/7 skemmd dæmi greinast; N5 og N7 sleppa, eins og skjalað er |
| `python3 profanir/verify.py --write` | Endurskapar `velraent-mat.json` án breytinga |
| `python3 -m unittest discover -s profanir` | 6/6 standast. Gamla skriftan var ekki innflytjanleg; gamla `check()` missir af báðum A1-dæmunum. |
| Blind hegðunarkeyrsla, [keyrslur/2026-10-27-claude-blind](../profanir/keyrslur/2026-10-27-claude-blind/KEYRSLA.md) | 17/18 vélrænt; T12 fellur vegna viðbætts „þó“ (sjá A7) |

**Ekki prófað:** hleðsla skills í Claude Code eða Codex; raunverulegar orðaleitir; mat íslensks ritstjóra; ný, ónotuð inntök.

## Eftirstandandi verkefni

1. Leyfi: leyst; notandi valdi MIT.
2. Uppsetningar- og hleðslupróf skills í Claude Code og Codex (A9).
3. Tillögur A5–A8.
4. Uppflettiferli (málið.is, Stafsetningarorðabók, BÍN). Ekki hafið.
5. Val á breytingartillögum (B1, B2 …). Ekki hafið.
6. Óháð prófun: ónotuð inntök með skráðum uppruna og mat íslensks ritstjóra.
7. Seinni yfirlestur Codex samkvæmt [CODEX-YFIRLESTUR.md](CODEX-YFIRLESTUR.md).
