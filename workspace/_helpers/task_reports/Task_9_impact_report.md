---
task: Task_9
status: Pending Review
target_terms: [db_limit, max_records]
new_term: max_db_records
context: "This variable standardizes the parameter used across sandman and all modules to limit the SQLite database footprint. It enforces chronological pruning during the teardown phase to keep the row count under this limit."
date_generated: 2026-03-10 15:13:53
---

# Documentation Scrubbing Report for Task_9

> **Instructions**: Review the `AI Analysis` and `Proposed Rewrite` for each block below. If accurate, apply the rewrite to the source file.

---

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

**AI Analysis:** Skipped (No client)

---

## File: `tasks.md` (Block #43)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] Execute a global search and replace in the Python codebase: change `db_limit` (or similar variants) to `max_db_records`.
- [ ] Verify that all SQLite database pruning functions (`DELETE FROM ... WHERE id NOT IN (SELECT id ... LIMIT ?)`) in the `DatabaseManager` classes are strictly referencing `max_db_records` from the parsed configuration.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #46)
**Original:**
```markdown
**Code Change Strategy**:
- Search codebase for `db_limit` and replace with `max_db_records`. 
- Ensure the database cleanup logic (e.g., SQLite `DELETE FROM ... WHERE id NOT IN (SELECT id ... LIMIT max_db_records)`) explicitly uses this standardized key in all `DatabaseManager` classes.
```

**AI Analysis:** Skipped (No client)

---

## File: `nomenclature2.md` (Block #68)
**Original:**
```markdown
### AI Analysis & Updated Plan:
- **Understanding**: A formal process is required to ensure that whenever nomenclature standardizations are applied in the code, the Markdown documentation is scrubbed and synchronized to prevent legacy terminology drift.
- **Review**: We need a helper script to aggregate mentions of old terms across all docs, mapping them by file and line number to facilitate surgical replacements.
- **New Plan**: 
  - Create `workspace/_helpers/scrub_docs.py`.
  - This script will take a dictionary mapping old terms to new terms (e.g., `{'verbosity': 'verbose', 'source': 'sources', 'db_limit': 'max_db_records', 'queue': 'routine'}`).
  - It will recursively `grep` the `docs/` folder, `README.md`, and other relevant `.md` files.
  - It will output a systematic checklist (e.g., `_helpers/legacy_terms_report.md`) detailing exactly where the old nomenclature still exists, allowing us to surgically verify and execute the replacements.
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #1)
**Original:**
```markdown
---
task: Task_9
status: Pending Review
target_terms: [db_limit, max_records]
new_term: max_db_records
context: "This variable standardizes the parameter used across sandman and all modules to limit the SQLite database footprint. It enforces chronological pruning during the teardown phase to keep the row count under this limit."
date_generated: 2026-03-10 15:13:16
---
```

**AI Analysis:** Skipped (No client)

---

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

**AI Analysis:** Skipped (No client)

---

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

**AI Analysis:** Skipped (No client)

---

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

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #14)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #68)
**Original:**
```markdown
### AI Analysis & Updated Plan:
- **Understanding**: A formal process is required to ensure that whenever nomenclature standardizations are applied in the code, the Markdown documentation is scrubbed and synchronized to prevent legacy terminology drift.
- **Review**: We need a helper script to aggregate mentions of old terms across all docs, mapping them by file and line number to facilitate surgical replacements.
- **New Plan**: 
  - Create `workspace/_helpers/scrub_docs.py`.
  - This script will take a dictionary mapping old terms to new terms (e.g., `{'verbosity': 'verbose', 'source': 'sources', 'db_limit': 'max_db_records', 'queue': 'routine'}`).
  - It will recursively `grep` the `docs/` folder, `README.md`, and other relevant `.md` files.
  - It will output a systematic checklist (e.g., `_helpers/legacy_terms_report.md`) detailing exactly where the old nomenclature still exists, allowing us to surgically verify and execute the replacements.
```
```

**AI Analysis:** Skipped (No client)

---

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

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #20)
**Original:**
```markdown
## File: `docs/readme_nomenclature adjustments.md` (Block #14)
**Original:**
```markdown
Wrong:
```
### Maximum DB Records
Description: Footprint control for the SQLite cache. When the DB exceeds this limit, the oldest records are pruned (does not touch Markdown files).
- Config: "max_db_records": 1000
- CLI: --max-records 1000
- Python: 'max_db_records': 1000
```
correct:
```
### DB size Limit: db_limit
Description: Footprint control for the SQLite cache. When the DB exceeds this limit, the oldest records are pruned (does not touch Markdown files).
- Config: "db_limit": 1000
- CLI: --db_limit 1000
- Python: 'db_limit': 1000
```
### Reddit Sort Method
Description: Choice of sort determines the flavor of your research: new (Default) for real-time tracking, hot for discovery, top for historical quality, or rising for momentum.
- Config: "sort": "new"
- CLI: --sort new
- Python: 'sort': 'new'
```
```

**AI Analysis:** Skipped (No client)

---

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

**AI Analysis:** Skipped (No client)

---

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

**AI Analysis:** Skipped (No client)

---

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

**AI Analysis:** Skipped (No client)

---

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

**AI Analysis:** Skipped (No client)

---

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

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #38)
**Original:**
```markdown
## File: `modules/reddit2md/README.md` (Block #40)
**Original:**
```markdown
### Maximum DB Records
Description: Footprint control for the SQLite cache. When the DB exceeds this limit, the oldest records are pruned (does not touch Markdown files).
- Config: "db_limit": 1000
- CLI: --db-limit 1000
- Python: 'db_limit': 1000
```
```

**AI Analysis:** Skipped (No client)

---

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

**AI Analysis:** Skipped (No client)

---

## File: `docs/readme_nomenclature adjustments.md` (Block #14)
**Original:**
```markdown
Wrong:
```
### Maximum DB Records
Description: Footprint control for the SQLite cache. When the DB exceeds this limit, the oldest records are pruned (does not touch Markdown files).
- Config: "max_db_records": 1000
- CLI: --max-records 1000
- Python: 'max_db_records': 1000
```
correct:
```
### DB size Limit: db_limit
Description: Footprint control for the SQLite cache. When the DB exceeds this limit, the oldest records are pruned (does not touch Markdown files).
- Config: "db_limit": 1000
- CLI: --db_limit 1000
- Python: 'db_limit': 1000
```
### Reddit Sort Method
Description: Choice of sort determines the flavor of your research: new (Default) for real-time tracking, hot for discovery, top for historical quality, or rising for momentum.
- Config: "sort": "new"
- CLI: --sort new
- Python: 'sort': 'new'
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

## File: `modules/unified_module_blueprint.md` (Block #24)
**Original:**
```markdown
Scrapers must allow users to suppress side effects or limit footprints:
- save_json (Boolean): Whether to persist the sanitized JSON data after processing.
- md_log (Boolean): Whether to append the run results to the human-readable Markdown log.
- db_limit (Integer): Maximum number of records to keep in the SQLite index. Older records are pruned to keep the database size manageable.
- min_age_hours (Integer): Setting this to 0 must disable all maturity/re-scraping logic, making every scrape final.
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

## File: `modules/reddit2md/README.md` (Block #40)
**Original:**
```markdown
### Maximum DB Records
Description: Footprint control for the SQLite cache. When the DB exceeds this limit, the oldest records are pruned (does not touch Markdown files).
- Config: "db_limit": 1000
- CLI: --db-limit 1000
- Python: 'db_limit': 1000
```

**AI Analysis:** Skipped (No client)

---

