# The Sandman Ecosystem — Architecture Overview v0.1 (ideation/planning stage)

_A suite of modular automation tools, orchestrated by a central controller_

## How to Read This Document

This is a north star document, not a technical spec. It describes intended 
functionality and how the components relate to each other. Implementation 
details — specific APIs, exact interfaces, trigger mechanisms — are 
intentionally left open until the relevant component is being built. Where 
examples appear, they illustrate intent, not commitment.

---

## The Metaphor

**Sandman** is the controller. It decides what happens, when, and in what order.

**Grains** are the individual tools. Each does one thing well and is useful on its own. Sandman picks them up and uses them as part of larger workflows.

**Dreams** are the automated workflows. A dream is a sequence of grains working together toward a specific outcome — scrape jobs, evaluate with AI, notify user, log results.

---

## Core Architectural Principles

Before describing any individual component, these principles apply to everything:

**1. Grains are standalone.** Every tool works without Sandman. It can be imported, configured, and run independently. Sandman is not a requirement — it's a convenience. This means someone else could build their own controller and use any grain in this suite.

**2. Don't reinvent shared infrastructure.** The biggest risk in this suite is duplicating the same logic in mutiple tools. JSON storage, markdown conversion, SQLite tracking, deduplication; these are shared concerns. They belong in a shared library that every grain imports, not reimplemented in each repo. Every tool should be the source of truth on it's own independent state and activities.

**3. Weigh existing tools before reinventing.** Before building anything, ask whether a mature library already solves it. The goal is for each grain to handle access and extraction — the domain-specific part — while shared infrastructure handles conversion, storage, and tracking. Where custom logic  is genuinely required (Digestitor's comment scoring and exact markdown formatting is one example), it  belongs in the grain or in a shared utility, not reimplemented per project. The decision of build vs. borrow should be made explicitly at the start of  each grain, not assumed either way.

**4. One central config, per-tool sections.** Sandman has one `config.yaml`. It contains a section for each grain, defining their configs, defaults, and interactions with others. Sandman (controller) either passes config values directly when calling a grain, or generates a per-tool config file from its own central one. Either way, the user edits one file.

**5. State is observable.** Every grain maintains its own SQLite database. Sandman maintains its own database that tracks the state of all grains. Automation triggers can be based on the state of any grain's database — "when digestitor has new posts matching X, trigger the brain."

---

## The Components

### Sandman (Controller)

**Repo:** `sandman` **Role:** Orchestrator. Runs forever. Reads config. Triggers grains on schedule or based on state.

Key responsibilities:

- APScheduler manages all job timing
- Central `config.yaml` defines all grains, schedules, and dream workflows
- Monitors each grain's SQLite database for state changes that should trigger downstream jobs
- Maintains its own database tracking workflow runs, outcomes, and cross-grain state
- Generates or passes per-tool config when invoking grains
- Is aware of which LLMs are available and routes brain calls accordingly

What Sandman does NOT do:

- Access external services directly (that's a grain's job)
- Convert content to markdown (that's core's job)
- Make LLM calls directly (that's the brain's job)

---

### The Brain (LLM Integration Layer)

**Repo:** `brain` (not yet built) **Role:** The AI reasoning layer. Called by Sandman when a workflow requires judgment, summarization, ranking, or generation.

Key design decisions:

- Brain is LLM-agnostic. It has a list of available backends: Gemini CLI, Claude API, local Ollama model, LM Studio endpoint. Sandman config specifies which to use per workflow.
- Inputs are always markdown files or SQLite query results — clean, structured, LLM-ready
- Outputs are always structured: a decision, a ranking, a summary, a set of flags to write back to a grain's database
- Brain never stores source content — it reads from grains, writes decisions back to grains

Example brain call from a dream workflow:

```
Input:  last 24hrs of job_grain results as markdown
Prompt: "user preferences: X. rank these by fit. return top 5 with reasoning."
Output: ranked list written back to job_grain db as workflow_flags
        summary markdown written to sandman output directory
```

Brain is where the real intelligence lives. Everything else is plumbing to feed it good inputs and act on its outputs.

---

### Digestitor (Reddit Grain)

**Repo:** `digestitor` **Role:** Pulls posts from Reddit subreddits, stores as JSON + markdown + SQLite.

Current state: fully functional but does too much itself. Refactor target: thin access layer on top of shared core.

Sandman config section:

```yaml
digestitor:
  schedule: "every 24 hours"
  sources:
    - subreddit: MachineLearning
      sort: hot
      limit: 10
      min_score: 100
    - subreddit: homelab
      sort: new
      limit: 5
```

Standalone use: `python digestitor.py --source MachineLearning --limit 10` As a grain: `from digestitor import RedditScraper; scraper.run(config)`

---

### Gmail Grain (Email Digestor)

**Repo:** `gmail_grain` (partially built as AppScript, being migrated) **Role:** Monitors Gmail inboxes for emails matching defined patterns, stores as JSON + markdown + SQLite.

Access method: Gmail API, authenticated as primary account, delegates to secondary. Pattern matching: Gmail labels, sender patterns, subject patterns. Output: one markdown file per email, standard frontmatter, body cleaned via core.

Sandman config section:

```yaml
gmail_grain:
  schedule: "every 15 minutes"
  accounts:
    - address: davidsutton585@gmail.com
      include_delegated: true
  patterns:
    - label: sandman/jobs
      workflow_flag: job_email
    - sender: "@linkedin.com"
      workflow_flag: linkedin_alert
```

Standalone use: `python gmail_grain.py --pattern job_email` As a grain: `from gmail_grain import GmailFetcher; fetcher.run(config)`

---

### Job Email Grain (Specialized Email Parser)

**Repo:** Integrated into gmail_grain or separate `job_grain` 
**Role:** The AppScript project being replaced. Takes job alert emails, extracts individual job links, stores each job as its own record, tracks source email, source service (LinkedIn, Indeed, etc.), match quality over time.

This is distinct from gmail_grain because it does domain-specific parsing — a job alert email contains multiple job links, each of which becomes its own database record. Gmail_grain stores emails. Job_grain stores jobs extracted from emails.

Database tracks:

- Job posting (title, company, link, salary if present)
- Source email it came from
- Source service (LinkedIn, Indeed, etc.)
- Search terms that produced it
- Brain's match score and reasoning (written back after brain evaluates)
- Over time: which sources and search terms produce the best matches

This is where the AppScript/Sheets work lives, migrated to Python + SQLite.

---

### Web Scraper Grain

**Repo:** `scraper_grain` (not yet built) **Role:** Scrapes non-Reddit, non-email web sources. Job boards, news sites, forums, any structured web content.

Uses `trafilatura` for content extraction (handles paywalls, ads, boilerplate removal better than raw BeautifulSoup). Falls back to BeautifulSoup for sites trafilatura can't handle.

Output: same JSON + markdown + SQLite pattern as all other grains.

Sandman config section:

```yaml
scraper_grain:
  schedule: "every 12 hours"
  sources:
    - name: "indeed_python_jobs"
      url: "https://www.indeed.com/jobs?q=python+developer"
      extractor: structured_list   # vs article, forum, etc.
      workflow_flag: job_posting
```

---

### Marketplace Grain

**Repo:** `marketplace_grain` (not yet built, may use existing tool) **Role:** Monitors Facebook Marketplace, eBay, Craigslist for items matching defined criteria.

**Check before building:** This space has existing tools. `pyppeteer`, `playwright`, or `selenium` for JS-heavy sites like Facebook. Search for existing Facebook Marketplace scrapers before writing one — this is a well-trodden problem.

Sandman config section:

```yaml
marketplace_grain:
  schedule: "every 6 hours"
  searches:
    - platform: facebook_marketplace
      query: "dell optiplex micro"
      max_price: 100
      radius_miles: 50
      workflow_flag: x86_candidate
    - platform: ebay
      query: "raspberry pi 4 8gb"
      max_price: 60
      workflow_flag: pi_candidate
```

---

## How a Dream Workflow Works

Example: **Job Alert Dream**

```
Trigger: gmail_grain finds new email with workflow_flag = "job_email"

Step 1 — gmail_grain:
  New job alert email stored as markdown + JSON

Step 2 — job_grain:
  Extracts individual job links from email
  Stores each as a job record in job_grain db
  Sets each record workflow_flag = "needs_evaluation"

Step 3 — brain:
  Reads all job records where workflow_flag = "needs_evaluation"
  Compares against user preferences from config
  Scores each job, writes score + reasoning back to job_grain db
  Sets workflow_flag = "evaluated"

Step 4 — sandman notifier:
  Reads job_grain db for records where score > threshold
  Composes summary markdown of top matches
  Sends notification (email, pushover, file output — TBD)
  Sets workflow_flag = "notified"
```

Each step is a grain. Sandman coordinates the handoffs. The brain provides judgment. Config defines the thresholds and criteria. No step has to know about any other step — they just read and write to their databases and Sandman watches the state.

---

## Config Philosophy

One `config.yaml` in the Sandman repo. Structure:

```yaml
sandman:
  log_level: INFO
  output_dir: /data/output

brain:
  preferred_model: claude_api
  fallback_model: local_ollama
  models:
    claude_api:
      type: api
      key_env: CLAUDE_API_KEY
    local_ollama:
      type: ollama
      endpoint: http://localhost:11434

grains:
  digestitor:
    enabled: true
    schedule: "0 6 * * *"    # 6am daily
    config: ...
  gmail_grain:
    enabled: true
    schedule: "*/15 * * * *"  # every 15 min
    config: ...

dreams:
  job_alert_dream:
    enabled: true
    # trigger format TBD (like most of this document) options include polling grain databases on interval, a shared event/signal table, filesystem watchers, or callback hooks.
	# Intent: sandman becomes aware when a grain produces output matchingdefined criteria, and uses that as a workflow trigger.
	trigger:
	  grain: gmail_grain
	  condition: new output matching workflow_flag "job_email"
    trigger: gmail_grain.new_record.workflow_flag == "job_email"
    steps:
      - grain: job_grain
      - grain: brain
        prompt_template: prompts/job_evaluation.md
      - action: notify
        threshold: score > 0.7
```

---

## What to Look for Before Building

Before writing a new grain, check whether a mature tool already exists:

| Need                   | Check first                                                                                                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Web content extraction | `trafilatura`, `newspaper3k`                                                                                                    |
| HTML to markdown       | `markdownify`, `html2text`                                                                                                      |
| Structured scraping    | `beautifulsoup4`, `playwright`                                                                                                  |
| RSS/Atom feeds         | `feedparser`                                                                                                                    |
| Facebook Marketplace   | Search GitHub for existing scrapers                                                                                             |
| eBay                   | eBay has an official API                                                                                                        |
| Job boards             | LinkedIn has an API (limited); Indeed does not, priority on less-competitive and congested job boards anyway, evaluate options. |
| Email to markdown      | `mail-parser`, `extract-msg`                                                                                                    |
| Notification delivery  | `apprise` (supports 70+ services in one library)                                                                                |

The rule: a grain should be thin access + configuration logic on top of existing, well-maintained tools. If you're writing HTML parsing logic from scratch, you're probably reinventing something.

---

## Build Order and Open Decisions

The sequence below reflects dependencies, not a fixed timeline. Each item 
carries open questions that should be resolved before building begins on 
that component — not before.

**First: `sandman_core`**
The shared library all grains depend on. Until its interface is defined, 
grains can't be designed to be consistent with each other. Key open 
questions: Does it live inside the sandman repo or as a standalone package? 
How do grains import it — as a local path dependency, a git dependency in 
requirements.txt, or something else? What is the exact contract for handing 
content off to core for storage and conversion?

**Second: Gmail Grain and Job Grain**
First real grains after core exists. Email is simpler than Reddit — good 
test of whether core handles the common case cleanly. Job grain tests 
whether one grain can consume another's output. Key open question: is 
job_grain a separate repo or a module inside gmail_grain?

**Third: Brain Interface**
Needs to be defined in terms of what goes in and what comes out before any 
grain is designed to hand off to it. Specific LLM backends, prompt formats, 
and output parsing are implementation details — the interface contract is 
what matters first.

**Fourth: Sandman Controller and Dream Workflows**
The controller can be stubbed early (just scheduling, no triggers), but 
full dream workflows depend on core, at least two grains, and a defined 
brain interface all existing first.

**Fifth: Digestitor Refactor**
Lower priority than building new capability. Refactor when the core library 
is stable and the pattern is proven across at least one other grain.

**Later: scraper_grain, marketplace_grain**
After the pattern is proven. Architecture should transfer directly.

---

## Key Open Questions

These are unresolved decisions that will shape implementation. They are 
documented here so they are resolved intentionally rather than by default 
when coding begins.

**How do grains communicate output to Sandman?**
Options include: grains write to their own SQLite and Sandman polls; a 
shared event table that all grains append to; filesystem watchers on output 
directories; explicit callback hooks passed in at call time. The right 
answer may differ by use case — polling is simple, event tables are more 
scalable.

**How does sandman_core get distributed?**
Options include: a folder inside the sandman repo (simplest, tight 
coupling), a separate private repo imported as a git dependency in each 
grain's requirements.txt (clean separation, more overhead), or eventually 
a private PyPI package. Start simple, extract when the cost of coupling 
becomes real.

**What is the brain's interface contract?**
Before any grain is designed to hand off to the brain, the contract needs 
defining: what format does input take (markdown files? SQLite rows? both?), 
what does output look like (structured JSON? flags written directly to db?), 
how are errors and timeouts handled, how does the caller know which LLM 
backend was used. These questions don't need answers yet — they need to be 
asked at the right time.

**How are prompt templates managed?**
The brain needs prompts that are workflow-specific. Options: prompts live 
in the sandman repo as markdown files, prompts live in each grain alongside 
the logic they relate to, or prompts are inline in config. Likely a 
combination — grain-specific prompts near the grain, workflow-level prompts 
in sandman.

**Notification delivery mechanism**
When a dream workflow produces output worth surfacing to the user, how does 
it get delivered? Options: write a markdown file to a known location (simple, 
no push), email via msmtp (already planned for Rascal), push notification 
via Apprise (supports 70+ services), or a simple web endpoint. The right 
answer depends on urgency — a job alert and a marketplace find have 
different latency requirements than a nightly digest.

---

## Long-Term: MCP / Multi-Agent

Once this suite is stable, the natural evolution is wrapping each grain as an MCP tool. An MCP server running on Rascal (or the future x86 machine) exposes each grain as a callable tool to Claude Code, Gemini CLI, or any MCP-compatible agent. At that point Sandman's scheduling and state management becomes the backend, and the AI agent becomes the front-end that decides which tools to call and when.

The architecture described here maps cleanly onto that future. Grains become MCP tools. Dreams become agent workflows. The brain becomes the agent itself. Nothing needs to be redesigned — just wrapped.
