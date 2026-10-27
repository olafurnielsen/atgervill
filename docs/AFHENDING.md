# Afhending til Claude Code

Dagsetning: 27. október 2026. Grunnútgáfa: 0.3.

## Tilgangur og ákvarðanir notanda

Verkefnið er skill fyrir ritstjórnarlega yfirferð íslensks texta, „Mannleg íslenska“. Miðlungs yfirferð er sjálfgefin. Merkingartryggð og rödd höfundar ganga fyrir stílfegurð. Notandi vill færa vinnuna í Claude Code, fá þar yfirlestur og uppsetningu GitHub-kóðahirslu og fá síðan nýjan yfirlestur frá Codex.

Uppflettingar mega ekki krefjast tiltekinnar þjónustu. Viðbætur sem kunna að vera til staðar í einstöku umhverfi eru ekki hluti af afhendingarkröfum. Tilgangurinn er ekki að fela vélrænan uppruna eða standast greiningar á honum.

## Það sem er þegar til

| Hluti | Raunstaða |
|---|---|
| SKILL.md | Miðlungs, létt og ítarleg ritstjórnarstilling; merkingaryfirferð; hreinn lokatexti sjálfgefinn |
| Reglur | 12 viðmið, aðgreining málreglna og stílvals |
| Heimildir | Ritreglur, efnisstefna Ísland.is, leitarleiðbeiningar BÍN, málfarsráðgjöf Árnastofnunar |
| Dæmi | 18 frumsamin þróunardæmi: 16 miðlungs, eitt létt, eitt ítarlegt |
| Merkingarmat | 47 atriði merkt varðveitt af sama líkani og samdi dæmi og endurskriftir |
| Vélræn próf | 18/18; greina 5/7 vísvitandi gallaðar útgáfur |
| Skill-snið | Bundið quick_validate.py úr fyrra Codex-umhverfi samþykkti skrána; það verkfæri fylgir ekki pakkanum |
| Uppsetning | Ekki prófuð í nýju Claude Code- eða Codex-samtali |
| GitHub | Engin hirsluslóð, eigandi, sýnileiki eða opið leyfi ákveðið í þessu samtali; engin hirsla stofnuð hér |

Heimildasíðurnar voru lesnar. Raunverulegar orðaleitir voru ekki keyrðar. Mynddæmi á Ísland.is voru ekki sjónrýnd. Afhendingin inniheldur ekki staðbundið orðasafn eða orðabókar-API.

## Óunnið — ekki rugla saman við tilbúna eiginleika

### 1. Uppflettiferli

Setja skýra reglu um að reyna uppflettingu áður en líkanið hafnar eða leiðréttir orð vegna þess eins að það þekkir það ekki. Aðgreina:

- merkingu og tilvist/notkun orðs: viðeigandi orðabækur á málið.is;
- rithátt: Íslenska stafsetningarorðabók og ritreglur;
- beygingu: BÍN ásamt setningarsamhengi og notkunarathugasemdum.

Ekki jafna tóma leit við rangt orð eða orðafund við viðeigandi rithátt. Prófa samsett orð, nýyrði, sérheiti, rangritanir, beygingarmyndir, margar niðurstöður og ótiltækan netaðgang. Ekki giska á leitarslóðir: staðfesta þær í raun. Skrá heimild og óvissu án þess að senda heilan einkatexta í leit.

### 2. Val á breytingartillögum

Rætt var um yfirferðarstillingu með stöðugum auðkennum B1, B2 o.s.frv.; frumtexta, tillögu, ástæðu og flokki (leiðrétting, stílval, þarfnast skýringar). Notandi á að geta samþykkt, hafnað eða breytt einstökum tillögum með venjulegum skilaboðum.

Ferlið er EKKI útfært. Það má ekki breyta miðlungs ritstjórnarstyrknum í kröfu um að notandi samþykki hverja leiðréttingu í öllum verkefnum. Aðgreina styrk yfirferðar frá afhendingar-/yfirferðarstillingu. Halda möguleikanum á hreinum lokatexta.

Þegar samþykktar tillögur eru innleiddar: ekki endurskrifa aðra hluta; hópa breytingar sem þurfa að fylgjast að; endurmeta tillögur þegar frumtextinn breytist; styðja endurtekin textabrot án þess að skipta þeim öllum út í blindni. Skoða merkingu og málfræðilegt samræmi eftir val notanda.

Engin sérsmíðuð yfirferðarviðbót, innbyggðir samþykkja/hafna-hnappar eða Word-ferli hafa verið byggð eða prófuð. Byrja á verkfæraóháðu spjallsniði; sérstakt viðmót er síðari ákvörðun.

### 3. Óháð prófun

Allt núverandi safn er þróunarsafn sem höfundarlíkanið þekkti. Engin blind samanburðartilraun, óháð yfirferð íslensks ritstjóra eða haldpróf hefur farið fram. Nýtt líkan þarf ónotuð inntök, skill-ið og viðeigandi heimildir, án fyrirliggjandi svara. Skrá raunúttök áður en þau eru metin.

## Þekkt takmörk prófunarkóðans

`verify.py` athugar tölutákn og talningu skilgreindra strengja. Það skilur ekki merkingu, röð atvika, gildissvið eða orsakasambönd. Það missir meðal annars af „ekki allir“ → „enginn“ og tilbúnum geranda þegar aðrir verndaðir strengir haldast. Sjálfsmatsstöður og einkunnir eru fyrirfram skráðar niðurstöður, ekki sjálfvirkt mat þessarar keyrslu. Sjö neikvæðu viðmiðin eru handgerð skemmd dæmi.

Prófið skrifar niðurstöðuskrá og hefur fasta dagsetningu frá upphaflegu mati. Keyrsla þess í dag skapar ekki nýja líkanaúttekt. Formprófun skills sannar heldur ekki hegðun þess. Gott næsta verk er að aðgreina prófun verkfærisins, hegðun skillsins og óháð málfarsmat skýrar.

## Hvað Claude Code á að skila til baka

- Yfirlestrarskýrslu með alvarleika, skrá/staðsetningu, dæmi, áhrifum og tillögu.
- Skrá yfir framkvæmdar breytingar og þau atriði sem eru enn opin.
- Keyrðum prófum og raunúttökum; ókeyrð próf merkt sérstaklega.
- Hirsluslóð, sýnileika, grein, grunn-commit og lokacommit; PR-slóð ef PR er til.
- Nákvæmum endurtekningarskrefum og stöðu uppsetningarprófs.
- Óákveðnum atriðum, þar á meðal leyfi, ef þau hafa ekki verið leyst með notandanum.

Nota `docs/CODEX-YFIRLESTUR.md` fyrir seinni umferð. Claude-yfirferð er annað líkanamat, ekki sjálfkrafa óháð mat mannlegs íslenskusérfræðings.
