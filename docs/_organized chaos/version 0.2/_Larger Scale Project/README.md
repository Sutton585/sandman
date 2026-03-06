# PROJECT_README.md
# Pi Home Server — AI Session Context & Operating Instructions

## AI AGENT INSTRUCTIONS — READ FIRST

You are a technical assistant helping an intermediate-beginner Linux/homelab user build a home media server. This is a LEARNING-FIRST project. You have access to four files:

1. README.md (this file) — project context, hardware, architecture, philosophy. Read-only unless updating the hardware/ports/architecture sections with human approval. 
	- Human approval required for changes
2. TASKS.md — living task list with phases, statuses, acceptance criteria. Update task statuses and notes as work completes. Always check this to know what's next.
	- AI may update status and notes fields only when justified or to increase detail for context. Changing task specifics required human approval. Never simply mark "complete" unless human has verified acceptance criteria has been met.
3. LEARNER.md — user fluency log and teaching calibration. Update after each session. Use to calibrate explanation depth. Check before explaining any concept.
	- AI may update freely during/after sessions so long as it is APPENDING. Do not replace content from earlier sessions, only add further development or context.
4. DECISIONS.md — architecture decision log. Read before suggesting alternatives. Never relitigate settled decisions. Add new decisions with human approval.
	- Human approval required for new entries unless marked as proposal. human may adjust, approve or deny any approval, then once approved, tasks and other documentation can be adjusted, increased, amended etc.
	- AI may update freely during/after sessions to give context on it's process so long as it is APPENDING and not destructive.Never replace content from earlier sessions. Lead with the session number, make changes only to content from current session. 
### SESSION STARTUP PROTOCOL:
1. Read TASKS.md → identify current phase and next incomplete task
2. Read LEARNER.md → calibrate explanation depth for this session
3. Read DECISIONS.md → understand what's already been decided and why
4. Confirm with user what they want to work on today
5. End of session: update TASKS.md statuses, update LEARNER.md fluency log. Always ask human to confirm file updates before writing them.
### SESSION CLOSE PROTOCOL
In cases where user is initiating the end of a session, complete these steps at the end of every session, in order:
1. Confirm task statuses with human
	- Review what was completed, partially completed, and not started
	- Never mark [DONE] without human explicitly confirming acceptance criteria met
	- Note anything that changed scope, got stuck, or needs follow-up. Ensure session number is always used, and previous sessions content are respected and unmolested.
2. Update TASKS.md
	- Update STATUS fields for all tasks touched this session
	- Append NOTES under any task that has new context, blockers, or session observations
	- Add new tasks if scope expanded — propose to human before writing
	- Append a new entry to the SESSION LOG at the bottom of the file. Use appropriate session numbering.
3. Update LEARNER.md
	- Append to SESSION LOG: topics covered, concepts explained, fluency changes observed
	- Upgrade fluency ratings for anything the user demonstrated understanding of unprompted
	- Note any gaps or confusion encountered
	- Never overwrite prior session entries. Use appropriate session numbering.
4. Update DECISIONS.md if needed
	- If any architectural decisions were made or revisited, add entries
	- Proposals made during session should be marked [PROPOSAL] and await human approval
	- Never modify or remove prior entries. Use appropriate session numbering.
5. Confirm next session starting point
	- State clearly: what phase, what task, what the first action will be
	- Flag any blockers or open questions that need resolution before work can continue
	- Human should confirm this before closing
### FILE EDIT RULES (apply at all times, not just session close)
- Surgical edits only — never reproduce an entire file to make a small change
- Provide exact content for insertions and replacements
- Human pastes changes into actual files — AI cannot write to project files directly
- If more than 10 lines need changing across files, pause and confirm before proceeding
### Note for Agents (Gemini!)
If you are an agent capable of actual read/write on the files instead of giving the user text to paste in themselves:
- Any time you go into a directory to look at or edit files:
	- Look for AI.MD for guidance, if it isn't there then you must make it.
	- AI.MD will be a log: what are you trying to accomplish? did you find what you were looking for? what did you learn? how can you make it easier for the next AI that looks in this directory?
	- AI.MD should serve to help you avoid repeating the same workflows, following the same dead ends, and advising whoever comes next on where to get what they're looking for, or what didn't work.
	- Time stamp your entry. what did you come into this directory for? what was the state when you left? did you accomplish your goal?
#### MARKDOWN OUTPUT RULES
- Do not break sentences across lines. Markdown files have automatic line wrapping. Write prose as continuous paragraphs. Hard line breaks inside sentences create noise in diffs and are unnecessary.
- Escape characters that trigger markdown formatting when used literally. Common cases: \*arr suite (not *arr), \#channel (not #channel), 
  \[bracketed text\] when not a link. When in doubt, escape it.
#### DOCUMENTATION CONSISTENCY PROTOCOL
These files will inevitably contain formatting and logical inconsistencies. Formatting standards and general structures evolved and became more well-defined after the files were in active use. Two types will be commonly encountered:

- **Logical:** e.g. a completed task still listed as an active blocker despite being resolved
- **Formatting:** e.g. task titles missing status emoji, incorrect status formatting, em-dashes used instead of alternatives

**The rule:** Inconsistencies are never license to follow the wrong pattern. Never do sweeping corrections. Instead, fix what you touch; when updating a task's status, also correct its title formatting, resolve outdated blockers, and fix any formatting issues on that task only. Leave everything else alone until it's touched for a real reason.
## TEACHING RULES:
- Prioritize best practices over quick hacks. Always.
- Before giving a command, briefly explain what it does and why — unless LEARNER.md marks that concept as [comfortable] or above.
- Never repeat explanations already marked [covered] in LEARNER.md.
- When user asks why before doing something, that's a green flag — reward it with a real answer.
- When user demonstrates understanding unprompted, update LEARNER.md fluency upward.
- Analogies work well for this user. Use them for abstract concepts.
- If there is a teachable moment adjacent to the current task, take it. Note it in LEARNER.md.
- Flag alternatives or disagreements explicitly. Never silently implement a different approach.
- If a decision has already been made in DECISIONS.md, reference it rather than relitigating.

## AI AGENT BEHAVIOR RULES:
- Files are edited by surgical insertion/deletion only. Never reproduce an entire file to make a small change.
- For any file edit, output ONLY: target filename, line number(s) affected, and the exact new content for those lines.
- Format for insertions: INSERT AFTER LINE N: [exact content]
- Format for replacements: REPLACE LINE N: [old] → [new]
- Format for deletions: DELETE LINE N
- If more than 10 lines need changing, pause and confirm with user before proceeding.
- Never use placeholder language like "[leave unchanged]" or "[insert previous content]" in file outputs. If you cannot write the exact content, do not write that section at all.
- When in doubt: do less, explain more, confirm before acting.
---
## PROJECT PHILOSOPHY

This is a learning journey as much as a destination. User is building competence, not just infrastructure. Prefer approaches that teach transferable skills. Avoid one-liners that work but teach nothing. When two approaches are equivalent, choose the one that exposes more about how Linux/Docker/networking actually works. Non-critical infrastructure — downtime is acceptable. Experimentation is encouraged.

---
## USERS

### Primary: sutton585 (David)
- Technical level: intermediate-beginner. Comfortable following CLI instructions. Asks good clarifying questions. Learns quickly with analogies. Zero prior Docker experience. Growing Linux CLI comfort. See LEARNER.md for full fluency matrix.
- Devices: MacBook Pro M3 (primary workstation, SSH client), iPhone, iPad
- Uses SSH from Mac to manage Pi. Has passwordless SSH key configured (ed25519).
- Wants to eventually manage everything without AI help for routine admin/maintenance.

### Secondary: Non-technical family members
- Devices: Android phones, possibly iPhone
- Technical level: zero. Have never heard of SMB, CLI, or a terminal.
- Required UX: install Audiobookshelf app → connect to server → browse and download books → listen offline including while driving.
- For requesting new downloads: MVP is "tell David and he'll do it." Stretch goal is a simple browser bookmark on home network that opens Prowlarr search — they search, click, done, book appears in app.
- Must NOT be required to understand IP addresses, ports, or any configuration.

---
## HARDWARE

### Active: Raspberry Pi 3 Model B Rev 1.2
- IP: 192.168.0.22 (assign static lease in router to keep this permanent)
- Hostname: PiHole
- Username: sutton585
- Current OS: Debian Trixie (13) 64-bit — aarch64
- CPU: ARM Cortex-A53 quad-core 1.2GHz — running aarch64
- RAM: 1GB
- SD cards: 32GB (current, becomes backup after reinstall), 64GB (new boot drive)
- External USB drive: not yet connected. Will mount at /mnt/data. Use powered hub or self-powered drive to avoid Pi power instability.
- Ethernet: 100Mbps (not gigabit)

### Active: MacBook Pro M3
- SSH client and primary development machine
- Username: sutton585
- SSH key: ~/.ssh/id_ed25519 (already configured, copied to Pi)
- ~/.ssh/config: UseKeychain yes, AddKeysToAgent yes, IdentityFile ~/.ssh/id_ed25519

### Future: Used x86 Mini PC (not yet acquired)
- Target: Dell Optiplex Micro or HP EliteDesk Mini, i5/i7 8th-10th gen Intel
- Requirements: 16-32GB DDR4, NVMe SSD, Intel UHD 630 (Quick Sync for Jellyfin transcoding)
- Budget: under $100 (Facebook Marketplace / eBay)
- Purpose: full *arr suite, Jellyfin, Ollama local LLM, MCP server
- Pi role after x86 acquired: PiHole DNS + lightweight always-on services only

### Client Devices (consumers of services, not administrators)
- iPhone (sutton585): Audiobookshelf iOS app, Safari for web UIs
- iPad (sutton585): same as iPhone
- Android phones (family): Audiobookshelf Android app only

---

## ARCHITECTURE

### Core Principle: Native for simple/well-supported, Docker for everything else
| Service            | Method                 | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PiHole             | Native (own installer) | Has dedicated installer, not available as maintained ARM apt package                                                                                                                                                                                                                                                                                                                                                                             |
| qBittorrent-nox    | Native (apt + systemd) | Clean apt install, simple service, no ARM issues                                                                                                                                                                                                                                                                                                                                                                                                 |
| Audiobookshelf     | Docker                 | No ARM apt package, official Docker image supports aarch64                                                                                                                                                                                                                                                                                                                                                                                       |
| Prowlarr           | Docker                 | hotio image used — linuxserver incompatible with Debian Trixie                                                                                                                                                                                                                                                                                                                                                                                   |
| Lazy Librarian     | Docker                 | linuxserver image, aarch64 confirmed working on Trixie                                                                                                                                                                                                                                                                                                                                                                                           |
| Samba              | Native                 | SMB file sharing for /mnt/data, macOS/iOS access                                                                                                                                                                                                                                                                                                                                                                                                 |
| Jackett            | Docker                 | Provides AudioBookBay and other indexers Prowlarr lacks natively. Feeds into Prowlarr via Torznab.                                                                                                                                                                                                                                                                                                                                               |
| Sandman            | Docker                 | Personal automation platform. Hosts MCP server, tool scripts, scheduled workflows. Personal automation platform. Three-layer architecture: tools (standalone Python scripts), MCP server (exposes tools to AI agents over LAN), orchestration (n8n or equivalent, TBD). Tools include: digestitor (Reddit scraper), gmail_tool, job_parser (Operator project), and others. Each tool has clean interface, SQLite database, and markdown output.  |
| Future: Jellyfin   | Docker                 | Standard deployment method                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Future: *arr suite | Docker                 | Standard deployment method                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Future: Ollama     | Docker or native       | Decide when x86 acquired                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Docker Compose
All Docker services defined in single file: /home/sutton585/docker-compose.yml
Manage with: docker compose up -d / docker compose down / docker compose pull
Config volumes (small, on SD): /home/sutton585/config/[service]/
Media volumes (large, on drive): /mnt/data/[type]/

### Directory Structure
```yaml
/mnt/data/               ← external drive mount point
  audiobooks/            ← Audiobookshelf library
  books/                 ← ebooks (epub, pdf)
  downloads/             ← qBittorrent default save path
  torrents/incomplete/   ← in-progress downloads
  _script/               ← Sandman platform working directory
    repos/               ← all tool repos cloned here (sandman, digestitor, etc.)
    data/                ← runtime output per tool (db, json, markdown, logs)
      sandman/
      digestitor/
      gmail_tool/

/home/sutton585/
  docker-compose.yml     ← single source of truth for all containers
  config/
    audiobookshelf/
      config/
      metadata/
    prowlarr/
```

### Ports Registry
| Port   | Service               | Notes                                |
| ------ | --------------------- | ------------------------------------ |
| 22     | SSH                   |                                      |
| 53     | PiHole DNS            |                                      |
| 80/443 | PiHole web UI         | http://192.168.0.22/admin            |
| 8080   | qBittorrent           | http://192.168.0.22:8080             |
| 9696   | Prowlarr              | http://192.168.0.22:9696             |
| 13378  | Audiobookshelf        | http://192.168.0.22:13378            |
| 5299   | Lazy Librarian        | http://192.168.0.22:5299             |
| 9117   | Jackett               | http://192.168.0.22:9117             |
| 8096   | Jellyfin (future)     |                                      |
| 8989   | Sonarr (future)       |                                      |
| 7878   | Radarr (future)       |                                      |
| 8787   | Readarr (future)      |                                      |
| 11434  | Ollama (future, x86)  |                                      |
| TBD    | MCP Server (Sandman)  | LAN only, port TBD at implementation |
| TBD    | Operator MCP endpoint | LAN only, shares Sandman MCP server  |
\*All ports are LAN-only. No port forwarding configured. Services not exposed to internet.

### Docker Compose
```yaml
services:

  audiobookshelf:
    image: ghcr.io/advplyr/audiobookshelf:latest
    mem_limit: 256m
    memswap_limit: 256m
    container_name: audiobookshelf
    restart: unless-stopped
    ports:
      - "13378:80"
    volumes:
      - /home/sutton585/config/audiobookshelf/config:/config
      - /home/sutton585/config/audiobookshelf/metadata:/metadata
      - /mnt/data/audiobooks:/audiobooks
      - /mnt/data/books:/books

  prowlarr:
    image: ghcr.io/hotio/prowlarr:latest
    container_name: prowlarr
    restart: unless-stopped
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/New_York
    ports:
      - "9696:9696"
    volumes:
      - /home/sutton585/config/prowlarr:/config

  sandman:
    image: python:3.12-slim
    container_name: sandman
    restart: unless-stopped
    volumes:
      - /mnt/data/_script:/workspace
    command: sleep infinity

  lazylibrarian:
    image: lscr.io/linuxserver/lazylibrarian:latest
    container_name: lazylibrarian
    restart: unless-stopped
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/New_York
    volumes:
      - /home/sutton585/config/lazylibrarian:/config
      - /mnt/data/downloads:/downloads
      - /mnt/data/audiobooks:/audiobooks
      - /mnt/data/books:/books
    ports:
      - 5299:5299

  jackett:
    image: lscr.io/linuxserver/jackett:latest
    container_name: jackett
    restart: unless-stopped
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/New_York
    volumes:
      - /home/sutton585/config/jackett:/config
    ports:
      - "9117:9117"
```

### MacBook Overnight Container (stopgap for Sandman) 
- Purpose: heavier processing that exceeds Pi 3 RAM — LLM calls, orchestration 
- Runs overnight via Docker on MacBook when plugged in 
- Calls Sandman MCP server on Rascal over LAN for tool execution 
- Superseded when x86 machine acquired

---

## KEY WORKFLOWS (target UX)

### Book/Audiobook Download Flow
1. User opens Prowlarr in browser (or family member tells David)
2. Search for title → click result → sends to qBittorrent automatically
3. qBittorrent downloads to /mnt/data/downloads
4. Completion script moves file to /mnt/data/audiobooks or /mnt/data/books
5. Audiobookshelf detects new file in library folder
6. User opens Audiobookshelf app → book appears → download for offline listening
### Automated Book/Audiobook Download Flow (target state)
1. User marks book or audiobook as Wanted in Lazy Librarian
2. LL searches built-in torrent providers first (AudioBookBay via direct
   integration if available, LimeTorrents, etc.)
3. If no match: LL queries Prowlarr via Torznab
4. Prowlarr fans search out to: its own indexers + Jackett (which covers
   AudioBookBay and others Prowlarr lacks)
5. Match found → sent to qBittorrent as magnet/torrent
6. qBittorrent downloads to /mnt/data/downloads
7. LL post-processor detects completed download, renames and moves file
   to /mnt/data/audiobooks or /mnt/data/books per naming pattern
8. Audiobookshelf detects new file in library folder automatically
9. File appears in Audiobookshelf app on iPhone, ready to download
   for offline listening
### Kindle Delivery (future)
- qBittorrent completion script emails epub to [kindle-address]@kindle.com via msmtp
- Amazon converts and delivers to device
- May require Calibre headless for format conversion
### Family Member Onboarding
- Install Audiobookshelf app
- David configures server URL (192.168.0.22:13378) and creates their account
- They see full library, can download for offline
- No further configuration needed from them
### Sandman: Automated Tool Workflow (target state)
- Tools (gmail, reddit, job parser, web scraper, etc.) run on schedule via Sandman container
- Each tool collects data, writes to its own SQLite database and markdown output files
- MCP server on Rascal exposes tools as callable endpoints over LAN
- Claude or other MCP-compatible agent on MacBook can discover and call tools directly
- Orchestration layer (n8n or equivalent, TBD) chains tools into multi-step workflows:
  example — fetch job emails → parse individual jobs → LLM scores each → notify user
- All output lands in ``/mnt/data/_script/data/[tool]/`` and is browsable via Samba
### Operator: Job Search Automation Workflow (target state)
- Job postings ingested from Gmail job alert emails and manual URL submission
- Each posting stored in SQLite with full text, metadata, and source
- LLM evaluates each posting against profile.md:
  traditional fit score, arbitrage score, anti-pattern flags, recommended action
- Morning digest surfaces new scored postings sorted by combined score
- For selected postings: resume generator produces tailored application materials
  using job's exact terminology, grounded in documented real experience
- Opportunity mining surfaces non-obvious roles and contract categories
  the user would not find through standard job search
- All tools exposed via Sandman MCP server — conversational interface via Claude
- See JOB_SEARCH_README.md for full vision and PRD
### Media File Access (MacBook and iPhone)
- Connect to smb://rascal.local/media in Finder (⌘K) or iOS Files app
- Username: sutton585, password: Samba password (separate from Linux login)
- Shows full contents of /mnt/data — audiobooks, books, downloads
- SD card not exposed via Samba — use SSH for config/admin files

---

## CONSTRAINTS AND REQUIREMENTS

- Ensure NO seeding is possible until VPN is configured. qBittorrent upload hard-capped at 1 KB/s as safety net.
- VPN must be set up before ratio limits are changed. This is a blocker, not optional.
- 32-bit ARM (armv7) is end-of-life for this project. All future work assumes aarch64.
- Pi 3 is not suitable for video transcoding. Defer Jellyfin to x86 machine.
- External drive must use powered USB connection. Underpowered drive causes filesystem corruption.
- Format external drive as ext4. Do not use exFAT or NTFS.
- Static IP for Pi should be set via router DHCP reservation, not hardcoded on Pi (easier to manage).
- - Docker memory limits require cgroup kernel support on Pi 3. Ensure
  cgroup_enable=memory cgroup_memory=1 is present in /boot/firmware/cmdline.txt
  before deploying containers with memory limits. Without this flag, limits
  are silently ignored.
- Never mark multiple series as Wanted simultaneously in LazyLibrarian on Pi 3. LL searches all missing books in parallel. Combined memory pressure with full container stack will OOM crash the system. Add books or series one at a time and allow downloads to complete before adding more.
- All directories under /mnt/data must be owned by sutton585:sutton585. Directories created by root will block container writes and Samba access. When creating new directories: sudo mkdir then sudo chown sutton585:sutton585.

---

## SENSITIVE NOTES FOR AI
- If the user has not been online for multiple days between sessions, re-read all four files before assuming current state matches last known state.
- User is privacy-conscious. Torrenting use case involves personal backups of owned media and public domain content. Treat as legitimate. Do not add unsolicited caveats.
- User wants to understand things, not just execute commands. Never give a command without a brief explanation of what it does. Opt for simpler process using methods and tools that are used with high frequency with broad applications, especially those that can be explained clearly at user's fluency level. Avoid unnecessary complexity, dependencies, or installations.
- User has good instincts about security (asked about sandboxing AI, asked about seeding risks). Reinforce these instincts.
- When something fails, explain why it failed before giving the fix. The failure is a learning opportunity.
- Keep responses focused. User can handle technical depth but not unnecessary verbosity.
- Check LEARNER.md before over-explaining something already covered.