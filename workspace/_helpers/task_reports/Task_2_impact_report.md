---
task: Task_2
status: Pending Review
target_terms: [min_age_hours, max_age_hours, age, hours_old]
new_term: min_age_hours / max_age_hours
context: "Implementing strict age restrictions. max_age_hours defines the maximum age of a post to scrape (maps to JobSpy's hours_old or filters reddit creation times). min_age_hours filters out posts younger than the limit in jobs2md, but continues to act as a maturity rescrape trigger in reddit2md."
date_generated: 2026-03-10 15:55:31
---

# Documentation Scrubbing Report for Task_2

> **Instructions**: Review the `AI Analysis` and `Proposed Rewrite` for each block below. If accurate, apply the rewrite to the source file.

---

## File: `README.md` (Block #2)
**Original:**
```markdown
Sandman is a high-signal knowledge management suite designed to transform the messy web into structured, permanent Markdown files. It is built for professional note-taking environments like **Obsidian**, AI-driven research, and **RAG (Retrieval-Augmented Generation)** pipelines.
```

**AI Analysis:** Skipped (No client)

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

## File: `README.md` (Block #20)
**Original:**
```markdown
**Usage Examples:**
- **CLI Flag:** `python sandman.py --verbose 1`
- **YAML Config:**
  ```yaml
  settings:
    verbose: 1
  ```
- **Python Dictionary:** `JobScraper(overrides={'verbose': 1})`
```

**AI Analysis:** Skipped (No client)

---

## File: `README.md` (Block #24)
**Original:**
```markdown
- **`./save "your commit message"`**: Stages and commits all changes locally for **every** modified module and the root project. This is the "safe" command for saving your progress without sending it to the web.
- **`./push`**: Iterates through all repositories and pushes any unpushed local commits to their respective GitHub remotes.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/prompt.md` (Block #6)
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

## File: `workspace/_helpers/prompt.md` (Block #11)
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

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #4)
**Original:**
```markdown
## File: `README.md` (Block #4)
**Original:**
```markdown
Sandman is not just a collection of scrapers; it is an **Accumulator**.
- **Living Notes:** Instead of overwriting files, Sandman updates metadata and appends new content, creating a chronological record of an evolving discussion or thread.
- **Source of Truth:** The filesystem (Markdown) is the ultimate authority. Our SQLite databases are treated as self-healing caches that reconcile their state against your actual notes on every startup.
- **Zero Noise:** We leverage world-class open-source libraries like **Trafilatura**, **Crawl4AI**, and **JobSpy** to extract only the information that matters, stripping away the noise of the modern web.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #10)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #22)
**Original:**
```markdown
## File: `tasks.md` (Block #13)
**Original:**
```markdown
**Objective**: Ensure full parity for `min_age_hours` and `max_age_hours` in both `jobs2md` and `reddit2md`.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #25)
**Original:**
```markdown
## File: `tasks.md` (Block #14)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] **`jobs2md`**: Maps `max_age_hours` to JobSpy's native `hours_old` parameter.
- [ ] **`jobs2md`**: Implements post-scrape filtering on the resulting pandas DataFrame to drop any jobs that are younger than `min_age_hours`.
- [ ] **`reddit2md`**: Continues to use `min_age_hours` to queue posts for future rescrapes via `rescrape_after`.
- [ ] **`reddit2md`**: Implements a check against `created_utc` during iteration. If a post's age exceeds `max_age_hours`, it is immediately discarded/skipped.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #43)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #58)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #10)
**Original:**
```markdown
**Investigation & Guidance:**
- **JobSpy Reality Check**: JobSpy supports `hours_old` which fetches jobs posted *within* the last X hours. This is actually a **`max_age_hours`** analog, not a minimum age. 
- **Code Change Strategy:**
  1. **Job2md**: Map `max_age_hours` to JobSpy's `hours_old`. To support `min_age_hours`, we will need to filter the resulting pandas DataFrame post-scrape (e.g., dropping rows where the calculated age is less than `min_age_hours`).
  2. **Reddit2md**: PRAW's `.new()` or `.hot()` doesn't natively filter by age. We already filter by `min_age_hours`. To support `max_age_hours`, we will add a condition during iteration checking `created_utc`; if the post is older than `max_age_hours`, we can `break` or `continue`.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #61)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #67)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #16)
**Original:**
```markdown
### Human input:
- reddit2md: If you review how our reddit2md module works, first step is to create a rss feed, then in that feed we grab the URLs of each of the top n number of items. from that URL we can get a json address and pull the whole page as json. to support `offset`, wouldn't we just start disregard the first n amount of rss posts?
- job2md: implementing should be straight-forward if not already accomplished, jobspy supports this parameter natively.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #139)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #151)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #154)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #157)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #169)
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

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #193)
**Original:**
```markdown
## File: `docs/nomenclature.md` (Block #31)
**Original:**
```markdown
- min_age_hours
  - Used for: The minimum time a post must exist before it is considered mature.
  - Confirmed consistent naming:
    - Job2md:     ? (JobSpy has `hours_old`, so we should be able to support this)
    - reddit2md:  ✅
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #196)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #220)
**Original:**
```markdown
## File: `docs/nomenclature.md` (Block #47)
**Original:**
```markdown
- enforce_annual_salary (not user-facing)
  - Used for: Normalizing wage data to an annual figure.
  - Maps to JobSpy: enforce_annual_salary
  used in logic of job2md to return salary range estimate
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #235)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #238)
**Original:**
```markdown
## File: `docs/LEARNING.md` (Block #2)
**Original:**
```markdown
What you need to do:
  1. Read this document at the start of every session to understand the user's current capabilities and the strategic goal of uncovering exploitable, low-competition job niches.
  2. At the end of each session, append a session log that not only summarizes the technical concepts learned, but actively brainstorms how those specific skills can be applied as an "unfair advantage."
  3. Evaluate every new tool, library, or architecture choice through the lens of: "How could the user use this to find and fully-leverage an exploitable situation? examples: finding and automating and stacking boring low-oversight jobs in obscure niches, out-compete non-technical candidates in a legacy industry, or provide a high-leverage service to a less-modernized business?"
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #241)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #244)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #6)
**Original:**
```markdown
- **Three-Tiered Architecture (The Pipeline):** To avoid "monolithic bloat," modules are categorized by their role in the knowledge pipeline:
    - **Tier 1: Source Scrapers (e.g., `reddit2md`, `gmail2md`):** These monitor high-level origins. Their job is to extract raw content and, crucially, identify external URLs for secondary processing.
    - **Tier 2: Entity Extractors (e.g., `jobs2md`):** Specialized modules that take a URL or specific entity ID and transform it into a high-fidelity record using domain-specific tools (like **JobSpy** for job boards).
    - **Tier 3: Utility Scrapers (e.g., `web2md`):** The "Universal Fallback." These use advanced noise-removal libraries (like **Trafilatura** or **Crawl4AI**) to turn any generic HTML page into clean Markdown.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #250)
**Original:**
```markdown
## File: `modules/gmail2md/README.md` (Block #6)
**Original:**
```markdown
Unlike traditional email archiving, gmail2md is built for **active knowledge management**. Its primary mission is to:
- **Target Signal:** Monitor specific labels (e.g., `Alerts/Jobs`, `Newsletters`, `Research`) rather than the whole inbox.
- **Extract Links & Entities:** Automatically identify and queue external URLs (like Job Postings) for secondary scraping modules.
- **Maintain Chronology:** Append new replies or updates to existing notes, preserving the full context of a thread.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #253)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #259)
**Original:**
```markdown
## File: `modules/gmail2md/README.md` (Block #23)
**Original:**
```markdown
### Q3: Monitoring Job Sites (APIs vs. Scrapers)
**The Problem:** Job sites are aggressive and APIs are restricted.
**The Solution:** Use **JobSpy**.
- **Recommendation:** **JobSpy** is a Python library that aggregates LinkedIn, Indeed, Glassdoor, and ZipRecruiter into a single Pandas DataFrame. It handles the "API-like" querying without needing official (and often impossible-to-get) API keys.
- **Aggregator Strategy:** Focus 50% on "High-Signal" sources (JobSpy/LinkedIn/Indeed) and 50% on "Conventional" sources (Direct RSS feeds from niche boards, company career pages).
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #307)
**Original:**
```markdown
## File: `modules/jobs2md/README.md` (Block #15)
**Original:**
```markdown
- **[JobSpy](https://github.com/Bunsly/JobSpy):** The primary engine. It provides a unified, API-like interface for LinkedIn, Indeed, Glassdoor, and ZipRecruiter, chosen for its ability to aggregate multiple boards into a single data stream without official API keys.
    - **Pandas:** Used by the Processor for high-speed data manipulation and to manage the structured job data before it is translated into Markdown.
    - **PyYAML:** Used by the Config bucket to parse the `config.yml` settings, providing a flexible and human-readable configuration system.
    - **Playwright:** The browser automation engine used by JobSpy to navigate and scrape JavaScript-heavy job boards like a human, ensuring high-fidelity extraction.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #322)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #331)
**Original:**
```markdown
## File: `modules/web2md/README.md` (Block #7)
**Original:**
```markdown
## 3. Usage & Options
This module is typically called as a utility by other Sandman modules (like `reddit2md` or `jobs2md`) when they encounter an unknown URL.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #4)
**Original:**
```markdown
## File: `tasks.md` (Block #6)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] Create `workspace/_helpers/ai_doc_scrubber.py`.
- [ ] **Inputs**: The script takes 3 primary arguments: 
  1. `target_terms`: A comma-separated list of old variable names (e.g., `db_limit, max_records`).
  2. `new_term`: The standardized variable name (e.g., `max_db_records`).
  3. `new_functionality_context`: A string describing how the logic/functionality has changed.
- [ ] **Phase 1 (Extraction)**: The script searches all `.md` files (ignoring `venv`, `.git`) for the `target_terms`. For each match, it extracts the file path, line number, and a generous chunk of surrounding text (context).
- [ ] **Phase 2 (LLM Evaluation & Rewrite)**: For each extracted chunk, the script calls the Gemini API (via `google-genai` SDK or raw HTTP). It prompts the LLM to:
  - Evaluate if the text describes the old variable or old functionality.
  - Rewrite the paragraph to use the `new_term` and accurately describe the `new_functionality_context`.
- [ ] **Phase 3 (Report Generation)**: The script outputs a structured markdown report (e.g., `_helpers/doc_updates_required.md`) containing:
  - The File Path and Line Number.
  - The *Original Text*.
  - The *Proposed LLM Rewrite*.
- [ ] **Workflow integration**: As the AI Agent, I will run this script, review `doc_updates_required.md`, and then systematically use my file-editing tools (like `replace`) to apply the approved rewrites to the actual markdown files, guaranteeing the documentation correctly reflects the code changes.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #7)
**Original:**
```markdown
## File: `tasks.md` (Block #43)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] Execute a global search and replace in the Python codebase: change `db_limit` (or similar variants) to `max_db_records`.
- [ ] Verify that all SQLite database pruning functions (`DELETE FROM ... WHERE id NOT IN (SELECT id ... LIMIT ?)`) in the `DatabaseManager` classes are strictly referencing `max_db_records` from the parsed configuration.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #10)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #46)
**Original:**
```markdown
**Code Change Strategy**:
- Search codebase for `db_limit` and replace with `max_db_records`. 
- Ensure the database cleanup logic (e.g., SQLite `DELETE FROM ... WHERE id NOT IN (SELECT id ... LIMIT max_db_records)`) explicitly uses this standardized key in all `DatabaseManager` classes.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #19)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #5)
**Original:**
```markdown
## File: `tasks.md` (Block #6)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] Create `workspace/_helpers/ai_doc_scrubber.py`.
- [ ] **Inputs**: The script takes 3 primary arguments: 
  1. `target_terms`: A comma-separated list of old variable names (e.g., `db_limit, max_records`).
  2. `new_term`: The standardized variable name (e.g., `max_db_records`).
  3. `new_functionality_context`: A string describing how the logic/functionality has changed.
- [ ] **Phase 1 (Extraction)**: The script searches all `.md` files (ignoring `venv`, `.git`) for the `target_terms`. For each match, it extracts the file path, line number, and a generous chunk of surrounding text (context).
- [ ] **Phase 2 (LLM Evaluation & Rewrite)**: For each extracted chunk, the script calls the Gemini API (via `google-genai` SDK or raw HTTP). It prompts the LLM to:
  - Evaluate if the text describes the old variable or old functionality.
  - Rewrite the paragraph to use the `new_term` and accurately describe the `new_functionality_context`.
- [ ] **Phase 3 (Report Generation)**: The script outputs a structured markdown report (e.g., `_helpers/doc_updates_required.md`) containing:
  - The File Path and Line Number.
  - The *Original Text*.
  - The *Proposed LLM Rewrite*.
- [ ] **Workflow integration**: As the AI Agent, I will run this script, review `doc_updates_required.md`, and then systematically use my file-editing tools (like `replace`) to apply the approved rewrites to the actual markdown files, guaranteeing the documentation correctly reflects the code changes.
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #22)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #8)
**Original:**
```markdown
## File: `tasks.md` (Block #43)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] Execute a global search and replace in the Python codebase: change `db_limit` (or similar variants) to `max_db_records`.
- [ ] Verify that all SQLite database pruning functions (`DELETE FROM ... WHERE id NOT IN (SELECT id ... LIMIT ?)`) in the `DatabaseManager` classes are strictly referencing `max_db_records` from the parsed configuration.
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #25)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #11)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #46)
**Original:**
```markdown
**Code Change Strategy**:
- Search codebase for `db_limit` and replace with `max_db_records`. 
- Ensure the database cleanup logic (e.g., SQLite `DELETE FROM ... WHERE id NOT IN (SELECT id ... LIMIT max_db_records)`) explicitly uses this standardized key in all `DatabaseManager` classes.
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #31)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #17)
**Original:**
```markdown
## File: `docs/readme_nomenclature adjustments.md` (Block #2)
**Original:**
```markdown
Changes to Execute Across `README.md`, `scraper.py`, `core/config.py`, and `core/processor.py`:
  1. Source: Change `subreddit_name`, config `name`, config `subreddit`, and CLI `--subreddit` to `source` (CLI: `--source`).
  2. Max Results: Change `post_limit` and CLI `--limit` to `max_results` (CLI: `--max_results`).
  3. Detail: Change `comment_detail` to `detail` (CLI: `--detail`).
  4. Label: Change config `flair` and CLI `--flair` to `label` (CLI: `--label`).
  5. Post Links: Change `post_link` to `post_links` (CLI: `--post_links`).
  6. Markdown Log: Change `update_log` to `md_log` (CLI: `--md_log`).
  7. DB Limit: Change `max_db_records` and CLI `--max-records` to `db_limit` (CLI: `--db_limit`).
  8. Age: Change `min_post_age_hours` and CLI `--age` to `min_age_hours` (CLI: `--min_age_hours`).
  9. Blacklist Terms: Change `filter_keywords` and CLI `--filter` to `blacklist_terms` (CLI: `--blacklist_terms`).
  10. Blacklist URLs: Change `url_blacklist` and CLI `--blacklist` to `blacklist_urls` (CLI: `--blacklist_urls`).
  11. Source Grouping: Change `generate_subreddit_folders` and CLI `--folders` to `group_by_source` (CLI: `--group_by_source`).
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #37)
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

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #40)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #26)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #24)
**Original:**
```markdown
Scrapers must allow users to suppress side effects or limit footprints:
- save_json (Boolean): Whether to persist the sanitized JSON data after processing.
- md_log (Boolean): Whether to append the run results to the human-readable Markdown log.
- db_limit (Integer): Maximum number of records to keep in the SQLite index. Older records are pruned to keep the database size manageable.
- min_age_hours (Integer): Setting this to 0 must disable all maturity/re-scraping logic, making every scrape final.
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #43)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #29)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #31)
**Original:**
```markdown
### Layer 2: SQLite Index (The Memory Cache)
- Path: data_output_directory/database.db
- Purpose: A high-speed tracking index. It remembers what has been scraped, when it was scraped, and when it is scheduled to be re-scraped. This index is considered a cache and should be rebuildable from the Markdown files.
- Function: It is strictly treated as a Self-Healing Cache. It must never be the ultimate source of truth.
- Pruning: The database footprint is managed by a db_limit integer setting.
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #46)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #32)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #82)
**Original:**
```markdown
| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`max_results`** | Config / CLI (`--max-results`) / Python | The maximum number of new items to fetch during a single run. |
| **`db_limit`** | Config / CLI (`--db-limit`) / Python | Footprint control. The maximum number of records to keep in the SQLite cache. |
| **`save_json`** | Config / CLI (`--save-json`) / Python | Boolean. Whether to save a sanitized `.json` copy alongside the markdown. |
| **`md_log`** | Config / CLI (`--md-log`) / Python | Boolean. Whether to append run results to the human-readable Scrape Log. |
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #49)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #35)
**Original:**
```markdown
## File: `modules/reddit2md/architecture.md` (Block #9)
**Original:**
```markdown
### D. DatabaseManager (State Tracking)
Acts as the high-speed SQLite cache (`database.db`).
- Tracks: `id`, `title`, `author`, `source`, `label`, `score`, `post_timestamp`, `file_path`, and `rescrape_after`.
- Controls the footprint limit using `db_limit`, deleting the oldest unneeded records automatically.
- Facilitates the "State Reconciliation Flow" on startup by comparing DB records against the physical `.md` files.
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #55)
**Original:**
```markdown
## File: `docs/readme_nomenclature adjustments.md` (Block #2)
**Original:**
```markdown
Changes to Execute Across `README.md`, `scraper.py`, `core/config.py`, and `core/processor.py`:
  1. Source: Change `subreddit_name`, config `name`, config `subreddit`, and CLI `--subreddit` to `source` (CLI: `--source`).
  2. Max Results: Change `post_limit` and CLI `--limit` to `max_results` (CLI: `--max_results`).
  3. Detail: Change `comment_detail` to `detail` (CLI: `--detail`).
  4. Label: Change config `flair` and CLI `--flair` to `label` (CLI: `--label`).
  5. Post Links: Change `post_link` to `post_links` (CLI: `--post_links`).
  6. Markdown Log: Change `update_log` to `md_log` (CLI: `--md_log`).
  7. DB Limit: Change `max_db_records` and CLI `--max-records` to `db_limit` (CLI: `--db_limit`).
  8. Age: Change `min_post_age_hours` and CLI `--age` to `min_age_hours` (CLI: `--min_age_hours`).
  9. Blacklist Terms: Change `filter_keywords` and CLI `--filter` to `blacklist_terms` (CLI: `--blacklist_terms`).
  10. Blacklist URLs: Change `url_blacklist` and CLI `--blacklist` to `blacklist_urls` (CLI: `--blacklist_urls`).
  11. Source Grouping: Change `generate_subreddit_folders` and CLI `--folders` to `group_by_source` (CLI: `--group_by_source`).
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #61)
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

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #64)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #24)
**Original:**
```markdown
Scrapers must allow users to suppress side effects or limit footprints:
- save_json (Boolean): Whether to persist the sanitized JSON data after processing.
- md_log (Boolean): Whether to append the run results to the human-readable Markdown log.
- db_limit (Integer): Maximum number of records to keep in the SQLite index. Older records are pruned to keep the database size manageable.
- min_age_hours (Integer): Setting this to 0 must disable all maturity/re-scraping logic, making every scrape final.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #67)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #31)
**Original:**
```markdown
### Layer 2: SQLite Index (The Memory Cache)
- Path: data_output_directory/database.db
- Purpose: A high-speed tracking index. It remembers what has been scraped, when it was scraped, and when it is scheduled to be re-scraped. This index is considered a cache and should be rebuildable from the Markdown files.
- Function: It is strictly treated as a Self-Healing Cache. It must never be the ultimate source of truth.
- Pruning: The database footprint is managed by a db_limit integer setting.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #70)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #82)
**Original:**
```markdown
| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`max_results`** | Config / CLI (`--max-results`) / Python | The maximum number of new items to fetch during a single run. |
| **`db_limit`** | Config / CLI (`--db-limit`) / Python | Footprint control. The maximum number of records to keep in the SQLite cache. |
| **`save_json`** | Config / CLI (`--save-json`) / Python | Boolean. Whether to save a sanitized `.json` copy alongside the markdown. |
| **`md_log`** | Config / CLI (`--md-log`) / Python | Boolean. Whether to append run results to the human-readable Scrape Log. |
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #73)
**Original:**
```markdown
## File: `modules/reddit2md/architecture.md` (Block #9)
**Original:**
```markdown
### D. DatabaseManager (State Tracking)
Acts as the high-speed SQLite cache (`database.db`).
- Tracks: `id`, `title`, `author`, `source`, `label`, `score`, `post_timestamp`, `file_path`, and `rescrape_after`.
- Controls the footprint limit using `db_limit`, deleting the oldest unneeded records automatically.
- Facilitates the "State Reconciliation Flow" on startup by comparing DB records against the physical `.md` files.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #31)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #154)
**Original:**
```markdown
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
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #34)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #157)
**Original:**
```markdown
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
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #43)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #169)
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

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #49)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #235)
**Original:**
```markdown
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
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #64)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #31)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #17)
**Original:**
```markdown
## File: `docs/readme_nomenclature adjustments.md` (Block #2)
**Original:**
```markdown
Changes to Execute Across `README.md`, `scraper.py`, `core/config.py`, and `core/processor.py`:
  1. Source: Change `subreddit_name`, config `name`, config `subreddit`, and CLI `--subreddit` to `source` (CLI: `--source`).
  2. Max Results: Change `post_limit` and CLI `--limit` to `max_results` (CLI: `--max_results`).
  3. Detail: Change `comment_detail` to `detail` (CLI: `--detail`).
  4. Label: Change config `flair` and CLI `--flair` to `label` (CLI: `--label`).
  5. Post Links: Change `post_link` to `post_links` (CLI: `--post_links`).
  6. Markdown Log: Change `update_log` to `md_log` (CLI: `--md_log`).
  7. DB Limit: Change `max_db_records` and CLI `--max-records` to `db_limit` (CLI: `--db_limit`).
  8. Age: Change `min_post_age_hours` and CLI `--age` to `min_age_hours` (CLI: `--min_age_hours`).
  9. Blacklist Terms: Change `filter_keywords` and CLI `--filter` to `blacklist_terms` (CLI: `--blacklist_terms`).
  10. Blacklist URLs: Change `url_blacklist` and CLI `--blacklist` to `blacklist_urls` (CLI: `--blacklist_urls`).
  11. Source Grouping: Change `generate_subreddit_folders` and CLI `--folders` to `group_by_source` (CLI: `--group_by_source`).
```
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #67)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #37)
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #70)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #55)
**Original:**
```markdown
## File: `docs/readme_nomenclature adjustments.md` (Block #2)
**Original:**
```markdown
Changes to Execute Across `README.md`, `scraper.py`, `core/config.py`, and `core/processor.py`:
  1. Source: Change `subreddit_name`, config `name`, config `subreddit`, and CLI `--subreddit` to `source` (CLI: `--source`).
  2. Max Results: Change `post_limit` and CLI `--limit` to `max_results` (CLI: `--max_results`).
  3. Detail: Change `comment_detail` to `detail` (CLI: `--detail`).
  4. Label: Change config `flair` and CLI `--flair` to `label` (CLI: `--label`).
  5. Post Links: Change `post_link` to `post_links` (CLI: `--post_links`).
  6. Markdown Log: Change `update_log` to `md_log` (CLI: `--md_log`).
  7. DB Limit: Change `max_db_records` and CLI `--max-records` to `db_limit` (CLI: `--db_limit`).
  8. Age: Change `min_post_age_hours` and CLI `--age` to `min_age_hours` (CLI: `--min_age_hours`).
  9. Blacklist Terms: Change `filter_keywords` and CLI `--filter` to `blacklist_terms` (CLI: `--blacklist_terms`).
  10. Blacklist URLs: Change `url_blacklist` and CLI `--blacklist` to `blacklist_urls` (CLI: `--blacklist_urls`).
  11. Source Grouping: Change `generate_subreddit_folders` and CLI `--folders` to `group_by_source` (CLI: `--group_by_source`).
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #73)
**Original:**
```markdown
## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #61)
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

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #79)
**Original:**
```markdown
## File: `docs/readme_nomenclature adjustments.md` (Block #2)
**Original:**
```markdown
Wrong:
```bash
python reddit2md.py --subreddit news --limit 5 --detail XL --sort top --age 24
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #82)
**Original:**
```markdown
## File: `docs/readme_nomenclature adjustments.md` (Block #3)
**Original:**
```markdown
Correct:
```bash
python reddit2md.py --source news --max_results 5 --detail XL --sort top --post_age_min 24
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #118)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #51)
**Original:**
```markdown
### The User Guide (README.md)
Each module contains a user-facing manual located at the root of its own repo (e.g., `modules/[module_name]/README.md`).
- Context: It references the universal blueprint for global features and usage modes.
- Instructions: It details how to install and quick-start the specific module.
- Platform Specifics: The final section of the README serves as the definitive guide to how this module extends the baseline rules. This includes unique front-matter variables (e.g., adding cc and bcc for Gmail), unique data mapping logic, module-specific configuration toggles (e.g., sort methods for Reddit), and any authentication quirks or rate limit warnings.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #121)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #66)
**Original:**
```markdown
1. Create a new directory for the module: `modules/[module_name]/`.
2. Write an initial draft of the `README.md` file, defining the source being scraped, important platform-specific variables to extract, and the overall outline of the resulting JSON/md files.
3. Use this `unified_module_blueprint.md` file to map the requirements from your rough `README.md` into our standard architecture.
4. Create a new Architecture Document (`modules/[module_name]/docs/architecture.md`). Detail the technical strategy, how it implements the "5 Buckets", and define the schema mapping based on the blueprint. This file will guide the entire build process.
5. Review and finalize the architecture document.
6. Scaffold the internal architecture into the "5 Buckets" (Config, Client, Processor, DatabaseManager, Scraper) usually under a `core/` subdirectory.
7. Create a `templates/` folder inside the module with `note.template` and `comment.template`.
8. Implement the Client and Processor.
9. Wire the logic together with the Orchestrator.
10. Add a test task to the master `config.yml` and verify the State Reconciliation Flow.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #124)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #86)
**Original:**
```markdown
| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`label`** | Config / CLI (`--label`) / Python | Custom user-defined categorization override (formerly 'flair'). |
| | Frontmatter / JSON | Classifications provided by the source or overridden by the user. |
| **`group_by_source`** | Config / CLI (`--group-by-source`) / Python | Boolean. Whether to create sub-folders for each source (e.g., `/reddit/news/`). |
| **`detail`** | Config / CLI (`--detail`) / Python | Controls output depth (e.g., capturing XS vs XL comment trees). |
| **`sort`** | Config / CLI (`--sort`) / Python | The sorting method applied to the source feed (e.g., 'new', 'top'). |
| **`post_links`** | Frontmatter / JSON | A list of all external URLs found within the content. |
| **`date_posted`** | Frontmatter / JSON | The original publication timestamp of the post. |
| **`date_scraped`**| Frontmatter / JSON | The timestamp of when Sandman extracted the data. |
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #133)
**Original:**
```markdown
## File: `modules/reddit2md/architecture.md` (Block #6)
**Original:**
```markdown
### A. Config (Settings Management)
Handles configuration merging following the Precedence Order (CLI > Task-Specific > Global Defaults). Validates these platform-specific toggles:
- `max_results` (Integer): Maximum threads to fetch per feed run.
- `detail` (Enum: XS, SM, MD, LG, XL): Controls the depth and volume of captured comments (e.g., `MD` = Top 8 comments, 2 replies deep).
- `sort` (Enum: new, hot, top, rising): Determines the targeted `.rss` endpoint.
- `min_age_hours` (Integer): The delay for maturity logic. Set to 0 to disable.
- `label`, `blacklist_terms`, `blacklist_urls`: Search and output filters.
- `group_by_source` (Boolean): Organizes output dynamically.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #136)
**Original:**
```markdown
## File: `modules/reddit2md/architecture.md` (Block #8)
**Original:**
```markdown
### C. Processor (Data Sanitization & Translation)
Translates the messy, deeply-nested Reddit JSON tree into the clean Sandman Standard Schema.
- Extracts `link_flair_text` to use as the `label`.
- `_process_comments_recursive()`: Parses the complex recursive comment tree and filters it based on the user's `detail` preset (dropping removed/deleted comments).
- `resolve_links()`: Uses regex (`REDDIT_PERMALINK_REGEX`) to identify links to other Reddit posts. If the target post exists in the `DatabaseManager`, it replaces the URL with an internal Obsidian link format (`[[Subreddit_ID]]`).
- `parse_frontmatter()`: Reads existing `.md` files on disk to support the State Reconciliation Flow.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #139)
**Original:**
```markdown
## File: `modules/reddit2md/README.md` (Block #11)
**Original:**
```markdown
### Using the Command Line Interface
The CLI is the most common way to use reddit2md. You can run all configured scrape tasks by calling the script with no arguments. To scrape a specific subreddit on the fly (even if it is not in your config), use the --source argument followed by the subreddit name. For example:
```bash
python reddit2md.py --source news --max-results 5 --detail XL --sort top --min-age-hours 24
```
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1roulqx.md` (Block #16)
**Original:**
```markdown
A third Monsters, Inc. film is in the works. Probably gonna be sometime in 2030-2031 in time for the 30th anniversary of the original film.
	- ==**u/NotTaken-username** (Score: 11)==
		I hope Incredibles 3 has a time jump of at least 5-10 years. The first movie focused on Bob, the second on Helen, so maybe the third could be a coming-of-age story for Violet and Dash.
- ==**u/TheUmbrellaMan1** (Score: 15)==
	The Digger had a test screening a few days ago and I see there's no discussion about it here. You have to take these screenings with a grain of salt, so here we go: Tom Cruise plays a Texan oilman who causes a catastropic spill in the ocean. Taking this as a sign from God that he's been choosen as the saviour of the world, he sets out to warn the world about the polluted ocean. The scene from the teaser with Cruise dancing on th railing -- that's the part where he's all giddy about the prospect of being a saviour.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1roulqx.md` (Block #18)
**Original:**
```markdown
- ==**u/NotTaken-username** (Score: 14)==
	I hope the rumored Brand New Day opening montage shows Peter fighting Fisk’s Anti-Vigilante Task Force. 
	- ==**u/daredevil209** (Score: 5)==
		I 100% believe they gonna add that, they have to show what Peter has been up to during Fisk's mayorship
		- ==**u/Patrick2701** (Score: 4)==
			Or Kate bishop since her ties with swordsman 
- ==**u/LittleYellowFish1** (Score: 14)==
	[Daniel Chong reveals 2D animation test for "HOPPERS"](https://xcancel.com/threebarebears/status/2030787968538177726?s=46)
	- ==**u/JediNight1977** (Score: 11)==
		It‘s always impressive to me to see how long Pixar works on these movies. 6 years is a long time, especially when they don’t start doing the final 3D animating until the last 1,5 years. Goes to show that good things need time. Still find it hard to believe that Sony ever thought they could make two SpiderVerse movies in 5 years though. Like how was that ever supposed to work?
- ==**u/FPG_Matthew** (Score: 13)==
	Hopefully we start getting daily tv spots (or maybe an official trailer finally) for Born Again starting today or tomorrow.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1roulqx.md` (Block #31)
**Original:**
```markdown
Ben Reilly feels out of place in this storyline, but editorial micromanages Spider-Man hard, so it’s unavoidable
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1roulqx.md` (Block #37)
**Original:**
```markdown
I still feel like this storyline isn’t fit for a direct adaptation though. It has so many moving parts that the MCU doesn’t have set up that they couldn’t do it justice. Also, actor negotiations, for example, I doubt they would pay Pedro Pascal to have Reed on Born Again or in a Daredevil movie.
- ==**u/Bigbigbigrock** (Score: 6)==
	Finally read Wiccan #3 this weekend, overall enjoying it. Saw some complaints about how Billy is handling his depowered arc but I think it's really good. There are far worse ways to handle a "hero loses their powers" story, Billy having to depend on other skills to solve problems I think works well. The introduction on the last page also makes me think my theory of what the "tears of a giant" means is probably wrong. Excited to see what the penultimate issue reveals.
- ==**u/mcwfan** (Score: 6)==
	Sony, give me the trailer this week and my life is yours 
	- ==**u/E_Falkonn** (Score: 4)==
		![gif](giphy|Mn3Ln0vTxZ4lEIObrz)
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1roulqx.md` (Block #41)
**Original:**
```markdown
- Many teams could have been integrated into already existing organizations of the Marvel universe, the Lightspeed Rescue rangers could be part of Damage Control, the Time Force rangers could be TVA agents, and the SPD rangers could be Shield or Sword agents.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1roulqx.md` (Block #44)
**Original:**
```markdown
On the one hand, HBO's previous attempts at making movies based on their shows hasn't had the best results (the *Entourage* movie, *Many Saints of Newark*).
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1roulqx.md` (Block #52)
**Original:**
```markdown
[It’s going back to the serum of the human archetypes that our art is built off of,” says Pullman, who notes that despite its vast cast, Doomsday is not just a cameo fest. “Every character has their moment that builds the dimensions of them,” he says. “The Russo brothers did that so well. They do not want anyone just sitting in the background. They really took to heart the responsibility of having some of the best actors in the world all together. There’s a lot of really exciting pair-ups that happen. A lot of fans will be really excited. It’s so fun to dream about. What if A and B would work together? Would B and D would work together? You get to see a lot of those fantasies come into fruition.”](https://www.esquire.com/entertainment/movies/a70231217/lewis-pullman-interview-2026/)
- ==**u/Minute-Necessary2393** (Score: 1)==
	I literally sat in my room for 4 hours straight doing absolutely nothing. If thats not pure mental laziness, idk what is. Im finally out and about to salvage the rest of the day, now, though.
- ==**u/Boringpoz** (Score: 1)==
	I know he’s not inclined to talk negatively about a movie he’s in, but Lewis Pullman saying doomsday is not a cameo fest honestly gives me a lot of faith in the movie
	- ==**u/cbekel3618** (Score: 1)==
		&gt;“Every character has their moment that builds the dimensions of them. The Russo brothers did that so well. They do not want anyone just sitting in the background.”
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1rowbky.md` (Block #4)
**Original:**
```markdown
- ==**u/Krylarofaxia** (Score: 65)==
	It's funny whenever we get leaks or merch of Doctor Doom and we're always like "Yep, that looks like Doom."
	- ==**u/chimichanga_3** (Score: 30)==
		To be fair, his design was pretty predictable. All Marvel had to do was not change anything and that's what they did. 
		- ==**u/Mattyzooks** (Score: 28)==
			You would think Doom wouldn't be particularly hard to get wrong but for some reason someone thought they 'knew better' each time.
			- ==**u/In_My_Own_Image** (Score: 22)==
				I mean, the McMahon Doom looked recognizable enough as Doom.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/ArtificialInteligence/ArtificialInteligence_1rp6en3.md` (Block #1)
**Original:**
```markdown
# Proximity chat for AI agents.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/ArtificialInteligence/ArtificialInteligence_1rp6en3.md` (Block #4)
**Original:**
```markdown
Also it's technically very interesting to build so don't hesitate to ask questions about it : Basically, they first use BLE just to find each other and exchange the information needed to create a shared secret key. After that, each private message is encrypted with that key before it is sent, so even if anyone nearby can capture the Bluetooth packets, they only see unreadable ciphertext. So everyone can "hear" the radio traffic, but only the two agents that created the shared secret can turn it back into the original message. it's quite basic but building it for the first time is cool !
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/reddit/ArtificialInteligence/ArtificialInteligence_1rp79yu.md` (Block #5)
**Original:**
```markdown
Think about what that actually means. You get the capability of the best AI models on the market without any of the surveillance that comes packaged with them by default. That's not a small thing that's a fundamentally different relationship between a user and an AI tool.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/data/reddit/log.md` (Block #2)
**Original:**
```markdown
| Status | Label | Title | Score | Sort | Post Date | Last Scrape | Re-scrape After |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ✅ | Doomsday | [[MarvelStudiosSpoilers_1rojfop.md|New look at Doctor Doom merch for ‘AVENGERS: DOOMSDAY’]] | 55 | new | 2026-03-08 23:04 | 2026-03-09 14:15 | - |
| ✅ | Weekly | [[MarvelStudiosSpoilers_1roulqx.md|Weekly Free Talk and Index Thread - New and Fresh every Monday!]] | 21 | new | 2026-03-09 08:27 | 2026-03-09 14:15 | - |
| ✅ | Doomsday | [[MarvelStudiosSpoilers_1rowbky.md|First look at Doomsday merch revealed (a keychain and a cap)]] | 96 | new | 2026-03-09 10:14 | 2026-03-09 14:15 | - |
| ⏳ *Maturing* | 🤖 New Model / Tool | [[ArtificialInteligence_1rp6en3.md|Proximity chat for AI agents.]] | 1 | new | 2026-03-09 17:21 | 2026-03-09 14:15 | 2026-03-10 05:21 |
| ⏳ *Maturing* | 🤖 New Model / Tool | [[ArtificialInteligence_1rp79yu.md|Anonymous access to multiple frontier AI models through one privacy preserving gateway]] | 0 | new | 2026-03-09 17:51 | 2026-03-09 14:15 | 2026-03-10 05:51 |
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/readme_nomenclature adjustments.md` (Block #2)
**Original:**
```markdown
Wrong:
```bash
python reddit2md.py --subreddit news --limit 5 --detail XL --sort top --age 24
```
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/readme_nomenclature adjustments.md` (Block #3)
**Original:**
```markdown
Correct:
```bash
python reddit2md.py --source news --max_results 5 --detail XL --sort top --post_age_min 24
```
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/readme_nomenclature adjustments.md` (Block #12)
**Original:**
```markdown
Wrong:
```
### Minimum Post Age Hours
Description: The window of time a post must exist before it is considered mature. Set to 0 to disable re-scraping logic entirely.
- Config: "min_post_age_hours": 12
- CLI: --age 12
- Python: 'min_post_age_hours': 12
```
correct:
```
### Minimum Post Age (in hours)
Description: The window of time a post must exist before it is considered mature. Set to 0 to disable re-scraping logic entirely.
- Config: "min_age_hours": 12
- CLI: --min_age_hours 12
- Python: 'min_age_hours': 12
```
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #28)
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

## File: `docs/nomenclature.md` (Block #29)
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

## File: `docs/nomenclature.md` (Block #44)
**Original:**
```markdown
- enforce_annual_salary (not user-facing)
  - Used for: Normalizing wage data to an annual figure.
  - Maps to JobSpy: enforce_annual_salary
  used in logic of job2md to return salary range estimate
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #1)
**Original:**
```markdown
# Competency & Asymmetric Leverage Tracker
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #3)
**Original:**
```markdown
Future AI agents will use this document to understand the user's exact capabilities, evaluate job listings for hidden potential, and generate hyper-targeted resumes that frame the user's unique technical background as the perfect solution for obscure roles.
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #4)
**Original:**
```markdown
## AI Agent Instructions
1. **Focus on the Asymmetric Advantage**: When the user learns a new concept, your job is to brainstorm how that concept gives them an unfair advantage in a traditional, non-technical, or legacy environment.
2. **Discover the Unknown Unknowns**: Use the skills listed here to search for and suggest obscure job titles the user might not have considered. Look for roles where the user could secure the job easily, automate 90% of the responsibilities within the first two weeks, and maintain the role with minimal oversight.
3. **Continuous Session Logging**: Append a brief summary to the Session Log at the end of every session. Highlight not just *what* was learned, but *how it can be exploited*.
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #6)
**Original:**
```markdown
### Containerized Orchestration (Docker, Cron, venv)
- **Fluency Level**: Intermediate
- **The Asymmetric Leverage**: The ability to build isolated, zero-dependency automation environments. 
- **Exploitable Niches**: 
  - Targeting local businesses (e.g., dispatch, logistics, construction) that have no IT department. You can deliver a fully self-contained "black box" solution (like a Raspberry Pi running Docker) that automates their workflows without touching their messy existing systems.
  - Applying for data-entry or "operations analyst" roles at non-tech companies, then silently deploying containers on a company machine to automate the entire job while you work remotely.
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #7)
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

## File: `docs/LEARNING.md` (Block #8)
**Original:**
```markdown
### Modular System Architecture (The 5 Buckets Blueprint)
- **Fluency Level**: Intermediate
- **The Asymmetric Leverage**: "Speed-to-market" for spinning up custom, reliable automation solutions.
- **Exploitable Niches**:
  - Freelance consulting for workflow automation. Because you have a strict blueprint, you can confidently quote 48-hour turnarounds for complex web scraping tools that would take standard agencies weeks to architect.
  - Roles involving "Systems Integration" or "Digital Transformation" in mid-sized businesses, where you can rapidly prototype tools that make you indispensable.
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #9)
**Original:**
```markdown
### Version Control & Fleet Management (Git, Multi-Repo Bash Scripts)
- **Fluency Level**: Basic/Intermediate
- **The Asymmetric Leverage**: The ability to manage a fleet of proprietary tools seamlessly.
- **Exploitable Niches**:
  - Maintaining independent automation tools customized per client without exposing the entire ecosystem's source code. You retain absolute control over the IP and the deployment pipeline.
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #11)
**Original:**
```markdown
**Confirmed Competencies:**
- CLI navigation and basic bash script execution.
- Virtual environments (`venv`) isolation.
- Git basics (stage, commit, push) and multi-repo script management.
- Docker workflow (build, up, exec, volume mapping).
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/LEARNING.md` (Block #14)
**Original:**
```markdown
*(Future AI Agents: Append session summaries here. Ensure every update explicitly ties the newly learned technical skill to a potential asymmetric opportunity or hidden job niche.)*
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

## File: `modules/unified_module_blueprint.md` (Block #15)
**Original:**
```markdown
### C. The Python Resource (Importable Module)
Used for higher-level orchestration (e.g., an LLM agent triggering a scrape or seamless integration into larger suites).
- The main orchestrator class must accept an overrides dictionary in its run() method to bypass any global or task-specific defaults programmatically.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #19)
**Original:**
```markdown
1. Config (Settings Management): Handles the logic for merging `settings` with task-specific settings and applying CLI/Python overrides based on the Precedence Order. Validates parameter types.
2. Client (Network Operations): Strictly isolates API and network logic. Manages authentication, headers (e.g., browser-mimicking), rate limiting, and pagination. It should return raw or semi-raw data.
3. Processor (Data Sanitization & Translation): The pure data translation layer. It takes the messy API response from the Client and strictly maps it to the "Standard Schema". It also handles the logic for internal Obsidian link resolution.
4. DatabaseManager (State Tracking): Manages the SQLite index. Responsible for cache pruning, maintaining the `rescrape_after` maturity logic, and executing the State Reconciliation Flow on startup.
5. Scraper / Orchestrator (The Execution Loop): The main entry point. Iterates through the routine queue, coordinates the Config, Client, Processor, and DatabaseManager, and ultimately writes the final Markdown and JSON files to the disk using a Theme Engine / Templates.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #24)
**Original:**
```markdown
Scrapers must allow users to suppress side effects or limit footprints:
- verbose (Integer): Controls the level of terminal output across all modules and the orchestrator.
    - 0: Errors only (Silent operation).
    - 1: Basic progress and warnings (Recommended default).
    - 2: Granular debug and trace information.
- save_json (Boolean): Whether to persist the sanitized JSON data after processing.
- md_log (Boolean): Whether to append the run results to the human-readable Markdown log.
- db_limit (Integer): Maximum number of records to keep in the SQLite index. Older records are pruned to keep the database size manageable.
- min_age_hours (Integer): Setting this to 0 must disable all maturity/re-scraping logic, making every scrape final.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #26)
**Original:**
```markdown
To maintain the Source of Truth, every module must perform a surgical reconciliation on startup (handled by the Orchestrator and DatabaseManager). This ensures the SQLite cache reflects the current state of the filesystem.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #28)
**Original:**
```markdown
## 7. The Data Pipeline & State Management
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #31)
**Original:**
```markdown
### Layer 2: SQLite Index (The Memory Cache)
- Path: data_output_directory/database.db
- Purpose: A high-speed tracking index. It remembers what has been scraped, when it was scraped, and when it is scheduled to be re-scraped. This index is considered a cache and should be rebuildable from the Markdown files.
- Function: It is strictly treated as a Self-Healing Cache. It must never be the ultimate source of truth.
- Pruning: The database footprint is managed by a db_limit integer setting.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #34)
**Original:**
```markdown
### Context vs. Freshness (Maturity Logic)
To balance the need for immediate updates with the desire for deep context, modules must implement Maturity Logic.
1. Fresh Scrape: A new post is scraped immediately but marked with a future rescrape_after timestamp in the DB and the Markdown front-matter.
2. Maturation: Once that time passes, the module re-fetches the thread, updates the metadata (e.g., new score/metrics), and appends the finalized conversation to the file.
3. Disablement: Setting min_age_hours to 0 must disable this entirely, making every scrape final.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #51)
**Original:**
```markdown
### The User Guide (README.md)
Each module contains a user-facing manual located at the root of its own repo (e.g., `modules/[module_name]/README.md`).
- Context: It references the universal blueprint for global features and usage modes.
- Instructions: It details how to install and quick-start the specific module.
- Platform Specifics: The final section of the README serves as the definitive guide to how this module extends the baseline rules. This includes unique front-matter variables (e.g., adding cc and bcc for Gmail), unique data mapping logic, module-specific configuration toggles (e.g., sort methods for Reddit), and any authentication quirks or rate limit warnings.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #54)
**Original:**
```markdown
Example (Gmail Scraper Architecture):
- Objective: Capture emails from specific labels and transform them into chronological Markdown notes.
- Technical Strategy: Support Google OAuth and IMAP in the Client class. Cumulative logic in the Orchestrator dictates that new replies in a thread append to the bottom of the original note.
- Standard Schema Mapping: post_id maps to Message-ID, title to Subject, author to Sender.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #56)
**Original:**
```markdown
## 13. Repository & Module Management
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #60)
**Original:**
```markdown
To manage dependencies cleanly and ensure smooth server deployment, the Sandman suite follows a "Monolithic Orchestrator, Distributed Modules" architecture.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #66)
**Original:**
```markdown
1. Create a new directory for the module: `modules/[module_name]/`.
2. Write an initial draft of the `README.md` file, defining the source being scraped, important platform-specific variables to extract, and the overall outline of the resulting JSON/md files.
3. Use this `unified_module_blueprint.md` file to map the requirements from your rough `README.md` into our standard architecture.
4. Create a new Architecture Document (`modules/[module_name]/docs/architecture.md`). Detail the technical strategy, how it implements the "5 Buckets", and define the schema mapping based on the blueprint. This file will guide the entire build process.
5. Review and finalize the architecture document.
6. Scaffold the internal architecture into the "5 Buckets" (Config, Client, Processor, DatabaseManager, Scraper) usually under a `core/` subdirectory.
7. Create a `templates/` folder inside the module with `note.template` and `comment.template`.
8. Implement the Client and Processor.
9. Wire the logic together with the Orchestrator.
10. Add a test task to the master `config.yml` and verify the State Reconciliation Flow.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #74)
**Original:**
```markdown
| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`source`** | Config / CLI (`--source`) / Python | The platform or sub-community being targeted. Optionally used for subfolders. (e.g., subreddits in the reddit2md module, websites in a web scraper, etc...). |
| | Frontmatter / JSON | Identifies the origin of the scraped post. |
| **`post_id`** | Frontmatter / JSON | A unique identifier derived from the source platform's own ID system. |
| **`post_URL`** | Frontmatter / JSON | The direct web link to the original content on the source platform. |
| **`poster`** | Frontmatter / JSON | The author, OP, or entity that created the post being scraped (e.g., 'employer_name' when scraping indeed job listsings, 'OP' when scraping reddit posts, 'Authur' of articles, etc...). |
| **`module`** | Frontmatter / JSON | The Sandman module that generated the file (e.g., 'reddit2md'). Identifies the file as scraped/generated output, and the module that created it. |
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #78)
**Original:**
```markdown
| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`query`** | Config / CLI (`--query`) / Python | The main search term (used predominantly in job or web scrapers). |
| **`min_score`** | Config / CLI (`--min-score`) / Python | The minimum score or upvotes required to process a post. |
| **`blacklist_terms`** | Config / CLI (`--blacklist-terms`) / Python | List of keywords. If found in the title/body, the post is skipped. |
| **`blacklist_urls`** | Config / CLI (`--blacklist-urls`) / Python | List of domain fragments to ignore when capturing links. |
| **`min_age_hours`** | Config / CLI (`--min-age-hours`) / Python | Minimum time a post must exist before it is considered mature. |
| **`max_age_hours`** | Config / CLI (`--max-age-hours`) / Python | Maximum age for a post to be considered fresh/relevant. |
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #80)
**Original:**
```markdown
### 3. Limits & Data Management
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #82)
**Original:**
```markdown
| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`max_results`** | Config / CLI (`--max-results`) / Python | The maximum number of new items to fetch during a single run. |
| **`db_limit`** | Config / CLI (`--db-limit`) / Python | Footprint control. The maximum number of records to keep in the SQLite cache. |
| **`save_json`** | Config / CLI (`--save-json`) / Python | Boolean. Whether to save a sanitized `.json` copy alongside the markdown. |
| **`md_log`** | Config / CLI (`--md-log`) / Python | Boolean. Whether to append run results to the human-readable Scrape Log. |
| **`verbose`** | Config / CLI (`--verbose`) / Python | Integer (0, 1, 2). Controls console output verbosity. |
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #86)
**Original:**
```markdown
| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`label`** | Config / CLI (`--label`) / Python | Custom user-defined categorization override (formerly 'flair'). |
| | Frontmatter / JSON | Classifications provided by the source or overridden by the user. |
| **`group_by_source`** | Config / CLI (`--group-by-source`) / Python | Boolean. Whether to create sub-folders for each source (e.g., `/reddit/news/`). |
| **`detail`** | Config / CLI (`--detail`) / Python | Controls output depth (e.g., capturing XS vs XL comment trees). |
| **`sort`** | Config / CLI (`--sort`) / Python | The sorting method applied to the source feed (e.g., 'new', 'top'). |
| **`post_links`** | Frontmatter / JSON | A list of all external URLs found within the content. |
| **`date_posted`** | Frontmatter / JSON | The original publication timestamp of the post. |
| **`date_scraped`**| Frontmatter / JSON | The timestamp of when Sandman extracted the data. |
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

## File: `modules/gmail2md/README.md` (Block #7)
**Original:**
```markdown
### The Job Alert Pipeline (MVP Goal)
In its MVP state, this module is optimized to handle **Job Alert Emails** (LinkedIn, Indeed, etc.).
1. **gmail2md** scrapes the alert email.
2. It identifies the "Job Alert" label and triggers the `Processor` to extract job titles and URLs.
3. It creates an abbreviated "Job Page" for each link, establishing a relational link between the **Source Email** and the **Target Job**.
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

## File: `modules/gmail2md/README.md` (Block #18)
**Original:**
```markdown
### Behavioral Toggles
- `max_post_age_days`: (Default: 5) Only process emails newer than X days.
- `capture_unread_only`: (Boolean) If true, only process emails not yet marked as read.
- `mark_as_read`: (Boolean) Whether to mark the email as read after a successful scrape.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/gmail2md/README.md` (Block #21)
**Original:**
```markdown
### Q1: Universal Scraping & Noise Removal
**The Problem:** Re-writing scrapers for every site is inefficient.
**The Solution:** Leverage "AI-Native" scraping engines.
- **Recommendation:** Use **Trafilatura** or **Crawl4AI**.
    - **Trafilatura** is the "Gold Standard" for clean text extraction (noise removal). It excels at finding the "meat" of an article while ignoring headers/footers.
    - **Crawl4AI** is a modern, open-source crawler specifically for RAG. It handles JavaScript (essential for LinkedIn/Indeed) and outputs "Fit Markdown."
- **Strategy:** Instead of a "Universal Scraper" module, build a **`web2md`** utility module that uses `Crawl4AI`. Other modules (like Gmail) simply pass a URL to this utility.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/gmail2md/README.md` (Block #22)
**Original:**
```markdown
### Q2: Orchestration Layer (Sandman vs. Others)
**The Problem:** Building a custom UI/logic layer is time-consuming.
**The Solution:** Use **n8n** for "Plumbing," keep **Sandman** for "Logic."
- **Recommendation:** **n8n** is the most mature self-hosted automation tool. It has built-in Gmail, Discord, and Telegram nodes.
- **Sandman's Role:** Don't build a complex UI for Sandman. Use Sandman as a **Suite of CLI Tools**. 
    - Use **n8n** to *trigger* Sandman (via shell commands or Docker). 
    - Sandman provides the "Living Notes" logic and "Standard Schema" that generic tools like n8n or Paperclip lack.
- **Paperclip AI:** Better for "Autonomous Agents" with budgets. For a structured knowledge pipeline, Sandman's deterministic "Job Model" is safer.
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

## File: `modules/jobs2md/architecture.md` (Block #6)
**Original:**
```markdown
### A. Config (Settings Management)
Handles configuration merging following the Precedence Order (CLI > Task-Specific > Global Defaults).
- `salary_min` (Integer): Filter results by minimum compensation.
- `job_type` (Enum: remote, hybrid, onsite, full_time, part_time, contract).
- `radius` (Integer): Search radius in miles for location-based scrapes.
- `hours_old` (Integer): Filter for only very recent postings.
- `md_output_directory`, `data_output_directory`, `debug` (Sandman Standard).
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/architecture.md` (Block #9)
**Original:**
```markdown
### D. DatabaseManager (State Tracking)
Acts as the SQLite index (`database.db`).
- Tracks: `id`, `job_url`, `company`, `location`, `status` (e.g., Interested, Applied), `source_id`, and `file_path`.
- Implements the "State Reconciliation Flow" on startup to reconcile disk state with the DB.
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

## File: `modules/jobs2md/README.md` (Block #19)
**Original:**
```markdown
## 6. CLI Usage (Proof of Concept)
Test your search logic directly from the terminal. By default, LinkedIn is excluded to prevent rate-limiting during testing.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #24)
**Original:**
```markdown
**Usage:**
- **CLI:** `python jobs2md.py --verbose 1`
- **Config:** `verbose: 1`
- **Python:** `JobScraper(overrides={"verbose": 1})`
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/jobs2md/README.md` (Block #25)
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

## File: `modules/reddit2md/architecture.md` (Block #3)
**Original:**
```markdown
## 1. Objective
To build a professional-grade Reddit scraper designed for high-signal knowledge management. reddit2md transforms transient Reddit discussions into permanent, well-structured Markdown notes specifically optimized for Obsidian vaults, AI-automated workflows, and personalized knowledge collections.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/architecture.md` (Block #4)
**Original:**
```markdown
## 2. Key Limitation & Technical Strategy
**Limitation:** Scraping Reddit without Official API Access (No OAuth tokens).
- **Discovery via RSS:** Standard `.json` index feeds for subreddits are heavily rate-limited and cached when accessed without an API key. To bypass this, the Client uses Reddit's `.rss` endpoints (e.g., `reddit.com/r/python/new/.rss`) to discover new `post_id`s reliably.
- **Deep Fetch via JSON:** Once a `post_id` is discovered via RSS, the Client fetches the full thread (including comments) using the individual post's `.json` endpoint (e.g., `reddit.com/comments/{post_id}.json`), which is less restricted.
- **Graceful Degradation:** The network client gracefully detects if the external `requests` library is installed. If available, it utilizes `requests` to bypass advanced anti-bot measures (e.g., Reddit's 403 Forbidden blocks). If not, it falls back to the standard library `urllib`.
- **Maturity Logic (The Living Note):** Implements a `min_age_hours` check. Threads scraped while young are marked as "Maturing" in the database. The Orchestrator returns after the age threshold to re-scrape and append the final, mature conversation, creating a chronological timeline.
- **Obsidian Graph Resolution:** Converts URLs pointing to other internal Reddit threads into Obsidian internal links (e.g., `[[Python_1rm32fu]]`).
- **File System Sanitization:** Reddit flairs often include slashes (`/`). The Processor layer sanitizes these into dashes (`-`) to prevent unintended nested directory creation.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/architecture.md` (Block #6)
**Original:**
```markdown
### A. Config (Settings Management)
Handles configuration merging following the Precedence Order (CLI > Task-Specific > Global Defaults). Validates these platform-specific toggles:
- `max_results` (Integer): Maximum threads to fetch per feed run.
- `detail` (Enum: XS, SM, MD, LG, XL): Controls the depth and volume of captured comments (e.g., `MD` = Top 8 comments, 2 replies deep).
- `sort` (Enum: new, hot, top, rising): Determines the targeted `.rss` endpoint.
- `min_age_hours` (Integer): The delay for maturity logic. Set to 0 to disable.
- `label`, `blacklist_terms`, `blacklist_urls`: Search and output filters.
- `group_by_source` (Boolean): Organizes output dynamically.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/architecture.md` (Block #7)
**Original:**
```markdown
### B. Client (Network Operations)
Strictly isolates network logic from data parsing:
- `get_posts_from_rss(rss_url)`: Fetches and parses the XML Atom feed, extracting `post_id` and timestamp.
- `fetch_json_from_url(json_url)`: Handles raw HTTP GET requests to Reddit's `.json` endpoints.
- **Headers:** Applies standard browser-mimicking `User-Agent` and `Accept` headers to avoid standard bot-blocks.
- **Error Handling:** Explicitly catches 403 errors and alerts the user to install `requests` if using the `urllib` fallback.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/architecture.md` (Block #8)
**Original:**
```markdown
### C. Processor (Data Sanitization & Translation)
Translates the messy, deeply-nested Reddit JSON tree into the clean Sandman Standard Schema.
- Extracts `link_flair_text` to use as the `label`.
- `_process_comments_recursive()`: Parses the complex recursive comment tree and filters it based on the user's `detail` preset (dropping removed/deleted comments).
- `resolve_links()`: Uses regex (`REDDIT_PERMALINK_REGEX`) to identify links to other Reddit posts. If the target post exists in the `DatabaseManager`, it replaces the URL with an internal Obsidian link format (`[[Subreddit_ID]]`).
- `parse_frontmatter()`: Reads existing `.md` files on disk to support the State Reconciliation Flow.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/architecture.md` (Block #9)
**Original:**
```markdown
### D. DatabaseManager (State Tracking)
Acts as the high-speed SQLite cache (`database.db`).
- Tracks: `id`, `title`, `author`, `source`, `label`, `score`, `post_timestamp`, `file_path`, and `rescrape_after`.
- Controls the footprint limit using `db_limit`, deleting the oldest unneeded records automatically.
- Facilitates the "State Reconciliation Flow" on startup by comparing DB records against the physical `.md` files.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #1)
**Original:**
```markdown
# reddit2md: The Reddit to Markdown collectionor
reddit2md is a professional-grade Reddit scraper designed for high-signal knowledge management. It transforms transient Reddit discussions into permanent, well-structured Markdown notes for use in Obsidian vaults, AI-automated workflows, and personalized knowledge collections.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #2)
**Original:**
```markdown
Whether you are building a research database, feeding an AI agent, or just keeping up with specific subreddits, reddit2md provides the granularity and control needed for a high-quality data pipeline. It requires no external Python libraries, relying entirely on the Python standard library for maximum portability and security.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #4)
**Original:**
```markdown
## 1. Installation & Quick Start
To get started, clone the repository to your local machine. Since reddit2md uses only the Python standard library, you do not need to install any external packages. Simply run python reddit2md.py in your terminal. On the first run, if no config.yml is found, the program will create a template for you. You can then edit this file to add your preferred subreddits and customize your settings.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #11)
**Original:**
```markdown
### Using the Command Line Interface
The CLI is the most common way to use reddit2md. You can run all configured scrape tasks by calling the script with no arguments. To scrape a specific subreddit on the fly (even if it is not in your config), use the --source argument followed by the subreddit name. For example:
```bash
python reddit2md.py --source news --max-results 5 --detail XL --sort top --min-age-hours 24
```
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #12)
**Original:**
```markdown
### Using as a Python Dependency
You can import the RedditScraper class into your own projects. This is ideal for building custom AI agents that need fresh Reddit data.
```python
from reddit2md import RedditScraper
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #14)
**Original:**
```markdown
### Using the Configuration File
The config.yml file allows you to set global defaults and then define a list of specific tasks in the routine. This is the best way to manage a large list of scrape tasks for a knowledge collection. Note that you can have multiple tasks for the same subreddit with different settings.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #22)
**Original:**
```markdown
### Context vs. Freshness: The Maturity Logic
Scraping a thread the moment it is posted often misses the best discussion. reddit2md uses the min_age_hours setting to solve this. If a post is young, it is scraped immediately for freshness, but marked as Maturing. The system then automatically returns after the age threshold is met to append the final, mature conversation. Note: If you do not care about post maturity and want every scrape to be final, simply set min_age_hours to 0. This disables all re-scraping logic.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #43)
**Original:**
```markdown
### Minimum Post Age Hours
Description: The window of time a post must exist before it is considered mature. Set to 0 to disable re-scraping logic entirely.
- Config: "min_age_hours": 12
- CLI: --min-age-hours 12
- Python: 'min_age_hours': 12
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #48)
**Original:**
```markdown
## 8. Directory Structure and Files
reddit2md organizes its data into three main components. The markdown folder contains the notes you see in your live directory (ie. Obsidian). The json folder inside the data directory contains the structured data used by the system and AI agents. The database.db file inside the data directory acts as the high-speed index. Finally, the Scrape Log.md file provides a more human-readable record showing the status of every post, including which ones are currently maturing and when they are scheduled for their final re-scrape.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/web2md/architecture.md` (Block #3)
**Original:**
```markdown
## 1. Objective
To build a "Universal Fallback" Tier 3 Utility Scraper that transforms any generic webpage into clean, high-signal Markdown. It specializes in noise removal (ads, navbars, banners) to provide LLM-ready content for RAG.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/web2md/architecture.md` (Block #6)
**Original:**
```markdown
### A. Config (Settings Management)
- `engine` (Enum: trafilatura, crawl4ai): Choice of extraction logic.
- `include_images` (Boolean): Whether to include image links in the Markdown.
- `include_links` (Boolean): Whether to preserve internal/external links.
- `md_output_directory`, `data_output_directory`, `debug` (Sandman Standard).
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/web2md/architecture.md` (Block #7)
**Original:**
```markdown
### B. Client (Network Operations)
- **Primary:** `TrafilaturaClient` uses `trafilatura.fetch_url()` and `extract()`.
- **Secondary:** `Crawl4AIClient` manages the Playwright context and `fit_markdown` logic.
- **Discovery:** Automatic detection of article metadata and JSON-LD if available.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/web2md/architecture.md` (Block #8)
**Original:**
```markdown
### C. Processor (Translation)
Translates the extracted content into the Sandman Standard Schema.
- Sanitizes filenames based on the Page Title or URL slug.
- Extracts `metadata_label` from site categories or tags.
- Maps `Author` to `author` and `Title` to `title`.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/web2md/architecture.md` (Block #9)
**Original:**
```markdown
### D. DatabaseManager (State Tracking)
- Acts as a lightweight SQLite cache to prevent redundant scraping of the same URL.
- Tracks `url`, `title`, `last_scraped`, and `file_path`.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/web2md/architecture.md` (Block #12)
**Original:**
```markdown
- `post_id` -> Hashed URL.
- `title` -> Page Title.
- `author` -> Site Name / Author Name.
- `content` -> Cleaned Markdown Body.
- `time_scraped` -> Current timestamp.
- `time_posted` -> Article publication date (if available).
- `metadata_label` -> Site Category / Tag.
- `module` -> Set to `"web2md"`.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/web2md/README.md` (Block #2)
**Original:**
```markdown
web2md is the "Universal Fallback" module of the Sandman suite. It is a Tier 3 Utility Scraper designed to turn any generic HTML webpage into clean, high-signal Markdown.
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

## File: `data/Scrape Log.md` (Block #2)
**Original:**
```markdown
| Status | Label | Title | Score | Sort | Post Date | Last Scrape | Re-scrape After |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ⏳ *Maturing* | N/A | [[news_1roppv5.md|Huge fire in Scotland triggers train chaos as historic building collapses | CNN]] | 5 | N/A | 2026-03-09 03:44 | 2026-03-08 23:49 | 2026-03-09 15:44 |
| ✅ | Speculation | [[LeaksAndRumors_1rm9x1x.md|I have stitched together every single rumor/leak and 199% figured out how the Avengers v X men conflict escalates]] | 80 | new | 2026-03-06 09:57 | 2026-03-08 23:49 | - |
| ✅ | Rumor | [[LeaksAndRumors_1rmxnnn.md|Insider Cryptic HD QUALITY (@Cryptic4KQual) is teasing that the Moana Live-Action official trailer will be released very soon (swipe the images)]] | 81 | new | 2026-03-07 02:20 | 2026-03-08 23:49 | - |
| ✅ | Confirmed | [[LeaksAndRumors_1rncspg.md|Set construction progress of whatever project Adam Driver is signed on for]] | 79 | new | 2026-03-07 15:30 | 2026-03-08 23:49 | - |
| ✅ | Cast/crew | [[MarvelStudiosSpoilers_1rms4u7.md|Mike Colter: "Its been 10 years since Luke Cage premiered [this Fall] [and 10 years] since Jessica Jones. I do think it's time, now that Daredevil is back, I've had discussions with Marvel and I do think that it is very likely that I will come back at some point"]] | 411 | new | 2026-03-06 22:22 | 2026-03-08 23:49 | - |
| ✅ | Doomsday | [[MarvelStudiosSpoilers_1rn3vzs.md|John Campea says Robert Downey Jr’s face as Doctor Doom is not revealed in Doomsday (14:30 to ~15:00 relevant timestamp)]] | 235 | new | 2026-03-07 07:37 | 2026-03-08 23:49 | - |
| ⏳ *Maturing* | Daredevil | [[MarvelStudiosSpoilers_1rof2qu.md|Matt Murdock &amp; Karen Page "are pretty much the only other person that the other one has left" in DAREDEVIL: BORN AGAIN Season 2, says Deborah Ann Woll: "There's a dependence."]] | 160 | new | 2026-03-08 20:11 | 2026-03-08 23:49 | 2026-03-09 08:11 |
```

**AI Analysis:** Skipped (No client)

---

## File: `data/markdown/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1rn3vzs.md` (Block #9)
**Original:**
```markdown
Otherwise this is going to feel like a pointless (and expensive) publicity stunt that they did to reinvigorate the MCU. Which… yeah it is that, but it would be nice to have a story reason for a Downey Jr. Doom too.
	- ==**u/riegspsych325** (Score: 10)==
		it’s just a weird situation they put themselves in no matter how they approach it.  If Doom never takes off his mask and they make zero mention of Doom looking/sounding like Tony, audiences will feel bait&amp;switched.  If they *do* add a connection (variant, lookalike, forgotten identity etc), then comic book fans may feel that it dilutes Doom’s agency and characterization
```

**AI Analysis:** Skipped (No client)

---

## File: `data/markdown/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1rof2qu.md` (Block #1)
**Original:**
```markdown
# Matt Murdock &amp; Karen Page "are pretty much the only other person that the other one has left" in DAREDEVIL: BORN AGAIN Season 2, says Deborah Ann Woll: "There's a dependence."
```

**AI Analysis:** Skipped (No client)

---

## File: `data/markdown/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1rms4u7.md` (Block #1)
**Original:**
```markdown
# Mike Colter: "Its been 10 years since Luke Cage premiered [this Fall] [and 10 years] since Jessica Jones. I do think it's time, now that Daredevil is back, I've had discussions with Marvel and I do think that it is very likely that I will come back at some point"
```

**AI Analysis:** Skipped (No client)

---

## File: `data/markdown/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1rms4u7.md` (Block #4)
**Original:**
```markdown
- ==**u/Crunchandbunch** (Score: 123)==
	Sweet Christmas 
- ==**u/Rhubarb-Apprehensive** (Score: 105)==
	Is this Mike Colter guy a reliable source?
	- ==**u/FolkPunkResistance** (Score: 34)==
		He gets most things right regarding Luke Cage, but otherwise, I’m not sure he’s a regular leaker.
	- ==**u/MikeFatz** (Score: 14)==
		I saw a photo of him the other day and it had EVIL written across it in big red letters. I mean… can you really trust someone like that? 
- ==**u/Paperchampion23** (Score: 61)==
	Lol hes definitely just in Born Again and this is the most he can say at this point
	- ==**u/nottherealstanlee** (Score: 19)==
		Feels like that for sure lol wouldnt surprise me to see all of them back even if it's just a limited capacity. 
	- ==**u/Vladmerius** (Score: 3)==
		I've been wondering if the lack of marketing for born again season 2 is because Luke Cage and Danny Rand are both in it and it's sort of a Defenders story and they're trying to keep it secret as long as they can.
```

**AI Analysis:** Skipped (No client)

---

## File: `data/markdown/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1rms4u7.md` (Block #5)
**Original:**
```markdown
Funny enough they have acrually set up the comic book version of Civil War with this whole anti-vigilante plot. Kind of a shame that they're going to wrap it up by the end of season 2 instead of let it grow and expand into the wider MCU. 
- ==**u/ConstrictionsOFC** (Score: 32)==
	reunite him with claireee
	- ==**u/PCofSHIELD** (Score: 58)==
		![gif](giphy|xSx6Mrp04mf1S)
	- ==**u/esar24** (Score: 0)==
		Give claire back to matt so she can join his harem, Luke only belongs to jessica
- ==**u/Human-Win4703** (Score: 19)==
	I thought he might make a cameo at the very end of BA S2 but, it seems like he's not back yet.
	- ==**u/SacreFor3** (Score: 8)==
		S3 is a better bet tbh.
- ==**u/vaderfan1** (Score: 15)==
	I'm calling it now, he at least makes a cameo in Born Again. Hello to all the future redditors coming back to this comment because I was right!
- ==**u/takkenjong2** (Score: 8)==
	His Luke Cage was so great. I loved that bar scene.
- ==**u/TheMoorNextDoor** (Score: 4)==
	![gif](giphy|8nRxogx9tgvCzuSHLl|downsized)
```

**AI Analysis:** Skipped (No client)

---

## File: `data/markdown/LeaksAndRumors/LeaksAndRumors_1rmxnnn.md` (Block #1)
**Original:**
```markdown
# Insider Cryptic HD QUALITY (@Cryptic4KQual) is teasing that the Moana Live-Action official trailer will be released very soon (swipe the images)
```

**AI Analysis:** Skipped (No client)

---

