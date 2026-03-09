# Sandman Docker Orchestrator

This directory contains the infrastructure for running the Sandman suite in a sandboxed, scheduled environment.

## 1. Deployment Strategy
The Sandman orchestrator is designed to run as a **Nightly Worker**. It lives inside a Docker container on your MacBook, ensuring that all resource-heavy tasks (Chromium instances for JobSpy, n8n workflows, and large-scale scraping) occur while you sleep.

## 2. Container Components
- **n8n:** The primary workflow engine, running as a service inside the container.
- **Python Runtime:** Pre-configured with all module dependencies.
- **Playwright/Chromium:** Bundled for `JobSpy` and `web2md` (Crawl4AI) support.

## 3. Sandboxing & Virtual Environments
To maintain strict modularity, each module within the `/modules` directory is managed via its own `requirements.txt`.
- The Docker build process creates a global environment for shared tools (n8n, playwright).
- Individual module logic is isolated to prevent version conflicts between scrapers.

## 4. Scheduling (macOS)
To automate the "Nightly" aspect without involving a 24/7 server:
1. **Docker Desktop:** Must be running.
2. **Apple Shortcut/Cron:** 
    - `0 0 * * * docker start sandman-orchestrator`
    - `0 7 * * * docker stop sandman-orchestrator`

## 5. Volume Mapping
- `./modules:/app/modules`: Direct access to the code.
- `./sandman_config:/app/config`: Access to credentials and YAML settings.
- `/Users/[User]/Documents/Vault:/app/output`: Mapping directly to your live Obsidian vault.
