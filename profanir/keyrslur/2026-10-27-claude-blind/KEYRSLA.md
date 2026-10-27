# Keyrsla 2026-10-27: Claude, blind gagnvart fyrri úttökum

Ný hegðunarkeyrsla á dæmunum 18. Úttakið er í `uttak.jsonl` (id, after, note). Fyrri úttök (`../../nidurstodur.jsonl`) og mat voru ekki notuð eða yfirskrifuð.

## Keyrsluskilyrði

- Framkvæmd: Claude-undirfulltrúi (general-purpose) ræstur úr Claude Code-samtali. Aðalsamtalið keyrði á `claude-opus-5-5`; líkan undirfulltrúans er ekki staðfest sérstaklega. Hitastig og slembifræ ekki tiltæk.
- Aðgangur: afrit af skill-möppunni (þá `mannleg-islenska/`, nú `yfirlestur/`) og inntaksskrá í sérstakri bráðabirgðamöppu. Fyrirmæli bönnuðu lestur annarra mappa. Það var ekki tæknilega framfylgt, en í samtalsskrá sjást aðeins lestrar í bráðabirgðamöppunni (6 tólnotkanir).
- Inntak: `id`, `genre`, `mode`, `prompt`, `before` úr `corpus.jsonl`. Merkingaratriði (`invariants`) og verndaðir strengir (`protected`) voru fjarlægð.
- Skill-ið var lesið sem skrár, ekki hlaðið gegnum skill-kerfi Claude Code. Hleðsla er óprófuð.

## Takmörk

- **Ekki fyllilega blind:** `genre`-reiturinn gefur prófunartilgang upp (t.d. „tvíræð tilvísun“, „gildissvið neitunar“, „ótilgreindur gerandi“). Næsta keyrsla ætti að sleppa honum eða nota hlutlaus tegundarheiti.
- Dæmin voru samin af öðru líkani (Codex) með þekktum gildrum; þetta er þróunarsafn, ekki haldpróf.
- Matið hér að neðan gerði sama samtal og ræsti keyrsluna. Það er líkanamat, ekki óháð mat íslensks ritstjóra.

## Vélræn athugun

`python3 profanir/verify.py --results profanir/keyrslur/2026-10-27-claude-blind/uttak.jsonl`

17/18 standast. T12 fellur: „Enginn sparnaður er tryggður.“ varð „Enginn sparnaður er þó tryggður.“ Neitunin og merkingin haldast; viðbætt „þó“ er leyfilegt samkvæmt R5, svo þetta er of þröngur verndaður strengur fremur en merkingarbreyting.

## Mat (Claude, ekki blint)

| Dæmi | Athugasemd |
|---|---|
| T06, T08, T09, T11, T13, T18 | Í samræmi við væntingar; T09 merkt tvírætt, T18 tilvitnun óhreyfð. |
| T17 | Jákvætt viðmið sem átti að standa óbreytt var sameinað í eina setningu („… fær kvöldálag en annað starfsfólk ekki“). Merking helst, en þetta er óþörf breyting. |
| T15 (létt) | „framkvæma yfirferð á drögunum“ → „fara yfir drögin“. Má telja staðbundna lagfæringu, en er á mörkum léttrar yfirferðar; fyrra úttak lét það standa. |
| T16 (ítarleg) | Varðveitti „við“-rödd og „Skráning fer fram“; fyrra úttak breytti í „þú“-ávarp og fyrirmæli. |
| T05, T14 | Hófsamari en fyrri úttök; T14 heldur innganginum „nokkur atriði“ í styttri mynd. |
| T02 | **Óljóst.** „svo hægt sé að taka umsókn þína til afgreiðslu“ → „svo hægt sé að afgreiða umsókn þína“. Fyrra orðalagið getur vísað til þess að hefja meðferð, hið síðara til þess að ljúka henni. Skýrsla 0.3 nefnir einmitt þennan greinarmun. Claude missti af þessu í fyrsta mati; Codex benti á það í seinni yfirlestri. Úttakið er óbreytt. |
| Önnur | Engin merkingarbreyting fannst. |
