# Prófunarsafn: uppruni og notkun

Útgáfa 0.1, 27. október 2026. Þetta er þróunarsafn með 18 tilbúnum textum, ekki úrtak úr íslenskri útgáfustarfsemi. Codex samdi alla textana fyrir þessa beiðni notanda. Nöfn, dagsetningar, tilvitnanir og aðstæður eru tilbúin; samningslíkt dæmi og rannsóknatextar eru ekki raunverulegar heimildir eða ráðgjöf. Tilvísunin `jon2024` er tilbúið sniðpróf og example.org er sýnislóð.

## Uppruni og réttindi

Hver færsla í corpus.jsonl hefur eigin provenance-reit með höfundi, dagsetningu, upprunategund og grundvelli notkunar. Öll dæmin eru nýsamin fyrir verkefnið; ekkert er flutt inn úr veftextum og ekkert endurbirtingarleyfi þriðja aðila er því lagt til grundvallar. Aðgangur að opinni vefsíðu var ekki túlkaður sem leyfi til að afrita efnið.

Pakkinn er afhentur notandanum til notkunar, breytinga og prófana í verkefninu. Þetta er upprunaskráning, ekki fullyrðing um höfundarréttarstöðu vélmyndaðs efnis eða leyfi til heimildavefjanna. Engin CC- eða önnur þriðja aðila leyfismerking er sett á þá. Kóðahirslan í heild er undir [MIT-leyfi](../LICENSE); það nær aðeins til efnis sem nýtur höfundarréttar og breytir engu um heimildavefina.

Reglur skillsins eru sjálfstæð samantekt. Skoðuð heimildadæmi voru ekki tekin í safnið. Fyrri samtalssvör birtust aðeins sem tilvísanamerki og engin ósýnileg viðhengi voru notuð. Beiðnir notandans staðfestu tilgang og sjálfgefna stillingu.

## Skrár og keyrsla

- corpus.jsonl: inntak, stilling, samhengi, uppruni, merkingaratriði og verndaðir strengir.
- nidurstodur.jsonl: raunveruleg ritstjórnarúttök þessarar umferðar, athugasemdir og sjálfsmat fyrir/eftir.
- fyrir-eftir.md: læsilegur samanburður allra texta ásamt 47 merkingarathugunum.
- neikvaed-vidmid.json: sjö vísvitandi spillt dæmi, ekki villur úr keyrslu annars líkans.
- verify.py: endurkeyranleg próf á tölutáknum og vernduðum strengjum (talin sem heil orð); þarf aðeins Python 3 staðalsafnið. test_verify.py prófar sjálft prófið.
- velraent-mat.json: útprentuð niðurstaða prófanna og samantekt sjálfsmatseinkunna.
- keyrslur/: síðari hegðunarkeyrslur, hver í eigin möppu með keyrsluskilyrðum. Þær breyta ekki fyrri úttökum.

Keyrið `python3 verify.py` úr þessari möppu (eða gefið fulla slóð). Það endurmetur geymdu pörin og prentar niðurstöðuna; `--write` skrifar velraent-mat.json og `--results <skrá>` athugar aðra keyrslu. Það kallar ekki á líkan og getur ekki staðfest merkingarjafngildi. Nýtt líkan þarf að fá corpus.jsonl ásamt skill-inu, en án fyrirliggjandi svara, til að framkvæma nýja endurskrift.

## Umfang

16 miðlungs dæmi, eitt létt og eitt ítarlegt. Safnið nær yfir vinnupóst, þjónustutexta, fræðileg rök, skyldu/heimild, tölur, persónulega rödd, tilvitnanir, óþekktan geranda, tvíræðni, Markdown, LaTeX, skilyrt loforð, gildissvið neitunar, lengri verkefnastöðu og afmarkandi setningar. T06 og T17 eru jákvæð viðmið sem eiga að standa óbreytt. T09 á að varðveita tvíræðni og merkja hana.

Engin óháð ritstjórayfirferð, blind samanburðartilraun, lesendaprófun, haldpróf eða prófun á gervigreindargreinum fór fram. Sama aðstoðarlíkan samdi inntak, úttak og mat. Keyrslan var í Codex-samtali 27. október 2026; nákvæm innri líkanaútgáfa, hitastilling og slembifræ voru ekki tiltæk sem staðfest lýsigögn. Einkunnir eru því þróunarathugasemdir en ekki áreiðanlegt árangursmat á almennum textum.

Næsta matsumferð ætti að nota ónotaða rauntexta með skráðu samþykki eða leyfi og sjálfstæðan íslenskan ritstjóra. Fyrir innflutt efni þarf að skrá slóð/útgáfu, höfund, afmarkaða lengd, nákvæmt leyfi eða samþykki, afleiddar breytingar og möguleg persónugögn áður en það er tekið í safnið.
