
# DECISIONS.md
# Pi Home Server — Architecture Decision Log

---

## AI AGENT INSTRUCTIONS
- Read this file at session start BEFORE suggesting any architectural approach.
- Never suggest an alternative that conflicts with a **`SETTLED`** decision without flagging it explicitly.
- If you believe a settled decision should be revisited, state your reasoning and ask human — do not silently implement alternatives.
- New decisions require human approval. AI may add **`PROPOSAL`** entries and await human response.
- Append new entries. Never modify or remove prior entries.
- Format: Decision ID | Title | Status | Date

Status values: **`SETTLED`** ==PROPOSAL== ~~**`REJECTED`**~~ **`REVISIT-WHEN: condition`**

---

## SETTLED DECISIONS — DO NOT RELITIGATE

### D-001 | Native vs Docker per service
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: PiHole and qBittorrent run natively. All other services run in Docker.
CONTEXT: Two install methods available. Native (apt + systemd) is simpler, less overhead. Docker provides isolation, ARM64 image support, easier updates.
ALTERNATIVES CONSIDERED:
  - All native: rejected — Audiobookshelf has no ARM apt package, native installs for *arr suite are messy
  - All Docker: rejected — adds overhead for services with clean native installs that work perfectly (PiHole has its own installer, qBittorrent-nox is simple apt)
RATIONALE: Pragmatic hybrid. Use native where it's clearly better, Docker where it solves a real problem (architecture compatibility, update management).
CONSEQUENCES: Stack is a mix of systemd services and Docker containers. Monitoring requires checking both `systemctl status` and `docker ps`. Acceptable trade-off.
DO NOT SUGGEST: Moving PiHole or qBittorrent into Docker unless a specific problem arises that Docker would solve.

### D-002 | Migrate to 64-bit Raspberry Pi OS
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: Wipe 32-bit Raspbian, install 64-bit Raspberry Pi OS Lite on 64GB SD card.
CONTEXT: Pi 3 was running 32-bit Raspbian (armv7l). Audiobookshelf Docker image does not support armv7. Pi 3 hardware is capable of 64-bit (aarch64).
ALTERNATIVES CONSIDERED:
  - Stay on 32-bit, use Node.js to run Audiobookshelf natively: rejected — armv7 will continue to cause friction with other modern Docker images. Technical debt.
  - Stay on 32-bit, use Docker armv7 images only: rejected — too many services dropping armv7 support.
  - Upgrade OS in-place: rejected — 32-bit to 64-bit cannot be done in-place, requires reinstall anyway.
RATIONALE: Clean break eliminates entire class of architecture compatibility problems. Better foundation for all future work. Small one-time cost.
CONSEQUENCES: Full reinstall required. PiHole config must be backed up via Teleporter first. All Phase 0 work is superseded by Phase 1 equivalents.

### D-003 | Use 64GB SD card as new boot drive
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: Flash 64-bit OS to 64GB card. Retire 32GB card as emergency backup.
CONTEXT: User has two SD cards: 32GB (current) and 64GB (unused).
RATIONALE: More headroom for OS, logs, config files. Old card preserved as fallback if new setup has catastrophic problems.
CONSEQUENCES: Old card kept intact until new setup confirmed stable, then can be reformatted.

### D-004 | Docker Compose over individual docker run commands
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: All Docker services defined in single /home/sutton585/docker-compose.yml. Use `docker compose up -d` to manage.
CONTEXT: Services can be managed via individual `docker run` commands or via a Compose file.
ALTERNATIVES CONSIDERED:
  - Individual docker run commands: rejected — hard to maintain, no single source of truth, easy to lose flags and configuration
  - Portainer (Docker GUI): rejected — adds complexity, unnecessary for this scale, better to learn compose directly
RATIONALE: Compose file is self-documenting, version-controllable, reproducible. Industry standard for multi-container setups. Single file to audit, back up, share with AI sessions.
CONSEQUENCES: All containers must be defined in compose file. Running ad-hoc `docker run` for testing is fine but production services go in compose.

### D-005 | ext4 for external drive filesystem
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: Format external drive as ext4.
CONTEXT: Drive will be permanently attached to Pi. Options: ext4, exFAT, NTFS.
ALTERNATIVES CONSIDERED:
  - exFAT: rejected — works cross-platform but adds overhead on Linux, less reliable for always-on use
  - NTFS: rejected — requires ntfs-3g driver on Linux, slower, designed for Windows
RATIONALE: ext4 is native Linux filesystem. Best performance, reliability, and journaling on a Linux host. Pi is the permanent home for this drive.
CONSEQUENCES: Drive cannot be read directly on Mac or Windows without third-party software. Acceptable since Pi is the access point.

### D-006 | qBittorrent-nox over Transmission
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: Use qBittorrent-nox as torrent client.
CONTEXT: Multiple torrent clients considered at project start.
ALTERNATIVES CONSIDERED:
  - Transmission: cleaner UI but fewer features, weaker category management
  - Deluge: more complex configuration
RATIONALE: qBittorrent-nox has better web UI, per-torrent file prioritization, category system that will integrate better with future *arr suite automation.
CONSEQUENCES: None significant.

### D-007 | Disable seeding until VPN configured
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: qBittorrent upload hard-capped at 1 KB/s AND seeding ratio set to 0 until VPN is running. This is a hard requirement, not a preference.
CONTEXT: Seeding exposes IP address and upload activity to ISP monitoring.
RATIONALE: ISP risk is real. Two independent mechanisms (upload cap + ratio limit) prevent accidental seeding.
CONSEQUENCES: VPN setup (T2-01) is a BLOCKER before any seeding settings are changed. AI must not suggest raising upload limits without VPN confirmation.
DO NOT SUGGEST: Raising upload limits or changing ratio settings until T2-01 is marked DONE by human.

### D-008 | AI sandbox with network_mode: none
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: AI sandbox Docker container has zero network access. File access scoped to /mnt/data/ai-sandbox only.
CONTEXT: User wants to give Claude Code / Gemini CLI access to a workspace on the Pi without exposing the broader system.
RATIONALE: Defense in depth. AI tools should not have network access from the server context. Filesystem-only access limits blast radius of any unexpected behavior.
CONSEQUENCES: Any AI-generated content must be manually reviewed and moved outside sandbox to take effect on the broader system.
DO NOT SUGGEST: Adding network access to ai-sandbox without explicit human decision and a new DECISIONS.md entry.

### D-009 | Defer Jellyfin and *arr suite to x86 machine
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: Jellyfin and full *arr suite (Sonarr, Radarr) will not be installed on Pi 3. Reserved for future x86 machine.
CONTEXT: Pi 3 has 1GB RAM and no hardware video encode/decode support usable by Jellyfin.
RATIONALE: Jellyfin transcoding on Pi 3 ARM CPU would fail or produce unwatchable results. *arr suite adds significant RAM pressure. Better to do it right on appropriate hardware.
CONSEQUENCES: Pi scope limited to: PiHole, qBittorrent, Audiobookshelf, Prowlarr, AI sandbox. All media transcoding deferred.
DO NOT SUGGEST: Installing Jellyfin or Sonarr/Radarr on Pi 3.

### D-010 | Prowlarr over Jackett for indexer management
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: Use Prowlarr as indexer manager.
CONTEXT: Two main options: Jackett (older) and Prowlarr (newer, same ecosystem).
ALTERNATIVES CONSIDERED:
  - Jackett: older, still works but less actively developed, worse integration with *arr suite
  - Manual indexer configuration: rejected — maintenance burden, URLs change
RATIONALE: Prowlarr is the modern successor to Jackett. Better *arr integration, actively maintained, crowdsourced indexer catalog means URLs are maintained by community.
CONSEQUENCES: None significant. Jackett guides found online can be adapted for Prowlarr.

### D-011 | Static IP via router DHCP reservation, not Pi config
STATUS: **`SETTLED`**
DATE: 2026-02-19
DECISION: Pi IP (192.168.0.22) maintained via router DHCP lease reservation, not hardcoded in Pi network config.
CONTEXT: Pi needs stable IP for service access. Two ways to achieve: configure static IP on Pi, or configure router to always assign same IP.
RATIONALE: Router-managed reservation is easier to change, survives OS reinstalls, and is the correct approach for home network management. Hardcoding on device creates maintenance burden across reinstalls.
CONSEQUENCES: If router is reset or DHCP reservation lost, Pi may get different IP. Low risk, easy to fix.

---

## PROPOSALS PENDING HUMAN DECISION

### D-P001 | Docker container auto-updates via Watchtower
STATUS: **`PROPOSAL`**
DATE: 2026-02-19
PROPOSED: Add Watchtower container to docker-compose.yml to automatically pull and restart updated images on a schedule.
ALTERNATIVES: Manual updates via `docker compose pull && docker compose up -d` on a schedule of David's choosing.
TRADE-OFFS:
  - Watchtower: hands-off, but updates may introduce breaking changes without warning
  - Manual: more control, aligns better with learning goals (understand what's changing and why)
RECOMMENDATION: Manual updates for now. Better for learning context. Revisit when x86 machine is set up and stack is more stable.
AWAITING: Human decision before T2-05 is implemented.

---

### D-012 | Prowlarr Docker image: hotio instead of linuxserver
STATUS: **`SETTLED`**
DATE: 2026-02-20
DECISION: Use ghcr.io/hotio/prowlarr:latest instead of lscr.io/linuxserver/prowlarr:latest
CONTEXT: Running Debian Trixie (13) instead of planned Raspberry Pi OS Bookworm (12). The linuxserver.io Prowlarr image has a libcrypto.so.3 incompatibility with Trixie's newer OpenSSL — basic system binaries (cut, cat, id, chown) fail with "Exec format error" and the container cannot start.
ALTERNATIVES CONSIDERED:
  - linuxserver/prowlarr: rejected — confirmed broken on Debian Trixie, libcrypto.so.3 incompatibility
  - Downgrade OS to Bookworm: rejected — unnecessary, Trixie is working fine for everything else
RATIONALE: hotio images are well-maintained, actively used in the *arr community, and started cleanly on Trixie. No functional difference from user perspective.
CONSEQUENCES: If linuxserver.io fixes Trixie compatibility in a future release, switching back is an option but not necessary. Monitor hotio image for aarch64 support continuity.
DO NOT SUGGEST: Switching back to linuxserver/prowlarr without first verifying Trixie compatibility.

### D-013 | Debian Trixie as OS (deviation from plan)
STATUS: **`SETTLED`**
DATE: 2026-02-20
DECISION: Accept Debian Trixie (13) as the operating system. Do not reinstall to achieve Bookworm.
CONTEXT: T1-02 called for Raspberry Pi OS Lite 64-bit (Bookworm). The flashed card booted into Debian Trixie (13) instead — likely selected in Raspberry Pi Imager. Discovered at T1-03 verification.
ALTERNATIVES CONSIDERED:
  - Reinstall with Bookworm: rejected — everything is working, one image incompatibility was resolved with an image swap, not worth the disruption
  - In-place downgrade: not possible
RATIONALE: Trixie is newer and has caused only one issue (Prowlarr image) which was easily resolved. All other services (PiHole, Docker, qBittorrent, Audiobookshelf) running cleanly. Stability concerns about "testing" branch are theoretical at this scale.
CONSEQUENCES: Some Docker images may have Trixie compatibility issues — check hotio or other image providers as alternatives to linuxserver.io if issues arise. Note for future reference when adding new containers.

### D-014 | Lazy Librarian for book/audiobook automation
STATUS: **`PROPOSAL`**
DATE: 2026-02-20
PROPOSED: Add Lazy Librarian as the primary tool for book and audiobook acquisition, supplementing or partially replacing manual Prowlarr/browser workflow.
CONTEXT: Prowlarr's catalog has no AudioBookBay entry and weak book/audiobook indexer support generally. Manual browser search + magnet link copy-paste identified as unworkable long-term UX especially on mobile.
ALTERNATIVES CONSIDERED:
  - Manual browser workflow (AudioBookBay, Anna's Archive): rejected as primary — acceptable as fallback only
  - Custom Cardigann definition for AudioBookBay in Prowlarr: viable, to be investigated in parallel (T1-19 notes)
  - RapidAPI Anna's Archive wrapper: rejected — third-party, paid, routes traffic through unknown server
TRADE-OFFS:
  - Lazy Librarian: adds another service, needs evaluation for aarch64 support and actual source coverage
  - Coverage assessment needed: strong for ebooks/Libgen, weaker for audiobooks, unlikely to fully replace AudioBookBay
AWAITING: T1-20 evaluation before settling. Anna's Archive and AudioBookBay likely remain as manual browser fallbacks regardless of outcome.

### D-015 | Prowlarr as admin-only tool
STATUS: **`SETTLED`**
DATE: 2026-02-20
DECISION: Prowlarr is treated as an admin-only interface. URL is not shared with family members. Authentication set to "disabled for local addresses" for David's convenience, with credentials stored for outside-the-house access.
CONTEXT: User asked about per-user adult content restrictions in Prowlarr for family members on the LAN.
RATIONALE: Prowlarr has no permission tiers — local access is full admin access. Family members have no use case for Prowlarr directly. Their interface is Audiobookshelf only. Adult content indexers in Prowlarr do not surface in any family-facing UI.
CONSEQUENCES: If a family member ever needs to request downloads, the workflow is "tell David" or a future simple request interface — not direct Prowlarr access.
DO NOT SUGGEST: Adding family member access to Prowlarr or implementing per-user category filtering — the tool does not support it and the use case doesn't require it.

### D-016 | Samba for external drive access
STATUS: **`SETTLED`**
DATE: 2026-02-25
DECISION: Samba installed natively on Pi. Single share [media] exposes /mnt/data only. SD card not shared via Samba — managed via SSH only.
CONTEXT: Need GUI access to media files from MacBook and iPhone. External drive contains all media content. SD card contains only OS, configs, and Docker data — no reason to expose via file share.
ALTERNATIVES CONSIDERED:
  - SFTP: works but no native Finder integration on Mac without third-party software
  - NFS: faster than Samba on Linux-to-Linux but worse macOS compatibility
  - Exposing full filesystem: rejected — SD card has no content worth browsing, unnecessary attack surface
RATIONALE: SMB is natively supported by macOS and iOS Files app. Accessible at smb://rascal.local/media via mDNS without requiring PiHole DNS. Single share keeps scope minimal.
CONSEQUENCES: Colon characters in filenames are invisible to macOS over SMB. LL filename patterns updated to avoid colons. Samba catia vfs module added as safety net for any other illegal characters.
DO NOT SUGGEST: Exposing SD card contents via Samba or adding guest access unless explicitly requested.

### D-017 | Anna's Archive direct downloads deferred — paid feature
STATUS: **`SETTLED`**
DATE: 2026-02-25
DECISION: Anna's Archive treated as optional paid upgrade. Not relied upon as primary download source.
CONTEXT: Anna's Archive .org domain seized by US court injunction January 2026. Working mirrors confirmed at .li and .gl. However direct downloads via API require paid membership — free tier returns 401 immediately, blocking automated use entirely.
ALTERNATIVES CONSIDERED:
  - Pay for membership: viable, donation-based not fixed subscription. Deferred.
  - Use as torrent source via Prowlarr/Torznab: not applicable — Anna's Archive is not a torrent tracker
  - Keep as direct provider with key: possible if user chooses to donate in future
RATIONALE: Libgen and torrent providers via LL's built-in trackers are sufficient for current needs. Anna's Archive membership is a nice-to-have not a dependency.
CONSEQUENCES: Anna's Archive disabled in LL config to prevent 401 error spam in logs. URL updated to annas-archive.li in config for when/if membership is added. Current working domains: annas-archive.li, annas-archive.gl — .org is dead.
DO NOT SUGGEST: Re-enabling Anna's Archive as primary provider without confirming paid key is configured.

### D-P002 | Second Pi as dedicated AI/LLM experimenter
STATUS: **`PROPOSAL`**
DATE: 2026-02-25
PROPOSED: Dedicate second Pi 3 (same hardware as Rascal) to AI/LLM experimentation, separate from primary Pi's role as media server.
CONTEXT: User has a second Pi 3 available. Primary Pi scope is intentionally limited (D-009). AI sandbox on primary Pi has network_mode: none and limited scope by design (D-008).
ALTERNATIVES CONSIDERED:
  - Use primary Pi for AI work: rejected — keeps scope clean, primary Pi RAM is already constrained
  - Use MacBook for all AI work: viable for LM Studio/local inference, but MacBook is daily driver
  - Use old 2012 MacBook i7: heat issues unresolved, decade-old hardware, not recommended
TRADE-OFFS:
  - Dedicated second Pi: clean separation, always-on, but Pi 3 too weak for real inference
  - Practical role limited to: API proxy, scheduler, lightweight automation, Sandman pipeline runner
AWAITING: Human decision. Recommend revisiting after Phase 1 complete on primary Pi.

### D-018 | Repurpose ai-sandbox container as Sandman automation platform
STATUS: **`SETTLED`**
DATE: 2026-02-28
DECISION: ai-sandbox container retired. Replaced by sandman container with full
  network access, python:3.12-slim base image, and a defined role as the personal
  automation platform on Rascal.
CONTEXT: D-008 established ai-sandbox with network_mode: none for interactive AI
  tool experimentation. Project scope expanded — a scheduled automation platform
  with Gmail API access and MCP server hosting requires network access. The
  isolation rationale of D-008 applied to unpredictable interactive tools, not
  a defined Python automation service with known network targets.
ALTERNATIVES CONSIDERED:
  - Keep ai-sandbox isolated, add separate sandman container: rejected — two
    containers serving overlapping purposes on a 1GB RAM machine is wasteful
  - Run Sandman natively on Pi without Docker: viable but Docker keeps dependencies
    clean and the pattern consistent with other services
RATIONALE: Sandman's network targets are defined and intentional (Gmail API, GitHub,
  MCP clients on LAN). This is a different risk profile from an interactive AI tool
  with unpredictable behavior. Network access is appropriate here.
CONSEQUENCES: No network-isolated AI sandbox currently exists on Rascal. If
  interactive AI tool experimentation is needed later, a new sandboxed container
  should be created separately and documented with a new decision entry.
DO NOT SUGGEST: Restoring network_mode: none to the sandman container — this
  would break Gmail API access and MCP server functionality.

### D-019 | Sandman platform architecture: tools, MCP, orchestration
STATUS: **`SETTLED`**
DATE: 2026-02-28
DECISION: Project Sandman is structured as three distinct layers — tools, MCP
  server, and orchestration — built and deployed in that order. Tools are the
  priority and are designed to be useful standalone regardless of what calls them.
CONTEXT: Original Sandman concept was a custom Python controller (APScheduler-based)
  orchestrating custom "grain" tools with bespoke inter-tool communication. Scope
  review identified that orchestration is well-served by existing tools (n8n,
  Huginn) and that MCP is the appropriate protocol for exposing tools to AI agents.
  Building a custom orchestration layer is reinventing solved problems.
ALTERNATIVES CONSIDERED:
  - Custom Python controller (original plan): rejected — reinvents orchestration
    tooling that already exists; not a transferable skill
  - n8n as full replacement: not yet evaluated for Pi 3 RAM constraints — see D-P003
  - LangChain / LangGraph for brain layer: worth evaluating before building custom
    LLM routing logic
RATIONALE: Tools (standalone Python scripts with clean interfaces) are genuinely
  novel and where build effort belongs. MCP is the industry standard for AI agent
  tool integration. Orchestration should use existing software. This approach
  teaches transferable skills rather than bespoke patterns.
CONSEQUENCES: Sandman repo becomes thinner than originally planned — config,
  scheduling bootstrap, and MCP server rather than a full workflow engine.
  Individual tool repos (gmail_tool, digestitor, job_parser, etc.) carry their
  own logic. See TASKS.md Phase 2.5-S for full build sequence.
DO NOT SUGGEST: Building a custom workflow engine or custom inter-tool
  communication protocol before evaluating n8n, Huginn, or equivalent.

### D-P003 | Orchestration tool selection for Sandman platform
STATUS: **`PROPOSAL`**
DATE: 2026-02-28
PROPOSED: Evaluate and select an orchestration tool before building any workflow
  automation in Sandman. Strong candidates: n8n (feature-rich, RAM-heavy),
  Huginn (lightweight, self-hosted, Pi-friendly), or Pi cron as minimal fallback.
CONTEXT: D-019 settled that orchestration should use existing tooling rather than
  a custom controller. The specific tool is not yet selected — RAM constraints on
  Pi 3 (1GB) are the primary filter. n8n is the most capable option but may be
  too heavy. Huginn is designed for exactly this use case at lower resource cost.
  MacBook overnight Docker container is a viable stopgap for heavier workloads.
ALTERNATIVES TO EVALUATE:
  - n8n: most capable, best integrations, aarch64 Docker image exists — benchmark
    RAM usage on Pi 3 before committing
  - Huginn: purpose-built for personal automation agents, lighter weight, less
    polished UI, fewer native integrations
  - Prefect / Airflow: ruled out — designed for data engineering teams, excessive
    overhead for this use case
  - Pi cron only: viable for simple schedules but cannot do event-driven triggers
    or multi-step conditional workflows
HARDWARE CONSIDERATION: If Pi 3 cannot run chosen orchestration tool comfortably,
  options are MacBook overnight container (stopgap) or wait for x86 machine.
  Tools (gmail_tool, digestitor, etc.) should be built regardless — they are
  orchestration-agnostic.
AWAITING: TS-02 evaluation task in TASKS.md. Decision should be recorded here
  before TS-08 (orchestration implementation) begins.

