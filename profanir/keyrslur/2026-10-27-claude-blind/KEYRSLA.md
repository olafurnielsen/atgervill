# Keyrsla 2026-10-27: Claude, án aðgangs að fyrri úttökum

Hegðunarkeyrsla á dæmunum 17. Úttakið er í `uttak.jsonl` (id, after, note). Fyrri úttök (`../../nidurstodur.jsonl`) og mat voru hvorki aðgengileg líkaninu né yfirskrifuð.

## Keyrsluskilyrði

- Líkan: Claude (Anthropic), keyrt sem undirfulltrúi í Claude Code. Nákvæm líkanaútgáfa, hitastig og slembifræ eru ekki staðfest.
- Aðgangur: afrit af skill-möppunni og inntaksskrá í sérstakri möppu. Líkanið las aðeins SKILL.md, `references/reglur.md` og inntakið.
- Inntak: `id`, `genre`, `mode`, `prompt` og `before` úr `corpus.jsonl`. Merkingaratriði (`invariants`) og verndaðir strengir (`protected`) voru fjarlægð.
- Skill-ið var lesið sem skrár, ekki hlaðið gegnum skill-kerfi.

## Takmörk

- **Ekki fyllilega blind:** `genre`-reiturinn gefur prófunartilgang upp (t.d. „tvíræð tilvísun“, „gildissvið neitunar“, „ótilgreindur gerandi“). Næsta keyrsla ætti að sleppa honum eða nota hlutlaus tegundarheiti.
- Dæmin voru samin af öðru líkani með þekktum gildrum; þetta er þróunarsafn, ekki haldpróf.
- Matið hér að neðan er líkanamat, ekki óháð mat íslensks ritstjóra.

## Vélræn athugun

`python3 profanir/verify.py --results profanir/keyrslur/2026-10-27-claude-blind/uttak.jsonl`

16/17 standast. T12 fellur: „Enginn sparnaður er tryggður.“ varð „Enginn sparnaður er þó tryggður.“ Neitunin og merkingin haldast og R5 leyfir „þó“; verndaði strengurinn er of þröngur.

## Mat

| Dæmi | Athugasemd |
|---|---|
| T06, T08, T09, T13, T18 | Í samræmi við væntingar; T09 merkt tvírætt, tilvitnun í T18 óhreyfð. |
| T02 | **Óljóst.** „svo hægt sé að taka umsókn þína til afgreiðslu“ → „svo hægt sé að afgreiða umsókn þína“. Fyrra orðalagið getur vísað til þess að hefja meðferð, hið síðara til þess að ljúka henni. |
| T17 | Jákvætt viðmið sem átti að standa óbreytt var sameinað í eina setningu („… fær kvöldálag en annað starfsfólk ekki“). Merking helst, en breytingin er óþörf. |
| T15 (létt) | „framkvæma yfirferð á drögunum“ → „fara yfir drögin“. Má telja staðbundna lagfæringu, en er á mörkum léttrar yfirferðar; fyrra úttak lét það standa. |
| T16 (ítarleg) | Varðveitti „við“-rödd og „Skráning fer fram“; fyrra úttak breytti í „þú“-ávarp og fyrirmæli. |
| T05, T14 | Hófsamari en fyrri úttök; T14 heldur innganginum „nokkur atriði“ í styttri mynd. |
| Önnur | Engin merkingarbreyting fannst. |
