# Mannleg íslenska — afhending 0.3

> Söguleg skrá frá afhendingu 0.3. Verkefnið hét þá „Mannleg íslenska“ og skill-mappan `mannleg-islenska/`; nú heitir það Atgervill og skill-ið `yfirlestur/` (`/yfirlestur`).

27. október 2026

Tilbúinn er skill-pakki með **miðlungs ritstjórnarlega yfirferð sem sjálfgefna stillingu**. Hann á að bæta skýrleika og eðlilegt mál án þess að breyta merkingu, rödd eða málsniði. Létt og ítarleg yfirferð eru valkostir. Engar fullyrðingar eru gerðar um að greina höfund eða komast hjá gervigreindargreinum.

## Afhent

- [SKILL.md](../yfirlestur/SKILL.md): virkjun, stillingar, vinnuferli og merkingartryggð.
- [Ritstjórnarreglur](../yfirlestur/references/reglur.md): 12 afmörkuð viðmið og frumsamin dæmi; málreglur aðgreindar frá stílvali.
- [Heimildir](../yfirlestur/references/heimildir.md): hlutverk heimilda, aðgangsstaða og takmörk endurnotkunar.
- [Prófunarsafn og réttindaskráning](../profanir/UPPRUNI-OG-NOTKUN.md): 18 frumsamin dæmi með uppruna fyrir hverja færslu.
- [Fyrir/eftir og merkingarmat](../profanir/fyrir-eftir.md): öll úttök og rök fyrir breytingum.
- [Vélræn niðurstaða](../profanir/velraent-mat.json) og [endurkeyranleg próf](../profanir/verify.py).

## Heimildavinna

[Ritreglur Íslenskrar málnefndar](https://ritreglur.arnastofnun.is/) styðja vinnu með rithátt og greinarmerki. [BÍN](https://bin.arnastofnun.is/forsida/umleit/) er uppflettileið fyrir orðmyndir, en ekki sjálfstæður úrskurðaraðili um heilar setningar. [Málfarsráðgjöf Árnastofnunar](https://www.arnastofnun.is/is/malfarsradgjof) vísar á viðeigandi orðabækur og málfarsgögn.

[Handbók efnisstefnunnar hjá Stafrænu Íslandi](https://island.is/handbaekur/handbok-efnisstefnunnar/efni-sem-notendur-skilja) veitir fyrirmynd fyrir skýran þjónustutexta. Upphaflega hindruðu 403-svar og JavaScript-skel beinan aðgang að þessari síðu og BÍN-leiðbeiningunum. Báðar sóttust síðar (HTTP 200), og textinn var lesinn. Mynddæmi á Ísland.is voru ekki sjónrýnd. Reglan um BÍN var skerpt: lesa þarf notkunarathugasemdir, því leitin getur sýnt myndir sem ekki samræmast núgildandi rithætti. Viðmið fyrir þjónustuvef eru ekki gerð að algildum reglum fyrir allan íslenskan texta.

Engir langir heimildatextar, beygingartöflur eða blaðagreinar eru endurbirt í afhendingarpakkanum. Prófunardæmin eru nýsamin, ekki merkt sem rauntextar eða mannlegur samanburðargrunnur.

## Prófanir og niðurstöður

Fyrsta ritstjórnarumferð var framkvæmd á öllum 18 dæmunum. Sama aðstoðarlíkan samdi dæmi, endurskrifaði og mat þau; þetta er **sjálfsmat á þróunarsafni**, ekki óháð prófun. Við merkingaryfirferð voru 47 efnisatriði metin varðveitt í lokaútgáfunum og engar nýjar staðhæfingar fundust. Það er mat höfundarlíkansins, ekki sjálfvirk sönnun.

| Athugun | Niðurstaða |
|---|---|
| Tölutákn og sérgreindir verndaðir strengir | 18/18 staðist |
| Vísvitandi merkingarvillur | 7 dæmi; 5 fundust vélrænt |
| Villur sem strengjaprófin misstu af | „Ekki allir“ varð „enginn“; óþekktur gerandi varð „stjórnin“ |
| Óbreyttir jákvæðir viðmiðstextar | T06 og T17 héldust óbreyttir |
| Óleyst tvíræðni | T09 varðveitt og útskýrð, ekki leyst með ágiskun |
| Form skill-skrár | quick_validate.py: staðist |

Matskenndar meðaleinkunnir hækkuðu fyrir skýrleika 3,61 → 4,78, eðlilegt mál 3,28 → 4,83 og rödd 4,56 → 4,89 á kvarðanum 1–5. Þær eru settar fram til rekjanleika, **ekki sem sönnun um mældan gæðabata**. Safnið er lítið, hannað í sama verkefni og matið ekki blint; háar loka-einkunnir geta endurspeglað matsbjögun.

Við yfirferð voru tvö orðalög hert áður en lokapör voru samþykkt: varðveitt var „taka umsókn til afgreiðslu“ í stað þess að láta textann gefa til kynna lokna afgreiðslu; „niðurstaða okkar“ var varðveitt í stað veikara „við teljum“. Þetta undirstrikar að liprara orðalag getur breytt styrk eða stöðu fullyrðingar. Vélrænt próf eitt nægir ekki.

## Notkun og staða

Skill-mappan heitir `mannleg-islenska`; prófunargögnin fylgja sérstaklega. Pakkinn er afhentur sem skrár og ZIP, **ekki settur upp í almenna skill-safninu**. Til að nota hann strax í samtali má vísa á SKILL.md og skrifa: „Notaðu Mannlega íslensku til að yfirfara þennan texta.“ Eftir uppsetningu í skill-safn má kalla á `$mannleg-islenska`. Sjálfvirkt val er leyft í lýsigögnum, en uppsetning og hleðsla í nýju samtali hafa ekki verið prófuð.

Verkefnið getur haldið áfram án frekari ákvarðana notanda. Áður en fullyrt er um almennan árangur er skynsamlegt að prófa ónotaða texta með skráðum heimildum og fá óháðan íslenskan ritstjóra til að meta þau. Engir slíkir textar eða samþykki eru tilbúin í þessum pakka.

## Viðbót í útgáfu 0.2

Lokið var við textasókn fyrir báðar heimildir sem höfðu aðeins verið lesnar í leitarútdráttum. Heimildaskrá og regla R9 voru uppfærðar. [Sóknarskrá](../yfirlestur/references/heimildasokn.json) geymir lýsigögn og efnisfingraför, ekki heimildatexta. Prófunarpör og sjálfsmat eru óbreytt frá fyrstu umferð; þessi viðbót er heimildastaðfesting en ekki ný hegðunarprófun líkans.

## Viðbót í útgáfu 0.3

Uppflettingar eru óháðar tilteknum þjónustuaðila eða verkfæri. Skill-ið notar þann vefaðgang sem er tiltækur og merkir óstaðfest atriði ef uppfletting tekst ekki.
