# TASKS.md
# Pi Home Server — Task Tracker

---

## AI AGENT INSTRUCTIONS
### Process
1. **Session start:** Identify current phase and next actionable task.
2. **During session:** Update STATUS and NOTES only. Never change Task IDs, titles, or acceptance criteria without explicit human approval. Append session notes with session number. Never overwrite prior notes.
3. **Session end:** Update all tasks touched. Remove strike-through on blockers resolved. Propose new tasks if scope expanded — await approval before writing.

### Rules
- **On marking Done:** Never mark task as "Done" without explicit human confirmation that acceptance criteria are both adequately defined and sufficiently met. If criteria prove incomplete mid-task, propose amended criteria or a numbered subtask (e.g. T1-18.1) rather than silently expanding scope.
- **On Blocked tasks:** Always include a BLOCKERS line listing specific dependencies. Strike through blockers as they are resolved: ~~T1-04~~.

### Task Status Annotation

| Status             | Title formatting                |
| ------------------ | ------------------------------- |
| TODO               | `### T5-01 : Task title`        |
| ==🚧 In Progress== | `### ==🚧 T5-01 : Task title==` |
| ✔️ Partial         | `### ✔️ T5-01 : Task title`     |
| ⛔️ Blocked         | `### ⛔️ T5-01 : Task title`     |
| ~~Skipped~~        | `### ~~T5-01 : Task title~~`    |
| ✅ Done             | `### ✅ T5-01 : Task title`      |
| 🔁 Recurring       | `### 🔁 T5-01 : Task title`     |

#### Formatting Rules:
- TODO is the only state with no emoji and no special formatting
- Skipped is the only state with no emoji, only strikethrough
- The `STATUS:` field is always present on every task, plain text, no emoji or formatting
- Never use em-dash, en-dash or similar. Find different structure or punctuation for that line.

---

## PHASE 0 — Completed Prior Work (32-bit setup, now superseded)
These tasks were completed on the old 32-bit OS. Documented for historical context only. Do not attempt to redo on new OS — they are superseded by Phase 1 equivalents.

### ✅ T0-01 : PiHole initial install
STATUS: Done
ACCEPTANCE: PiHole running, serving DNS to home network, web UI accessible at http://192.168.0.22/admin
NOTES: Installed on 32-bit Raspbian Bookworm. Blocklists, whitelists, blacklists configured by user over time. Config must be exported before wipe.

### ✅ T0-02 : qBittorrent-nox install (32-bit)
STATUS: DONE — SUPERSEDED]
ACCEPTANCE: Was running on port 8080, seeding disabled
NOTES: Installed natively via apt. Required manual systemd service file creation because packaged service file was missing. User=sutton585 (not pi). Seeding disabled via 1 KB/s upload cap and ratio 0 setting.

### ✅ T0-03 : Docker install (32-bit)
STATUS: DONE — SUPERSEDED]
ACCEPTANCE: Docker 28.5.2 installed, sutton585 added to docker group
NOTES: Installed via get.docker.com script. Audiobookshelf container failed — armv7 not supported by ghcr.io/advplyr/audiobookshelf image. Root cause of 64-bit migration decision.

### ✅ T0-04 : SSH key setup (Mac → Pi)
STATUS: DONE
ACCEPTANCE: Passwordless SSH from MacBook to Pi using ed25519 key. ~/.ssh/config configured with UseKeychain and AddKeysToAgent.
NOTES: Key already existed at ~/.ssh/id_ed25519. ssh-copy-id used to push to Pi. Will need to re-run ssh-copy-id after 64-bit reinstall since authorized_keys will be wiped.

---

## PHASE 1 — 64-bit Reinstall and Core Services
Goal: Clean aarch64 OS with all core services running. This is the active phase.

### ✅ T1-01 : Export PiHole config before wipe
STATUS: DONE
PRIORITY: CRITICAL — must complete before any other Phase 1 task
ACCEPTANCE CRITERIA:
  - Teleporter export .zip downloaded to MacBook
  - File confirmed present locally before SD card is touched
  - File named with date e.g. pihole-backup-2026-02-19.zip
HOW: PiHole web UI → Settings → Teleporter → Export → download file
NOTES:
- Session 5: Terminology standardized. Sandman vocabulary confirmed: tools, integrations, automations, workflows. Metaphor-specific terms (grains, dreams) fully retired. Operator confirmed as the name for the job search automation project. It follows the same tool architecture as other Sandman tools and will be exposed via the same MCP server.
### ✅ T1-02 : Flash 64GB SD card with 64-bit Raspberry Pi OS Lite
STATUS: DONE
BLOCKED BY: T1-01
ACCEPTANCE CRITERIA:
  - Raspberry Pi Imager used (not manual dd)
  - OS selected: Raspberry Pi OS Lite (64-bit) — no desktop
  - Advanced settings configured before flash:
    - Hostname: PiHole
    - SSH enabled
    - Username: sutton585
    - Password set
    - WiFi configured if not using ethernet
  - Card flashed successfully, Pi boots from new card
NOTES:

### ✅ T1-03 : Verify 64-bit OS
STATUS: DONE
BLOCKED BY: T1-02
ACCEPTANCE CRITERIA:
  - SSH into Pi succeeds from MacBook
  - `uname -m` returns aarch64
  - `cat /etc/os-release` shows Bookworm
  - `free -h` shows ~900MB total RAM available
NOTES:

### ✅ T1-04 : Re-run ssh-copy-id for new OS
STATUS: DONE
BLOCKED BY: T1-03
ACCEPTANCE CRITERIA:
  - `ssh-copy-id sutton585@192.168.0.22` run from MacBook
  - Subsequent SSH connections require no password
NOTES:

### ✅ T1-05 : Install PiHole on 64-bit OS
STATUS: DONE
BLOCKED BY: T1-03
ACCEPTANCE CRITERIA:
  - PiHole installed via official installer: curl -sSL https://install.pi-hole.net | bash
  - Web UI accessible at http://192.168.0.22/admin
  - Pi is serving DNS to home network (test: other devices can browse internet normally)
  - Teleporter backup from T1-01 imported: Settings → Teleporter → Import
  - Blocklists, whitelists confirmed restored
NOTES:

### ✅ T1-06 : Set static DHCP lease in router
STATUS: DONE
BLOCKED BY: T1-05
ACCEPTANCE CRITERIA:
  - Router admin UI used to assign permanent DHCP reservation for Pi MAC address → 192.168.0.22
  - Pi IP confirmed stable after reboot
  - NOTE: Do NOT hardcode IP on Pi itself — manage via router
NOTES:

### ✅ T1-07 : Install Docker and Docker Compose on 64-bit OS
STATUS: DONE
BLOCKED BY: T1-03
ACCEPTANCE CRITERIA:
  - Docker installed via: curl -fsSL https://get.docker.com | sh
  - sutton585 added to docker group: sudo usermod -aG docker sutton585
  - Logged out and back in after group change
  - `docker --version` works without sudo
  - `docker compose version` works (confirms compose plugin present)
  - Install compose plugin if needed: sudo apt install docker-compose-plugin -y
NOTES:

### ✅ T1-08 : Connect and mount external USB drive
STATUS: DONE
BLOCKED BY: T1-03
ACCEPTANCE CRITERIA:
  - Drive connected via powered USB hub or self-powered drive (not raw Pi USB)
  - `lsblk` shows drive (e.g. /dev/sda or /dev/sda1)
  - Drive formatted as ext4 (WARNING: destructive — confirm drive is empty first)
  - Mount point created: sudo mkdir -p /mnt/data
  - UUID retrieved: sudo blkid -s UUID -o value /dev/sda1
  - /etc/fstab entry added with nofail flag for safe boot if drive absent
  - `sudo mount -a` runs without error
  - `df -h` shows /mnt/data with expected capacity
NOTES:

### ✅ T1-09 : Create directory structure on external drive
STATUS: DONE
BLOCKED BY: T1-08
ACCEPTANCE CRITERIA:
  - All directories created:
    /mnt/data/audiobooks
    /mnt/data/books
    /mnt/data/downloads
    /mnt/data/torrents/incomplete
    /mnt/data/ai-sandbox
  - Ownership set: sudo chown -R sutton585:sutton585 /mnt/data
  - `ls -la /mnt/data` confirms structure and correct ownership
NOTES:

### ✅ T1-10 : Create config directory structure on SD card
STATUS: DONE
BLOCKED BY: T1-03
ACCEPTANCE CRITERIA:
  - Directories created:
    /home/sutton585/config/audiobookshelf/config
    /home/sutton585/config/audiobookshelf/metadata
    /home/sutton585/config/prowlarr
  - Owned by sutton585
NOTES:

### ✅ T1-11 : Install qBittorrent-nox (native, 64-bit)
STATUS: DONE
BLOCKED BY: T1-03
ACCEPTANCE CRITERIA:
  - Installed via: sudo apt install qbittorrent-nox -y
  - systemd service file created at /etc/systemd/system/qbittorrent-nox.service with User=sutton585
  - Service enabled and running: sudo systemctl enable qbittorrent-nox --now
  - `systemctl status qbittorrent-nox` shows active (running)
  - Web UI accessible at http://192.168.0.22:8080
  - Default password changed from adminadmin immediately
  - Download path set to /mnt/data/downloads
  - Upload global rate limit set to 1 KB/s
  - BitTorrent → seeding ratio set to 0 → pause on reach
NOTES:

### ✅ T1-12 : Create docker-compose.yml with all container definitions
STATUS: DONE
BLOCKED BY: T1-07, T1-09, T1-10
ACCEPTANCE CRITERIA:
  - File created at /home/sutton585/docker-compose.yml
  - Contains service definitions for: audiobookshelf, prowlarr, ai-sandbox
  - Volume paths use /mnt/data/ for media, /home/sutton585/config/ for config
  - ai-sandbox has network_mode: none
  - All services have restart: unless-stopped
  - File is valid: docker compose config runs without errors
NOTES:

### ✅ T1-13 : Start Docker services via compose
STATUS: DONE
BLOCKED BY: T1-12
ACCEPTANCE CRITERIA:
  - `docker compose up -d` runs from /home/sutton585/ without errors
  - `docker ps` shows audiobookshelf, prowlarr, ai-sandbox all running
  - Audiobookshelf web UI accessible at http://192.168.0.22:13378
  - Prowlarr web UI accessible at http://192.168.0.22:9696
NOTES:

### ==🚧 T1-14 : Configure Prowlarr indexers==
STATUS: In Progress
BLOCKED BY: T1-13
ACCEPTANCE CRITERIA:
  - Prowlarr web UI opened and admin account created
  - At minimum these indexers added and tested: Anna's Archive, AudioBookBay
  - Each indexer shows green status (working)
  - qBittorrent added as download client in Prowlarr settings
  - Test search performed and result successfully sent to qBittorrent
NOTES:
- Session #2:  YTS, EZTV, Internet Archive added. AudioBookBay and Anna's Archive are NOT in Prowlarr's catalog and cannot be added via normal flow. One Russian book tracker added (semi-private, account created by user). Libgen not found in catalog during session. Cloudflare blocking encountered on some indexers — requires FlareSolverr to resolve (see new tasks). qBittorrent not yet connected to Prowlarr as a download client app — not done this session.
- Session 3: Indexer audit completed. Removed dead indexers (ebookbay, isohunt2, BTdirectory, btstate, damag, magnet cat, postman, extratorrent, KickassTorrents clones). Retained YTS, EZTV, and a small set of working general indexers. qBittorrent not yet connected to Prowlarr as download client — still pending T1-18.

### ==🚧 T1-15 : Configure Audiobookshelf==
STATUS: In Progress
BLOCKED BY: T1-13
ACCEPTANCE CRITERIA:
  - Admin account created in web UI
  - Library added pointing to /audiobooks (which maps to /mnt/data/audiobooks)
  - Library scan runs without errors
  - iOS app (Audiobookshelf) installed on David's iPhone
  - App connected to server at 192.168.0.22:13378
  - App shows library (even if empty)
  - Offline download tested: add a test audiobook, download in app, verify playable with no network
NOTES:
- Still need to configure client-side (iphone app)
- Session 3: Still pending iOS app setup and offline download test. Blocked on having clean audiobook content to test with. Library path confirmed correct in container config.
- Session 5: ABS web UI confirmed working. Library path set to /audiobooks. iOS app not yet installed. Import workflow explored — user can drop files directly into /mnt/data/audiobooks and ABS will detect on library scan without involving LL. Permissions issue on /mnt/data/audiobooks resolved.

### T1-16 : Set up AI sandbox container
STATUS: TODO
BLOCKED BY: T1-13
ACCEPTANCE CRITERIA:
  - ai-sandbox container running (confirmed via docker ps)
  - network_mode: none confirmed (container cannot reach internet)
  - /mnt/data/ai-sandbox accessible from inside container as /workspace
  - Test: `docker exec -it ai-sandbox bash` → `ls /workspace` → exits cleanly
  - Test: create file in /mnt/data/ai-sandbox on Pi host → verify visible inside container
NOTES:

---

## ~~PHASE 1.5 : Book/Audiobook Automation Gap (added Session 2)~~
Goal: Replace manual browser search + copy-paste workflow with automated or near-automated book and audiobook acquisition. Identified as a gap during Phase 1 — Prowlarr alone is insufficient for this use case.
### T1-17 | Set static DHCP lease in router
STATUS: Skipped
PRIORITY: Low — router does not support custom DHCP DNS. IP has been stable. Revisit if IP changes.
ACCEPTANCE CRITERIA:
  - Router admin UI used to assign permanent DHCP reservation for Pi MAC → 192.168.0.22
  - Pi IP confirmed stable after reboot
NOTES: Was T1-06 in original plan. Not completed Session 2. Not blocking anything critical since IP has been stable.


### ✔️⛔️ T1-18 : Connect qBittorrent to Prowlarr as download client
STATUS: Partial
BLOCKED BY: T1-30 (directory structure must exist before download client config is meaningful)
BLOCKED BY: nothing — ready to do
ACCEPTANCE CRITERIA:
  - In Prowlarr: Settings → Apps → Add Application → qBittorrent
  - Prowlarr Server: http://localhost:9696
  - qBittorrent Host: http://192.168.0.22 (use Pi IP, not localhost — qBittorrent is native, not in Docker)
  - Port: 8080
  - Username and password: qBittorrent web UI credentials
  - Test connection succeeds
  - Search result in Prowlarr can be sent directly to qBittorrent
NOTES: 
- Not completed Session 2. Required for Prowlarr to be useful as more than a search engine.
- Session 4: Prowlarr→qBittorrent download client connection is the only  remaining criteria. Deferred until T1-30 establishes clean directory structure. Torznab connection to LL is a separate concern handled in T1-26.

### ~~T1-19 : Add FlareSolverr container for Cloudflare bypass~~
STATUS: Skipped
STATUS: TODO
BLOCKED BY: T1-18
ACCEPTANCE CRITERIA:
  - FlareSolverr added to docker-compose.yml
  - Container running via docker compose up -d
  - In Prowlarr: Settings → Indexers → Indexer Proxies → Add → FlareSolverr
  - FlareSolverr URL set to http://flaresolverr:8191 (Docker internal network name)
  - Cloudflare-blocked indexers retested and returning results
NOTES: 
- ~~FlareSolverr runs a headless browser to solve Cloudflare challenges on behalf of Prowlarr. Required for several indexers that were blocked during Session 2. Use image: ghcr.io/flaresolverr/flaresolverr:latest — check for aarch64 compatibility before adding.~~
- FlareSolverr runs a headless browser to solve Cloudflare challenges on behalf of Prowlarr. Required for 1337x and potentially other general indexers. For book/audiobook use case, evaluate Lazy Librarian (T1-20) first — it may handle AudioBookBay natively without needing FlareSolverr at all, which could reduce priority of this task. Use image: ghcr.io/flaresolverr/flaresolverr:latest — verify aarch64 compatibility before adding. 
- Reorder: complete T1-20 evaluation before investing time here. 
- Additionally: before investing time in FlareSolverr for AudioBookBay specifically, search GitHub for an existing AudioBookBay Cardigann definition (search "AudioBookBay cardigann" or "AudioBookBay yml jackett"). If a community definition exists it can be dropped into Prowlarr's custom definitions folder directly. If none exists, writing one is also viable once Lazy Librarian has been assessed. Two parallel paths to AudioBookBay in Prowlarr: (1) find/use existing Cardigann definition, (2) write one from scratch. Neither is urgent until T1-20 assessment is complete.
- Session 5: Skipped entirely. LL native providers confirmed non-functional
  (AudioBookBay 404ing, TPB rate-limited, TDL 403 blocked). All audiobook
  indexer access now handled via Jackett Torznab connections directly from LL.
  FlareSolverr not needed for this use case. Revisit only if general Prowlarr or Jackett
  indexers need Cloudflare bypass for future \*arr suite use. For audiobooka, lazy librarian, and audiobookshelf use cases, this can be deferred for now.
### T1-19.1 | Investigate Jackett Cardigann definitions for AudioBookBay in Prowlarr
STATUS: TODO
BLOCKED BY: T1-25 (confirm LL providers first)
ACCEPTANCE CRITERIA:
- github.com/Jackett/Jackett checked for AudioBookBay .yml definition
	- https://github.com/Jackett/Jackett/blob/master/src/Jackett.Common/Indexers/Definitions/AudioBookBay.cs
	- https://github.com/Jackett/Jackett/blob/master/src/Jackett.Common/Indexers/Definitions/EpubLibre.cs
  - If found: copied to /home/sutton585/config/prowlarr/Definitions/Custom/
  - Prowlarr restarted and AudioBookBay appears in indexer catalog
  - Test search returns results, otherwise, do the files need adjustment to work in prowlarr, or are the same files able to work as-is?
NOTES:
Session 3: Prowlarr uses same Cardigann format as Jackett. Community
definitions are drop-in compatible. AudioBookBay is highest priority
missing indexer. Check Jackett repo before writing a custom definition
from scratch.
Session 3.5: files copied via samba to HDD /mnt/data/downloads

### ✅ T1-20 : Evaluate and install Lazy Librarian
STATUS: Done
BLOCKED BY: T1-18
ACCEPTANCE CRITERIA:
  - Confirm Lazy Librarian has working aarch64 Docker image
  - Add to docker-compose.yml
  - Container running, web UI accessible
  - Connected to qBittorrent as download client
  - Connected to Audiobookshelf library path (/mnt/data/audiobooks)
  - Test search for an audiobook returns results
  - Test download completes and file appears in Audiobookshelf library
NOTES: 
- ~~Lazy Librarian is a book/audiobook automation tool similar to Sonarr/Radarr but for books. Integrates with multiple book sources including AudioBookBay and others. Identified as solution to gap where Prowlarr catalog lacks book/audiobook indexers. Verify source support (AudioBookBay, Anna's Archive, Libgen) before committing. Port is typically 5299 — add to ports registry in README.~~
- Lazy Librarian is a book/audiobook automation tool similar to Sonarr/Radarr but for books. Has direct integrations with AudioBookBay, Libgen, and other sources that bypass Prowlarr entirely — may solve the AudioBookBay gap without FlareSolverr. Verify aarch64 Docker image availability before committing. Check which sources it supports natively: AudioBookBay, Libgen, Goodreads metadata. Port typically 5299 — add to ports registry in README if confirmed. If Lazy Librarian handles AudioBookBay natively, T1-19 (FlareSolverr) becomes lower priority and can be deferred until needed for general Prowlarr indexers.
- Session 3: Lazy Librarian installed and operational. 
	- Anna's Archive .org domain seized by court order Jan 2026 — updated to annas-archive.li. 
	- Error message in LL says direct downloads from Anna's Archive require paid membership key (401 error confirmed). Docs confirm, membership is required. have to determine what minimum donation is to get a membership.
	- Libgen and Zlip both configured as direct providers, also not working.
	- Built-in torrent providers enabled in LL. 
	- First successful download confirmed (Rothfuss - The Narrow Road Between Desires via LimeTorrents). 
	- Post-processor working correctly — file renamed and moved to /mnt/data/books with correct Author/Series/Book folder structure. 
	- qBittorrent default save path was incorrectly set to /home/sutton585/Downloads — corrected to /mnt/data/downloads. Incomplete torrents path set to /mnt/data/torrents/incomplete. 
	- Docker daemon DNS set to 8.8.8.8 globally via /etc/docker/daemon.json. 
	- LL cache directories (JSONCache, HTMLCache) had to be manually created — LL does not create them on first run. 
	- DNB provider disabled due to missing pkg_resources Python module bug in image. 
	- HardCover disabled — no API key. 
	- Anna's Archive disabled — too many 401 failures polluting logs.
- Session 5: Confirmed complete. LL operational, downloading via Jackett Torznab connections. Six Torznab connections added covering AudioBookBay and other indexers. End-to-end download chain confirmed working. AudioBookBay is the primary and most reliable audiobook source. Only potential loose end is if audiobookshelf setup has issues discovering files.

### T1-21 : Complete Audiobookshelf setup
STATUS: TODO
BLOCKED BY: T1-20 (want library workflow clear before finalizing setup)
ACCEPTANCE CRITERIA:
  - Library added pointing to /audiobooks (maps to /mnt/data/audiobooks)
  - Library scan runs without errors
  - iOS app installed on David's iPhone
  - App connected to server at 192.168.0.22:13378
  - Offline download tested with a real audiobook file
NOTES: 
- Web UI and admin account confirmed working in Session 2. Library and app setup deferred until download workflow is resolved.
- Session 3: LL processing confirmed working. Download path, folder naming patterns, and file structure all verified. Colon characters in filenames cause macOS/Samba visibility issues — LL filename patterns updated to avoid colons. Samba catia module added as safety net. No testing has been done to confirm caria module is functioning to spec.
- Session 5: In progress. ABS library setup started but not validated end to end. Key understanding: ABS reads metadata from folder structure first, embedded ID3 tags second. Clean LL folder structure is sufficient for ABS to identify author, title, series correctly without custom tags. SERIES and SERIES-PART are non-standard ID3 fields ABS reads natively — can add via Mp3tag custom fields if needed later. Not required for MVP.

### ~~T1-22 : Prowlarr indexer audit and cleanup~~
STATUS: Skipped
BLOCKED BY: T1-19, T1-20 (want full picture before finalizing indexer list)
REVISED ACCEPTANCE CRITERIA (SESSION 4):
  - All direct indexers removed from Prowlarr
  - Only connection remaining in Prowlarr indexers: Jackett Torznab
  - Prowlarr functions as clean pass-through to Jackett, not hybrid
  - Test search in Prowlarr returns results sourced via Jackett only
  - Confirmed: no direct indexers in Prowlarr that aren't also in Jackett
~~ORIGINAL ACCEPTANCE CRITERIA (OUTDATED):~~
  - ~~All indexers with SSL errors removed (ebookbay confirmed dead)~~
  - ~~All indexers returning no results removed (isohunt2 confirmed dead)~~
  - ~~Adult content indexers retained but documented — confirm family-facing~~
    ~~services (Audiobookshelf) are unaffected by their presence~~
  - ~~Final confirmed indexer list documented in a NOTES entry here~~
  - ~~Recommended keepers: YTS, EZTV, 1337x (pending FlareSolverr), SkidrowRepack~~
    ~~(low priority until x86), Russian book tracker (user has account)~~
  - ~~Recommended removals: ebookbay, isohunt2, BTdirectory, btstate, damag,~~
    ~~magnet cat, postman, extratorrent, KickassTorrents clones~~
NOTES: 
- Adult content indexers are Prowlarr admin-only and do not surface in Audiobookshelf or any family-facing interface. No per-user restriction needed — access control is handled by the fact that family members never access Prowlarr.
- Session 4: Approach revised. Original plan was to audit and retain  selective indexers in Prowlarr. New approach: remove all direct indexers from Prowlarr entirely. Jackett is the indexer layer. Prowlarr is the routing and category-filtering layer. Cleaner separation of concerns. When *arr suite arrives on x86, Prowlarr's value is routing to the right app, not managing indexers directly.
-  Session 5: Architecture changed. LL connects directly to Jackett via per-indexer Torznab URLs, bypassing Prowlarr entirely for the book/audiobook workflow. Prowlarr's role is now limited to future \*arr suite routing on x86 machine. Direct indexer cleanup in Prowlarr is deferred until that phase begins.

### ✅ T1-23 : Samba share for external drive
STATUS: DONE
ACCEPTANCE CRITERIA:
  - Samba installed via apt
  - [media] share defined in /etc/samba/smb.conf pointing at /mnt/data
  - sutton585 Samba password set via smbpasswd
  - Share accessible from MacBook at smb://rascal.local/media
  - Share accessible from Finder sidebar, persists across sessions
  - mangled names = no and catia module configured for macOS filename compatibility
NOTES:
- Session 3: Completed. Share working and visible in Finder as rascal.local. Colon characters in filenames were invisible to macOS — resolved via catia vfs module in smb.conf and fixing LL filename patterns to avoid colons. Auto-connect on login configured via macOS Login Items.

### ==🚧 T1-24 : Manual torrent intervention workflow in LazyLibrarian==
STATUS: In Progress
BLOCKED BY: T1-30 (directory config must be clean before meaningful testing)
ACCEPTANCE CRITERIA:
  - User can trigger a manual search for a specific wanted item
  - User can view which providers were queried and what each returned
    (confirm via debug logs: docker logs lazylibrarian --tail 100 | grep -i
    "provider\|search\|found\|AudioBookBay\|limetorrent")
  - User can confirm AudioBookBay is being queried — not just LimeTorrents
  - User can manually select a specific torrent result and send to qBittorrent
    even when title is not an exact match
  - User understands how to handle series packs that don't match individual
    book requests
  - Workflow documented as repeatable SOP for edge cases automation can't handle
NOTES:
- Session 3: Identified as key gap. Automation works for exact title matches but breaks down for series packs, alternate editions, and audiobook torrents where naming doesn't match LL's expected pattern.
	- Key open question: LL claims AudioBookBay is configured but there is no confirmation it is actually being queried. Debug log trace is needed to verify provider cycling. If AudioBookBay is actually being searched, it should find almost any audiobook currently in the wanted list.
	- Next session: set log level to Debug, trigger a manual search, grep for each provider name to confirm all are being queried in sequence.
- Session 4: Elevated to explicit blocker for T1-26. Must confirm LL is actually querying its built-in providers before adding Torznab. Silent failures at this layer make Torznab debugging significantly harder.
- Session 5: Partially understood. User can trigger manual search per book via
  AudioBooks page. Full manual result selection flow not yet fully documented.
  LL does show results and allows manual selection when automatic match fails.
  Workflow documentation still needed as acceptance criteria item.

### ~~T1-25 : Confirm LL built-in torrent providers working for audiobooks~~
STATUS: Skipped
BLOCKED BY: T1-30
ACCEPTANCE CRITERIA:
  - Log level set to Debug, manual search triggered, provider query sequence
    confirmed for each enabled provider (not just LimeTorrents)
  - AudioBookBay confirmed as highest priority in LL provider config
  - Anna's Archive Types field set to AE (audiobook + ebook, no separator needed)
  - At least one audiobook successfully downloaded via built-in torrent provider
  - If AudioBookBay queries confirmed but returning zero results: investigate
    whether Cardigann definition exists at github.com/Jackett/Jackett and
    import into Prowlarr custom definitions as alternative path
  - Search trace completed: wanted → search → match → qBittorrent confirmed
  - Manual intervention workflow documented per T1-24
NOTES:
- Session 3: One ebook downloaded via LimeTorrents, zero audiobooks. Root cause unknown — may be provider not actually being queried, naming mismatch, or AudioBookBay returning no results for searched titles. Debug log trace is the first diagnostic step. Do not add Torznab complexity until built-in providers confirmed working or confirmed insufficient. Anna's Archive Types field clarified: use AE for both audio and ebook, A for audiobook only. No comma, not case sensitive.
- Session 4: Explicit blocker for T1-26. Procedure: set LL log level to Debug, trigger manual search, run: ``` docker logs lazylibrarian --tail 200 | grep -i "provider\|AudioBookBay\|limetorrent\|search\|found\|error"```
	- Confirm each provider appears in sequence. Confirm AudioBookBay is queried  not just configured. If providers are queried but returning zero results,  that is a different problem than providers not being queried at all.  Distinguish between the two before proceeding.
- Session 5: Investigation completed. LL native providers confirmed non-functional: AudioBookBay returning 404 (domain changed, hardcoded in image), TPB rate-limited to 429, TDL blocked with 403. Provider blocklist was masking the root cause — providers were being skipped entirely, never appearing in logs. Native providers are not a viable path. All audiobook indexing now via Jackett Torznab. This task is resolved by the architecture change, not by fixing native providers.

### ✅ T1-26 : Connect Torznab (Jackett → LL) as primary torrent source
STATUS: Done
BLOCKED BY: T1-24, T1-25, T1-22, T1-18
ACCEPTANCE CRITERIA:
  - Prowlarr API key retrieved and entered in LL Torznab config
  - Torznab URL set to http://prowlarr:9696 (container name, same Docker network)
  - LL successfully queries Prowlarr indexers via Torznab
  - Prowlarr treated as fallback — LL built-in providers take priority
  - Test search returns results from Prowlarr indexers
  - Successful download via Torznab path confirmed
NOTES:
- Session 3: Torznab connection not yet set up. Deliberately deferred until  built-in providers confirmed working (T1-25). Prowlarr API key already  retrieved during session. URL will be http://prowlarr:9696 using Docker  container name resolution. 
- Session 4: Torznab URL confirmed as http://prowlarr:9696 (container name). Categories field to set: 3030,7000,7020,7050. Jackett→Prowlarr Torznab connection confirmed working. LL Torznab config to be completed next session. T1-25 blocker removed — sufficient confidence in chain to proceed.
- Session 5: Completed with architecture change. LL connects directly to Jackett
  via per-indexer Torznab URLs, not via Prowlarr. Six Torznab connections added.
  Immediate results confirmed on first connection — AudioBookBay returned results
  for a book that had zero results from all native providers. This is the canonical
  approach going forward. Prowlarr is not in the LL indexer chain, nor are lazylibrarian's built-in torrent trackers. All is handled via torznab connection to Jackett.

### ✅ T1-27 : Install Jackett for AudioBookBay and other missing indexers
STATUS: Done
BLOCKED BY: ~~T1-13~~, T1-25, T1-26
ACCEPTANCE CRITERIA:
  - Jackett added to docker-compose.yml
  - Container running, web UI accessible at http://192.168.0.22:9117
  - AudioBookBay indexer added and tested in Jackett — returns results
  - epubLibre added if yml or cs available
  - Jackett connected to Prowlarr as a Torznab source
    (Prowlarr → Settings → Indexers → Add → Torznab → Jackett URL)
  - AudioBookBay results visible in Prowlarr via Jackett passthrough
NOTES:
- Session 3: Jackett chosen over custom Cardigann yml because AudioBookBay uses complex C# parsing including base64 decoding of hidden posts — not easily expressible in declarative yml format. Jackett natively supports AudioBookBay via compiled .cs indexer. Standard pattern: Jackett feeds into Prowlarr via Torznab, Prowlarr feeds into LL via Torznab. Ports registry: add 9117 to README.
- Session 4: Jackett installed and running. AudioBookBay confirmed added.  Jackett→Prowlarr Torznab connection tested green. Remaining criteria  (LL receiving results via full chain) blocked until T1-25 and T1-26 complete.
- Session 5: Confirmed complete. Jackett running, AudioBookBay confirmed working, six indexers connected via Torznab to LL. Full chain validated end to end.

### ✅ T1-28 : Complete download chain: Jackett → LL → qBittorrent
STATUS: Done
BLOCKERS: T1-18, T1-25, T1-27
ACCEPTANCE CRITERIA:
  - Jackett running with AudioBookBay confirmed working (T1-27)
  - Jackett added to Prowlarr as Torznab indexer source
  - Prowlarr API key added to LL Torznab config
  - LL Torznab URL set to http://prowlarr:9696 (Docker container name)
  - LL provider priority confirmed: built-in trackers first, Torznab/Prowlarr
    second, direct providers (Anna's Archive, Libgen) last
  - Full chain tested end to end:
    LL wanted → Torznab search → Prowlarr → Jackett → AudioBookBay
    → result returned → sent to qBittorrent → downloaded to /mnt/data/downloads
  - Post-processor confirmed picking up completed download
  - File renamed and moved to correct library folder
NOTES:
- Session 3: Full chain not yet connected. This task represents the complete automation pipeline. Do not mark done until an audiobook has completed the entire chain without manual intervention.
- Session 5: Confirmed working. Chain is LL → Jackett Torznab → AudioBookBay
  (and other indexers) → result → qBittorrent → /mnt/data/downloads.
  Post-processor confirmed moving files to library directories. Multiple series
  marked as Wanted and downloads confirmed in qBittorrent. Prowlarr is not in
  this chain — architecture simplified from original plan.

### T1-29 : Audiobookshelf iPhone app setup and offline listening validation
STATUS: TODO
BLOCKED BY: T1-21 (ABS library setup must be confirmed first)
ACCEPTANCE CRITERIA:
  - App options researched at install time: check App Store rating and 
    reviews for official Audiobookshelf app, note any viable alternatives
  - Official Audiobookshelf iOS app installed (free, same developer as server)
  - App connected to server at 192.168.0.22:13378
  - At least one audiobook visible in library
  - Audiobook downloaded to device for offline listening
  - Offline playback confirmed: airplane mode on, book plays without 
    network connection
  - Progress sync confirmed: listen on iPhone, progress reflected in 
    server web UI
NOTES:
Session 4: Official Audiobookshelf iOS app is the clear primary option —
first-party, purpose-built, free, same developer as server. Historically
rated 4.5+ on App Store. Supports offline download as explicit design goal,
not an afterthought. Progress syncs back to server. Third-party clients
exist in theory but none with meaningful adoption — API is purpose-built
for the official client. Android version also available for family member
onboarding (T2-04). Verify current App Store rating at install time rather
than assuming — confirm no major known iOS version bugs in recent reviews.

### T1-30 : Configure qBittorrent categories and LL directory mapping
STATUS: TODO
BLOCKED BY: T1-20 (LL operational — confirmed)
ACCEPTANCE CRITERIA:
  - qBittorrent categories created with explicit save paths:
    "audiobooks" → /mnt/data/downloads/audiobooks
    "books"      → /mnt/data/downloads/books
  - Subdirectories created on external drive if not already present:
    /mnt/data/downloads/audiobooks
    /mnt/data/downloads/books
  - LL config updated:
    Audiobook download dir → /mnt/data/downloads/audiobooks
    eBook download dir     → /mnt/data/downloads/books
  - LL docker-compose.yml volumes tightened to explicit mounts only:
    /mnt/data/downloads/audiobooks → /downloads/audiobooks
    /mnt/data/downloads/books      → /downloads/books
    /mnt/data/audiobooks           → /audiobooks
    /mnt/data/books                → /books
  - LL set to use qBittorrent category tags when submitting torrents
  - Test download confirmed landing in correct subdirectory
  - Post-processor confirmed moving file to correct library directory
NOTES:
- Session 4: Current state — LL respects qBittorrent default save path  which was previously misconfigured to /home/sutton585/Downloads.  Corrected to /mnt/data/downloads in Session 3 but no per-category  separation exists yet. This task establishes clean separation of concerns so LL,  future Sonarr, Radarr, and manual downloads never cross-contaminate.
- Session 5: Partially done. qBittorrent Default Torrent Management Mode set to Automatic. Category save path behavior confirmed. Subdirectories need creation and LL config needs updating to match. Not yet confirmed end to end.

### ✅ T1-31 : Confirm /mnt/data directory permissions and ownership
STATUS: Done
ACCEPTANCE CRITERIA:
  - All directories under /mnt/data owned by sutton585:sutton585
  - Permissions set to 755 across all subdirectories
  - Docker containers can write to their mapped volumes
  - Samba can write to /mnt/data from MacBook
NOTES:
- Session 5: Fixed this session. Root ownership was blocking LL from writing to /audiobooks volume. Fixed with:
```bash
sudo chown -R sutton585:sutton585 /mnt/data
sudo chmod -R 755 /mnt/data
```
  Root cause: directories created during early setup before ownership was established. Future directories should be created as sutton585 directly.

### ✅ T1-32 : Docker memory limits and cgroup kernel support
STATUS: Done
ACCEPTANCE CRITERIA:
  - cgroup_enable=memory cgroup_memory=1 added to /boot/firmware/cmdline.txt
  - Pi rebooted with new kernel flags
  - docker inspect [container] confirms Memory field is non-zero
  - docker stats shows per-container limits not full 906MiB for each container
  - All containers in docker-compose.yml have deploy.resources.limits.memory set
NOTES:
- Session 5: Completed after OOM crash caused by LL flooding qBittorrent with simultaneous torrent requests for multiple series. Pi crashed repeatedly. Physical console access required to fix. Lessons:
  1. Never mark entire series as Wanted simultaneously on 1GB RAM machine
  2. Pi requires explicit kernel flag to support Docker memory limits
  3. deploy.resources.limits syntax required (not deprecated mem_limit syntax)
- Memory limits per container: lazylibrarian 200m, audiobookshelf 256m, prowlarr 128m, jackett 128m, sandman 128m. Power issues also identified and resolved: powered USB hub for external drive, better 5V/2.5A charger. vcgencmd get_throttled command documented for
  future power diagnostics.

---
## PHASE 2 — Automation and Polish (after Phase 1 complete)

### T2-01 : VPN configuration
STATUS: TODO
BLOCKED BY: Phase 1 complete
PRIORITY: HIGH — required before seeding is enabled
ACCEPTANCE CRITERIA:
  - VPN client installed and configured on Pi
  - Kill switch configured (no traffic if VPN drops)
  - qBittorrent bound to VPN interface only
  - Only after above confirmed: upload cap raised from 1 KB/s, seeding ratio adjusted
NOTES: VPN provider not yet selected. Research needed. Mullvad and ProtonVPN are common self-hosted choices.

### T2-02 : Torrent completion scripts (auto-sort downloads)
STATUS: TODO
BLOCKED BY: T1-11 complete, T1-15 complete
ACCEPTANCE CRITERIA:
  - Script created that runs when qBittorrent torrent completes
  - Script moves/copies files to correct library folder based on category:
    audiobooks → /mnt/data/audiobooks
    ebooks → /mnt/data/books
  - Audiobookshelf detects new files automatically after move
  - Script tested end-to-end with a real download
NOTES:

### T2-03 : Kindle delivery automation
STATUS: TODO
BLOCKED BY: T2-02
ACCEPTANCE CRITERIA:
  - msmtp installed and configured with sending email credentials
  - Completion script extended to email epub to [kindle]@kindle.com on completion
  - Amazon Kindle email whitelist updated to allow sending address
  - Test epub delivered successfully to Kindle device
NOTES: May require Calibre headless for format conversion if epub needs processing first.

### T2-04 | Family member Audiobookshelf onboarding
STATUS: TODO
BLOCKED BY: T1-15 complete, library has some content
ACCEPTANCE CRITERIA:
  - Family member accounts created in Audiobookshelf
  - Android app installed on family device
  - David configures server URL — family member does not need to touch settings
  - Family member can browse library and download a book without David's help
  - Family member can listen offline (in car, no WiFi)
NOTES:

### T2-05 : Docker container auto-updates
STATUS: TODO
BLOCKED BY: Phase 1 complete
ACCEPTANCE CRITERIA:
  - Watchtower container added to docker-compose.yml
  - Configured to auto-pull and restart updated images on a schedule
  - OR documented manual update procedure: docker compose pull && docker compose up -d
NOTES: Decision needed: automated vs manual updates. Manual is safer for a learning context. Add to DECISIONS.md when decided.

### T2-06 : Reverse proxy for friendly local URLs
STATUS: TODO
BLOCKED BY: Phase 1 complete
ACCEPTANCE CRITERIA:
  - Nginx Proxy Manager or Caddy running as Docker container
  - Local DNS entries added in PiHole custom DNS:
    audiobooks.home → 192.168.0.22
    prowlarr.home → 192.168.0.22
  - Services accessible via friendly URLs instead of IP:port
NOTES: Lower priority. IP:port access is functional. This is a polish task.

---

---

## PHASE 2.5 — Side Projects and Quality of Life (non-blocking)

### T2.5-01 : Local web page on Pi via lighttpd
STATUS: TODO
ACCEPTANCE CRITERIA:
  - /var/www/html/home/ directory created
  - index.html serving at http://rascal.local/home
  - Content pulled from GitHub repo via cron job (*/5 * * * *)
  - Page useful as landing page for family or self (links to services etc.)
NOTES:
Session 3: lighttpd already running as part of PiHole. Web root at /var/www/html/. GitHub-pull approach agreed as right pattern for real content. Deferred — not blocking anything. Simple hugo setup or similar might be pursued, new tasks will need to be generated based on decisions at that point.

### T2.5-02 : LM Studio setup on MacBook M3 for local coding assistance
STATUS: TODO
ACCEPTANCE CRITERIA:
  - LM Studio installed on MacBook
  - Discussion and confirmed understanding of basics of comparing and choosing LLM models, reviewing their testing metrics, limitations on how performance is reported due to widespread practice of building models specifically to do well on specific test metrics/tasks, making decisions and understanding model's feasibility and estimating trade-offs in performance based on model specs and system hardware specs.
  - Coding-focused model pulled (Qwen2.5-Coder or DeepSeek-Coder, 7B or 13B quantized)
  - Local API endpoint confirmed working
  - Continue.dev or equivalent VS Code extension connected to local model
  - Basic coding assistance tested and usable
NOTES:
Session 3: M3 MacBook confirmed as right hardware for local inference. 16GB unified memory handles 7B-13B models well. Pi too weak for meaningful inference — not a candidate.

### T2.5-03 : Project Sandman — overnight scrape and summarize pipeline
STATUS: TODO
BLOCKED BY: T2.5-02 (or decision to use API instead of local model)
ACCEPTANCE CRITERIA:
  - Scraper configured for target sources (TBD — online posts/forums)
  - Markdown conversion working (trafilatura or readability)
  - LLM prompt filters and ranks posts by user-defined criteria
  - Pipeline runs on cron schedule overnight
  - Morning digest output in readable format (markdown file, email, or similar)
  - Decision made: fully local (LM Studio) vs hybrid (local scrape + Claude/Gemini API)
NOTES:
Session 3: Use case defined — running ai processes off peak hours to accomodate the most powerful hardware being the daily driver laptop. Initial prokect for gaining compentency and validating this as proof-of-concept for off hours ai task processing is a simple project where online posts are scraped, convert to markdown, then LLM ranks which are worth showing the user according to programmed rubric. Hybrid approach (local scrape + API inference) may give better results at negligible cost for nightly digest. Architecture not yet designed, tasks need to be generated upon initiation of this pursuit.

### T2.5-04 : Second Pi as dedicated AI/LLM experimenter
STATUS: TODO
BLOCKED BY: Primary Pi stack stable (Phase 1 complete)
ACCEPTANCE CRITERIA:
  - Second Pi 3 (same model as Rascal) configured with 64-bit OS
  - Docker installed
  - Role defined: API proxy, scheduler, or lightweight model host
  - Connected to home network with static DHCP reservation
NOTES:
Session 3: Second Pi identified as available hardware. Too weak for serious inference but useful as dedicated experimenter/scheduler separate from primary Pi. Revisit after Phase 1 complete. "Project Sandman" is to utilize local compute power (local LLM), but when relying on external compute power (claude code, gemini CLI, etc.) a weaker machine can be the one making the calls. Project and tasks need definition: what determines which tasks are done locally versus spending tokens on? When is local important for privacy or concerns or censorship avoidance?
### T2.5-05 | Remote access via Tailscale (or Headscale)
STATUS: TODO
BLOCKED BY: Nothing — can be done anytime
ACCEPTANCE CRITERIA:
  - Decision made: Tailscale (Tailscale coordination server) vs Headscale
    (self-hosted coordination, no third-party metadata visibility)
  - Chosen client installed on Pi
  - Tailscale/Headscale installed on MacBook and iPhone
  - Pi services reachable from outside home network via Tailscale IP
  - SSH to Pi confirmed working over Tailscale from iPhone/MacBook off-network
  - Audiobookshelf, Prowlarr, LL accessible via Tailscale IP from outside
NOTES:
Session 4: Tailscale uses WireGuard for traffic (strong, audited). 
Coordination metadata (device list, connection times, account identity) 
visible to Tailscale Inc — a US company subject to compelled disclosure. 
Headscale eliminates that: self-hosted coordination plane, no external 
visibility, same WireGuard underneath. Requires Pi reachable from outside 
(port forward or VPS relay). User is privacy-conscious — flag Headscale 
as the right answer if threat model includes government metadata requests.
### T2.5-06 : Calibre Web for ebook reading and library management
STATUS: TODO (OPTIONAL)
BLOCKED BY: Phase 1 complete
ACCEPTANCE CRITERIA:
  - Evaluate if this is a priority use-case, user might not ever need server-based reading unless it can sync to devices like kindle, ipad, etc.
  - Calibre Web running as Docker container
  - Connected to /mnt/data/books as library source
  - Browser-based reading confirmed working on MacBook and iPhone
  - LL ebook-convert path configured if format conversion needed
NOTES:
Session 3: Calibre Web provides browser-based ebook reader on top of
existing library. LL can use headless Calibre for format conversion
(epub → mobi etc). Separate concern from Calibre Web UI. Evaluate
whether format conversion is actually needed before installing.

### T2.5-07 : PhotoPrism for photo/video backup and browsing
STATUS: TODO
BLOCKED BY: Phase 1 complete — evaluate RAM requirements first
ACCEPTANCE CRITERIA:
  - Evaluate other options, there should be several competitors in this space. Decide if this task is worthwhile, or if other provider is better fit.
  - RAM usage benchmarked — may require x86 machine (D-009)
  - PhotoPrism running as Docker container
  - Photo library imported and browsable
  - Mobile app confirmed working on iPhone
NOTES:
Session 3: Identified as Google Photos / iCloud alternative.
Docker image available, good mobile support. RAM-intensive —
may not be suitable for Pi 3 with 1GB RAM. Revisit when x86
machine acquired.

---

## PHASE 2.5-S — Project Sandman: Personal Automation & MCP Platform

### Overview

Project Sandman is a personal automation platform built on industry-standard tooling. The goal is to build reusable, callable tools that collect, process, and surface information — and expose them through standard protocols so they can be orchestrated by AI agents, workflow engines, or scheduled scripts.

The platform has three layers:

**Tools** — standalone Python scripts that do one thing well. Fetch emails, scrape Reddit, parse job postings, query a database. Each tool has a clean interface, runs independently, and produces structured output (SQLite + markdown + JSON). These are the building blocks.

**MCP Server** — a lightweight server running on Rascal that exposes tools as callable endpoints following the Model Context Protocol standard. Any MCP-compatible client (Claude, Gemini, future agents) can discover and call these tools over the LAN. This is how AI agents interact with your personal data and automations.

**Orchestration** — a workflow engine (n8n or equivalent) that chains tools together into automated workflows on a schedule or trigger basis. Runs on Rascal if RAM allows, otherwise on the MacBook overnight or the future x86 machine. This layer is deliberately deferred — tools come first.

### Architecture Principles

- Tools are the priority. Orchestration is replaceable; well-built tools are not.
- Each tool is useful standalone. MCP and orchestration are convenience layers on top.
- Pi handles always-on I/O work. MacBook or future x86 handles compute-heavy processing.
- Standard protocols throughout. MCP for tool exposure, REST where appropriate, SQLite as the shared data layer between tools.
- Learn transferable skills. Every decision should prioritize patterns used in professional environments.

### Hardware Strategy

**Rascal (Pi 3, always-on)**
- Runs lightweight Python tools on schedule via cron or MCP calls
- Hosts SQLite databases — source of truth for all collected data
- Hosts MCP server — exposes tools to LAN clients
- Hosts lightweight orchestration if RAM allows

**MacBook (overnight, when available)**
- Docker container running heavier orchestration or LLM processing
- Calls tools on Rascal via MCP over LAN
- Stopgap until x86 machine acquired

**Future x86 machine**
- Full orchestration stack (n8n or equivalent)
- Local LLM inference (Ollama)
- All heavy processing moves here permanently

---

### TS-01 | Update architecture documentation for new scope
STATUS: TODO
ACCEPTANCE CRITERIA:
  - Ecosystem README updated to replace metaphor-specific terms (grains, dreams)
    with industry-standard terms (tools, integrations, automations, workflows)
  - Document reflects three-layer architecture: tools, MCP server, orchestration
  - Hardware strategy documented: Pi for I/O, MacBook overnight, x86 future
  - Open questions section retained — implementation details still TBD
  - Document suitable as onboarding reference for the project
NOTES:
  Sandman ecosystem README lives in the sandman repo. Keep the Sandman name
  as the project name — just standardize the internal terminology.

### TS-02 | Evaluate orchestration options
STATUS: TODO
BLOCKED BY: TS-01
ACCEPTANCE CRITERIA:
  - n8n evaluated: RAM requirements benchmarked on Pi 3, confirmed viable or not
  - Huginn evaluated as lightweight alternative if n8n too heavy for Pi
  - MacBook Docker overnight option documented as fallback
  - Decision made and recorded: which orchestration tool, on which hardware
  - If n8n: confirm aarch64 Docker image availability
  - Result documented in DECISIONS.md
NOTES:
  Do not build a custom orchestration layer (original Sandman controller concept)
  until this evaluation confirms no existing tool meets the need. Strong prior
  toward using something that already exists.

### TS-03 | Define and document sandman_core shared library
STATUS: TODO
BLOCKED BY: TS-01
ACCEPTANCE CRITERIA:
  - Decision made on where core lives: inside sandman repo, or standalone repo
  - Decision made on how tools import it: local path, git dependency, or other
  - Interface defined for: markdown conversion, SQLite base schema, file writer,
    standardized logger
  - Interface documented well enough that a new tool can be built against it
    without ambiguity
  - Result documented — not necessarily implemented yet
NOTES:
  Core exists to prevent duplicating storage, conversion, and logging logic
  across every tool. Decision on structure should precede building any new tool.
  Digestitor is the reference implementation to extract patterns from.

### TS-04 | Build gmail tool
STATUS: TODO
BLOCKED BY: TS-03
ACCEPTANCE CRITERIA:
  - Standalone Python script: python gmail_tool.py runs independently
  - Authenticates via Gmail API using stored OAuth2 credentials
  - Queries primary inbox (davidsutton585@gmail.com) and delegate
    (suttoncx@googlemail.com) using same token
  - Pattern matching configurable: by label, sender, subject
  - Each matched email stored as: SQLite record, JSON file, markdown file
  - Markdown output uses standard frontmatter schema (id, source, date, labels,
    sender, subject)
  - Deduplication by Gmail message ID — re-running never creates duplicate records
  - Logging to file, explicit errors, no silent failures
  - Importable as a module: from gmail_tool import GmailFetcher
  - Config-driven: pattern rules defined in config file, not hardcoded
NOTES:
  OAuth2 one-time auth flow run on MacBook. token.json stored at
  /home/sutton585/config/sandman/ on Rascal. Credentials never in repo.
  See sandman-project-spec.md for full schema and directory layout.

### TS-05 | Build job parser tool
STATUS: TODO
BLOCKED BY: TS-04
ACCEPTANCE CRITERIA:
  - Takes gmail_tool output (job alert emails) as input
  - Extracts individual job postings from each email (one email contains many)
  - Each job stored as its own SQLite record with: title, company, link,
    salary if present, source email ID, source service (LinkedIn, Indeed, etc.),
    search terms that produced it
  - Importable as a module, callable with a config
  - Schema designed to support brain scoring written back to same record later
  - Tracks which sources and search terms produce results over time
NOTES:
  This replaces the AppScript/Google Sheets project. AppScript files should
  be reviewed before building to capture existing pattern matching logic.
  Job grain may be a module inside gmail_tool repo or a separate repo —
  decide when building TS-04 and the boundary becomes clearer.

### TS-06 | Set up MCP server on Rascal
STATUS: TODO
BLOCKED BY: TS-04, TS-05
ACCEPTANCE CRITERIA:
  - MCP server running on Rascal as a lightweight Python process
  - gmail_tool exposed as a callable MCP tool
  - job_parser exposed as a callable MCP tool
  - digestitor exposed as a callable MCP tool
  - Server accessible from MacBook over LAN
  - Claude on MacBook can discover and call tools via MCP
  - Tools callable with arguments matching each tool's config interface
  - Server runs as a systemd service or Docker container — survives reboots
  - Port documented in README ports registry
NOTES:
  MCP server is a thin HTTP layer over existing tool functions. Tools do not
  need to change to be exposed via MCP — server imports and wraps them.
  Evaluate existing MCP server frameworks before writing from scratch.
  This is the milestone where Rascal becomes a personal AI tool server,
  not just a media server.

### TS-07 | Wire digestitor into platform
STATUS: TODO
BLOCKED BY: TS-03, TS-06
ACCEPTANCE CRITERIA:
  - Digestitor refactored to use sandman_core for storage and conversion
    where it makes sense — evaluate carefully, do not break existing functionality
  - Digestitor callable via MCP (covered in TS-06)
  - Output lands in standardized data directory structure
  - Config-driven: subreddit list, schedule, output path all in config file
NOTES:
  Refactor is lower priority than new tools. Only refactor what is needed
  to bring digestitor in line with the platform's shared patterns.
  If refactoring risks breaking working functionality, defer and document
  the divergence instead.

### TS-08 | Evaluate and implement orchestration
STATUS: TODO
BLOCKED BY: TS-02, TS-06
ACCEPTANCE CRITERIA:
  - Chosen orchestration tool installed and running (per TS-02 decision)
  - At least one end-to-end automated workflow running:
    gmail_tool fetches job emails → job_parser extracts jobs → output available
  - Workflow runs on schedule without manual intervention
  - Workflow observable: logs, run history, failure alerts
  - If n8n: confirm MCP integration or HTTP trigger from n8n to MCP server
NOTES:
  This task is intentionally late in the sequence. Tools and MCP server
  must exist before orchestration is worth configuring. Do not start here.

### TS-09 | Brain: LLM integration layer
STATUS: TODO
BLOCKED BY: TS-06
ACCEPTANCE CRITERIA:
  - Decision made on LLM backend priority: Claude API, local Ollama, Gemini CLI
  - Brain callable as an MCP tool — takes markdown input, returns structured output
  - At minimum: job scoring workflow — reads job records, returns ranked list
    with reasoning, writes scores back to job_parser SQLite
  - Prompt templates stored as markdown files in repo, not hardcoded
  - LLM backend configurable — swap Claude for local model without code changes
  - Output format structured and consistent: JSON with defined schema
NOTES:
  Brain is an integration layer, not a new LLM. It routes inputs to available
  models and normalizes outputs. Evaluate LangChain, LlamaIndex, or similar
  before building routing logic from scratch.
  Start with Claude API (lowest friction). Add local model support after
  the interface is proven.

---

## PHASE 2.5-J — Operator: Job Search Automation Platform

### Overview
Operator is a personal job search intelligence system. It evaluates job postings
against a detailed personal profile, generates tailored application materials,
and surfaces non-obvious opportunities where the user's skills create
disproportionate, unexpected advantage. See JOB_SEARCH_README.md for full vision,
principles, and open questions.

Architecture mirrors the Sandman tool pattern: each capability is a standalone
tool with a clean interface, a SQLite database, and markdown output. Tools are
built in order of dependency. The evaluation loop (JS-01 through JS-02) must
work and be validated before any other phase begins.

---

### JS-01 | Build profile.md — personal source of truth
STATUS: TODO
ACCEPTANCE CRITERIA:
  - Single markdown file at defined path in repo
  - Sections defined and populated:
    - Work history: each role with specific outcomes, not responsibilities
    - Projects: what was built, what stack, what it demonstrates
    - Technical skills: each with evidence reference, not just claimed
    - Soft skills and working style preferences
    - Goals: what good looks like in 1 year, 3 years
    - Constraints: salary floor, location, remote requirements
    - Anti-patterns: specific things to screen against regardless of fit score
    - Arbitrage skills: capabilities that create non-obvious advantage in
      non-technical environments, each with a specific scenario description
  - Format validated: an LLM given only this file can answer specific
    questions about experience without hallucinating details
  - Reviewed and confirmed accurate before any tooling is built on top of it
NOTES:
  This is the most important task in the entire phase. Every downstream output
  is only as good as this document. Do not skip or rush it.
  The arbitrage skills section is the novel piece. It should describe not just
  what the user can do but where that capability is rare and unexpected.
  Example: "Agentic AI workflow scripting: advantage in ops-heavy roles at
  non-technical companies. User can automate significant portions of the role
  within weeks of starting without drawing attention."

### JS-02 | Build Phase 0 MVP — folder-based evaluation loop
STATUS: TODO
BLOCKED BY: JS-01
ACCEPTANCE CRITERIA:
  - A folder: /operator/inbox/ — user drops JD markdown files here manually
  - A single script: evaluate.py — reads all files in inbox, reads profile.md,
    calls LLM, writes scored evaluation for each
  - Output per job: markdown file with frontmatter containing:
    - traditional_fit_score (0-100)
    - arbitrage_score (0-100)
    - recommended_action: apply / skip / monitor / research
    - anti_pattern_flags: list, empty if none
    - fit_reasoning: 2-3 sentences
    - arbitrage_reasoning: 2-3 sentences, present even when score is low
    - missing_skills: list
    - transferable_skills: list of existing skills with non-obvious application
  - Prompt template stored as separate markdown file, not hardcoded in script
  - LLM backend configurable via config file, not hardcoded to one provider
  - Idempotent: re-running skips already-scored files unless --force is passed
  - Output is human-readable and designed to be reviewed, not just logged
NOTES:
  This is the validation phase. If evaluation output is not useful and accurate,
  nothing else is worth building. Iterate on the prompt and profile document
  until output quality is consistently good before proceeding to JS-03.
  anti_pattern_flags should fire on signals like: mandatory in-office, activity
  tracking language, excessive approval chains, requirements-to-compensation
  mismatch, or cultural indicators incompatible with autonomous working style.
  arbitrage_reasoning should never be empty even for low scores. It should
  explicitly explain why this is or is not an arbitrage play.

### JS-03 | Build job database and ingestion layer
STATUS: TODO
BLOCKED BY: JS-02 validated and working
ACCEPTANCE CRITERIA:
  - SQLite database stores all job records
  - Schema: id, title, company, url, date_posted, source, salary_range,
    location, remote_ok, status, traditional_fit_score, arbitrage_score,
    recommended_action, anti_pattern_flags, full_text, date_evaluated
  - Status lifecycle: new > scored > reviewed > applied > response > closed
  - Ingestion from manual file drop (extends Phase 0 folder approach)
  - Ingestion from Gmail job alert emails (depends on TS-04 gmail_tool)
  - Deduplication by URL: re-ingesting same posting updates record, no duplicate
  - User can add a posting by URL: system fetches, stores, and queues for scoring
  - Morning digest output: markdown report of new scored postings since last run,
    sorted by combined fit and arbitrage score, anti-pattern flags shown prominently
NOTES:
  Gmail integration depends on TS-04. Stub with manual file drop initially
  and add email ingestion when gmail_tool exists. Do not block on it.
  The status lifecycle enables a feedback loop later: which scored postings
  got interviews? That data can improve scoring calibration over time.

### JS-04 | Build resume generator
STATUS: TODO
BLOCKED BY: JS-01, JS-02
ACCEPTANCE CRITERIA:
  - Takes a job record and profile.md as input
  - Extracts and ranks requirements from job posting by inferred priority:
    order of appearance, frequency, phrasing strength (must vs preferred),
    known norms for similar roles
  - Rewrites profile bullet points using job's exact terminology and phrasing
    while grounding every claim in documented real experience
  - Ensures complete coverage of required skills in output language
  - Never fabricates experience: if a required skill is missing, flags it
    rather than inventing a claim
  - Outputs: tailored resume as markdown
  - Outputs: cover letter variant as markdown
  - Outputs: skills gap analysis noting what to address in cover letter
    or interview rather than resume
  - Human review is a required step before use: output is clearly marked as draft
  - Transparency check: flags phrases that are too directly copied from the JD
    and suggests paraphrase alternatives to avoid pattern-matching detection
NOTES:
  The reframing principle: "built automated data pipeline" and "developed ETL
  workflow" describe the same thing. The tool finds the employer's phrasing.
  This is translation, not fabrication. The line is: real experience reframed
  vs invented experience claimed. System should never cross that line.
  The transparency check is the human-in-the-loop mechanism. Output that
  reads like it was written by someone who memorized the job description is
  a red flag. The generator should flag this and suggest natural alternatives.

### JS-05 | Build opportunity mining tool
STATUS: TODO
BLOCKED BY: JS-01
ACCEPTANCE CRITERIA:
  - Given profile.md, generates a structured opportunity report containing:
    - Non-obvious job title suggestions with reasoning for each
    - Contract and freelance opportunity categories worth investigating
    - Arbitrage plays: specific role types at specific company sizes and
      contexts where user's skill combination is rare and valuable
    - Unknown unknowns: job categories the user likely has not searched
      due to career path bias
  - Integrates with SAM.gov API to surface active government contract
    opportunities matching user's capabilities
  - Output stored as dated markdown report
  - Re-runnable as profile.md is updated: fresh suggestions reflect new skills
NOTES:
  Examples of what this should surface:
  "Operations analyst at 50-200 person company with no dedicated tech team:
  user automates the role and has capacity to stack a second within 90 days"
  "Government micro-purchase data analysis contracts under $25k on SAM.gov:
  low competition, reliable payment, LLM-fulfillable for simple deliverables"
  "Series A startups hiring first ops role: need someone who builds the
  infrastructure, not just runs it. Technical ops background is rare here."
  "Local service businesses with stable revenue and aging owner-operators:
  candidate for seller-financed acquisition to technically capable buyer."
  Government surplus and resale opportunities should also be scoped here
  if SAM.gov integration surfaces relevant contract vehicle types.

### JS-06 | Wire Operator into MCP server
STATUS: TODO
BLOCKED BY: JS-02, JS-03, JS-04, TS-06
ACCEPTANCE CRITERIA:
  - job_scorer exposed as MCP tool
  - resume_generator exposed as MCP tool
  - opportunity_miner exposed as MCP tool
  - User can paste a job URL into Claude and receive full scored evaluation
  - User can request resume generation for a specific job ID
  - User can request fresh opportunity mining report
  - All tool calls return structured output, not raw text
NOTES:
  This is the milestone where Operator becomes conversational. The full
  research-to-draft workflow happens in one Claude conversation without
  switching tools or manually running scripts.

---
## PHASE 3 — x86 Machine Expansion (future, hardware not yet acquired)

### T3-01 : Acquire x86 mini PC
STATUS: TODO
ACCEPTANCE CRITERIA:
  - Machine meets spec: i5/i7 8th-10th gen, 16GB+ DDR4, NVMe SSD, Intel UHD 630
  - Purchased under $100
  - Powers on and POSTs successfully
  - Linux boots from USB installer
NOTES: Search terms: Optiplex 7060/7070/7080 Micro, EliteDesk 800 G4/G5 Mini, ThinkCentre M720q Tiny

### T3-02 : Install OS and Docker on x86
STATUS: TODO
BLOCKED BY: T3-01
ACCEPTANCE CRITERIA:
  - Ubuntu Server 22.04 LTS or Debian Bookworm installed
  - Docker and Docker Compose installed
  - SSH key from MacBook copied
  - Static DHCP lease assigned in router
NOTES:

### T3-03 : Migrate Docker services from Pi to x86
STATUS: TODO
BLOCKED BY: T3-02
ACCEPTANCE CRITERIA:
  - docker-compose.yml copied and adapted for x86 paths
  - Audiobookshelf, Prowlarr migrated with config intact
  - External drive remounted on x86 machine
  - All services verified working on new host
  - Pi reverts to PiHole-only role
NOTES:

### T3-04 : Install Jellyfin on x86
STATUS: TODO
BLOCKED BY: T3-02
ACCEPTANCE CRITERIA:
  - Jellyfin running as Docker container
  - Intel Quick Sync hardware transcoding configured (vaapi)
  - Media library added
  - Transcoding tested: stream to device that requires transcode, CPU usage stays low
NOTES:

### T3-05 : Install full *arr suite on x86
STATUS: TODO
BLOCKED BY: T3-02
ACCEPTANCE CRITERIA:
  - Sonarr, Radarr, Readarr added to docker-compose.yml
  - Each connected to Prowlarr for indexers
  - Each connected to qBittorrent as download client
  - Monitored library path set correctly
NOTES:

### T3-06 : Install Ollama for local LLM on x86
STATUS: TODO
BLOCKED BY: T3-02
ACCEPTANCE CRITERIA:
  - Ollama installed (Docker or native — decide at time)
  - At least one model pulled and responding (e.g. llama3)
  - API accessible locally
  - Memory usage benchmarked with available RAM
NOTES:

### T3-07 : MCP server setup
STATUS: TODO
BLOCKED BY: T3-06
ACCEPTANCE CRITERIA:
  - MCP server running and accessible to Claude Code / Gemini CLI on MacBook
  - AI sandbox concept extended to x86 with appropriate isolation
  - Tools and file access scoped intentionally
NOTES: Architecture for this not yet fully designed. Revisit when Ollama is running.




---
## SESSION LOG

### Session 2 — 2026-02-20

#### Completed this session (acceptance criteria met):
- T1-01: PiHole config exported via Teleporter before wipe — zip confirmed on MacBook
- T1-02: 64GB SD card flashed with 64-bit Raspberry Pi OS Lite
- T1-03: 64-bit OS verified — aarch64, Debian Trixie (13), 906MB RAM
  NOTE: OS is Debian Trixie, not Raspberry Pi OS Bookworm as originally planned. Trixie is newer/slightly less stable but working fine. Caused one Docker image compatibility issue (see below).
- T1-04: SSH keys confirmed working, passwordless login active. Hostname is "rascal" not "PiHole" — cosmetic, not a problem.
- T1-05: PiHole installed, Teleporter backup restored, blocklists confirmed, password reset via `pihole -a -p`
- T1-07: Docker 29.2.1 and Docker Compose v5.0.2 installed. sutton585 added to docker group.
- T1-08: External 931.5GB USB HDD formatted as ext4 (was briefly exFAT — reformatted), mounted at /mnt/data, fstab entry added with nofail flag, confirmed stable.
- T1-09: Directory structure created on external drive: audiobooks, books, downloads, torrents/incomplete, ai-sandbox. Owned by sutton585.
- T1-10: Config directories created on SD card: ~/config/audiobookshelf/config, ~/config/audiobookshelf/metadata, ~/config/prowlarr
- T1-11: qBittorrent-nox installed natively, systemd service file created, running. Web UI accessible at 192.168.0.22:8080. Password changed, upload capped at 1 KB/s, seeding ratio set to 0.
- T1-12: docker-compose.yml written and validated. Contains audiobookshelf, prowlarr, ai-sandbox.
- T1-13: All three containers started via docker compose up -d. Audiobookshelf confirmed at 192.168.0.22:13378. Prowlarr confirmed at 192.168.0.22:9696 (after image fix — see below).
- T1-15 (partial): Audiobookshelf web UI accessible, admin account created. Library and iOS app setup not yet done.

#### Attempted / partially complete:
- T1-14 (Prowlarr indexers): Partially complete. YTS, EZTV, Internet Archive added. AudioBookBay and Anna's Archive are NOT in Prowlarr's catalog and cannot be added via normal flow. One Russian book tracker added (semi-private, account created by user). Libgen not found in catalog during session. Cloudflare blocking encountered on some indexers — requires FlareSolverr to resolve (see new tasks). qBittorrent not yet connected to Prowlarr as a download client app — not done this session.
- T1-06: Static DHCP lease in router — not done this session. Low risk, do early next session.

#### Not started this session:
- T1-16: AI sandbox verification
- All Phase 2+ tasks

#### Issues encountered:
- linuxserver/prowlarr image failed on Debian Trixie due to libcrypto.so.3 incompatibility. Fixed by switching to ghcr.io/hotio/prowlarr:latest. docker-compose.yml already updated with correct image.
- AudioBookBay has no Prowlarr catalog entry and no straightforward custom Cardigann path in current Prowlarr version. Manual browser workflow is not acceptable as long-term solution.
- Anna's Archive is not a torrent tracker — it aggregates direct download sources and two Libgen forks, Sci-Hub, and Z-Library. Cannot be replicated inside Prowlarr. Must be used via browser or alternative tooling.
- Cloudflare protection blocking some indexers in Prowlarr. Requires FlareSolverr container to resolve.
- Copy-pasting magnet links manually from browser into qBittorrent web UI identified as unworkable long-term UX, especially on mobile.

#### Decisions made this session:
- D-005 confirmed: ext4 chosen over exFAT after deliberation. Drive reformatted correctly.
- D-P001 (Watchtower): Not yet decided. Carry forward.
- New: Lazy Librarian identified as likely solution for book/audiobook automation to replace manual search workflow.
- New: FlareSolverr needed to unblock Cloudflare-protected indexers in Prowlarr.
- New: hotio image used for Prowlarr instead of linuxserver due to Trixie compatibility. Should be noted in DECISIONS.md.

### Session 3 — 2026-02-25

#### Completed this session:
- T1-23: Samba installed and configured. /mnt/data shared as [media] at smb://rascal.local/media. Working in Finder with auto-connect.
- T1-20: Lazy Librarian fully operational. First book downloaded, post-processed, renamed, and filed correctly.
- Docker daemon DNS configured globally via /etc/docker/daemon.json (8.8.8.8)
- qBittorrent save paths corrected to /mnt/data/downloads and /mnt/data/torrents/incomplete
- LL cache directories manually created (JSONCache, HTMLCache) — not auto-created by LL
- Anna's Archive domain updated to annas-archive.li after .org court seizure
- LL filename patterns updated to remove colons (macOS/Samba incompatibility)
- Samba catia module configured for illegal character translation
- Prowlarr indexer audit completed — dead and low-quality indexers removed

#### Partially complete:
- T1-14: Prowlarr indexers partially configured. qBittorrent not yet connected as download client.
- T1-15: Audiobookshelf web UI working. iOS app and offline test still pending.
- T1-20: LL downloading ebooks via torrent providers. Audiobook downloads not yet confirmed working. Torznab/Prowlarr connection not yet set up.

#### Not started:
- T1-16: AI sandbox verification
- T1-18: qBittorrent → Prowlarr download client connection
- T1-19: FlareSolverr
- T1-22: Final Prowlarr indexer cleanup

#### Issues encountered:
- Anna's Archive .org domain seized Jan 2026 — use .li or .gl mirrors
- Anna's Archive direct downloads require paid membership — treating as optional
- LL does not auto-create cache directories — manual mkdir required
- DNB provider crashes due to missing pkg_resources Python module in image — disabled
- Colons in filenames invisible to macOS over Samba — fixed via catia module and LL pattern change
- Docker containers couldn't resolve certain domains — fixed via global daemon DNS config
- qBittorrent was saving to SD card (/home/sutton585/Downloads) instead of HDD — corrected

#### New scope added:
- T2.5-01: Local web page via lighttpd + GitHub
- T2.5-02: LM Studio on MacBook for coding assistance
- T2.5-03: Project Sandman overnight pipeline
- T2.5-04: Second Pi as AI experimenter and/or symbiosis with Sandman

#### Next session starting point:
- T1-18: Connect qBittorrent to Prowlarr as download client — ready to do, no blockers
- T1-19: FlareSolverr — evaluate after T1-18
- T1-20: Wire up Torznab in LL pointing at Prowlarr — key step for audiobook torrent searching
- T1-22: Final indexer audit and cleanup
- Investigate why LL audiobook searches are returning zero results
- Manual torrent selection in LL — show user how to browse results and pick manually


### Session 5 — 2026-03-03

#### Completed this session (acceptance criteria met or superseded):
- T1-19: Skipped — FlareSolverr not needed, Jackett Torznab handles all indexing
- T1-19.1: Skipped — Jackett native support makes this irrelevant
- T1-20: Confirmed Done — LL fully operational via Jackett Torznab
- T1-22: Skipped — architecture changed, Prowlarr not in LL chain
- T1-25: Skipped — native providers confirmed non-functional, architecture changed
- T1-26: Done — LL connected to Jackett via six per-indexer Torznab URLs
- T1-27: Done — Jackett confirmed with AudioBookBay and other indexers
- T1-28: Done — full download chain confirmed working end to end
- T1-31: Done — /mnt/data permissions fixed, all directories owned by sutton585
- T1-32: Done — cgroup kernel support enabled, memory limits active on all containers

#### Key technical findings this session:
- LL native providers (AudioBookBay, TPB, TDL, LimeTorrents) are unreliable or
  broken for audiobook use. Native AudioBookBay was 404ing — domain changed,
  hardcoded URL in image. Provider blocklist was masking this — providers were
  silently skipped, never appearing in logs at all.
- Torznab per-indexer URLs from Jackett are the correct architecture. LL can
  accept multiple Torznab connections, one per indexer. Immediate results on
  first connection.
- Raspberry Pi 3 requires cgroup_enable=memory cgroup_memory=1 in
  /boot/firmware/cmdline.txt for Docker memory limits to work. Without this,
  deploy.resources.limits.memory is silently ignored and containers can consume
  all available RAM.
- OOM crash can be triggered by marking multiple series as Wanted simultaneously.
  LL searches all missing books in parallel with no rate limiting. On 1GB RAM
  with full container stack, this is enough to crash the system.
- /mnt/data directories created as root during early setup were blocking LL and
  Samba writes. Fixed with chown -R sutton585:sutton585 /mnt/data.
- ABS reads metadata from folder structure primarily. Clean LL naming patterns
  are sufficient — no custom ID3 tagging required for basic functionality.

#### Partially complete:
- T1-24: Manual torrent intervention workflow — partially understood, not documented
- T1-30: qBittorrent categories — mode set to Automatic, categories not yet created
- T1-21: ABS library setup started, not yet validated end to end
- T1-29: ABS iOS app not yet installed

#### Scope added this session:
- Operator (job search automation) project fully scoped
- JOB_SEARCH_README.md created — full PRD and vision document
- TASKS_operator_additions.md created — JS-01 through JS-06 task definitions
- Sandman setup script concept defined — desired state management pattern,
  hardware-agnostic deployment, sandboxed isolation model

#### Concepts covered this session:
- Desired state management as a pattern (vs imperative scripting)
- Why Kubernetes is wrong for this scale, and why the mental model still applies
- Docker memory limits and cgroup kernel requirements on Pi
- vcgencmd get_throttled for Pi power diagnostics
- LL provider architecture: native providers vs Torznab protocol
- ABS metadata priority: folder structure > ID3 tags > external fetch
- SERIES and SERIES-PART as non-standard ID3 fields ABS reads natively
- qBittorrent category system and Automatic torrent management mode
- Linux ownership model: user:group format, 755 permission breakdown
- Tailscale vs Headscale: WireGuard underneath, coordination server is the
  only difference. Headscale self-hosts the coordination plane.
- Operator project framing: arbitrage over competition, unknown unknowns,
  overemployed model as legitimate career strategy

#### Fluency upgrades this session:
- Docker memory limits and cgroup: [none] → [familiar]
- LL architecture and Torznab protocol: [aware] → [comfortable]
- Linux file permissions (chmod/chown): [familiar] → [comfortable]
- qBittorrent category system: [familiar] → [comfortable]
- ABS metadata model: [none] → [aware]
- Tailscale/WireGuard/Headscale: [aware] → [familiar]

#### Next session starting point:
- T1-30: Create qBittorrent categories (audiobooks, books) with correct save paths
- T1-21: Confirm ABS library scan picks up downloaded audiobooks correctly
- T1-29: Install ABS iOS app, connect to server, test offline download
- T1-24: Document manual torrent selection workflow in LL
- These four tasks complete Phase 1. Nothing else is blocking them.

#### Open questions carried forward:
- qBittorrent web UI was showing port 33607 instead of 8080 at one point —
  confirm this is resolved or investigate
- LL staging files in /config during processing confirmed as expected behavior
  (temporary, moves to /audiobooks on completion) — verify this is actually
  happening correctly now that permissions are fixed
- SSH key may need re-copying after crash cycle — confirm passwordless SSH
  is working from MacBook
