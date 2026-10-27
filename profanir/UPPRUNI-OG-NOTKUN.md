# Prófunarsafn: uppruni og notkun

Þróunarsafn með 17 tilbúnum textum, ekki úrtak úr íslenskri útgáfustarfsemi. Textarnir voru samdir af líkani (Codex frá OpenAI) 27. október 2026. Nöfn, dagsetningar, tilvitnanir og aðstæður eru tilbúin; samningslíkt dæmi og rannsóknatextar eru ekki raunverulegar heimildir eða ráðgjöf. example.org er sýnislóð.

## Uppruni og réttindi

Hver færsla í `corpus.jsonl` hefur eigin `provenance`-reit með höfundi, dagsetningu, upprunategund og grundvelli notkunar. Öll dæmin eru nýsamin fyrir verkefnið; ekkert er flutt inn úr veftextum og ekkert endurbirtingarleyfi þriðja aðila er því lagt til grundvallar. Aðgangur að opinni vefsíðu var ekki túlkaður sem leyfi til að afrita efnið.

Verkefnið er undir [MIT-leyfi](../LICENSE). Það nær aðeins til efnis sem nýtur höfundarréttar; óvíst er hvort vélsamið efni geri það. Leyfið veitir engan rétt til heimildavefjanna sem vísað er í. Reglur skillsins eru sjálfstæð samantekt og skoðuð heimildadæmi voru ekki tekin í safnið.

## Skrár og keyrsla

- `corpus.jsonl`: inntak, stilling, samhengi, uppruni, merkingaratriði og verndaðir strengir.
- `nidurstodur.jsonl`: ritstjórnarúttök fyrstu umferðar, athugasemdir og sjálfsmat fyrir/eftir.
- `fyrir-eftir.md`: læsilegur samanburður allra texta ásamt 44 merkingarathugunum.
- `neikvaed-vidmid.json`: sjö vísvitandi spillt dæmi, ekki villur úr keyrslu líkans.
- `verify.py`: endurkeyranleg próf á tölutáknum og vernduðum strengjum (orðamörk gilda við enda sem eru bókstafir eða tölur). `test_verify.py` prófar sjálft prófið.
- `velraent-mat.json`: niðurstaða prófanna og samantekt sjálfsmatseinkunna.
- `keyrslur/`: síðari hegðunarkeyrslur, hver í eigin möppu með keyrsluskilyrðum. Þær breyta ekki fyrri úttökum.

Keyrið `python3 verify.py` úr þessari möppu (eða gefið fulla slóð). Það endurmetur geymdu pörin og prentar niðurstöðuna; `--write` skrifar `velraent-mat.json` og `--results <skrá>` athugar aðra keyrslu. Það kallar ekki á líkan og getur ekki staðfest merkingarjafngildi. Ný keyrsla fær inntak úr `corpus.jsonl` ásamt skill-inu, en án fyrirliggjandi svara.

## Umfang

15 miðlungs dæmi, eitt létt og eitt ítarlegt. Safnið nær yfir vinnupóst, þjónustutexta, fræðileg rök, skyldu/heimild, tölur, persónulega rödd, tilvitnanir, óþekktan geranda, tvíræðni, Markdown, skilyrt loforð, gildissvið neitunar, lengri verkefnastöðu og afmarkandi setningar. T06 og T17 eru jákvæð viðmið sem eiga að standa óbreytt. T09 á að varðveita tvíræðni og merkja hana.

Engin óháð ritstjórayfirferð, blind samanburðartilraun, lesendaprófun, haldpróf eða prófun á gervigreindargreinum hefur farið fram. Sama líkan samdi inntak, fyrstu úttök og mat þeirra; nákvæm líkanaútgáfa, hitastilling og slembifræ eru ekki þekkt. Einkunnir eru því þróunarathugasemdir en ekki áreiðanlegt árangursmat á almennum textum.

Næsta matsumferð ætti að nota ónotaða rauntexta með skráðu samþykki eða leyfi og sjálfstæðan íslenskan ritstjóra. Fyrir innflutt efni þarf að skrá slóð/útgáfu, höfund, afmarkaða lengd, nákvæmt leyfi eða samþykki, afleiddar breytingar og möguleg persónugögn áður en það er tekið í safnið.
