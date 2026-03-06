# Project Sandman: Architecture & File Structure

## Overview
Project Sandman is a config-driven personal automation platform that acts as an intelligence layer. It orchestrates a collection of standalone scraper modules, enriches the collected data using a centralized AI layer, and delivers organized insights and digests. It is built to prioritize "arbitrage over competition," focusing on low-competition, high-leverage opportunities.

## Overall Architecture

### 1. The Core Engine (Dockerized)
To ensure the system is portable, easily reproducible, and isolated, Sandman runs entirely inside a Docker container.
- **Docker Compose**: Orchestrates the Sandman core engine, the central database, and any local AI tooling.
- **Config-Driven UX**: A single, simple configuration file (`config.yml`) drives the entire platform. Users define their feed sources, schedules (cron), AI enrichment parameters, and digest settings without needing to edit code.

### 2. The AI Layer (Intelligence Engine)
The intelligence engine is responsible for evaluating, scoring, and summarizing all incoming data streams based on the user's profile and criteria.
- **LiteLLM**: Used as the universal translation layer to route LLM requests. This provides a unified API allowing Sandman to seamlessly switch between local models and external APIs without changing core logic.
- **LM Studio (Local Inference)**: Handles local, open-source models for privacy-focused or cost-free inference when computational power permits.
- **Gemini CLI Support**: The platform integrates with the Gemini CLI. The Sandman core exposes MCP (Model Context Protocol) endpoints, allowing the Gemini CLI to interact conversationally with the database, trigger manual scrapes, evaluate specific job postings, or generate resumes on the fly directly from the terminal.

### 3. Modular Scrapers (The Sources)
Scrapers are decoupled from the core Sandman logic. Each scraper is a standalone repository acting as a module that Sandman clones and updates via `git pull`.

Required Modules:
- **`gmail_scraper`**: Monitors a designated Gmail inbox for specific alerts (e.g., job alerts, newsletters) and extracts the raw text/HTML content.
- **`jobber` (LinkedIn / Indeed Scraper)**: 
  - **Email Parsing**: Processes job alerts forwarded by the `gmail_scraper`.
  - **Direct Scraping / API**: Executes custom search terms and filters on job boards (via official APIs if available, or structured web scraping) to find roles that match the user's "arbitrage" criteria.
  - **Manual Input Processing**: Can take manual input via an Apple Shortcut for jobs the user discovers while browsing.
- **`manual_input`**: A dedicated webhook listener module. It captures arbitrary data sent from client devices (like Apple Shortcuts triggered on iOS/macOS) and routes the content into the central Sandman inbox for AI evaluation.
- **`digestitor`**: The fully realized Reddit and social feed scraper.
- **`market_monitor`**: Monitors platforms like eBay, Facebook Marketplace, and Gov Surplus sites for physical arbitrage opportunities.

### 4. Storage & Inbox (SQLite + Markdown)
- **`operator.db` (SQLite)**: The central memory of the system. It handles deduplication, stores raw scraped data, tracks the status of job applications, and logs AI evaluation scores.
- **Markdown Feeds & Digests**: AI-enriched items are output as Markdown files containing structured YAML frontmatter (Score, Summary, Arbitrage Potential). This makes the data natively readable in tools like Obsidian.

---

## File Structure

```text
/sandman_project/
├── docker-compose.yml          # Container definitions (Sandman core, SQLite, LiteLLM proxy)
├── install.sh                  # Bootstrap script (pulls modules, sets up environment)
├── teardown.sh                 # Graceful shutdown script
├── ~/.sandman/                 # User config directory (mapped as volume, persists across installs)
│   ├── config.yml              # Easy UX config for automations, schedules, and AI routing
│   ├── prompts/                # Custom AI prompts for scoring and summarization
│   └── criteria/               # User context files (profile.md, logic.md, anti-patterns)
├── /workspace/                 # Runtime Data (mapped as volume)
│   ├── operator.db             # Central SQLite database
│   ├── feeds/                  # Raw markdown outputs from individual modules
│   └── digests/                # Finalized, AI-curated Markdown digests
└── modules/                    # Cloned scraper repositories (updated via 'git pull')
    ├── digestitor/             # Reddit / social scraping module
    ├── gmail_scraper/          # Email alert extraction module
    ├── jobber/                 # LinkedIn/Indeed & job evaluation module
    ├── manual_input/           # Apple Shortcut webhook listener module
    └── market_monitor/         # Marketplace and surplus scraping module
```

---

## The Automation Workflow

1. **Scheduling**: The Sandman core reads `config.yml` and triggers modules on their defined cron-style schedules.
2. **Ingestion**: A module runs (e.g., `jobber` checks LinkedIn APIs, or `gmail_scraper` pulls new emails).
3. **AI Enrichment**: Sandman sends the raw scraped data, the user's `profile.md`, and the specific task prompt to the AI Layer via **LiteLLM**.
   - Complex reasoning (e.g., matching a job against deep arbitrage criteria) routes to a high-tier model.
   - Routine summarization routes to a local model via LM Studio.
4. **Storage**: The AI returns structured data (Priority Score, Fit Reasoning, Arbitrage Flags). This is inserted into `operator.db` and written as a Markdown file in `/workspace/feeds/`.
5. **Digestion**: A scheduled Digest automation aggregates the highest-scoring items across all active modules and compiles a clean, actionable Markdown summary into `/workspace/digests/`.
6. **CLI Interaction**: At any time, the user can use the Gemini CLI to query the database, ask for resume generation for a specific high-scoring job, or manually push a new link into the evaluation loop.

---

## Additional Technical Considerations & Corrections

- **Python Automation, Not Cron**: While schedules may be defined in `config.yml` using familiar syntax, the actual execution and orchestration rely on Python-based automation loops (e.g., the `schedule` library) running continuously within the containers, rather than raw system `cron` jobs. This ensures cross-platform reliability and better state management.
- **Configurable Output Paths**: In development or **Debug Mode**, scrapers will output their data to the localized `/workspace/feeds/` and `/workspace/digests/` directories. However, in practice, the user specifies exact absolute paths in the config file so that the markdown files export directly into their Obsidian Vault or personal folder structure.
- **External Secret Management**: API keys, tokens, and sensitive credential files (such as the `credentials.json` required for the Gmail API) are kept strictly outside of the repository (e.g., `~/.sandman/auth/`). Scrapers read these paths dynamically from the configuration file.