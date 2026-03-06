# LEARNER.md
# Pi Home Server — User Fluency Log & AI Teaching Calibration

---

## AI AGENT INSTRUCTIONS
- Read this file at session start BEFORE explaining any concept.
- Check fluency level for a topic before deciding how much to explain.
- Update this file at session end by APPENDING to SESSION LOG. Never overwrite prior entries.
- When user demonstrates understanding unprompted → upgrade fluency rating.
- When user is confused by something assumed known → downgrade fluency rating and add note.
- When a concept is newly explained → mark as [covered: session N] and set initial fluency.
- Teaching goal: build genuine understanding, not command memorization.

---

## TEACHING STYLE PROFILE

- Learns well with analogies. Use them for abstract/architectural concepts.
- Asks "why" before running commands — this is a strength. Always reward with a real answer.
- Prefers to understand before doing. Never dump commands without context.
- Gets frustrated by unnecessary complexity. Prefer common, broadly applicable tools.
- Comfortable with iterative learning — doesn't need to master everything at once.
- Responds well to "here's what just happened and why" explanations after failures.
- Does NOT need encouragement or praise — just clear, direct technical guidance.
- Prefers focused responses. Depth is welcome, verbosity is not.

---

## FLUENCY MATRIX

Scale: [none] [aware] [familiar] [comfortable] [proficient]
Format: TOPIC | LEVEL | covered session N | notes

### Operating Systems & Hardware
- ARM vs x86 architecture          | [familiar]     | session 1 | Explained via instruction set analogy. Understands why armv7 causes Docker image failures.
- 32-bit vs 64-bit OS              | [familiar]     | session 1 | Understands Pi 3 hardware supports 64-bit but was running 32-bit OS. Knows reinstall required.
- Raspberry Pi hardware            | [familiar]     | session 1 | Knows own hardware specs, understands RAM/CPU constraints.
- SD card as boot drive            | [comfortable]  | session 1 | Intuited using 64GB card as upgrade. Understands old card as backup.

### Linux CLI
- Basic navigation (ls, cd, pwd)   | [familiar]     | session 1 | Follows commands reliably. Has not demonstrated independent navigation yet.
- File creation/editing (nano)     | [familiar]     | session 1 | Used nano to create systemd service files with guidance.
- sudo and permissions             | [aware]        | session 1 | Uses sudo correctly but hasn't been taught why or the full permission model.
- File permissions (chmod/chown)   | [aware]        | session 1 | Mentioned briefly. Not yet explained in depth. Cover when setting up /mnt/data.
- Filesystem concepts (/mnt, etc)  | [aware]        | session 1 | Understands mount point concept at surface level. fstab not yet explained.
- Piping and redirection (|, >) | [familiar] | session 1, 3 | Session 3: grep flags explained (-A, -B, -i, \|), --since vs --tail, used pipes independently for log filtering.
- Process management               | [none]         |           | Not yet covered.
- Shell scripting basics           | [aware]        | session 3, 4 | Session 4: understands scripts as automation, not just one-off commands. Needs more practice writing independently.

### Package Management
- apt (install, update, upgrade)   | [familiar]     | session 1 | Explained via App Store analogy. Understands repositories, keys, sources.list.
- apt vs other package managers    | [familiar]     | session 1 | Homebrew, Flatpak, pip, npm all explained. Understands ecosystem-specific managers.
- Dependency resolution            | [aware]        | session 1 | Saw it happen in install output. Not formally explained yet.

### systemd and Services
- systemd concepts                 | [familiar]     | session 1 | Explained as service manager. Wrote service files, used enable/start/status/restart.
- systemctl commands               | [familiar]     | session 1 | Used enable, start, restart, status, daemon-reload. Understands --now flag.
- Service file structure           | [familiar]     | session 1 | Wrote [Unit] [Service] [Install] sections manually. Debugged User= field error.
- journalctl / logs                | [none]         |           | Not yet covered. Will be useful for debugging.

### Networking
- IP addresses and LAN             | [comfortable]  | session 1 | Knows own network layout, Pi IP, understands LAN-only exposure.
- Ports and port mapping           | [familiar]     | session 1 | Explained what ports are, built ports registry. Understands -p flag in Docker.
- DNS and PiHole | [comfortable] | session 1, 3 | Session 3: reads nslookup output correctly, understands NXDOMAIN, mDNS/.local explained, docker DNS debugging.
- SSH protocol                     | [familiar]     | session 1 | Understands client/server model. Configured keys and config file.
- SSH public/private keys          | [familiar]     | session 1 | Explained from scratch. Generated keypair, configured ~/.ssh/config, ran ssh-copy-id.
- HTTP vs HTTPS                    | [aware]        | session 1 | Knows the difference. Safari URL bar confusion with IP addresses noted.
- Subnets / CIDR                   | [none]         |           | Not yet covered. Relevant when firewall rules come up.
- VPN concepts                     | [aware]        | session 1 | Understands seeding risk. VPN as solution mentioned but not configured yet.

### Docker
- What Docker is (images/containers)| [familiar]   | session 1 | Explained blueprint/instance analogy. Understands isolation concept.
- docker run flags                 | [familiar]     | session 1 | Walked through -d, --name, --restart, -p, -v flags in detail.
- docker ps / logs / exec          | [aware]        | session 1 | Commands shown but not practiced independently yet.
- Docker volumes | [comfortable] | session 1, 3 | Session 3: deepened via native vs container path confusion. Now understands mounts vs symlinks, shared storage between containers.
- Docker networking | [familiar] | session 1, 3 | Session 3: container isolation explained, daemon DNS configured, understands why containers need explicit DNS.
- Docker Compose                   | [aware]        | session 1 | Explained as single source of truth for multi-container setup. Not yet used in practice.
- Updating containers              | [aware]        | session 1 | docker pull + restart explained conceptually. Not yet practiced.
- Docker vs VM                     | [familiar]     | session 1 | Kernel sharing vs full emulation explained. User grasped it quickly.
-  Docker vs VM (filesystem) | [comfortable] | session 1, 3 | Session 3: deep dive on container isolation, kernel sharing, volume mounts vs symlinks. Solid understanding now.

### Home Server / Self-Hosting
- PiHole / DNS blocking            | [comfortable]  | session 1 | Operates it confidently. Understands Teleporter backup.
- Torrenting concepts              | [comfortable]  | prior     | Knows how torrenting works. Understands seeding risk.
- qBittorrent-nox                  | [familiar]     | session 1 | Installed, configured, understands web UI. Knows seeding settings.
- Prowlarr / indexers              | [aware]        | session 1 | Conceptually explained. Not yet installed or configured.
- Audiobookshelf                   | [aware]        | session 1 | Understands purpose and iOS app. Not yet successfully installed.
- Jellyfin                         | [aware]        | session 1 | Mentioned as future service. Not yet installed.
- *arr suite                       | [aware]        | session 1 | Understands purpose at high level. Deferred to x86 phase.
- Reverse proxy                    | [none]         |           | Not yet covered. Relevant for Phase 2 friendly URLs.
- fstab and drive mounting         | [none]         |           | Will be covered when external drive is connected in T1-08.
- Samba / SMB server config | [familiar] | session 3 | Configured smb.conf, share definitions, smbpasswd, catia module, mDNS hostname access. 
- lighttpd / web servers | [aware] | session 3 | Explained as file server on port 80. Web root concept. Understands PiHole uses it already.
- cron jobs | [familiar] | session 3, 4 | Session 4: wrote and installed a real crontab entry for git pull. Understands timing syntax and log redirection.

### macOS / Development Tools
- Terminal / zsh                   | [comfortable]  | prior     | Uses terminal regularly. No issues.
- Homebrew                         | [familiar]     | session 1 | Mentioned as Mac equivalent of apt.
- Git / GitHub                     | [familiar]     | session 1, 4 | Session 4: generated SSH keypair on Pi, added to GitHub, cloned repo, understood tracked vs untracked files, fixed .gitignore for already-tracked files, set up automated pull via cron.
- SMB file sharing                 | [comfortable]  | prior     | Already had SMB share set up on MacBook.
- .gitignore patterns              | [familiar]     | session 4 | Understands tracked vs untracked distinction. Knows git rm --cached to untrack without deleting. Uses glob patterns (client_secret*.json) over exact filenames.
- requirements.txt / pip           | [familiar]     | session 4 | Understands requirements.txt as dependency manifest. Knows pip installs from it automatically via Docker command. No manual pip installs needed.
- Python project structure         | [familiar]     | session 4 | Understands separation of code (repo), runtime data (output dirs), and secrets (config, never in repo). Independently pushed back on poor directory choices.

### Software Architecture and Platform Concepts
- MCP (Model Context Protocol)     | [aware]        | session 4 | Understands MCP as standard protocol for AI agents calling tools. Knows it's a thin HTTP layer over existing functions, not a framework.
- Workflow orchestration (n8n etc) | [aware]        | session 4 | Understands orchestration tools as existing solutions for dream/workflow logic. Knows n8n, Huginn as candidates. Understands RAM tradeoff on Pi 3.
- APScheduler                      | [aware]        | session 4 | Introduced as Python-native scheduling library. Understands role vs cron — runs inside process, supports job chaining.
- OAuth2 / API credentials         | [aware]        | session 4 | Understands client_secret vs token.json distinction. Knows one-time auth flow produces reusable token. Knows credentials never go in repos.
- Build vs borrow principle        | [comfortable]  | session 4 | Demonstrated strong instinct throughout — independently questioned reinventing orchestration, challenged Digestitor's self-contained approach, asked about existing solutions before committing to custom builds. This is a professional-grade instinct.
- Layered architecture             | [familiar]     | session 4 | Understands tools/MCP/orchestration as distinct layers with different responsibilities. Correctly identified that tools are the priority and orchestration is replaceable.
- Containers as execution env      | [comfortable]  | session 4 | Solid model now: container runs code, volume mounts provide data, image provides dependencies. Independently corrected directory structure mistakes based on this understanding.

---

## SKILLS INVENTORY
### Purpose
This section serves double duty: teaching calibration for this project, and
source material for the Operator job search tool. Each entry describes a skill
the user has demonstrated, what it looks like in professional terminology, and
where it creates non-obvious leverage. When building profile.md (JS-01), draw
directly from this section.

### Format
SKILL | FLUENCY | PROFESSIONAL LABEL | ARBITRAGE CONTEXT | EVIDENCE

### Entries

**Agentic AI workflow design** | [comfortable] |
PROFESSIONAL LABEL: AI Automation Engineer, Workflow Architect, AI Integration Specialist
ARBITRAGE CONTEXT: Any ops-heavy role at a non-technical company where nobody
has seen someone build a pipeline that fetches, processes, and stores structured
data automatically. User can automate significant portions of the role within
weeks without drawing attention. Also: any company still doing manual research,
reporting, or data entry workflows.
EVIDENCE: Digestitor pipeline end-to-end, Sandman platform architecture design,
Reddit-to-markdown workflow with SQLite tracking and scheduled re-scraping

**LLM prompt engineering and output structuring** | [familiar] |
PROFESSIONAL LABEL: Prompt Engineer, AI Product Specialist, ML Operations
ARBITRAGE CONTEXT: Most teams using LLMs are using them like a search engine.
User understands structured output, context window management, system prompts,
multi-turn conversation design, and tool use. This is a meaningful skill gap
at most non-AI-native companies.
EVIDENCE: Digestitor processor, Sandman tool design, this project's session
management system (README/LEARNER/DECISIONS/TASKS pattern)

**SQLite and structured local data pipelines** | [familiar] |
PROFESSIONAL LABEL: Data Engineer, Backend Developer, Database Administrator
ARBITRAGE CONTEXT: Any role that currently tracks things in spreadsheets or
disconnected documents. Office manager, operations coordinator, project
manager at SMBs — user can introduce persistent structured storage where
none existed, making themselves indispensable without anyone understanding
what changed.
EVIDENCE: Digestitor database layer, LL database investigation (read schema,
wrote direct SQL queries to fix state), understanding of deduplication patterns

**Linux server administration** | [familiar] |
PROFESSIONAL LABEL: Systems Administrator, DevOps Engineer, Infrastructure Engineer
ARBITRAGE CONTEXT: Most non-technical companies have no one who can SSH into
a server and fix a problem. Being the person who can is disproportionately
valuable at smaller organizations even if it is not the job description.
EVIDENCE: Full Pi setup from scratch, systemd service management, fstab,
permissions model, cgroup kernel configuration, journalctl debugging

**Docker and containerized service deployment** | [familiar] |
PROFESSIONAL LABEL: DevOps Engineer, Platform Engineer, Infrastructure Engineer
ARBITRAGE CONTEXT: Docker is table stakes in technical roles but rare in
ops and admin roles. User can deploy, maintain, and debug containerized
services — giving them the ability to run sophisticated tooling on any
machine without IT involvement or vendor dependency.
EVIDENCE: Full docker-compose stack, memory limit configuration, volume
architecture, container networking, image troubleshooting across architectures

**HTML/RSS scraping and web data extraction** | [familiar] |
PROFESSIONAL LABEL: Data Engineer, Web Scraper, Research Analyst
ARBITRAGE CONTEXT: Any role where "research" means a human manually reads
websites all day. Market research, competitive intelligence, compliance
monitoring — user can script the collection and leave humans to do only
the judgment work.
EVIDENCE: Digestitor RSS + JSON pipeline, Reddit API interaction, LL
provider debugging (reading HTTP responses, diagnosing 404/403/429 patterns)

**Self-directed technical learning under ambiguity** | [comfortable] |
PROFESSIONAL LABEL: (soft skill — mention in cover letters and interviews)
ARBITRAGE CONTEXT: Most candidates either know the stack or don't. User
demonstrates ability to pick up unfamiliar tools, debug without documentation,
and build working systems across multiple new domains simultaneously.
EVIDENCE: This entire project — Docker, Linux, Python, SQLite, networking,
service configuration — all acquired in parallel while building a working system

**Documentation and AI context management** | [comfortable] |
PROFESSIONAL LABEL: Technical Writer, Knowledge Manager, AI Operations
ARBITRAGE CONTEXT: Underrecognized skill. Designing documentation that is
optimally useful for AI agents — structured, consistent, machine-readable
without losing human readability — is a capability most teams do not have
and increasingly need.
EVIDENCE: README/LEARNER/DECISIONS/TASKS system design, session protocol
design, fluency tracking format, Digestitor frontmatter schema

---
## DO NOT RE-EXPLAIN (already clearly understood)
- What a Raspberry Pi is
- What SSH is at a high level
- What a torrent is
- Why seeding without VPN is risky
- The difference between the MacBook and the Pi
- That the username sutton585 exists on both machines
- Why credentials never go in git repos
- The difference between code (repo), runtime data (output dirs), and secrets (config dir)
- Container filesystem is ephemeral — data must live in volume mounts to persist
- MCP as a protocol concept — what it is and why it matters for this project. Focus on what will be possible with MCP and it's professional/career utility for the future.
- The arbitrage framing for career strategy — user understands and endorses the overemployed model, automation-first approach to roles, and non-obvious opportunity categories including government contracting and SMB acquisition
- That profile.md is the source of truth for Operator and must be built before any tooling — user understands this dependency
- The three-layer Sandman architecture: tools, MCP server, orchestration
- That Operator is a Sandman tool following the same architecture pattern as Digestitor and gmail_tool


---

## SESSION LOG

### Session 1 — 2026-02-19
Topics covered this session:
- Full stack planning: torrent client, Prowlarr, Audiobookshelf, future Jellyfin/*arr/LLM
- Compared Pi vs x86 for home server use case
- Explained x86 vs ARM instruction sets
- Package managers survey (apt, Homebrew, Flatpak, pip, npm)
- Installed qBittorrent-nox natively, debugged missing service file and wrong User= field
- Explained systemd service files in detail
- Explained Docker concepts: images, containers, volumes, flags, compose
- Explained SSH key pairs from scratch, configured ~/.ssh/config
- Attempted Audiobookshelf install — discovered armv7 incompatibility
- Decision made to migrate to 64-bit OS
- Built four-file project documentation system
- Explained Docker Compose as preferred multi-service management approach

User strengths observed:
- Excellent instinct for asking "why" before executing commands
- Caught username confusion in Docker commands (sutton585 on both machines)
- Read Audiobookshelf docs independently and flagged architecture concern correctly
- Good security instincts (sandboxing AI, seeding risk)
- Learns architectural concepts quickly with analogies

Gaps identified this session:
- File permissions model (chmod/chown) not yet understood — needed when setting up /mnt/data
- fstab not yet covered — needed for external drive mount
- Shell scripting not yet started — needed for Phase 2 completion scripts
- journalctl not yet introduced — would help with debugging
- Docker Compose used conceptually but not yet in practice

---
### Session 2 — 2026-02-20

Topics covered this session:

**Docker Compose in practice**
- Wrote and validated a real docker-compose.yml with three services
- Explained each field in detail: image, restart, ports, volumes, environment, network_mode, command
- User now understands the file as a recipe that describes containers without starting them
- `docker compose up -d`, `docker ps`, `docker logs` all used in practice
- Fluency upgrade: Docker Compose [aware] → [familiar]. Used it for real, understands why it exists.

**Docker image troubleshooting**
- linuxserver/prowlarr failed with libcrypto.so.3 Exec format error on Debian Trixie
- Diagnosed as image/OS incompatibility, not a user error
- Fixed by substituting ghcr.io/hotio/prowlarr:latest
- User observed that architecture/OS compatibility issues recur across this project — good pattern recognition
- Fluency upgrade: Docker image troubleshooting [none] → [aware]

**docker logs**
- Used `docker logs prowlarr` to diagnose a failing container
- Explained as the container equivalent of journalctl
- Fluency: docker ps / logs / exec [aware] → [familiar]

**systemd symlinks explained**
- User asked about "Created symlink" message from systemctl enable
- Explained symlink as a shortcut/alias — the enable command creates a pointer in the boot folder
- User understood immediately with the analogy
- Fluency upgrade: systemd concepts [familiar] → [comfortable]

**File permissions / ownership**
- Hit a real permissions error: couldn't mkdir on /mnt/data because root owned it after mount
- Explained why: drive was mounted by root, ownership wasn't transferred yet
- Fixed with sudo chown before mkdir — user understood the sequence
- Good concrete lesson in why ownership matters
- Fluency upgrade: file permissions (chmod/chown) [aware] → [familiar]

**fstab and drive mounting**
- Walked through full drive setup: parted, mkfs.ext4, blkid, fstab entry with nofail
- Explained UUID vs device name (/dev/sda1 can change, UUID doesn't)
- Explained nofail flag: Pi boots cleanly even if drive is absent
- Fluency upgrade: fstab and drive mounting [none] → [familiar]

**ext4 vs exFAT tradeoffs**
- User challenged the ext4 decision with a reasonable performance argument
- Discussed journaling, always-on reliability, cross-platform convenience tradeoffs
- User made an informed decision to stick with ext4
- Good example of user engaging critically rather than just following instructions

**Torrent/indexer ecosystem**
- Explained Prowlarr indexer catalog, public vs private trackers
- Explained Cardigann definition format and its relationship to Jackett
- Explained why Anna's Archive can't be replicated in Prowlarr (not a torrent tracker)
- Explained FlareSolverr purpose: headless browser to bypass Cloudflare
- Introduced Lazy Librarian as book/audiobook automation alternative
- Fluency: Prowlarr/indexers [aware] → [familiar]

**Prowlarr access control**
- User asked about per-user adult content restrictions
- Explained Prowlarr has no permission tiers — single admin access model
- Conclusion: treat Prowlarr as admin-only, don't share URL with family

Gaps identified or reinforced this session:
- Shell scripting still not covered — will be needed for completion scripts (T2-02)
- journalctl not yet formally introduced — used docker logs as practical equivalent
- Reverse proxy concepts not yet covered — deferred to Phase 2

User strengths observed this session:
- Pushed back on ext4 decision with a coherent argument — good critical thinking
- Asked for explanations before proceeding multiple times — consistent with learning style
- Caught when AI was repeating itself unhelpfully (AudioBookBay catalog search) and called it out directly
- Good instinct on Prowlarr access control — thought through the family UX implication
- Proposed aggregating Anna's Archive sources into Prowlarr — creative thinking, engaged with the architecture

---
### Session 3 — 2026-02-25

Topics covered this session:

**Samba / SMB file sharing**
- Installed and configured Samba on Pi
- Explained share definitions in smb.conf
- Explained why [media] and [nobody] appear as separate shares
- Explained mDNS / .local hostname resolution (Bonjour) — why rascal.local works without DNS
- Explained illegal characters in filenames (colons) causing macOS visibility issues over SMB
- catia vfs module explained as character translation layer
- Fluency: SMB file sharing [comfortable] → [comfortable] (already had prior experience, extended to server-side config)

**Docker networking and filesystem — deepened understanding**
- User asked excellent question about container filesystem isolation vs VMs
- Explained containers share host kernel, VMs emulate entire machine
- Explained volume mappings as mounts not symlinks — physical files land on host
- Explained why two containers with same volume mapping share real storage
- Explained why qBittorrent (native) uses real paths while Docker containers use container-internal paths
- Fluency upgrade: Docker volumes [familiar] → [comfortable]
- Fluency upgrade: Docker networking [aware] → [familiar]

**Shell scripting — first real script**
- User ran first for loop: renaming files with colon substitution
- Explained for f in *, mv, and ${f/: / - } variable substitution syntax
- User understood immediately and ran it successfully
- Shell scripting basics | [aware] | session 3 | First for loop — file renaming with variable substitution. Understood immediately. Needs more practice.

**cat command clarified**
- User correctly questioned cat = concatenate
- Explained dual use: concatenation vs quick file read
- Good critical thinking — catches inconsistencies

**cron jobs introduced**
- Explained cron syntax (*/5 * * * *) in context of GitHub pull use case
- User understood scheduling concept immediately
- Fluency: cron/scheduling [none] → [aware]

**DNS deeper understanding**
- Worked through nslookup output — user now reads Server, Address, Non-authoritative answer correctly
- Explained NXDOMAIN vs successful resolution
- Explained mDNS vs traditional DNS
- Explained why .local works without PiHole
- Fluency upgrade: DNS and PiHole [familiar] → [comfortable]

**Web servers introduced**
- Explained lighttpd as lightweight web server
- Explained web root concept (/var/www/html/)
- Explained port 80 and why rascal.local hits PiHole
- Connected to existing knowledge: same concept as volume mappings — configured directory serves files
- Fluency: Reverse proxy / web servers [none] → [aware]

**grep flags deepened**
- Explained -A (after) and -B (before) context flags
- Explained \| as OR operator in grep patterns
- Explained --since flag for docker logs vs --tail
- Fluency upgrade: Piping and redirection [aware] → [familiar]

**Package/service debugging pattern reinforced**
- User now independently reaching for logs as first debugging step
- Correctly diagnosed download path misconfiguration from symptoms
- Correctly identified colon as cause of Samba visibility issue
- Good pattern: observe symptom → form hypothesis → test → fix

**Anna's Archive domain situation**
- Explained court injunction and domain seizure
- Explained why .org is NXDOMAIN while .li and .gl resolve
- Good real-world example of why infrastructure needs maintenance

**LLM/AI hardware assessment**
- Discussed Pi 3 limitations for local inference
- Explained why M3 MacBook is strong for local models (unified memory)
- Introduced LM Studio, quantized models, Continue.dev
- Explained hybrid vs fully local pipeline tradeoffs
- Fluency: LLM/AI tooling [none] → [aware]

Gaps identified or reinforced this session:
- journalctl still not formally introduced — used docker logs as practical equivalent throughout
- Torznab/Prowlarr connection not yet completed — key gap in LL workflow
- Shell scripting exposure minimal — one for loop, needs more practice
- VPN still not configured — D-007 blocker remains in place

User strengths observed this session:
- Caught cat/concatenate inconsistency immediately — good critical thinking
- Diagnosed download path issue correctly before being told
- Asked excellent architectural question about container vs VM filesystem visibility
- Good instinct to fix root cause (LL filename pattern) rather than just patch symptoms (catia only)
- Independently reached for logs as debugging tool multiple times
- Proposed GitHub-pull approach for web content unprompted — good architectural instinct
- Identified Project Sandman as a real workflow need, not just a toy idea

---
### Session 4 — 2026-02-27

Topics covered this session:

**Torznab category filtering across multiple hops**
- Confirmed &cat= parameter is forwarded intact through Prowlarr→Jackett chain
- Explained that non-compliant indexers may ignore filter regardless
- User now understands category filter as the correct architectural lever,
  not hop reduction
- Fluency: Torznab/indexer protocols [aware] → [familiar]

**qBittorrent category system**
- Explained per-category save paths as the conventional *arr suite pattern
- User correctly identified this solves cross-contamination without LL needing
  to parse unrelated downloads
- User correctly identified Docker volume scoping as reinforcement of this
- Fluency: qBittorrent categories [none] → [familiar]

**LL per-content-type directory config**
- Explained LL has separate download dir fields per content type
- User correctly chose Scenario A (per-type directories) over Scenario B
  (single LL staging hopper) once capabilities confirmed
- Fluency: LL config/architecture [familiar] → [comfortable]

**arr suite architecture**
- Explained Radarr/Sonarr/Readarr as air traffic controllers per content type
- User correctly identified the pattern before being told
- Noted Readarr is retired — LL fills that role in this stack
- Explained Jellyfin library scoping as the correct solution for adult content
  isolation from family profiles
- Fluency: *arr suite [aware] → [familiar]

**Tailscale vs Headscale**
- Explained WireGuard as underlying protocol (strong, audited)
- Explained Tailscale coordination server metadata exposure
- Explained Headscale as self-hosted coordination plane eliminating third-party
  visibility
- User identified this as relevant to their threat model
- Fluency: VPN/remote access concepts [aware] → [familiar]

User strengths observed:
- Correctly identified Prowlarr as redundant middle layer before being told,
  then correctly reversed position when shown future *arr value
- Insisted on validating built-in providers before expanding Torznab — good
  debugging instinct, correctly identified as a blocker not a nice-to-have
- Identified Readarr retirement independently
- Pushed back on adding complexity before validating existing config works


---
### Session 4 — 2026-02-28

Topics covered this session:

**Git on Rascal — SSH keys and repo setup**
- Generated ed25519 keypair on Pi (ssh-keygen)
- Added Pi's public key to GitHub account — Pi now has push/pull access
- Explained GitHub host verification prompt — user initially rejected it thinking
  it was an error. Clarified: typing "yes" is correct and expected on first connect.
- Cloned sandman repo to Pi successfully
- Understood that Rascal having full push/pull access vs read-only deploy key is
  appropriate for a personal private workflow
- Fluency upgrade: Git / GitHub [aware] → [familiar]

**Git hygiene — .gitignore mechanics**
- Explained tracked vs untracked file distinction — .gitignore only affects
  untracked files, has no effect on files already committed
- Taught git rm --cached to stop tracking a file without deleting it from disk
- User correctly identified that exact filename in .gitignore is fragile — glob
  pattern (client_secret*.json) is better practice
- Noted that client ID string in credentials filename is semi-public but no reason
  to broadcast it — pattern-based ignore handles it cleanly
- Fluency upgrade: .gitignore [none] → [familiar]

**Directory structure — code vs data vs secrets**
- Extended discussion over multiple iterations. User independently identified
  and pushed back on poor suggestions (code on SD card, data mixed with code).
- Settled on clean three-way separation: repos in _script/repos/, runtime output
  in _script/data/, credentials in config/ outside all repos.
- User grasped that this separation is not arbitrary — it's about SD card wear,
  git hygiene, and credential security simultaneously.
- Strong instinct: user kept asking "why isn't this in the obvious place" and
  was right every time.

**cron jobs — practiced for real**
- Wrote and installed a real crontab entry for automated git pull
- Understood */5 timing syntax and log redirection (>> logfile 2>&1)
- Understood that cron on the Pi host updates files that container sees
  immediately via volume mount — no container restart needed for code changes
- Fluency upgrade: cron jobs [aware] → [familiar]

**requirements.txt and Docker startup command**
- Explained requirements.txt as the manifest that eliminates manual pip installs
- Understood the sh -c pattern in Docker command: install deps then start script
- Understands that pushing requirements.txt to GitHub triggers automatic
  dependency installation on next container restart — no SSH needed
- Fluency upgrade: requirements.txt / pip [none] → [familiar]

**Container architecture — solidified**
- Extensive back-and-forth about why code lives where it does relative to containers
- User independently corrected several mistakes by applying the ephemeral
  filesystem model correctly without being prompted
- Now has solid working model: image = dependencies, volume = data, command = entrypoint
- Fluency upgrade: containers as execution environment [familiar] → [comfortable]

**APScheduler introduced**
- Introduced as the Python-native scheduling alternative to cron inside containers
- Explained why sleep loops are fragile (exceptions kill the process silently,
  code changes not picked up)
- Understood APScheduler's advantage: runs inside the process, supports job
  chaining, config-driven scheduling
- Fluency: APScheduler [none] → [aware]

**MCP (Model Context Protocol) introduced**
- Explained MCP as Anthropic's standard for AI agents calling external tools
- Understood that grains/tools map directly onto MCP tool concept
- Understood MCP server as a thin HTTP layer — tools don't change, just get wrapped
- Excited by the implication: Claude on MacBook calling Pi tools over LAN
- Fluency: MCP [none] → [aware]

**Workflow orchestration — n8n, Huginn, existing solutions**
- Major architectural pivot: user independently questioned whether building a
  custom controller was reinventing solved problems
- Explained n8n, Huginn, Prefect as the existing landscape
- Explained RAM tradeoffs: n8n likely too heavy for Pi 3, Huginn worth evaluating
- User correctly identified that tools (grains) are the novel work — orchestration
  is infrastructure that should use existing software
- Fluency: workflow orchestration [none] → [aware]

**"Build vs borrow" principle — demonstrated strong instinct**
- Came up repeatedly and unprompted: Digestitor reinventing html2text, Sandman
  reinventing n8n, credentials JSON reinventing standard OAuth patterns
- User consistently asked "does this already exist" before committing to building
- This is a professional-grade engineering instinct — explicitly noted because
  it will serve well beyond this project
- Fluency: build vs borrow principle [none] → [comfortable]

**Layered architecture — tools / MCP / orchestration**
- User understood the three-layer model quickly and correctly
- Independently identified that tools are the priority because they are the
  novel, non-replaceable layer
- Understands that orchestration layer can be swapped (cron → n8n → something else)
  without touching tool code if tools have clean interfaces
- Fluency: layered architecture [none] → [familiar]

**Project Sandman — scope redefined**
- Original concept (custom Python controller orchestrating custom grain tools)
  replaced with industry-standard approach
- Sandman repo becomes: MCP server + config + scheduling bootstrap
- Individual tool repos (gmail_tool, digestitor, job_parser) carry their own logic
- Vocabulary shifted from metaphor-specific (grains, dreams) to industry-standard
  (tools, integrations, automations, workflows)
- TASKS.md Phase 2.5-S written with full build sequence and acceptance criteria
- DECISIONS.md updated: D-018 (ai-sandbox → sandman), D-019 (platform architecture),
  D-P003 (orchestration tool selection pending)

Gaps identified or reinforced this session:
- OAuth2 auth flow not yet run — gmail_tool cannot be built until token.json exists
- APScheduler used conceptually only — not yet written any scheduler code
- MCP server implementation not yet started — no hands-on experience yet
- n8n / Huginn not yet evaluated for RAM on Pi — TS-02 is the task for this
- Python packaging / how tools import shared code — mentioned but not practiced

User strengths observed this session:
- Strongest session yet for architectural thinking and professional instincts
- Repeatedly identified reinvention risks before being told — unprompted
- Pushed back on directory structure suggestions and was correct every time
- Correctly identified that tools are the valuable layer, orchestration is replaceable
- Asked "is this well-trodden ground I'm reinventing needlessly" — exactly the
  right question at exactly the right time
- Shifted vocabulary to professional terms naturally once the distinction was clear
- Scope redefinition was user-driven, not AI-driven — strong ownership of the project

### Session 5 — 2026-03-03

Topics covered this session:

**LazyLibrarian deep debugging**
User developed strong independent debugging instincts throughout this session.
Correctly insisted on understanding native provider failures before adding
Torznab complexity — this was the right call and led to finding the root cause
(AudioBookBay 404, providers silently blocked). Demonstrated ability to read
log output and form accurate hypotheses. Correctly identified that the blocklist
was masking the real problem.

**Torznab protocol and indexer architecture**
LL can accept multiple independent Torznab connections, one per Jackett indexer.
No daisy-chaining required. This is the canonical approach for LL. User
understood this immediately once demonstrated and applied it to solve the
indexer problem completely.

**Docker memory limits and Pi cgroup support**
OOM crash was a hard lesson but a valuable one. User now understands that
Pi 3 requires explicit kernel flag for Docker memory limits to work, that
deploy.resources.limits syntax is required over deprecated mem_limit, and that
LL's parallel search behavior is dangerous on 1GB RAM without limits enforced.

**Linux permissions model — deepened**
Real consequence of wrong ownership — blocked LL writes, blocked Samba.
Fixed with chown and chmod. User now understands user:group format and 755
breakdown from first principles, not just pattern-matching.

**Desired state management as a pattern**
Explained the difference between imperative scripting (do this thing) and
desired state management (ensure this state exists). User connected this
correctly to Kubernetes without needing it explained — asked whether they
were doing Kubernetes. Good instinct. Explained why K8s is wrong at this
scale but the mental model is identical.

**Sandman architecture finalized**
Three-layer model confirmed: tools, MCP server, orchestration. Sandman setup
script concept defined as hardware-agnostic desired-state deployment system
with sandboxed isolation. All metaphor-specific terminology retired.

**Operator project scoped**
Full PRD written. Arbitrage framing as core philosophy. Overemployed model
explicitly endorsed. Government contracting, SMB acquisition, and unknown
unknowns identified as opportunity categories. JS-01 through JS-06 tasks
defined. User correctly identified profile.md as the foundation everything
else depends on.

**ABS metadata model**
User learned that ABS reads folder structure first, not ID3 tags. SERIES
and SERIES-PART fields explained. User correctly deferred metadata tagging
automation as non-blocking — proves understanding that infrastructure should
only be built when a real problem exists.

Fluency upgrades this session:
- Docker memory limits and cgroup support: [none] → [familiar]
- LL architecture and Torznab debugging: [aware] → [comfortable]
- Linux file permissions in practice: [familiar] → [comfortable]
- qBittorrent category system: [none] → [familiar]
- ABS metadata model: [none] → [aware]
- Tailscale vs Headscale vs WireGuard: [aware] → [familiar]
- Desired state management pattern: [none] → [aware]
- Operator/job search project architecture: [none] → [familiar]

User strengths observed this session:
- Correctly blocked Torznab addition until native provider failure was understood
- Identified blocklist as suspicious from log patterns without being told
- Independently insisted on understanding root cause before adding complexity
- Asked "is this what Kubernetes is?" — correct conceptual leap at the right moment
- Pushed back on moving all config to HDD — correctly accepted the reasoning
  when explained rather than just following the suggestion
- Identified profile.md as the critical dependency before any tooling is built
- Strong arbitrage instinct — immediately saw the overemployed angle as more
  interesting than traditional career path optimization