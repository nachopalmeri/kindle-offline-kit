# Sources and community search

Checked2026-10-22. Bounded search of relevant documentation, GitHub repositories/issues, MobileRead, Reddit and X. Not every repository, post or reply on the Internet. Repository descriptions are not hardware tests; social reports are anecdotes unless independently reproduced.

## Technical sources

| Source | What it supports / limitation |
|---|---|
| [KindleModding introduction](https://kindlemodding.org/jailbreaking/) | Official entry point and current method-selection flow |
| [FAQ](https://kindlemodding.org/jailbreaking/jailbreak-faq.html) | Preservation, architecture and recovery caveats; some text is older than newer projects |
| [Wizard](https://kindlemodding.org/jailbreak-wizard.html) | Canonical link followed from the official introduction; check exact combination on execution day, not this guide's case |
| [Véra guide](https://kindlemodding.org/jailbreaking/Vera/) | Live instructions; older version-range prose remains at this check |
| [Véra source metadata](https://github.com/KindleModding/kindlemodding.github.io/blob/main/content/jailbreaking/Vera/__index.md) | Lists PW6/5.20.1 at check date; source-versus-rendered discrepancy is an unresolved execution gate for a new device |
| [Reset recovery](https://kindlemodding.org/jailbreaking/recovering-from-a-reset.html) | Why reset with update modifications is not a routine undo |
| [KOReader Kindle install](https://github.com/koreader/koreader/wiki/Installation-on-Kindle-devices) | KPM/Véra and matching build requirements |
| [KOReader release](https://github.com/koreader/koreader/releases/tag/v2026.07.1) | Actual installed revision in documented case; not a universal pin for future installs |
| [KOReader user guide](https://koreader.rocks/user_guide/) | Built-in reading/layout/vocabulary/export capabilities |
| [Dictionary support](https://github.com/koreader/koreader/wiki/Dictionary-support) | StarDict format and setup |
| [Wiktionary generator](https://github.com/xxyzz/wiktionary_stardict) | Dataset source/generation; check each download and attribution |
| [WikDict](https://www.wikdict.com/page/about) | Bilingual data provenance/licensing; not a commercial native dictionary |
| [Additional dictionary catalog](https://github.com/DanielGregorini/koreader-dicts) | Optional resource, not an extra required installation |
| [Highlight exports](https://github.com/koreader/koreader/wiki/Highlight-export) | Local export separate from reading-position sync |
| [Progress sync](https://github.com/koreader/koreader/wiki/Progress-sync) | Separate protocol; no Amazon progress migration promise |
| [Calibre server](https://manual.calibre-ebook.com/server.html) | Optional library delivery while host is available |
| [Marek scriptlets](https://scriptlets.notmarek.com/) | Reference for reviewed diagnostics/ad behavior, not permission to run destructive scriptlets blindly |

## Repositories evaluated but outside offline baseline

| Project | Decision |
|---|---|
| [PW6 Tailscale](https://github.com/zackify/kindle-pw6-tailscale) | Optional remote connectivity; no VPN is needed in airplane mode. Do not copy autostart/credentials by default |
| [Tailscale KOReader plugin](https://github.com/jadehawk/tailscale.koplugin) | Alternative implementation, not a second manager to run beside an existing daemon |
| [Custom screensaver](https://github.com/chengandre/kindle-custom-screensaver) | Published PW6 tested versions do not establish5.20.1 support; not needed for a working book cover |
| [KPP Patch](https://github.com/KindleModding/KPP_Patch) | Home-app changes have a blank-screen failure risk; excluded from blanket ad removal |
| [Native library bridge](https://github.com/kaikozlov/kindle.koplugin) | Project claims native-library/progress integration; not reproduced here, not required, do not generalize it to every book/DRM/firmware |
| [Shelfmark](https://github.com/calibrain/shelfmark) | Server search/request/ingest workflow; redundant for current offline need |
| [CWA](https://github.com/crocodilestick/Calibre-Web-Automated) | Additional server/library. Its ingest consumes input files; never point at originals |
| [Readeck](https://codeberg.org/readeck/readeck) | Article archive/EPUB/OPDS; optional server, no verified automatic read-state return |
| [KOAssistant](https://github.com/zeeyado/koassistant.koplugin) | AI plugin; explicitly excluded from this offline setup |
| [Anki exporter](https://github.com/Dankoy/korvo-to-anki) | Extra dependencies/workflow; built-in vocabulary first |

## Community reports and access limits

- [Véra/PW6 discussion](https://www.reddit.com/r/koreader/comments/1vktftw/new_jailbreak_vera_kt5pw5kt6pw6csksks2_up_to_5196/): individual installation/launcher/sleep reports; not a failure rate or exact firmware certification.
- [PW6/5.20.1 report](https://www.reddit.com/r/kindlejailbreak/comments/1x027bn/12th_gen_pw6_5201_jailbreak/): anecdotal neighboring-version workaround; do NOT turn it into a universal installation step.
- [KOReader ad-screen issue](https://github.com/koreader/koreader/issues/14375): useful diagnosis lead; exact installed code/device was inspected separately in the case.
- [KFX Input author thread](https://www.mobileread.com/forums/showthread.php?t=291290): conversion of supported personal files is separate from jailbreak and not a DRM authorization.
- [Adrian thread](https://x.com/adriandlam_/status/2111845968492790095): direct web access returned403 in this review. Supplied thread excerpts inspired the project; full replies/media were not independently available, so no claim to have read them all.

No benchmark from a social post, BOOX firmware example, Doom demonstration or claimed offline model speed was used as evidence for this PW6.
