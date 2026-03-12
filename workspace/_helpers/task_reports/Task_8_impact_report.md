---
task: Task_8
status: Pending Review
target_terms: [job queue, jobs, job-specific]
new_term: routine
context: "We are deprecating the 'jobs' key in YAML and replacing it with 'routine' which accepts named keys"
date_generated: 2026-03-10 15:14:20
---

# Documentation Scrubbing Report for Task_8

> **Instructions**: Review the `AI Analysis` and `Proposed Rewrite` for each block below. If accurate, apply the rewrite to the source file.

---

## File: `README.md` (Block #4)
**Original:**
```markdown
Sandman is not just a collection of scrapers; it is an **Accumulator**.
- **Living Notes:** Instead of overwriting files, Sandman updates metadata and appends new content, creating a chronological record of an evolving discussion or thread.
- **Source of Truth:** The filesystem (Markdown) is the ultimate authority. Our SQLite databases are treated as self-healing caches that reconcile their state against your actual notes on every startup.
- **Zero Noise:** We leverage world-class open-source libraries like **Trafilatura**, **Crawl4AI**, and **JobSpy** to extract only the information that matters, stripping away the noise of the modern web.
```

**AI Analysis:** Skipped (No client)

---

## File: `README.md` (Block #8)
**Original:**
```markdown
### Tier 2: Entity Extractors
These are "domain experts" that take a specific URL and turn it into a high-fidelity record.
- `jobs2md`: Uses **JobSpy** to turn LinkedIn/Indeed URLs into structured Job Notes (Salary, Skills, Company).
```

**AI Analysis:** Skipped (No client)

---

## File: `README.md` (Block #12)
**Original:**
```markdown
### The Standard Cycle
- **Status:** Dormant during the day to save resources.
- **Trigger:** An automated schedule (Cron or Apple Shortcut) spins up the `sandman-orchestrator` container on a recurring schedule.
- **Action:** The container executes the full pipeline:
    1. **n8n** (Self-hosted inside Docker) manages the high-level workflow logic.
    2. **Tier 1 Scrapers** pull fresh data from Gmail and Reddit.
    3. **Tier 2 Extractors** (JobSpy) process any identified job links.
    4. **Tier 3 Utilities** (Trafilatura) clean up generic web content.
- **Finality:** The container shuts down once the "To-Do" queue is empty, leaving your vault updated and your system resources free for later review.
```

**AI Analysis:** Skipped (No client)

---

## File: `README.md` (Block #16)
**Original:**
```markdown
1.  **Project Overview:** Start with this `README.md` to understand the high-level vision and the "Orchestrator" deployment model.
2.  **Global Standards:** Read the [Unified Module Blueprint](modules/unified_module_blueprint.md). This document defines the mandatory architectural rules (The "5 Buckets"), schema baselines, and cross-module communication protocols shared by all scrapers.
3.  **Module Registry:** Review the `modules/` directory. Each subdirectory (e.g., `jobs2md`, `gmail2md`) is an independent GitHub repository with its own isolated virtual environment.
4.  **Specific Module Context:** Once you've identified a module to work on, read its local `README.md` and its `architecture.md` file. These documents detail the platform-specific strategies, unique metadata fields, and implementation progress for that specific scraper.
```

**AI Analysis:** Skipped (No client)

---

## File: `README.md` (Block #24)
**Original:**
```markdown
### Typical Workflow
1.  **Code:** Make changes across one or multiple modules.
2.  **Save Locally:** `./save "implemented job filtering in jobs2md"`
3.  **Go Live:** `./push` (when you're ready to share your changes).
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #10)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] `core/config.py` in `jobs2md`, `reddit2md`, and Sandman orchestrator parse `verbose` as an integer (0, 1, 2) from YAML.
- [ ] All CLI argument parsers (`argparse`) use `--verbose` and store the result in `args.verbose`.
- [ ] Any existing references to `verbosity` in configuration parsers or Python logic are removed or aliased to throw a deprecation warning while falling back to `verbose`.
- [ ] `jobs2md`: Passes `verbose` directly into JobSpy's configuration.
- [ ] `reddit2md`: Implements `logging.getLogger().setLevel()` based on the `verbose` integer (0: ERROR, 1: WARNING, 2: INFO/DEBUG).
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #13)
**Original:**
```markdown
**Objective**: Ensure full parity for `min_age_hours` and `max_age_hours` in both `jobs2md` and `reddit2md`.
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #14)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] **`jobs2md`**: Maps `max_age_hours` to JobSpy's native `hours_old` parameter.
- [ ] **`jobs2md`**: Implements post-scrape filtering on the resulting pandas DataFrame to drop any jobs that are younger than `min_age_hours`.
- [ ] **`reddit2md`**: Continues to use `min_age_hours` to queue posts for future rescrapes via `rescrape_after`.
- [ ] **`reddit2md`**: Implements a check against `created_utc` during iteration. If a post's age exceeds `max_age_hours`, it is immediately discarded/skipped.
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #18)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] The `offset` parameter (integer) is exposed in YAML configs and CLI parsers for all modules.
- [ ] **`jobs2md`**: Passes the `offset` value natively to JobSpy's `offset` parameter during the `scrape()` call.
- [ ] **`reddit2md`**: Implements standard Python list slicing (e.g., `rss_feed_items[offset:]`) to discard the first N items in the parsed RSS feed before initiating JSON fetch requests.
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #22)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] Remove any backend implementation attempts to force `sort` into `jobs2md`, as it is unsupported by JobSpy.
- [ ] Ensure `reddit2md` continues to support `sort` natively via PRAW/RSS paths.
- [ ] Update `nomenclature.md` to explicitly document that `sort` is a `reddit2md`-only parameter, and `jobs2md` relies on the target site's default relevance algorithms.
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #26)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] **`reddit2md`**: Continues to output the posting user under the key `author: `.
- [ ] **`jobs2md`**: Outputs the posting company under the key `employer: ` (mapped from JobSpy's `company` output).
- [ ] **`jobs2md`**: Verify if JobSpy returns a specific Company/Employer ID. If so, expose an `employer_id` parameter in the config/CLI allowing users to query jobs posted strictly by that specific ID. Ensure this behavior is documented. Attempt coherent naming with the rest of the project, as seen in nomenclature.md.
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #30)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] **`reddit2md`**: Continues mapping `link_flair_text` directly to `category: `.
- [ ] **`jobs2md`**: Does *not* generate a `category` key. 
- [ ] **`jobs2md`**: Generates a YAML list for `employment_type: ` (e.g., `[Full-time, Contract]`) mapped from JobSpy.
- [ ] **`jobs2md`**: Generates a YAML list for `workplace: ` (e.g., `[Remote, In-office, Hybrid]`) mapped from JobSpy's location/remote flags.
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #33)
**Original:**
```markdown
**Objective**: Unify the configuration and execution layers to universally support both `source` (string) and `sources` (list) across Sandman, `jobs2md`, and `reddit2md`. This avoids breaking legacy configs while elegantly scaling multi-target routines.
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #34)
**Original:**
```markdown
**Implementation Plan & Investigation:**
- **Configuration Parsing (`core/config.py` in all modules):** When the `settings` or `routine` YAML block is parsed, the Config manager should act as a normalizer. If a routine block contains `sources: ["A", "B"]`, the config manager should dynamically duplicate that routine into two discrete jobs in the runtime queue—one for `source: A` and one for `source: B`. The underlying execution loop then remains oblivious; it simply processes a list of single-source jobs. 
- **CLI & Python kwargs:** 
  - *CLI*: Add `add_mutually_exclusive_group()` or alias logic in `argparse` to allow both `--source` and `--sources`. If a user passes `--sources A,B`, `argparse` splits it into a list. The initialization logic then iterates over this list, functionally queueing multiple single-source runs.
  - *Python calls*: Standardize the class constructors (e.g., `Scraper(source="A")` and `Scraper(sources=["A", "B"])`). The init method will intercept either argument, normalize it into an iterable list of sources, and process them sequentially.
- **Development Effort**: Low/Medium. It requires centralizing the normalization logic within the shared architecture blueprint (`core/config.py` and `argparse` setup) and replicating that standard across Sandman, `jobs2md`, and `reddit2md`.
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #35)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] **Configuration Expansion**: Update YAML parsing in Sandman, `jobs2md`, and `reddit2md` so that a single routine containing a `sources` list is automatically unrolled into multiple single-source jobs within the execution queue.
- [ ] **CLI Support**: Update `argparse` in all three projects to accept both `--source` and `--sources` flags seamlessly, routing them to the same normalization logic.
- [ ] **Python API**: Ensure the main orchestrator classes in all three projects gracefully accept both `source` (str) and `sources` (list) keyword arguments without failing.
- [ ] **Consistent Execution**: Confirm that `jobs2md`, `reddit2md`, and Sandman utilize the exact same underlying logic pattern to handle the expansion of sources, keeping the architecture unified.
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #49)
**Original:**
```markdown
## Task 11: Two-Way Queue via `rescrape_after` in jobs2md
**Context Reference**: `nomenclature2.md` -> `## 11. Jobs2md Specifics (Descriptions, Country, etc.) & Rescrape Logic`
```

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #51)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] **`jobs2md`**: Standardize `detail` as a boolean flag (default `false`). Do not alter `reddit2md`'s enum-based `detail` implementation.
- [ ] **`jobs2md`**: During front-matter generation, always inject the `rescrape_after: ` key.
- [ ] **`jobs2md`**: If `detail` is `false` during the scrape, leave `rescrape_after:` empty.
- [ ] **Orchestrator Logic**: Implement a pre-run scan in `jobs2md` that checks existing Markdown files in the output directory. If a file has a populated `rescrape_after` timestamp that is in the past:
  - Extract the job's URL.
  - Execute a targeted JobSpy scrape for that specific URL with `detail: true` (mapping to `linkedin_fetch_description: True`).
  - Overwrite/update the markdown file with the full description and clear the `rescrape_after` field.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #5)
**Original:**
```markdown
**Analysis & Guidance:**
- Standardize on `verbose` as an integer (0: errors, 1: warnings, 2: all/debug). "Verbosity" is standard CLI nomenclature, but `verbose` is more common as a parameter name. "Detail" is ambiguous (could mean data detail vs log detail).
- **Code Change Strategy:**
  1. **Job2md**: Expose `verbose` in `core/config.py` and CLI arguments. Pass this integer directly to JobSpy's `verbose` parameter when instantiating or calling it in `jobs2md.py`.
  2. **Reddit2md**: Implement a logging configuration based on the `verbose` integer. 
     - 0 = `logging.ERROR`
     - 1 = `logging.WARNING`
     - 2 = `logging.INFO` / `logging.DEBUG`
  3. **Sandman**: Ensure the orchestrator passes `--verbose X` down to all modules.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #10)
**Original:**
```markdown
**Investigation & Guidance:**
- **JobSpy Reality Check**: JobSpy supports `hours_old` which fetches jobs posted *within* the last X hours. This is actually a **`max_age_hours`** analog, not a minimum age. 
- **Code Change Strategy:**
  1. **Job2md**: Map `max_age_hours` to JobSpy's `hours_old`. To support `min_age_hours`, we will need to filter the resulting pandas DataFrame post-scrape (e.g., dropping rows where the calculated age is less than `min_age_hours`).
  2. **Reddit2md**: PRAW's `.new()` or `.hot()` doesn't natively filter by age. We already filter by `min_age_hours`. To support `max_age_hours`, we will add a condition during iteration checking `created_utc`; if the post is older than `max_age_hours`, we can `break` or `continue`.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #12)
**Original:**
```markdown
### AI Analysis & Updated Plan:
- **Understanding**: You want absolute confirmation that parity will be achieved for both parameters in both modules.
- **Review**: Yes, full parity is entirely achievable and is the goal. 
- **New Plan**: 
  - **job2md**: Implement both. `max_age_hours` will natively map to JobSpy's `hours_old`. `min_age_hours` will be implemented by actively filtering the JobSpy DataFrame output after the initial scrape completes.
  - **reddit2md**: Implement both. We already have the logic for `min_age_hours` (for rescrape queuing). We will add explicit logic for `max_age_hours` to simply skip and discard posts that are too old.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #15)
**Original:**
```markdown
**Investigation & Guidance:**
- **JobSpy**: Supports a numeric `offset`. 
- **PRAW (Reddit)**: Uses cursor-based pagination (`after` and `before` IDs), not numeric offsets. To support a numeric `offset` in reddit2md, we would have to fetch `offset + max_results` and slice the array (discarding the first `N`). This is inefficient but standardizes the UX.
- **Code Change Strategy**: Add `offset` to all CLI parsers. In `jobs2md.py` `execute_task`, pass `offset` to `self.client.scrape`. In `reddit2md.py`, implement list slicing to skip the first `offset` items.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #16)
**Original:**
```markdown
### Human input:
- reddit2md: If you review how our reddit2md module works, first step is to create a rss feed, then in that feed we grab the URLs of each of the top n number of items. from that URL we can get a json address and pull the whole page as json. to support `offset`, wouldn't we just start disregard the first n amount of rss posts?
- job2md: implementing should be straight-forward if not already accomplished, jobspy supports this parameter natively.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #17)
**Original:**
```markdown
### AI Analysis & Updated Plan:
- **Understanding**: You clarified that `reddit2md` utilizes an RSS feed architecture rather than the PRAW API, meaning pagination is just a matter of skipping the first `n` items in the parsed RSS list.
- **Review**: This makes implementation significantly simpler and much more efficient than API cursor emulation. Slicing the RSS list is highly performant.
- **New Plan**: 
  - **job2md**: Pass `offset` directly down to JobSpy's native parameter.
  - **reddit2md**: Apply standard Python list slicing (e.g., `rss_entries[offset:]`) to the parsed RSS feed list before iterating to fetch the individual JSON URLs.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #20)
**Original:**
```markdown
**Investigation & Guidance:**
- Reddit inherently supports complex sorting (hot, new, top, controversial).
- Job boards generally only support "relevance" vs "date" sorting.
- **Action**: Investigate JobSpy's native parameters. If JobSpy has no explicit `sort` argument, it likely defaults to relevance/date depending on the provider. 
- **Code Change Strategy**: We can allow `sort: date` vs `sort: relevance` at the Sandman level. If JobSpy does not support this natively via arguments, we may need to sort the resulting pandas DataFrame ourselves by date if `sort: new` is passed to jobs2md.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #21)
**Original:**
```markdown
### Human input:
Forget about the sanman level. Think only about jobspy. is there any parameter than changes the way the results are listed? for example "show most recent first" or "show best results first" or "show recommended first"? or is there no use for a sort parameter in this module?
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #22)
**Original:**
```markdown
### AI Analysis & Updated Plan:
- **Understanding**: You want to know if JobSpy actually exposes a sorting parameter that dictates what the job boards return, or if trying to support `sort` in `jobs2md` is pointless.
- **Review**: JobSpy does *not* expose a dedicated `sort` parameter natively. It relies entirely on the default sorting of the underlying job boards being scraped (which is usually a black-box mix of relevance and date). Trying to shoehorn `sort` into `jobs2md` would create a false promise to the user.
- **New Plan**: Deprecate the concept of `sort` for `job2md`. It will be strictly a `reddit2md` parameter. The Sandman documentation will explicitly state that `jobs2md` relies on the provider's default relevance sorting algorithm.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #25)
**Original:**
```markdown
**Investigation & Guidance:**
- In job listings, the "author" is effectively the employer/company. JobSpy returns `company`.
- **Code Change Strategy**: 
  - Update `jobs2md` frontmatter generation to map `row.get('company')` to the standard `author` field. 
  - Ensure Reddit2md maps the post's author directly to the `author` field.
  - This unifies the concept of "creator of the post" across modules.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #26)
**Original:**
```markdown
### Human input:
I don't want to shoe-horn the "author" field into a module that doesn't need it. if what is returned is never an individual poster of a job, and always the company itself, then the frontmatter should show "employer" instead of "author". The only other acceptable solution is something generic like "creator" or "poster", but that's unintuitive when making queries on jobs by creator instead of employer, and would only make sense in front-matter. We'll have "employer" in front-matter for job2md. Keep author in front-matter for reddit2md.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #28)
**Original:**
```markdown
### Human input:
- Reddit2md doesn't do anything like that. the "author" variable in reddit is limited to markdown output, not any particular user-facing parameter, as far as I am aware.
- Jobspy (i believe) allows us to querie by "author" or employer or whatever, so it COULD be a useful parameter to use in config files or python or CLI calls. "show me jobs posted by this employer". I'm still not sure if that's really how it works. but if we can run queries like that, then this parameter needs to be user-facing to some extent to allow for the detail to be used in their queries. 
  - If the employer returns `company` or `employerID` or something similar, we can just call it `employer: ` in the front-matter, but i still don't have clarity on the exact variable. I want to know how i'd use it in jobspy queries. empoloyer ID? company?
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #33)
**Original:**
```markdown
### AI Analysis & Updated Plan:
- **Understanding**: You want to utilize Markdown YAML's native support for lists and distinct keys rather than awkwardly concatenating disparate data into a single string.
- **Review**: This is the correct approach for robust data structure in Obsidian/Markdown. Separating independent metadata concepts prevents filtering nightmares later.
- **New Plan**: 
  - **reddit2md**: Map Reddit flair directly to `category`.
  - **job2md**: Do not synthesize a generic `category`. Instead, utilize specific, descriptive list keys in the front-matter, matching the data returned by JobSpy, such as:
    ```yaml
    employment_type: [Full-time, Contract]
    workplace: [Remote]
    ```
### Human input:
yes, but we don't need brackets and I'm asking for your advice on naming those properties. my examples were "employment_type and workplace" but there's gotta be a better way to name them. remote vs in person vs hybrid is "workplace"? it almost works. you know what I'm asking for?
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #36)
**Original:**
```markdown
**Investigation & Guidance:**
- `jobs2md` requires multiple sources (`indeed`, `linkedin`). 
- Reddit API (PRAW) natively supports multiple subreddits via the `+` operator (e.g., `reddit.subreddit("python+learnpython")`).
- **Code Change Strategy**: 
  1. Standardize on **`sources`** (list or comma-separated string) across all modules.
  2. In `reddit2md`, accept a list of `sources`, join them with `+`, and query them as a single multi-reddit. 
  3. Deprecate `source` but add a fallback mechanism in Sandman config parsing to convert a single `source` string into a `sources` list.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #37)
**Original:**
```markdown
### Human input:
We don't use the API. We use a workaround. Explained in above answer. Each call is individual, so in order to support `sources`, we'd need new logic that creates several calls, then makes them in succession. similar to how we put routines in the config files to do several jobs at a time, we'd just do something similar here, under the hood. User wouldn't see.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #38)
**Original:**
```markdown
### AI Analysis & Updated Plan:
- **Understanding**: Because `reddit2md` hits individual RSS endpoints, we cannot query multiple subreddits in a single network call. We must iterate.
- **Review**: Your proposed solution—handling the list internally by looping over the sources and making successive calls—is perfectly aligned with the goal of unifying the user-facing configuration to `sources`.
- **New Plan**: 
  - Standardize on **`sources`** (list format) universally across all config files. Deprecate `source`.
  - **job2md**: Pass the list natively to JobSpy.
  - **reddit2md**: Implement an internal loop in the scraper. For every item in the `sources` list, execute the RSS fetch workflow sequentially and compile the results.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #56)
**Original:**
```markdown
## 11. Jobs2md Specifics (Descriptions, Country, etc.) & Rescrape Logic
**Reference**: `docs/nomenclature.md` (Lines 172-184)
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #57)
**Original:**
```markdown
**Guidance:**
- **`fetch_full_description`**: Expose this boolean. Internally map to `linkedin_fetch_description`. By default, LinkedIn does not return full HTML descriptions via JobSpy to save time/requests. Standardizing this enables the user to opt into slower, high-fidelity scrapes.
- **`target_country` / `enforce_annual_salary` / `query_google`**: These should be grouped under a specific `jobs2md_options` dictionary in Sandman or explicitly documented as job-specific overrides to avoid polluting the universal nomenclature.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #62)
**Original:**
```markdown
How we can use this for job2md:
When we are scraping from a source (linkedin) that doesn't give full details by default, then we can use the detail field. In reddit, it's something like XS, SM, MD, LG, and XL. for jobs2md it can just be a boolean. default value is false. if we run a scrape on linkedin where we need the full details, we just specify detail: true.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #64)
**Original:**
```markdown
### AI Analysis & Updated Plan:
- **Understanding**: 
  1. You want to repurpose the `detail` parameter across modules: in `reddit2md` it controls comment depth, while in `jobs2md` it will serve as a boolean flag dictating whether to fetch full job descriptions (specifically for LinkedIn).
  2. You want to port the `rescrape_after` workflow from `reddit2md` over to `jobs2md`. In `reddit2md`, immature posts get stamped with `rescrape_after: <timestamp>` so the system knows to re-fetch and expand them later. In `jobs2md`, if a job is scraped shallowly (`detail: false`), it should output the markdown with an empty `rescrape_after:` field. If the user later decides they want the full job description, they populate that field manually, triggering the orchestrator to re-scrape that specific job with `detail: true`.
- **Review**: This is a brilliant, cohesive architecture. Using the Markdown files themselves as a two-way interface/database queue is extremely powerful. It keeps initial scrapes fast while giving the user granular, on-demand control over data hydration.
- **New Plan**: 
  - Standardize `detail` across modules: as a boolean in `jobs2md` (default: false), and as an enum/size string in `reddit2md`.
  - In `jobs2md` front-matter generation, always include the `rescrape_after: ` key. If `detail: false` during the run, leave it blank.
  - Implement orchestrator logic for `jobs2md` that scans existing Markdown outputs. If it finds a populated, past-due `rescrape_after` field, it parses the `post_url`, fires a targeted JobSpy request with `detail: true` (which maps to `linkedin_fetch_description: True`), and updates the Markdown file.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #65)
**Original:**
```markdown
### Human input:
don't touch detail in reddit2md. we are just establishing that in jobs2md it happens to be a boolean. No changes needed to reddit2md regarding this.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #1)
**Original:**
```markdown
---
TO-AI: |
  This is a master coordination prompt for the Sandman Unified Nomenclature & YAML Initiative. 
  Your mission is to synchronize the codebases of Sandman, reddit2md, and jobs2md with the newly established documentation, nomenclature and config functionality and format standards.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #2)
**Original:**
```markdown
FILE_MAP:
  sandman:
    - path: sandman.py
      action: Update config loader to strictly use YAML; rename 'jobs' list processing to 'routine'; ensure dispatch dictionary matches Universal Nomenclature.
    - path: config.yml
      action: Ensure structure follows 'settings' and 'routine' (using 'routine' as the key instead of 'jobs').
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #3)
**Original:**
```markdown
reddit2md:
    - path: modules/reddit2md/reddit2md/core/config.py
      action: Swap json.load for yaml.safe_load; rename internal keys from 'jobs' to 'routine'.
    - path: modules/reddit2md/reddit2md/scraper.py
      action: Update the main execution loop to iterate over the 'routine' key; ensure all local variables match nomenclature.md.
    - path: modules/reddit2md/reddit2md.py
      action: Update CLI help text and arguments if any underscores survived the hyphenation initiative.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #4)
**Original:**
```markdown
jobs2md:
    - path: modules/jobs2md/core/config.py
      action: Swap json/yaml loading logic to be strictly YAML; implement the translation layer between Sandman Standard (e.g. 'source') and JobSpy (e.g. 'site_names').
    - path: modules/jobs2md/jobs2md.py
      action: Update the execution loop to process the 'routine' key; ensure the output mapping matches the Standard Markdown Schema.
    - path: modules/jobs2md/core/client.py
      action: Verify that Sandman Standard variables are correctly mapped to the JobSpy dependency.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #5)
**Original:**
```markdown
ACCEPTANCE_CRITERIA:
  - No .json files are used for configuration.
  - The key 'jobs' does not appear in any config.yml or configuration-handling logic (replaced by 'routine').
  - 'sandman.py' can execute a full cycle of both reddit2md and jobs2md using only the root config.yml.
  - All Markdown front-matter generated uses the names defined in nomenclature.md (e.g., 'post_URL', 'poster', 'label').
  - Every change is verified by a successful execution run.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #9)
**Original:**
```markdown
- name: "UX Ops Remote Search"
          module: "jobs"
          source: "indeed"
          query: "software engineer"
          location: "Remote"
          salary_min: 120000
          is_remote: true
          max_results: 20
          sources: ["indeed", "zip_recruiter", "google"]
      ``
  reddit2md example yaml config file:
    - "this shows the defaults for this module, as well as the routine it would perform if this module was called without any other specified parameters, just like sandman, but it can only use itself, no t other modules."
    contents:
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #17)
**Original:**
```markdown
1.  **Strict YAML Enforcement:** Update `sandman.py` to remove any fallback or legacy JSON loading. Use `yaml.safe_load`.
2.  **Terminology Migration:** In `sandman.py`, rename the variable `jobs` to `routine`. Update the config parsing logic to look for the `routine:` key in `config.yml`.
3.  **Path Verification:** Ensure `sandman.py` looks for `config.yml` in the project root by default.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #19)
**Original:**
```markdown
1.  **Config Class Refactor:** Modify `modules/reddit2md/reddit2md/core/config.py` to use YAML. 
    - Ensure it correctly merges `settings` with the tasks defined in the `routine`.
2.  **Scraper Loop Refactor:** Update `modules/reddit2md/reddit2md/scraper.py`.
    - Change `self.config_manager.get_jobs()` to `self.config_manager.get_routine()`.
    - Ensure the loop `for task in routine:` is used throughout.
3.  **Nomenclature Audit:** Check `processor.py` one last time to ensure the keys it writes to Markdown perfectly match the "Front-Matter Schema" in `nomenclature.md`.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #20)
**Original:**
```markdown
## Phase 3: Tier 2 Synchronization (jobs2md)
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #21)
**Original:**
```markdown
1.  **Nomenclature Translation Layer:** This is the most critical task. Update `modules/jobs2md/core/config.py` to translate:
    - `source` -> `site_names`
    - `query` -> `search_term`
    - `max_results` -> `results_wanted`
    - This allows the user to write "Standard Sandman" in the config, while the module handles the "Legacy JobSpy" names internally.
2.  **YAML Integration:** Ensure `jobs2md` no longer looks for a `.json` file.
3.  **Routine Loop:** Update `jobs2md.py` to iterate through the `routine` key.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #23)
**Original:**
```markdown
1.  **The "Empty Call" Test:** Run `python3 sandman.py` with no arguments.
    - **Pass Condition:** It successfully executes all tasks in the `routine` section of the root `config.yml`.
    - **Pass Condition:** reddit2md creates files with the correct front-matter.
    - **Pass Condition:** jobs2md creates files with the correct front-matter.
2.  **The "Manual Override" Test:** Run `python3 modules/reddit2md/reddit2md.py --source news --max-results 1`.
    - **Pass Condition:** The CLI arguments still work and override the `config.yml` correctly.
3.  **Blueprint Check:** Open `modules/unified_module_blueprint.md`. If you encountered a weird edge case or needed a new variable during this refactor, **add it to the blueprint now.** Do not let the documentation rot.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #24)
**Original:**
```markdown
## Verification Checklist for Agents
- [ ] Did you rename `jobs` to `routine` in the code?
- [ ] Did you rename `config.json` references to `config.yml` in the code?
- [ ] Did you run the code to see if it actually works?
- [ ] Does the generated Markdown front-matter match `nomenclature.md` exactly?
- [ ] Is `yaml.safe_load` used instead of `json.load` for configs?
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #38)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #23)
**Original:**
```markdown
## File: `docs/nomenclature.md` (Block #2)
**Original:**
```markdown
verbose:
    - "verbose, verbocity, detail."
    - "evaluate any overlap or confusion across programs."
    - "reddit2md doesn't currently support this argument, but it should. it has lots of output in CLI by default, and we should be able to limit that"
    - "job2md doesn't support by default, but should, since verbocity is an arg used by it's primary dependency JobSpy."
    desired state: "verbocity is supported in all three. for now, reddit2md should follow the pattern set by jobspy. 0 means only show errors, 1 means include warnings, 2 means show everything. it's current state looks like the default value is 2, so let's build support for the other two settings."
  min_age_hours and max_age_hours:
    - "I don't think there are currently supported in job2md. The logic is simple since jobspy uses hours_old."
    - "I think reddit2md only supports the min, but not max"
  offset:
    - "jobspy supports, but it's not in job2md or reddit2md. it should be."
  sort:
    - "supported by reddit2md"
    - "Is this a viable target to support in job2md?"
      derired state: 
        - "Investigate how it might be used by job2md, and create a report."
        - "reddit can sort by best, top, controversial, new, etc."
        - "Can jobspy support looking for top results of a query versus most recently-posted results, as an example? what about top trending results or something? Is there a 'sort' analog for job2md or not?  "
  author:
    - "I think this term is only used in reddit2md mardown frontmatter. not sure though"
      - "option exists to generalize to 'poster' or something."
      - "used for reddit post as well as the individual comments having authors."
    - "what about job2md? Is the poster/author the individual who posted the job, or the employer as an org? is there any difference when we look at the results we get from jobspy? maybe it only returns a employerID or employer name."
    desried state: "investigate. front-matter in job2md will probably have employerID, and if we do have the ability to see the individual author, maybe this can exist in job2md also."
  category:
    - "metadata-label, label, and category"
    - "originally called 'project' in reddit2md, then 'flair', now I'm not sure what it's called. label? category is probably the best approach that can work across job2md and reddit2md"
    desired state: "investigate how this might be used in job2md. should the analog be `is_remote`? and our category can be something like remote, hybrid, in-office? How else might it be useful? not sure what else is like category in job listings."
  source & sources:
    - "job2md uses `sources` and supports more than one. ex: linkedin, indeed, glassdoor"
    - "reddit2md uses `source` and requires a single subreddit name."
    desired state:
      - "investigate"
      - "can/should reddit2md support `sources`? what's the dev effort for this?"
      - "if so, can/should reddit2md remove `source`, or support both?"
      - "if no change is made, how is sandman handling it when mutiple sources are put into a reddit2md routine? Seems like we should support it."
  name:
    - "sandman allows a 'name' variable for each routine. This is great, it is almost like the declaration to start off that item of the yaml, then each argument can be indented under it, making it clear how many routines are listed instead of just looking like a bunch of arguments for some unclear amount of queries."
    - "modules do not yet support this field, they should."
    desired state:
      - "investigate how to acccomplish the following, create report."
      - "in sandman, in reddit2md and in job2md:"
        - "each item in routine section has a name declared."
        - "name shows up in front-matter of the markdown being created. Not sure what to call that variable. something like 'created by' or something, maybe 'query description' 'generator_process' 'originated by:'"
        - "with several named routines, we can not only trace which queires produced each file, but user can call THAT exact routine by name. Instead of putting all those parameters together to make the one-off call to that exact routine, and instead of calling ALL routines, they can just call that one by name in CLI and in python"
  max_db_records:
    - "Need to confirm max_db_records is used in sandman, reddit2md and in job2md instead of other naming like db_limit."
  md_log and enable_md_log.:
    - "to my knowledge, there's somthing like: md_log_enable, then we can have md_log_path. Default value true. But we have weird naming with md_output_directory and md_log. They should be consistent with each other and with json."
    Ideas:
      - "output_db"
      - "output_json"
      - "output_md_log"
      valid input formats (output_db as an example):
        output_db: "/path/to/"
          end result: file ends up  `/path/to/tracking.db`
        output_db: "/path/to"
          end result: file ends up  `/path/to/tracking.db`
        output_db: "/path/to/file-name.db"
          end result: file ends up  `/path/to/file-name.db`
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #62)
**Original:**
```markdown
## File: `docs/nomenclature.md` (Block #2)
**Original:**
```markdown
verbose:
    - "verbose, verbocity, detail."
    - "evaluate any overlap or confusion across programs."
    - "reddit2md doesn't currently support this argument, but it should. it has lots of output in CLI by default, and we should be able to limit that"
    - "job2md doesn't support by default, but should, since verbocity is an arg used by it's primary dependency JobSpy."
    desired state: "verbocity is supported in all three. for now, reddit2md should follow the pattern set by jobspy. 0 means only show errors, 1 means include warnings, 2 means show everything. it's current state looks like the default value is 2, so let's build support for the other two settings."
  min_age_hours and max_age_hours:
    - "I don't think there are currently supported in job2md. The logic is simple since jobspy uses hours_old."
    - "I think reddit2md only supports the min, but not max"
  offset:
    - "jobspy supports, but it's not in job2md or reddit2md. it should be."
  sort:
    - "supported by reddit2md"
    - "Is this a viable target to support in job2md?"
      derired state: 
        - "Investigate how it might be used by job2md, and create a report."
        - "reddit can sort by best, top, controversial, new, etc."
        - "Can jobspy support looking for top results of a query versus most recently-posted results, as an example? what about top trending results or something? Is there a 'sort' analog for job2md or not?  "
  author:
    - "I think this term is only used in reddit2md mardown frontmatter. not sure though"
      - "option exists to generalize to 'poster' or something."
      - "used for reddit post as well as the individual comments having authors."
    - "what about job2md? Is the poster/author the individual who posted the job, or the employer as an org? is there any difference when we look at the results we get from jobspy? maybe it only returns a employerID or employer name."
    desried state: "investigate. front-matter in job2md will probably have employerID, and if we do have the ability to see the individual author, maybe this can exist in job2md also."
  category:
    - "metadata-label, label, and category"
    - "originally called 'project' in reddit2md, then 'flair', now I'm not sure what it's called. label? category is probably the best approach that can work across job2md and reddit2md"
    desired state: "investigate how this might be used in job2md. should the analog be `is_remote`? and our category can be something like remote, hybrid, in-office? How else might it be useful? not sure what else is like category in job listings."
  source & sources:
    - "job2md uses `sources` and supports more than one. ex: linkedin, indeed, glassdoor"
    - "reddit2md uses `source` and requires a single subreddit name."
    desired state:
      - "investigate"
      - "can/should reddit2md support `sources`? what's the dev effort for this?"
      - "if so, can/should reddit2md remove `source`, or support both?"
      - "if no change is made, how is sandman handling it when mutiple sources are put into a reddit2md routine? Seems like we should support it."
  name:
    - "sandman allows a 'name' variable for each routine. This is great, it is almost like the declaration to start off that item of the yaml, then each argument can be indented under it, making it clear how many routines are listed instead of just looking like a bunch of arguments for some unclear amount of queries."
    - "modules do not yet support this field, they should."
    desired state:
      - "investigate how to acccomplish the following, create report."
      - "in sandman, in reddit2md and in job2md:"
        - "each item in routine section has a name declared."
        - "name shows up in front-matter of the markdown being created. Not sure what to call that variable. something like 'created by' or something, maybe 'query description' 'generator_process' 'originated by:'"
        - "with several named routines, we can not only trace which queires produced each file, but user can call THAT exact routine by name. Instead of putting all those parameters together to make the one-off call to that exact routine, and instead of calling ALL routines, they can just call that one by name in CLI and in python"
  max_db_records:
    - "Need to confirm max_db_records is used in sandman, reddit2md and in job2md instead of other naming like db_limit."
  md_log and enable_md_log.:
    - "to my knowledge, there's somthing like: md_log_enable, then we can have md_log_path. Default value true. But we have weird naming with md_output_directory and md_log. They should be consistent with each other and with json."
    Ideas:
      - "output_db"
      - "output_json"
      - "output_md_log"
      valid input formats (output_db as an example):
        output_db: "/path/to/"
          end result: file ends up  `/path/to/tracking.db`
        output_db: "/path/to"
          end result: file ends up  `/path/to/tracking.db`
        output_db: "/path/to/file-name.db"
          end result: file ends up  `/path/to/file-name.db`
```
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/readme_nomenclature adjustments.md` (Block #9)
**Original:**
```markdown
### Using the Configuration File
Wrong:
```json
{
    "settings": {
        "md_output_directory": "My Vault/Reddit",
        "min_score": 50,
        "data_output_directory": "data"
    },
    "jobs": [
        { 
            "name": "Python", 
            "sort": "top" 
        },
        { 
            "name": "Python", 
            "comment_detail": "XL" 
        }
    ]
}
```
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/readme_nomenclature adjustments.md` (Block #10)
**Original:**
```markdown
Correct:
```json
{
    "settings": {
        "md_output_directory": "My Vault/Reddit",
        "min_score": 50,
        "data_output_directory": "data"
    },
    "jobs": [
        { 
            "source": "Python", 
            "sort": "top" 
        },
        { 
            "source": "Python", 
            "detail": "XL" 
        }
    ]
}
```
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #1)
**Original:**
```markdown
---
Concerns:
  - "we are trying to standardize nomenclature so the same variable names and parameters can be used in sandman, reddit2md and in jobs2md (now called job2md, but i'll change in future)"
  - "i'll put a brain dump of my concerns, and based on that, and what you see in this file below, you can hopefully help me come up with a good approach that works for everything."
  - "the primary purpose of THIS FILE is to document every variable name. In all cases where it's possible, we try to standardize a name, then annotate under it once we have confirmed it words in each program, sandman, reddit2md and job2md."
  - "right now, we need to make some decisions on stardization and how the variables are used, then we need to verify they all work as intended."
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #2)
**Original:**
```markdown
verbose:
    - "verbose, verbocity, detail."
    - "evaluate any overlap or confusion across programs."
    - "reddit2md doesn't currently support this argument, but it should. it has lots of output in CLI by default, and we should be able to limit that"
    - "job2md doesn't support by default, but should, since verbocity is an arg used by it's primary dependency JobSpy."
    desired state: "verbocity is supported in all three. for now, reddit2md should follow the pattern set by jobspy. 0 means only show errors, 1 means include warnings, 2 means show everything. it's current state looks like the default value is 2, so let's build support for the other two settings."
  min_age_hours and max_age_hours:
    - "I don't think there are currently supported in job2md. The logic is simple since jobspy uses hours_old."
    - "I think reddit2md only supports the min, but not max"
  offset:
    - "jobspy supports, but it's not in job2md or reddit2md. it should be."
  sort:
    - "supported by reddit2md"
    - "Is this a viable target to support in job2md?"
      derired state: 
        - "Investigate how it might be used by job2md, and create a report."
        - "reddit can sort by best, top, controversial, new, etc."
        - "Can jobspy support looking for top results of a query versus most recently-posted results, as an example? what about top trending results or something? Is there a 'sort' analog for job2md or not?  "
  author:
    - "I think this term is only used in reddit2md mardown frontmatter. not sure though"
      - "option exists to generalize to 'poster' or something."
      - "used for reddit post as well as the individual comments having authors."
    - "what about job2md? Is the poster/author the individual who posted the job, or the employer as an org? is there any difference when we look at the results we get from jobspy? maybe it only returns a employerID or employer name."
    desried state: "investigate. front-matter in job2md will probably have employerID, and if we do have the ability to see the individual author, maybe this can exist in job2md also."
  category:
    - "metadata-label, label, and category"
    - "originally called 'project' in reddit2md, then 'flair', now I'm not sure what it's called. label? category is probably the best approach that can work across job2md and reddit2md"
    desired state: "investigate how this might be used in job2md. should the analog be `is_remote`? and our category can be something like remote, hybrid, in-office? How else might it be useful? not sure what else is like category in job listings."
  source & sources:
    - "job2md uses `sources` and supports more than one. ex: linkedin, indeed, glassdoor"
    - "reddit2md uses `source` and requires a single subreddit name."
    desired state:
      - "investigate"
      - "can/should reddit2md support `sources`? what's the dev effort for this?"
      - "if so, can/should reddit2md remove `source`, or support both?"
      - "if no change is made, how is sandman handling it when mutiple sources are put into a reddit2md routine? Seems like we should support it."
  name:
    - "sandman allows a 'name' variable for each routine. This is great, it is almost like the declaration to start off that item of the yaml, then each argument can be indented under it, making it clear how many routines are listed instead of just looking like a bunch of arguments for some unclear amount of queries."
    - "modules do not yet support this field, they should."
    desired state:
      - "investigate how to acccomplish the following, create report."
      - "in sandman, in reddit2md and in job2md:"
        - "each item in routine section has a name declared."
        - "name shows up in front-matter of the markdown being created. Not sure what to call that variable. something like 'created by' or something, maybe 'query description' 'generator_process' 'originated by:'"
        - "with several named routines, we can not only trace which queires produced each file, but user can call THAT exact routine by name. Instead of putting all those parameters together to make the one-off call to that exact routine, and instead of calling ALL routines, they can just call that one by name in CLI and in python"
  max_db_records:
    - "Need to confirm max_db_records is used in sandman, reddit2md and in job2md instead of other naming like db_limit."
  md_log and enable_md_log.:
    - "to my knowledge, there's somthing like: md_log_enable, then we can have md_log_path. Default value true. But we have weird naming with md_output_directory and md_log. They should be consistent with each other and with json."
    Ideas:
      - "output_db"
      - "output_json"
      - "output_md_log"
      valid input formats (output_db as an example):
        output_db: "/path/to/"
          end result: file ends up  `/path/to/tracking.db`
        output_db: "/path/to"
          end result: file ends up  `/path/to/tracking.db`
        output_db: "/path/to/file-name.db"
          end result: file ends up  `/path/to/file-name.db`
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #5)
**Original:**
```markdown
This document establishes the unified naming conventions across the Sandman ecosystem. Sandman orchestration translates these universal standard variables down into the specific parameters required by individual modules (like reddit2md for Reddit, or jobs2md).
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #15)
**Original:**
```markdown
- group_by_module
  - Used for: If true, Sandman creates subfolders in the output directories for each module (e.g. reddit, jobs).
  - Applies to: md_output_directory, json_output_directory
  - Default value: true
  - Does not apply to modules, only used in orchestration layer (Sandman)
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #17)
**Original:**
```markdown
### Module: jobs2md
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #19)
**Original:**
```markdown
- query
  - Used for: The primary search term.
  - Confirmed consistent naming:
    - Job2md:     ✅ (translates to search_term in jobspy, or necesary other variable for other sources like google)
    - reddit2md:  N/A (reddit2md relies on source instead of search query)
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #23)
**Original:**
```markdown
- job_type
  - Used for: Employment classification (fulltime, parttime, internship, contract).
    - Confirmed consistent naming:
    - Job2md:     ✅ (Maps to JobSpy: job_type)
    - reddit2md:  N/A
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #24)
**Original:**
```markdown
- is_remote
  - Used for: Filtering for remote-only opportunities.
  - Confirmed consistent naming:
    - Job2md:     ✅ (Maps to JobSpy: is_remote)
    - reddit2md:  N/A
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #26)
**Original:**
```markdown
- max_results
  - Used for: The upper limit of items to retrieve or process.
  - Confirmed consistent naming:
    - Job2md:     ✅ (Maps to JobSpy: results_wanted)
    - reddit2md:  ✅
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #31)
**Original:**
```markdown
- min_age_hours
  - Used for: The minimum time a post must exist before it is considered mature.
  - Confirmed consistent naming:
    - Job2md:     ? (JobSpy has `hours_old`, so we should be able to support this)
    - reddit2md:  ✅
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #32)
**Original:**
```markdown
- max_age_hours
  - Used for: The maximum age of a post to be considered relevant.
  - Maps to reddit2md: ?
  - Confirmed consistent naming:
    - Job2md:     ? (JobSpy has `hours_old`, so we should be able to support this)
    - reddit2md:  ?
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #35)
**Original:**
```markdown
- easy_apply
  - Used for: Filtering for jobs hosted directly on the job board.
  - Confirmed consistent naming:
    - Job2md:     ✅
    - reddit2md:  N/A
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #38)
**Original:**
```markdown
- verbocity
  - Used for: General level of conslole output and warnings/errors.
  - Confirmed consistent naming:
    - Job2md:     ? Should map to JobSpy: verbose (0 for errors, 1 for warnings, 2 for all)
    - reddit2md:  ? (limits console output and errors)
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #41)
**Original:**
```markdown
- auth_cert
  * Used for: Path to a CA Certificate file for network authentication.
  - Confirmed consistent naming:
    - Sandman:    N/A
    - Job2md:     ✅ (Maps to JobSpy: ca_cert)
    - reddit2md:  N/A
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #43)
**Original:**
```markdown
- sort
  * Used for: Sorting method for the platform feed.
  * Maps to JobSpy: N/A
  * Maps to reddit2md: sort (new, hot, top, rising)
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #44)
**Original:**
```markdown
## Jobs2md Specific Concerns, mostly for the module's default settings.
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #45)
**Original:**
```markdown
- fetch_full_description
  * Used for: Fetching complete descriptions when not provided by default feeds.
  * Maps to JobSpy: linkedin_fetch_description
  This should all be in job2md concerns. What level of detail is returned by default? if not complete, we need to support the variable `detail` just like reddit2md. Does it depend on source? linkedIn doesn't give full detail by defualt. need to learn more here.
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #46)
**Original:**
```markdown
- target_country
  - Used for: Platform-specific country filtering.
  - Maps to JobSpy: country_indeed
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #47)
**Original:**
```markdown
- enforce_annual_salary (not user-facing)
  - Used for: Normalizing wage data to an annual figure.
  - Maps to JobSpy: enforce_annual_salary
  used in logic of job2md to return salary range estimate
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #48)
**Original:**
```markdown
- query_google (not user facing)
  * Used for: Search term specific to Google jobs edge case.
  * Maps to JobSpy: google_search_term
  used in logic of job2md for handling google query logic, it doesn't use our normal query field (I guess. need to investigate use case)
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #54)
**Original:**
```markdown
* module
  * Description: The specific Sandman module that executed the scrape (e.g. jobs2md, reddit2md).
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #55)
**Original:**
```markdown
* author
  * Description: The entity that created the post (e.g. employer company name for jobs, original poster for Reddit).
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #59)
**Original:**
```markdown
- employer_id
  * Used for: Searching for records posted by specific corporate IDs.
  * Maps to JobSpy: linkedin_company_ids
  * Maps to reddit2md: N/A
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #1)
**Original:**
```markdown
---
learning: "in larger scale project, and in this one too, I'm specifically tracking my learning so the various LLM sessions know that this is a learning project, and the focus is on understanding my current understanding level, and pushing it forward, teaching me what i need to know to accomplish at each step. A great example is that chown command to initiate that script as a program. Great learning opportunity, but it was just declared as 'enter this in terminal' without real explanation of how it all worked and why we are using it that way."
    what i need from you: "check out the existing files for reference, but let's create our own one here for this project of creating the modules we are working on. Include the reddit one and these ones we are working on. Skills that make a difference when evaluating which jobs to pursue. Skills and experience that might end up being mentioned on a job posting. That sort of thing. For each entry, we should have two sub-points: 1: what kind of opportunities this skill or experience can directly translate to (ex: python and docker both translate to softare development, but lets be specific about potential niches that might be valueable to our priorities. what options does it open up that I might not have already tought of 2: what kind of opportunties does it create that are based in assymetric knowledge/skills? like, how is this exploitable? can this skill be used as an unfair advantage in certain industries or job types? is this a skill that can be used to create opportunities or automate jobs that are triddionally filled by people not technical enough to attempt it? is it a skill that can be used to solve a problem that is likely to be found in gov contracts? we could bid on those and have solutions in place ready to go, adapt for each instance. etc. in other words, how might this skill be applied with info assymetry and high leverage when applying moral flexibility and being scrappy and industrious."
    priorities:  
      - "check the LEARNING.md file, ensure we are prioritizing an approach that aligns with best practices and can have applications in the professional world. The skills gained in these projects should be documented in this document because eventually we will have to develop a much more robust solution for AI agents to be able to understand my level of experience in these various area when they will be responsible for assessing my candidacy for certain job listings and making suggestions. Haven't decided on an approach, but initially, we just ensure the agent knows to actively document and update any indications i give about my proficiency in various areas as well as the material learned and practiced and explained via these AI sessions."
      why competency listing/tracking DB/list is important: 
          - "There needs to be something to compare job listings to in order to make a good assessment of if it would be a good opportunity for me to apply to, if I would even be a good candidate."
          - "An automation will need to be able to have an AI agent create appropriate resume and cover letter outputs. If they don't have real info to pull from, those will be useless."
          - "I am NOT interested in deciding upon a system for tracking these experiences and skills and capabilities right now. I'm using markdown, and that's good enough for now. But we need to stay on top of it. It's crucial.  "
          - "The biggest leverage part of this whole project involves having AI discover unknown unknowns. That's not possible without my system having high levels of info about what I'm capable of, and low levels of moralizing."
            unknown unknown generation directive: 
              - "I can look for jobs with similar titles to jobs I've had before, i don't need this complex AI agent automation suite to facilitate that. Based on my experience and abilities, there are traditional next steps in my career that I can see. There are opportunities that someone in my position would be aware of. That's lower-leverage targeting. That's where there's an excess of competition. Using Linkedin and indeed to target the obvious job titles is VERY competitive, and the resulting jobs are likely to not be as great a fit for my priorities."
              - "What important to isolate and attach is what I NOT already aware of. I have extensive background in UX, product and software development, and so on. There are definitely niches I haven't considered like managing the knowledge base, sharepoints, design systems in Figma, governance models, sprint facilitation, design sprint facilitation, UX workshops, MVP design workshops, usability tear-downs, notion setups and maintenance, salesforce admin and setup, etc. There are all sorts of niches that are very close to my existing roles and experiences, but I wouldn't have thought to pursue because i either wasn't are of them or wasn't aware of how exploitable they are with my skill set."
              - "Out there somewhere is a job that's being posted on some obscure job title on some obscure job board that almost nobody outside of that obscure industry even knows about. I might not know the industry, the job type, or the place to find it. But someone with my background would easily be able to use my existing experience to land that job, take the first two weeks to quietly automate most of the responsibilities, then try to disappear and stay off everyone's radar. There are less-competitive roles with less-sexy titles in very boring industries at really negligible companies. They're being posted on a website I've never heard of. Some of them are very unlikely to have high levels of micromanagement or tracking, and may even be able to be performed remotely. They are totally possible for me by simply framing my experience in a different light, and (at the most) doing a little research into a new technology, skill or industry. Maybe a quick online certification. I will never be able to find those jobs on my own. I need a system that allows them to uncover themselves, and allows me to not let them go un-noticed. Nobody goes to school to be 'the ERP installer', and nobody ever set a goal to be the analyst in charge of making spreadsheets about bus routes. But sometimes niches like that are easy to obtain and entirely automate because none of the regular applicants would ever have anywhere near the technical ability i have. The supervisor for that employee has no idea what to look for, and isn't interested in micro-managing or tracking anyway, so they're free to automate the job away so long as they aren't attracting attention. I need a system for uncovering, discovering, evaluating, tracking and noticing when they're in front of me. Approaching the owner of a drywall business and offering a seller-finaced buyout because they're burned out managing all the jobs could be a good move if i already lined up a perfect software solution to taking over all their dispatch and job tracking work. I could offer them a retirement path and give myself a semi-passive income stream. That's not a job I can click 'easy apply' to on indeed. I need to think asymmetrically like that."
First attempt at summarizing for AI:
  learner file needed: "we're engagine with a lot of employable and exploitable skills, it needs to be tracked. it's also important that the document sets expectations with future agent sessions that it's a learning project. knowledge and skills need to be documented, and everything needs tobe explained unless the doc says it's already understood. I don't need huge solutions created for me or complicated and unexplained CLI commands to solve problems. i need to understand everything."
    background reference: "I cobbled together some of the stuff from various files and pasted them into this file. I have no idea how to optimize it to be easy to update the way i need it updated. I think the best reference might be the file from the larger project. It's also here in the docs folder. I don't like how disorganized and unweildy it became over time, and i hate that it uses markdown tables and bold text and other ugly stuff. i do like how there's basically a detailed update appended periodicaly by the AI agent. makes it easy to just makes sense of structuring it later. I just wish it was more optimized to what our future usecase will be."
    what i need from you: "create LEARNER.md according to your best judgement of what i need. I have specific ideas about how this info will be applied in the future, so we need to support that future use case in how we organize that file and how we instruct the AI to update it by considering employable competnecies and exploitable competencies, alsong with how to leverage it optimally and creatively for assymetric benefit."
TO-AI: |
  Your primary mission is to track the user's technical competencies with a relentless focus on "income stacking" and asymmetric leverage.
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #2)
**Original:**
```markdown
What you need to do:
  1. Read this document at the start of every session to understand the user's current capabilities and the strategic goal of uncovering exploitable, low-competition job niches.
  2. At the end of each session, append a session log that not only summarizes the technical concepts learned, but actively brainstorms how those specific skills can be applied as an "unfair advantage."
  3. Evaluate every new tool, library, or architecture choice through the lens of: "How could the user use this to find and fully-leverage an exploitable situation? examples: finding and automating and stacking boring low-oversight jobs in obscure niches, out-compete non-technical candidates in a legacy industry, or provide a high-leverage service to a less-modernized business?"
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #11)
**Original:**
```markdown
### High-Signal Data Extraction (Trafilatura, JobSpy, Crawl4AI)
- **Fluency Level**: Developing
- **The Asymmetric Leverage**: The ability to bypass modern web noise and structure unstructured data at scale.
- **Exploitable Niches**:
  - Uncovering unlisted, seller-financed business buyouts by scraping obscure local forums or registry sites.
  - Bidding on niche government contracts that require massive data consolidation. You can have the architecture ready to go and easily win on price and speed because your pipeline is fully automated.
  - Creating proprietary, highly curated datasets for legacy industries (like real estate zoning changes or legal dockets) and selling subscriptions to the data.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #6)
**Original:**
```markdown
- **Three-Tiered Architecture (The Pipeline):** To avoid "monolithic bloat," modules are categorized by their role in the knowledge pipeline:
    - **Tier 1: Source Scrapers (e.g., `reddit2md`, `gmail2md`):** These monitor high-level origins. Their job is to extract raw content and, crucially, identify external URLs for secondary processing.
    - **Tier 2: Entity Extractors (e.g., `jobs2md`):** Specialized modules that take a URL or specific entity ID and transform it into a high-fidelity record using domain-specific tools (like **JobSpy** for job boards).
    - **Tier 3: Utility Scrapers (e.g., `web2md`):** The "Universal Fallback." These use advanced noise-removal libraries (like **Trafilatura** or **Crawl4AI**) to turn any generic HTML page into clean Markdown.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #7)
**Original:**
```markdown
- **Cross-Module Handoff Schema:** Modules communicate through the filesystem.
    - **Extraction:** A Tier 1 module extracts URLs and stores them in the `extracted_links` front-matter field of its generated Markdown file.
    - **Queueing:** It also sets a `[entity]_scraped: false` (e.g., `jobs_scraped: false`) flag.
    - **Processing:** The corresponding Tier 2 module scans the output directory for files with this flag set to `false`, processes the links, and then updates the flag to `true` (or the count of items found).
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/gmail2md/README.md` (Block #6)
**Original:**
```markdown
Unlike traditional email archiving, gmail2md is built for **active knowledge management**. Its primary mission is to:
- **Target Signal:** Monitor specific labels (e.g., `Alerts/Jobs`, `Newsletters`, `Research`) rather than the whole inbox.
- **Extract Links & Entities:** Automatically identify and queue external URLs (like Job Postings) for secondary scraping modules.
- **Maintain Chronology:** Append new replies or updates to existing notes, preserving the full context of a thread.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/gmail2md/README.md` (Block #14)
**Original:**
```markdown
1. **Config (Settings):** Manages `label` targeting, `max_post_age` (to avoid historical bloat), and `auth_directory` paths.
2. **Client (Network):** Supports **Google OAuth (Gmail API)** for high-volume users and **IMAP** for users wanting a simpler, protocol-based connection.
3. **Processor (Translation):**
    - Maps `Message-ID` to `post_id`.
    - Sanitizes HTML body into clean Markdown.
    - **Entity Extraction:** Specifically looks for patterns matching job board URLs to populate the `jobs` metadata.
4. **DatabaseManager (State):** Tracks which `Message-ID` has been processed to ensure zero duplicates.
5. **Orchestrator (Loop):** Iterates through labels, handles the "Job Scraper" handoff, and executes the State Reconciliation Flow.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/gmail2md/README.md` (Block #17)
**Original:**
```markdown
### Unique Front-Matter Fields
- `sender`: The "From" address.
- `label`: The Gmail label being targeted.
- `thread_id`: The Gmail thread identifier (used for appending replies).
- `extracted_links`: A list of URLs found in the body.
- `jobs_scraped`: (Boolean/Int) Status of the secondary job-extraction pass.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/gmail2md/README.md` (Block #23)
**Original:**
```markdown
### Q3: Monitoring Job Sites (APIs vs. Scrapers)
**The Problem:** Job sites are aggressive and APIs are restricted.
**The Solution:** Use **JobSpy**.
- **Recommendation:** **JobSpy** is a Python library that aggregates LinkedIn, Indeed, Glassdoor, and ZipRecruiter into a single Pandas DataFrame. It handles the "API-like" querying without needing official (and often impossible-to-get) API keys.
- **Aggregator Strategy:** Focus 50% on "High-Signal" sources (JobSpy/LinkedIn/Indeed) and 50% on "Conventional" sources (Direct RSS feeds from niche boards, company career pages).
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/gmail2md/README.md` (Block #24)
**Original:**
```markdown
### Q4: Organizing the Next Steps
**The Strategy:** A Three-Tiered Module Architecture.
1.  **Tier 1: Source Scrapers (e.g., `gmail2md`, `reddit2md`)**
    - Responsibility: Identify URLs and high-level context.
2.  **Tier 2: Entity Extractors (e.g., `jobs2md`)**
    - Responsibility: Take a URL (from Gmail or Manual Input) and turn it into a "Job Note" using **JobSpy** or **Crawl4AI**.
3.  **Tier 3: Utility Modules (e.g., `web2md`)**
    - Responsibility: General HTML -> Markdown conversion for any URL not handled by a specific Entity Extor.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/gmail2md/README.md` (Block #25)
**Original:**
```markdown
**Manual Input:** Support this via a simple **CLI command** or **Webhook**.
Example: `python sandman.py --module jobs2md --url [LINK]`. 
This allows your Apple Shortcut to simply send an HTTP POST to your server, which then triggers the Job Scraper.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/gmail2md/README.md` (Block #27)
**Original:**
```markdown
## 5. Next Steps for gmail2md
1.  **Architecture:** Draft the `docs/architecture.md` using `imaplib` for the Client bucket (fastest path to MVP).
2.  **Job Scraper:** Create a sibling directory `modules/jobs2md/` and initialize it with **JobSpy**.
3.  **Integration:** Define the "Handoff Schema" where gmail2md writes a list of `extracted_links` that `jobs2md` picks up in the next cycle.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/architecture.md` (Block #1)
**Original:**
```markdown
# jobs2md Architecture Document
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/architecture.md` (Block #2)
**Original:**
```markdown
**Target Platform:** Multi-Source Job Boards (LinkedIn, Indeed, Glassdoor, ZipRecruiter)  
**Module Name:** jobs2md
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/architecture.md` (Block #4)
**Original:**
```markdown
## 2. Technical Strategy
- **Aggregator Engine:** Primary extraction is handled by **JobSpy**, which provides a unified, concurrently-scraped data stream from major platforms without requiring official API keys.
- **Dynamic Content:** Utilizes **Playwright** (Chromium) to handle JavaScript-heavy sites that simple HTTP requests cannot see.
- **Relational Awareness:** Implements "Parent Linking." When a job is scraped from an email-derived URL, it finds the original `gmail_[post_id].md` file and updates its `jobs_scraped` metadata while linking the new job note back to the sources email.
- **State Reconciliation:** Follows the Sandman Blueprint by scanning the `md_output_directory` on startup to ensure the SQLite index matches the actual Markdown files on disk.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/architecture.md` (Block #7)
**Original:**
```markdown
### B. Client (Network Operations)
- **Primary:** `JobSpyClient` wraps the `jobspy.scrape_jobs()` function.
- **Fallback:** `WebFallbackClient` uses `Trafilatura` or `Crawl4AI` for direct scraping if the URL's domain is not supported by JobSpy.
- **Stealth:** Applies `selenium-stealth`-style headers to minimize bot detection on LinkedIn.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/architecture.md` (Block #8)
**Original:**
```markdown
### C. Processor (Translation)
Translates the Pandas DataFrame returned by JobSpy into the Sandman Standard Schema.
- Maps `job_url` to `post_id` (sanitized hash if no direct ID is found).
- Extracts and maps:
    - `title` -> `title`
    - `company` -> `author`
    - `description` -> `content`
    - `min_amount`, `max_amount`, `currency` -> `salary` metadata.
    - `location`, `is_remote` -> `logistics` metadata.
- **Internal Linking:** Resolves the sources email ID to create `[[gmail_xyz]]` back-links.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/architecture.md` (Block #10)
**Original:**
```markdown
### E. Orchestrator / Scraper (The Execution Loop)
The main entry point (`jobs2md.py`).
- **Initialization:** Validates the state of the Obsidian vault.
- **Pipeline Check:** Scans the `md_output_directory` for any `.md` file with `jobs_scraped: false`. Extracts those URLs into a local routine.
- **Processing Loop:** Iterates through the queue (URLs from pipeline + CLI overrides).
- **Update Logic:** If a job note already exists, it checks for updates (e.g., salary change or job removal) and appends to the "Living Note."
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/architecture.md` (Block #12)
**Original:**
```markdown
- `post_id` -> Hashed or Platform-Specific ID (e.g., `LI_12345`).
- `title` -> Job Title.
- `author` -> Company Name.
- `content` -> Full Job Description.
- `time_scraped` -> Current timestamp.
- `time_posted` -> Original posting date from platform.
- `metadata_label` -> Job Category (e.g., Software Engineering).
- `score` -> Not applicable (maps to `salary_min` if needed).
- `module` -> Set to `"jobs2md"`.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #1)
**Original:**
```markdown
# jobs2md: Specialized Job Board Extractor (Tier 2)
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #2)
**Original:**
```markdown
jobs2md is a professional-grade Tier 2 Entity Extractor designed to transform job posting URLs into high-fidelity, structured Markdown notes. It is a core component of the Sandman "Job Alert Pipeline," specifically optimized for Obsidian vaults and AI-driven career tracking.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #5)
**Original:**
```markdown
## 1. Core Mission
The primary mission of jobs2md is to eliminate "context fragmentation" in job searching. While email alerts provide a teaser, and job boards are transient, jobs2md creates a permanent, structured record of every opportunity, capturing:
- **Financials:** Salary ranges and compensation structure.
- **Requirements:** Skills, technologies, and experience levels.
- **Logistics:** Work type (Remote/Hybrid/On-site) and location.
- **Metadata:** Company details, posting date, and source tracking.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #10)
**Original:**
```markdown
### Running a Query
You can get results from a specific source, or several at a time, directly from the CLI:
```bash
python jobs2md.py --source "indeed"
```
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #12)
**Original:**
```markdown
## 3. Integration & Handoff
jobs2md is designed to work seamlessly within the Sandman ecosystem:
- **Input (Tier 1 Handoff):** Scans job sources (linkedin, indeed, etc.) and outputs the results in Markdown format. Tracks activity to ensure no repeats.
- **Input (Manual):** Accepts URLs via CLI for real-time scraping (e.g., from an Apple Shortcut).
- **Output:** Generates standalone `job_[source]_[post_id].md` files.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #15)
**Original:**
```markdown
- **[JobSpy](https://github.com/Bunsly/JobSpy):** The primary engine. It provides a unified, API-like interface for LinkedIn, Indeed, Glassdoor, and ZipRecruiter, chosen for its ability to aggregate multiple boards into a single data stream without official API keys.
    - **Pandas:** Used by the Processor for high-speed data manipulation and to manage the structured job data before it is translated into Markdown.
    - **PyYAML:** Used by the Config bucket to parse the `config.yml` settings, providing a flexible and human-readable configuration system.
    - **Playwright:** The browser automation engine used by JobSpy to navigate and scrape JavaScript-heavy job boards like a human, ensuring high-fidelity extraction.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #18)
**Original:**
```markdown
1.  **Initialize Environment:**
    ```bash
    cd modules/jobs2md
    python3 -m venv venv
    source venv/bin/activate
    ```
2.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Install Scraper Browser:**
    ```bash
    playwright install chromium
    ```
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #20)
**Original:**
```markdown
```bash
# Simple remote search
python jobs2md.py --query "software engineer"
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #21)
**Original:**
```markdown
# Granular search with salary and location filters
python jobs2md.py --query "frontend" --location "Seattle" --salary-min 120000 --hours-old 24
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #22)
**Original:**
```markdown
# Targeted sites
python jobs2md.py --query "data scientist" --sources "google,zip_recruiter"
```
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #23)
**Original:**
```markdown
## Proof of concept usage from Sandman layer
Sandman layer uses the same interfaces (python, CLI, config files, etc.) so just like we can queue our default routine and global settings defaults in our config file in the module, we can do the same in sandman like so:
```yaml
{
    "settings": {
        "debug": false,
        "md_output_directory": "../../workspace/feeds/reddit",
        "md_log": "../../workspace/data/reddit/scrape_log.md",
        "data_output_directory": "../../workspace/data/reddit/",
        "group_by_source": true,
        "min_age_hours": 0,
        "min_score": 20,
        "max_results": 10,
    },
    routine: [
        {
            "name": "Python-related jobs from indeed and glassdoor",
            "module": "jobs2md",
            "sources": ["indeed", "glassdoor"],
            "query": "python",
            "max_age_days": 14,
            "is_remote": true
        },
        {
            "name": "Docker-related jobs from indeed and glassdoor",
            "module": "jobs2md",
            "sources": ["linkedIn"],
            "query": "Docker",
            "max_results": 10,
            "is_remote": true
        }
    ]
}
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #26)
**Original:**
```markdown
## 6. Directory Structure
```text
modules/jobs2md/
├── core/               # The "5 Buckets" logic
├── templates/          # Markdown rendering templates
├── data/               # Local cache and SQLite (Debug Mode)
├── architecture.md     # Detailed technical specification
└── jobs2md.py     # Main entry point
```
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/web2md/architecture.md` (Block #4)
**Original:**
```markdown
## 2. Technical Strategy
- **Noise Removal Engine:** Primary extraction uses **Trafilatura** for high-precision content identification and metadata extraction (Author, Date, Title).
- **Dynamic Fallback:** Uses **Crawl4AI** (Playwright-based) for sites that require JavaScript rendering to display their main content.
- **Single-Source Context:** Designed to be used as both a standalone CLI tool and a Python library for other Sandman modules (like `reddit2md` or `jobs2md`).
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/web2md/README.md` (Block #7)
**Original:**
```markdown
## 3. Usage & Options
This module is typically called as a utility by other Sandman modules (like `reddit2md` or `jobs2md`) when they encounter an unknown URL.
```

**AI Analysis:** Skipped (No client)

---

