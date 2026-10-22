# Private backup

Copy originals, do not move them. Store all captures OUTSIDE this Git repo. An independent disk is better protection than two folders on the same disk; do not claim the latter protects against disk failure.

PW6 can appear as Windows MTP without a drive letter. Close KOReader normally if USB transfer is unavailable. Use an available MTP client, such as Explorer, or reviewed read-only Calibre WPD access when Calibre is already installed. Do not install random drivers.

Acquire two private copies retaining original paths, Unicode, hidden/nested files and errors. Explorer can omit hidden/protected objects: record that limitation. Include visible Documents and sidecars (.sdr), My Clippings if present, and the whole visible KOReader tree with settings, metadata, vocabulary/history/statistics. My Clippings alone is not every annotation; some private/native/cloud state is not exposed.

Close readers before SQLite capture and include WAL/SHM companions when present. Differences between copies require explanation. Do not checkpoint/repair/migrate original databases just to make hashes match.

The included comparison tool accepts two already acquired filesystem folders, not a displayed MTP device name. It does not copy files, freeze databases or certify coverage. It detects byte/path/directory differences and refuses reports inside this repo or input trees.

Validate representative authorized books and read-only SQLite copies. Restore a selected subset to a NEW LOCAL test folder and compare paths/bytes. Never rehearse a restore over originals. Matching copies prove integrity only within the supplied trees, not hidden data, cloud/DRM restoration, atomicity or firmware recovery.

Reports contain book filenames; keep them private and share only redacted counts/outcomes.
