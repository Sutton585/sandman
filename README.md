# Sandman: The AI Automation Orchestrator

Sandman is a high-signal knowledge management suite designed to transform the messy web into structured, permanent Markdown files. It is built for professional note-taking environments like **Obsidian**, AI-driven research, and **RAG (Retrieval-Augmented Generation)** pipelines.

## 1. Project Philosophy

Sandman is not just a collection of scrapers; it is an **Accumulator**.
- **Living Notes:** Instead of overwriting files, Sandman updates metadata and appends new content, creating a chronological record of an evolving discussion or thread.
- **Source of Truth:** The filesystem (Markdown) is the ultimate authority. Our SQLite databases are treated as self-healing caches that reconcile their state against your actual notes on every startup.
- **Zero Noise:** We leverage world-class open-source libraries like **Trafilatura**, **Crawl4AI**, and **JobSpy** to extract only the information that matters, stripping away the noise of the modern web.

## 2. The Three-Tiered Architecture

To ensure scalability and maintainability, Sandman is organized into three distinct tiers of modules:

### Tier 1: Source Scrapers
These monitor your primary entry points and capture raw content.
- `reddit2md` (reddit2md): Scrapes subreddits (sources) and tracks thread maturity.
- `gmail2md`: Monitors Gmail labels (e.g., Job Alerts, Newsletters) and extracts embedded URLs.

### Tier 2: Entity Extractors
These are "domain experts" that take a specific URL and turn it into a high-fidelity record.
- `jobs2md`: Uses **JobSpy** to turn LinkedIn/Indeed URLs into structured Job Notes (Salary, Skills, Company).

### Tier 3: Utility Scrapers
The "Universal Fallback" for generic web content.
- `web2md`: Uses **Trafilatura** to de-clutter any generic article or blog post into clean Markdown.

## 3. Orchestration & Deployment: The "Orchestrator"

Sandman is designed for **Zero-Impact Productivity**. To ensure your daytime CPU cycles are reserved for your work, the suite is built to run within a scheduled **Docker Container** on your primary machine (e.g., MacBook).

### The Standard Cycle
- **Status:** Dormant during the day to save resources.
- **Trigger:** An automated schedule (Cron or Apple Shortcut) spins up the `sandman-orchestrator` container on a recurring schedule.
- **Action:** The container executes the full pipeline:
    1. **n8n** (Self-hosted inside Docker) manages the high-level workflow logic.
    2. **Tier 1 Scrapers** pull fresh data from Gmail and Reddit.
    3. **Tier 2 Extractors** (JobSpy) process any identified job links.
    4. **Tier 3 Utilities** (Trafilatura) clean up generic web content.
- **Finality:** The container shuts down once the "To-Do" queue is empty, leaving your vault updated and your system resources free for later review.

### Sandboxed Architecture
- **Isolation:** Each module is strictly sandboxed within its own virtual environment (`venv`) or sub-container logic to prevent dependency hell.
- **Volume Mapping:** Only the `md_output_directory` (Obsidian Vault) and `sandman_config` are mapped to the host, keeping the system footprint minimal and secure.

## 4. Developer Onboarding & Project Context

To quickly understand the Sandman ecosystem and get up to speed on the current state of development, follow this recommended reading path. This is especially useful at the start of a new development session to establish a complete context of the project's goals and structural standards.

1.  **Project Overview:** Start with this `README.md` to understand the high-level vision and the "Orchestrator" deployment model.
2.  **Global Standards:** Read the [Unified Module Blueprint](modules/unified_module_blueprint.md). This document defines the mandatory architectural rules (The "5 Buckets"), schema baselines, and cross-module communication protocols shared by all scrapers.
3.  **Module Registry:** Review the `modules/` directory. Each subdirectory (e.g., `jobs2md`, `gmail2md`) is an independent GitHub repository with its own isolated virtual environment.
4.  **Specific Module Context:** Once you've identified a module to work on, read its local `README.md` and its `architecture.md` file. These documents detail the platform-specific strategies, unique metadata fields, and implementation progress for that specific scraper.

## 5. Getting Started

1.  Clone the repository.
2.  Review `sandman_config/config.yml` to set your global paths (`md_output_directory`, `data_output_directory`).
3.  Configure your credentials in `sandman_config/auth/`.
4.  Run a module: `python modules/reddit2md/reddit2md.py`.

### Controlling Output (`verbose`)
All Sandman modules and the central orchestrator respect the `verbose` integer parameter to control console output. This parameter is standardized across the entire ecosystem:
- **`0`**: Errors only (silent operation, best for background cron jobs).
- **`1`**: Standard progress and warnings (Recommended default, shows clear milestones).
- **`2`**: Granular debug information (best for development and troubleshooting).

**Usage Examples:**
- **CLI Flag:** `python sandman.py --verbose 1`
- **YAML Config:**
  ```yaml
  settings:
    verbose: 1
  ```
- **Python Dictionary:** `JobScraper(overrides={'verbose': 1})`

### Age Restrictions (`min_age_hours` / `max_age_hours`)
Sandman allows you to strictly filter the data you extract based on its age.
- **`min_age_hours`**: The minimum time a post or listing must exist before it is considered valid. Anything newer is entirely ignored by the scrapers.
- **`max_age_hours`**: The maximum age of a post to be considered relevant. Anything older than this limit is entirely ignored by the scrapers.

### Maturity Logic (`rescrape_threshold_hours`)
Some modules (like `reddit2md`) support a maturity queue to capture conversations as they develop.
- **`rescrape_threshold_hours`**: The window of time a post must exist before it is considered mature. If a post is scraped and its age is less than this limit, it will be marked with a `rescrape_after` timestamp so Sandman knows to update it later.

**Usage Examples:**
- **CLI Flag:** `--min-age-hours 12 --max-age-hours 48 --rescrape-threshold-hours 24`
- **YAML Config:**
  ```yaml
  settings:
    min_age_hours: 12
    max_age_hours: 48
    rescrape_threshold_hours: 24
  ```
- **Python Dictionary:** `JobScraper(overrides={'min_age_hours': 12, 'rescrape_threshold_hours': 24})`

### Pagination (`offset`)
When scheduling large, multi-part scrapes, or attempting to resume a stopped queue, you can use the `offset` parameter to skip the beginning of a source feed.
- **`offset`**: Discards the first N results returned by the source before the scraper begins processing them.

**Usage Examples:**
- **CLI Flag:** `--offset 10`
- **YAML Config:**
  ```yaml
  settings:
    offset: 10
  ```
- **Python Dictionary:** `JobScraper(overrides={'offset': 10})`

## 6. Managing Multiple Repositories (Git Workflow)

Each module in the `modules/` directory is an independent GitHub repository. Because of this, a standard `git add .` from the root of Sandman will **not** track or commit changes to the history of the individual modules.

To simplify your workflow, two helper scripts are provided in the root directory:

- **`./save "your commit message"`**: Stages and commits all changes locally for **every** modified module and the root project. This is the "safe" command for saving your progress without sending it to the web.
- **`./push`**: Iterates through all repositories and pushes any unpushed local commits to their respective GitHub remotes.

### Initial Setup
Before running these for the first time, you must give them permission to execute on your system:
```bash
chmod +x save push
```

### Typical Workflow
1.  **Code:** Make changes across one or multiple modules.
2.  **Save Locally:** `./save "implemented job filtering in jobs2md"`
3.  **Go Live:** `./push` (when you're ready to share your changes).
