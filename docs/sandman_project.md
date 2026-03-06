# Sandman
# Initial brain dump:

## Larger Project Scope:
- Larger Project: Rascal:
  - homelab server: contains many services in parallel:
    - torrenting
    - audio book service
    - piHole
    - Project Sandman
    - and so on...
  limitations: raspberry pi 3. can't handke most of what's needed for project sandman in compute power. Eventually upgrading hardware; for now, compute-heavy processes will be on the macbook during non peak-use hours since the macbook is the daily driver machine and can't afford to be slowed in work hours. Overnight processing on macbook, low-compute automations can be done on Rascal.

## This Project: Project Sandman
Named due to our required adjustment due to hardware constraints. Since Rascal (pi server) can't handle all the jobs, we will let it handle the simple tasks, with the real compute done by the macbook. We can either have Rascal handle the simple stuff like scraping, then queue the biggger jobs for the macbook, or simply have the macbook do everything, but only enable the sandman's sandboxed environment in non-peak hours.

## Unanswered questions:
How to properly sandbox this all so if can be torn down or assembled easily. We want user to just have to worry abou their config files and everything else including installs are automated. Each service has it's own docker container and it's own intuitive configs.

## What is Sandman?
A sandbox that runs on your schedule. Three modules (automation layer, ai layer, digest layer) enabled by default, Many more available as we develop them as their ow ngithub repos.
Out of the box, Sandman is a python automation environment. User config file specifies sources of info,  how to query to only get useful info, how to scrape them into json/markdown, how often, and how to interpret them.
Sandman supports specifying output file paths for markdown files so that each scrape automation results in markdown files in a partular folder in Obsidian, though Obsidian use is totally optional.
Sandman supports an AI layer, which is able to be called by other automations. It is the interpretation layer for all streams of data.

## Scraper automations
Since this project is all about taking large amounts of scraped info and making it into a digest that is made according to user's interests, we will end up with several streams of scraped content, all operating on their own schedule.

### Current development progress:
- Reddit scraper: complete (sandman just needs to pull the github repo i made called "digestitor")
- Jobs scraper: partially built in sheets/appscript, needs to be build in python in a way that's compatible with this larger sandman ecosystem.
  - reads job alerts from linkedin and indeed email alerts, extracts each job, title, URL, description, AI prioritizes and it tracks them all in DB, with reference to their sour (email)
  - user is able to browse linkedin and indeed, and when they see a job of interest, trigger an apple shortcut/automation that scrapes that page, extracts the full job details, then sends HTML/POST to the DB. In this way we get full job details, which is better than the limited into in alert emails. Generates keyID from URL, so we can detect dupes, and if it's a dupe of something from email alert, this entry now provides more detail than the older entry, and can replace it.
- marketplace scraper: not started
  - specific searches on facebook markplace
  - specific searches on ebay
- youtube scraper
  - specific youtube channels, extracts transcripts.

### What happens with each stream of scheduled scrapes:
- markdown version of relevant into is created. front-matter shows date of scrape, date of original post, ID of the automation that scraped it included, "prompt" and "context" value defined in the automation that scraped it. user feedback value is null.

### What about the digest automations?
Digest automations aren't scraping external data. They are "scraping" or aggregating all of those streams of scraped data. They look to see the value in frontmatter of each post for "digests". If it doesn't exist, or it doesn't include the ID of this digest, the digest will include it in this digest.

#### What the digest does:
1. Sees the prompt value for this digest.
2. Sees the giant list of markdown files that don't contain this digest's ID in their "digests" front-mantter variable
3. Sees the "prompt" and "context" value for each of these items/automation.
4. Sees any non-null values for "user feedback" on these items. 
5. Each item will now be assigned new front-matter values by:
  - calling the ai module with something like: "I'm assigning priority values and creating summaries of posts for a digest of posts across a variety of topics. The specific prompt guiding me is {myPrompt}, I'll give you the info you need to assign a priority to the item in this feed, and I want you to briefly summarize it. Your summary should be framed around whatever factors influenced how you scored the priority. The post you're evaluating ans summarizing right now comes from a stream that provides you guidance with this prompt: {postPrompt} and you'll need the info from this context {postContext}. Please review the post, and enter a summary and priority in the front-matter. Take particular interest in anything you may find in the user-feedback value"
6. creates a new markdown file that lists all the items that were just processed by AI, organized in a intuitive way, including their summaries and listed in order of priority. each item links back to the markdown file it is referencing.
7. Based on each section's summaries, priorities and the prompts used in their scraper automations, editorialize about these recent updates, summarize what is of note, and don't spend time on what isn't. Utmost important: fully understand the user-feedback of each item. Based on what we know about how each scraper is querying and prompting, how well are we doing? are there suggestions you could be making to improve or increase our sources of information?






# version 2: scope of project



### Personal Automation Platform

---

## What This Is

Sandman is a config-driven automation platform that runs on a schedule, collects information from the web via modular scraper integrations, enriches each item with AI-assigned metadata, and delivers organized summaries to the user. It is designed to move between machines by copying a config directory and re-running the install script.

Sandman does not contain scrapers. It orchestrates them. Scrapers are standalone repos (Digestitor for Reddit, job scraper, marketplace scraper, etc.) that Sandman clones and invokes. Sandman provides the scheduling, the AI enrichment layer, the inbox, and the digest system.

---

## The Core Mental Model: Feeds

Every automation in the config produces a feed. A feed is a folder of markdown files, one per collected item, each with structured frontmatter. Think of it as a private RSS feed — items arrive on a schedule, accumulate until read, and carry enough metadata for automated and human processing.

Every feed item goes through an AI enrichment step before it enters the feed. This step assigns frontmatter values (priority, summary, feedback placeholder) and is mandatory. It can be configured to a simple inline prompt or a detailed external criteria file depending on how much judgment the evaluation requires.

Digest automations are feeds too. They scrape other feeds instead of the web, read frontmatter, and produce their own markdown files: summaries of what arrived across all streams since the last time that digest ran. Multiple digests can exist simultaneously — daily, weekly, monthly — each with its own scope and schedule. A post being included in one digest does not exclude it from another.

---

## What Sandman Contains

**Automation engine.** Reads config, schedules jobs, invokes scraper modules, manages data directories, and runs the AI enrichment step on each item.

**AI layer.** A single module that accepts: a payload (markdown and/or JSON), a prompt (inline string or path to a file), context (inline string or paths to reference files), and a model selector. Returns structured output. All AI calls across all automations route through this one module. Supports external APIs (Claude, Gemini, OpenAI) and local models (Ollama). Swapping providers requires changing one config value.

**Inbox.** A SQLite database and a folder of markdown files. Every item from every feed is stored here. The inbox is the shared data layer — no automation talks to another directly.

**Digest system.** A first-class automation type that reads from the inbox instead of the web, produces summary markdown files, and tracks which items each digest has already included (per-digest, not globally — the same item can appear in both a daily and a monthly digest if both are configured to include it).

**Install and teardown scripts.** The install script reads config, generates a docker-compose file containing only enabled services, clones required scraper repos, and starts containers. The teardown script stops containers and removes images. Config and data are never touched by either script.

---

## What Sandman Does Not Contain

Scraper logic lives in separate repos. Sandman clones and invokes them. Currently:

- **Digestitor** — Reddit scraper
- **Job scraper** — early stage; currently AppScript-based email parser with manual enrichment via Apple Shortcut. Full direct scraper not yet built.
  - sub-modules: indeed, linkedIn, job alert emails scraper (partially built), manual entry via client-side submission scraper (partially build in appscript, eneds work)
- **Marketplace scraper** — not yet built. submodules: facebook marketplace, ebay, etc.
- email scraper

When a config file references a scraper source that is not installed, the install script clones the appropriate repo automatically. Adding a new scraper to the ecosystem requires only: a standalone repo with a clean CLI interface, and a Sandman config block that references it.

---

## Automation Types

### Scrape Automation

Collects items from an external source on a schedule. Each scrape automation is its own feed — its own folder, its own tag in Obsidian, its own inbox stream.

Config specifies the source (which scraper repo and which query), a schedule (cron expression), and AI enrichment settings: prompt (inline or file path), context (inline or file paths), model selector, and min_priority_to_keep (items scoring below this threshold are discarded before reaching the inbox).

Each collected item produces a markdown file and a SQLite record with frontmatter: id, source, timestamp, priority, summary, feedback (empty), included_in_digests (empty list). The full content body is always preserved unchanged. The AI enrichment step only writes frontmatter — it never alters the body. The full original item is always available and always linked from digests.

### Digest Automation

Reads inbox frontmatter across all feeds (or a configured subset) and produces a summary markdown file. Each digest tracks which items it has already included using the included_in_digests frontmatter field. An item is excluded from a given digest only if that digest's name already appears in its included_in_digests list. Being included in a daily digest does not affect eligibility for a weekly or monthly digest.

The AI call for a digest receives a manifest of all qualifying items (frontmatter only: id, source, priority, summary, feedback if present) plus prompt and context files. It is instructed to: organize by priority, summarize each item proportionally to its score, surface patterns in user feedback, suggest new or modified queries where feedback supports it, and flag underperforming feeds.

The digest links to each full item file. The user reads the digest, follows links to items of interest, and leaves plain-language feedback directly in the item's frontmatter.

---

## The AI Layer

Every AI call routes through the same module regardless of which automation triggers it:

```
Input:
  payload    the markdown or JSON content to evaluate
  prompt     what the AI is asked to do (inline string or file path)
  context    background, criteria, reference logic (inline string or file paths)
  model      which LLM to use

Output:
  structured frontmatter values (priority, summary, and any automation-specific fields)
```

The prompt defines the task and required output format. Example for a job scrape: "These are job postings from the Indeed query {query_string}. Using the criteria and user background in the context files, score each posting 0-100. Write a one-sentence summary focused on what influenced the score most. Output only frontmatter fields: priority (int), summary (str)."

Context files are plain markdown, edited by the user, updated without touching the codebase. For job scoring, context includes professional background, skill inventory, scoring criteria, anti-patterns to screen against, and historical feedback metrics once available.

---

## Feedback

Every inbox item has a frontmatter field `feedback:` that starts empty. The user fills it in with plain language in their markdown editor. No required format — "good fit", "skip — too senior", "exactly what I want more of", "wrong location but otherwise perfect" are all valid.

A feedback processing automation reads filled fields on a schedule, writes values to SQLite, and makes them available as context for future AI calls on that feed. The weekly digest prompt is specifically instructed to review feedback patterns and suggest: feed refinements, new queries to add, and queries to retire.

Plain-language feedback is intentional. The AI reasons more usefully about "skip — too senior" than about a binary upvote.

---

## Digest Examples

**Daily digest.** All feeds, past 24 hours, items not yet in this digest. Comprehensive listing ordered by priority. High-priority items get full summaries. Low-priority items get one line. Tone: direct, no filler.

**Weekly digest.** All feeds, past 7 days, items not yet in this digest. Reviews feedback received during the week. Surfaces highest-priority items that may have been buried in daily digests. Makes specific suggestions: new queries, feeds to pause, criteria to adjust.

**Monthly digest.** All feeds plus Obsidian daily notes folder, past 30 days. Synthesizes scraped content with the user's recorded activity. AI reads what the user has been working on and connects it to high-priority feed items. Produces a high-level reflection, not an item list.

---

## Portability and Sandboxing

```
sandman/                     the repo (code only, never config or data)
  install.sh
  teardown.sh
  docker-compose.template.yml
  modules/
    ai_brain/
    inbox/
    digest/

~/.sandman/                  config (outside repo, preserved across machine moves)
  config.yml
  prompts/
  criteria/
  auth/

/workspace/                  runtime data (Docker volume, separate from repo)
  feeds/
  digests/
  inbox.db
  logs/
```

Moving to a new machine: copy `~/.sandman/` to the new machine, clone the repo, run `install.sh --config ~/.sandman/config.yml`. The install script clones required scraper repos automatically. Optionally copy `/workspace` to preserve inbox history — if not copied, the instance starts fresh and rebuilds from the next scheduled scrape.

Teardown: `./teardown.sh` stops containers and removes images. Config and data untouched. Re-running `install.sh` restores everything.

---

## Example Config

```yaml
sandman:
  data_dir: /workspace
  obsidian_vault: /mnt/data/vault

llm:
  default_backend: claude
  default_model: claude-sonnet-4-20250514
  keys_file: /config/auth/llm_keys.env
  local_backend: ollama
  local_model: llama3

automations:

  - name: marvelstudios_daily
    type: scrape
    source: digestitor
    config:
      subreddit: MarvelStudiosSpoilers
      sort: new
      post_limit: 8
      min_score: 50
    schedule: "0 6 * * *"
    ai:
      prompt: "Score each post 0-100 for how much a Marvel fan would want to read it. Output frontmatter only: priority (int), summary (str, one sentence)."
      context: null
      model: claude-sonnet-4-20250514
      min_priority_to_keep: 20

  - name: jobs_linkedin_ux
    type: scrape
    source: job_scraper
    config:
      platform: linkedin
      query: "UX designer OR product designer"
      filters:
        location: remote
        min_age_hours: 48
        max_applicants: 50
    schedule: "0 5 * * *"
    ai:
      prompt: /config/prompts/jobs_eval.md
      context:
        - /config/criteria/jobs.md
        - /config/criteria/profile.md
      model: claude-sonnet-4-20250514
      min_priority_to_keep: 35

  - name: optiplex_watch
    type: scrape
    source: marketplace_scraper
    config:
      platform: facebook_marketplace
      query: "'optiplex mini' AND ('i7' OR 'i5')"
      filters:
        max_price: 80
        min_age_hours: 96
    schedule: "0 8 * * *"
    ai:
      prompt: /config/prompts/marketplace_eval.md
      context: /config/criteria/x86_target_spec.md
      model: claude-sonnet-4-20250514
      min_priority_to_keep: 50

  - name: daily_digest
    type: digest
    feeds: all
    lookback_hours: 24
    schedule: "0 7 * * *"
    output: /workspace/digests/daily/
    ai:
      prompt: /config/prompts/digest_daily.md
      context: null
      model: claude-sonnet-4-20250514

  - name: weekly_digest
    type: digest
    feeds: all
    lookback_days: 7
    schedule: "0 7 * * 1"
    output: /workspace/digests/weekly/
    ai:
      prompt: /config/prompts/digest_weekly.md
      context:
        - /config/criteria/jobs.md
        - /config/criteria/profile.md
      model: claude-sonnet-4-20250514

  - name: monthly_digest
    type: digest
    feeds: all
    lookback_days: 30
    include_obsidian_notes: true
    obsidian_notes_path: /mnt/data/vault/daily_notes/
    schedule: "0 7 1 * *"
    output: /workspace/digests/monthly/
    ai:
      prompt: /config/prompts/digest_monthly.md
      context:
        - /config/criteria/profile.md
      model: claude-sonnet-4-20250514
```

---

## Open Questions

- Delivery mechanism beyond writing to a folder: email via msmtp, push notification via ntfy.sh or Pushover, lightweight RSS server. Config should support multiple output targets per digest.
- How does feedback processing handle conflicting signals over time from the same query?
- Should the inbox have a TTL, or does the user manage size manually?
- The job scraper's email-based approach misses full job detail. Moving to a direct scraper is a job_scraper repo concern, not a Sandman concern, but it is a known quality ceiling for job feed items until resolved.
- Minimum viable local LLM model size for reliable structured frontmatter output. This determines whether Pi or MacBook is the right host for local inference.
