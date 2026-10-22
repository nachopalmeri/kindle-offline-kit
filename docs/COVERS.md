# Covers: two separate readers

Try the native Show covers/Display Cover option first; names/location vary. Ad-enabled devices may differ. Select a cover in KOReader's own sleep-screen settings and test with a book open. Sleep is not full shutdown.

## The documented case

KOReader initially deferred to a loaded Amazon ad-screen module; its installed code and read-only module query explained the behavior. A local KOReader-only workaround enabled its cover, then the owner confirmed it.

The native reader still showed ads. The real registry schema and exact ad property were inspected. A coherent database backup and ad-data archive were acquired and hash-verified on the PC. A device-specific change touched only the fully identified property and preserved the ad directory by rename. SQL change/reversal was tested on a disposable DB copy before the owner followed execution/reboot steps and confirmed the native cover.

Those scripts depended on private device state and are NOT reusable public installers. They are not published here. [Marek's scriptlet catalog](https://scriptlets.notmarek.com/) is a reference to inspect, not a deletion/reboot command to run blindly.

## Controls for a similar device

Verify exact compatibility, owner approval, schema/key/original value, coherent backups and local integrity. Review the script, prepare selective rollback, preserve ad data and stop on any different state. MTP cannot read private root databases directly; a verified shell or reviewed local scriptlet with a physical tap may be required.

Never reuse another device's key, issue a generic multirow update, delete folders blindly, patch home binaries or reset/deregister to force the setting.

Then check native setting availability, two book covers, page/notes on wake, normal restart and later Wi-Fi-sync behavior. Test KOReader separately. Local changes do not cancel account Special Offers officially, and persistence can differ.

Lockscreen cover success does not prove removal of home/store recommendations, all advertising or improved performance.
