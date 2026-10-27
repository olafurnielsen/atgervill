# Atgervill

Ritstjórnar-skill fyrir íslenskan texta. Það gerir texta skýrari og eðlilegri án þess að breyta því sem höfundur segir: neitanir, fyrirvarar, skyldur og heimildir, tölur, gerendur og tilvitnanir haldast. Merking og rödd höfundar ganga fyrir stílfegurð.

Skill-ið heitir `yfirlestur` og er kallað fram með `/yfirlestur` í Claude Code. Það metur ekki hvort texti sé vélskrifaður og lofar engu um gervigreindargreina.

Þetta er þróunarútgáfa. Hegðunin hefur aðeins verið prófuð á litlu, tilbúnu dæmasafni og ekki verið metin af óháðum íslenskum ritstjóra.

## Stillingar

- **Miðlungs** (sjálfgefin): leiðréttir málfar, losar um stirðar setningar, fellir brott innihaldslausar endurtekningar og lagar röð innan efnisgreina.
- **Létt:** leiðréttingar og staðbundnar lagfæringar; setningaskipan helst að mestu.
- **Ítarleg:** endurskipuleggur efnisgreinar og framsetningu eftir þörfum, með sömu kröfum um merkingartryggð.

Skill-ið skilar hreinum, endurskoðuðum texta og stuttum athugasemdum um efnislegan vafa. Fyrir/eftir-samanburð eða breytingalista má biðja um sérstaklega.

## Uppsetning

Í Claude Code verður `/yfirlestur` tiltækt þegar mappan liggur í `~/.claude/skills/yfirlestur/` (öll verkefni) eða `.claude/skills/yfirlestur/` (eitt verkefni), til dæmis sem tákntengill:

```sh
ln -s "$PWD/yfirlestur" ~/.claude/skills/yfirlestur
```

`yfirlestur/agents/openai.yaml` geymir lýsigögn fyrir Codex. Skill-ið krefst hvorki tiltekinnar vefþjónustu, API-lykils né viðbótar; uppflettingar nota þann vefaðgang sem er tiltækur.

## Skipulag

- `yfirlestur/`: skill-ið sjálft. [SKILL.md](yfirlestur/SKILL.md), [ritstjórnarreglur](yfirlestur/references/reglur.md), [heimildir](yfirlestur/references/heimildir.md) og [matsaðferð](yfirlestur/references/mat.md).
- `profanir/`: 17 tilbúin dæmi, geymd úttök, vélræn varðveislupróf og síðari keyrslur. Sjá [uppruna og notkun](profanir/UPPRUNI-OG-NOTKUN.md).

## Próf

```sh
python3 profanir/verify.py
python3 -m unittest discover -s profanir
```

Þarf aðeins Python 3. `verify.py` athugar tölutákn og verndaða strengi í geymdum úttökum og hvort vísvitandi spillt dæmi greinist. Vænt niðurstaða: 17/17 standast og 5/7 spilltra dæma greinast; prófið fellur ef færri greinast. `--results <skrá>` athugar aðra keyrslu og `--write` uppfærir `profanir/velraent-mat.json`.

Prófið keyrir ekki líkan og staðfestir ekki merkingarjafngildi. Það missir meðal annars af „ekki allir“ → „enginn“ og tilbúnum geranda þegar aðrir verndaðir strengir haldast.

## Útgáfur

Útgáfum er stýrt með [release-please](https://github.com/googleapis/release-please). Commit-skilaboð fylgja [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:` o.s.frv.). Eftir hverja sameiningu í `main` uppfærir release-please útgáfu-PR með `CHANGELOG.md` og `version.txt`. Útgáfa og tag (`vX.Y.Z`) verða til þegar sá PR er sameinaður. Fyrir 1.0 hækkar `feat:` minni útgáfutöluna og `fix:` plásturstöluna.

## Leyfi og réttindi

[MIT](LICENSE). Leyfið nær til efnis sem nýtur höfundarréttar; óvíst er hvort vélsamið efni, til dæmis prófunardæmin, geri það. Heimildatextar eru ekki endurbirtir og leyfið veitir engan rétt til heimildanna sem vísað er í.
