# Atgervill

Atgervill er viðbót sem les yfir íslenskan texta, fyrir Claude Code, Codex, ChatGPT og claude.ai. Hún gerir textann skýrari og eðlilegri án þess að breyta því sem höfundur segir: neitanir, fyrirvarar, skyldur og heimildir, tölur, gerendur og tilvitnanir haldast. Merking og rödd höfundar ganga fyrir stílfegurð.

Viðbótin metur ekki hvort texti sé vélskrifaður og lofar engu um gervigreindargreina.

Þetta er þróunarútgáfa. Hegðunin hefur aðeins verið prófuð á litlu, tilbúnu dæmasafni og ekki verið metin af óháðum íslenskum ritstjóra.

## Uppsetning

### Claude Code

Í Claude Code (2.1.275 eða nýrri) dugar ein skipun:

```
/plugin install atgervill --marketplace olafurnielsen/atgervill
```

Einnig má biðja Claude um það, til dæmis: „Settu upp viðbótina atgervill úr olafurnielsen/atgervill.“

Úr skel:

```sh
claude plugin install atgervill --marketplace olafurnielsen/atgervill
```

Á eldri útgáfum Claude Code þarf tvö skref:

```sh
claude plugin marketplace add olafurnielsen/atgervill
claude plugin install atgervill@atgervill
```

Viðbótin verður virk í næstu lotu, eða strax eftir `/reload-plugins`. Nýjar útgáfur sækir `claude plugin update atgervill`.

### Codex

Codex les sama viðbótasafn:

```sh
codex plugin marketplace add olafurnielsen/atgervill
codex plugin add atgervill@atgervill
```

Nýjar útgáfur sækir `codex plugin marketplace upgrade`. Einnig má biðja Codex að setja viðbótina upp.

### ChatGPT

Í ChatGPT eru viðbætur af þessu tagi í boði á Business-, Enterprise-, Healthcare- og Edu-áskriftum. Tvær leiðir eru færar:

- **Fyrir einn notanda:** sæktu `yfirlestur.zip` af [nýjustu útgáfunni](https://github.com/olafurnielsen/atgervill/releases/latest) og hladdu henni upp undir **Plugins → Skills → Create → Upload from your computer**.
- **Fyrir vinnusvæði:** stjórnandi flytur inn `https://github.com/olafurnielsen/atgervill` undir **Plugins → Add → Import marketplace** í Admin Console. ChatGPT samstillir viðbótina daglega eftir það.

### claude.ai og Claude Desktop

Sæktu `yfirlestur.zip` af [nýjustu útgáfunni](https://github.com/olafurnielsen/atgervill/releases/latest) og hladdu henni upp í stillingunum.

## Notkun

Í Claude Code má kalla viðbótina fram með `/atgervill:yfirlestur` og textanum. Alls staðar má einfaldlega biðja um yfirlestur á íslenskum texta. Viðbótin skilar endurskoðuðum texta og stuttum athugasemdum um efnislegan vafa. Fyrir/eftir-samanburð eða breytingalista má biðja um sérstaklega.

Þrjár stillingar eru í boði:

- **Miðlungs** (sjálfgefin): leiðréttir málfar, losar um stirðar setningar, fellir brott innihaldslausar endurtekningar og lagar röð innan efnisgreina.
- **Létt:** leiðréttingar og staðbundnar lagfæringar; setningaskipan helst að mestu.
- **Ítarleg:** endurskipuleggur efnisgreinar og framsetningu eftir þörfum, með sömu kröfum um merkingartryggð.

Viðbótin krefst hvorki API-lykils, tiltekinnar vefþjónustu né annarra viðbóta. Uppflettingar nota þann vefaðgang sem er tiltækur.

## Án viðbótakerfisins

Mappan `yfirlestur/` virkar líka ein og sér. Í Claude Code verður hún að `/yfirlestur` ef hún liggur í `~/.claude/skills/` (öll verkefni) eða `.claude/skills/` (eitt verkefni), til dæmis sem tákntengill úr klóni af hirslunni:

```sh
ln -s "$PWD/yfirlestur" ~/.claude/skills/yfirlestur
```

`yfirlestur/agents/openai.yaml` geymir lýsigögn fyrir Codex.

## Skipulag

- `yfirlestur/`: viðbótin sjálf. [SKILL.md](yfirlestur/SKILL.md), [ritstjórnarreglur](yfirlestur/references/reglur.md), [heimildir](yfirlestur/references/heimildir.md) og [matsaðferð](yfirlestur/references/mat.md).
- `.claude-plugin/`: lýsing viðbótarinnar og viðbótasafnsins fyrir Claude Code.
- `profanir/`: 17 tilbúin dæmi, geymd úttök, vélræn varðveislupróf og síðari keyrslur. Sjá [uppruna og notkun](profanir/UPPRUNI-OG-NOTKUN.md).

## Próf

```sh
python3 profanir/verify.py
python3 -m unittest discover -s profanir
claude plugin validate .
```

Fyrstu tvær skipanirnar þurfa aðeins Python 3. `verify.py` athugar tölutákn og verndaða strengi í geymdum úttökum og hvort vísvitandi spillt dæmi greinist. Vænt niðurstaða: 17/17 standast og 5/7 spilltra dæma greinast; prófið fellur ef færri greinast. `--results <skrá>` athugar aðra keyrslu og `--write` uppfærir `profanir/velraent-mat.json`.

Prófið keyrir ekki líkan og staðfestir ekki merkingarjafngildi. Það missir meðal annars af „ekki allir“ → „enginn“ og tilbúnum geranda þegar aðrir verndaðir strengir haldast.

## Útgáfur

Útgáfum er stýrt með [release-please](https://github.com/googleapis/release-please). Commit-skilaboð fylgja [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:` o.s.frv.). Eftir hverja sameiningu í `main` uppfærir release-please útgáfu-PR með `CHANGELOG.md`, `version.txt` og útgáfunúmerinu í `.claude-plugin/plugin.json`. Útgáfa og tag (`vX.Y.Z`) verða til þegar sá PR er sameinaður og þá fyrst sækir `claude plugin update` nýju útgáfuna. Fyrir 1.0 hækkar `feat:` minni útgáfutöluna og `fix:` plásturstöluna.

## Leyfi og réttindi

[MIT](LICENSE). Leyfið nær til efnis sem nýtur höfundarréttar; óvíst er hvort vélsamið efni, til dæmis prófunardæmin, geri það. Heimildatextar eru ekki endurbirtir og leyfið veitir engan rétt til heimildanna sem vísað er í.
