# One case, not universal compatibility

Date2026-10-22. PW6/Paperwhite12th generation7-inch, firmware5.20.1, Windows host.

| Outcome | Evidence | Limit |
|---|---|---|
| Model/firmware/root | Device report and owner screen | Other combinations untested |
| KOReader | KPM package2026.7.2; installed git-rev v2026.07.1; real EPUB displayed | No version upgrade requirement |
| Three offline dictionaries | Dataset integrity and real engine lookups | Popup selection still needs direct user check; not native dictionaries |
| Backup | Two visible acquisitions, one active DB differed; both retained | Not atomic/full device image |
| English copies |29 existing books converted where unprotected, originals hashed unchanged | No DRM bypass or progress migration |
| KOReader cover | Initial problem diagnosed; owner confirmed cover and same-page wake | Local workaround, not universal support |
| Amazon cover | Targeted backup/change prepared, SQL tested on disposable copy, owner confirmed cover after execution instructions | Final device log acquisition and long-term persistence pending; home/store ads not removed |
| Calibre/Tailscale | Earlier real private EPUB download; later managed daemon not alive | Excluded from offline baseline, no always-online promise |
| Battery/performance | No controlled measurements | No speedup/autonomy claim |

Remaining owner work: annotation/progress backup and restore rehearsal, dictionary UI checks and sustained offline use. No new AI/server stack.

Private books/history, device-generated settings/keys, backups, photos and transcripts are not published.
