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
- `reddit2markdown` (Digestitor): Scrapes subreddits and tracks thread maturity.
- `gmail2markdown`: Monitors Gmail labels (e.g., Job Alerts, Newsletters) and extracts embedded URLs.

### Tier 2: Entity Extractors
These are "domain experts" that take a specific URL and turn it into a high-fidelity record.
- `job2markdown`: Uses **JobSpy** to turn LinkedIn/Indeed URLs into structured Job Notes (Salary, Skills, Company).

### Tier 3: Utility Scrapers
The "Universal Fallback" for generic web content.
- `web2markdown`: Uses **Trafilatura** to de-clutter any generic article or blog post into clean Markdown.

## 3. Orchestration & Deployment: The "Nightly Worker"

Sandman is designed for **Zero-Impact Productivity**. To ensure your daytime CPU cycles are reserved for your work, the suite is built to run within a scheduled **Docker Container** on your primary machine (e.g., MacBook).

### The Nightly Cycle
- **Status:** Dormant during the day to save resources.
- **Trigger:** An automated schedule (Cron or Apple Shortcut) spins up the `sandman-orchestrator` container at night.
- **Action:** The container executes the full pipeline:
    1. **n8n** (Self-hosted inside Docker) manages the high-level workflow logic.
    2. **Tier 1 Scrapers** pull fresh data from Gmail and Reddit.
    3. **Tier 2 Extractors** (JobSpy) process any identified job links.
    4. **Tier 3 Utilities** (Trafilatura) clean up generic web content.
- **Finality:** The container shuts down once the "To-Do" queue is empty, leaving your vault updated and your system resources free for the morning.

### Sandboxed Architecture
- **Isolation:** Each module is strictly sandboxed within its own virtual environment (`venv`) or sub-container logic to prevent dependency hell.
- **Volume Mapping:** Only the `output_directory` (Obsidian Vault) and `sandman_config` are mapped to the host, keeping the system footprint minimal and secure.

## 4. Developer Onboarding & Project Context

To quickly understand the Sandman ecosystem and get up to speed on the current state of development, follow this recommended reading path. This is especially useful at the start of a new development session to establish a complete context of the project's goals and structural standards.

1.  **Project Overview:** Start with this `README.md` to understand the high-level vision and the "Nightly Worker" deployment model.
2.  **Global Standards:** Read the [Unified Module Blueprint](modules/unified_module_blueprint.md). This document defines the mandatory architectural rules (The "5 Buckets"), schema baselines, and cross-module communication protocols shared by all scrapers.
3.  **Module Registry:** Review the `modules/` directory. Each subdirectory (e.g., `job2markdown`, `gmail2markdown`) is an independent GitHub repository with its own isolated virtual environment.
4.  **Specific Module Context:** Once you've identified a module to work on, read its local `README.md` and its `architecture.md` file. These documents detail the platform-specific strategies, unique metadata fields, and implementation progress for that specific scraper.

## 5. Getting Started

1.  Clone the repository.
2.  Review `sandman_config/config.yml` to set your global paths (`output_directory`, `data_directory`).
3.  Configure your credentials in `sandman_config/auth/`.
4.  Run a module: `python modules/digestitor/digestitor.py`.

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
2.  **Save Locally:** `./save "implemented job filtering in job2markdown"`
3.  **Go Live:** `./push` (when you're ready to share your changes).
