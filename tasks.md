# Nomenclature Standardization Strategy & Action Plan

This document organizes the approach for addressing the nomenclature and standardization concerns raised in `docs/nomenclature.md`. It translates architectural decisions into concrete development tasks with clear acceptance criteria.

---

## Task 0: AI-Assisted Documentation & Functionality Scrubbing Utility
**Context Reference**: `nomenclature2.md` -> `## 12. NEW TASK: Documentation Scrubbing Protocol`

**Objective**: Create a Python utility designed specifically to be executed by the AI Agent *prior* to or *during* each standardization task. This script leverages the Gemini API to not only find outdated nomenclature but intelligently rewrite documentation to reflect the *new* functionality and variables.

**Acceptance Criteria:**
- [x] Create `workspace/_helpers/ai_doc_scrubber.py`. (Completed)
- [x] **Inputs**: The script takes a `--task-id` (e.g. "Task_7"), `--target-terms` (comma-separated list of old variable names), `--new-term` (the standardized variable name), and `--context` (a string describing how the logic/functionality has changed).
- [x] **Output Organization**: The script must generate a separate markdown report for *each task*, saving them to a dedicated directory: `workspace/_helpers/task_reports/{task_id}_impact_report.md`.
- [x] **Report Front-Matter**: The generated report must include markdown front-matter outlining the `task`, `status`, `target_terms`, `new_term`, and `context` so the user and AI can immediately grasp the scope of the report.
- [x] **Phase 1 (Extraction)**: The script searches all `.md` files (ignoring `venv`, `.git`) for the `target_terms`. For each match, it extracts the file path, line number (or block ID), and a generous chunk of surrounding text (context).
- [x] **Phase 2 (LLM Evaluation & Rewrite)**: For each extracted chunk, the script calls the Gemini API. It prompts the LLM to evaluate if the text is inaccurate, and if so, propose a rewrite.
- [x] **Phase 3 (Report Generation)**: The script outputs the structured markdown report with the original text and the AI's proposed rewrite.
- [ ] **Workflow integration**: Before starting any of the below tasks (1-11), the AI Agent will run this script, present the `task_reports/{task_id}_impact_report.md` for human review, and then systematically apply the approved rewrites.
- [ ] **Mandatory Definition Injection**: *After* applying rewrites, the AI Agent must explicitly append a new explanatory section for the standardized term (detailing its usage across Config, CLI, and Python) into the following 4 core files:
  1. `README.md` (Root/Sandman)
  2. `modules/unified_module_blueprint.md`
  3. `modules/jobs2md/README.md`
  4. `modules/reddit2md/README.md`
- [ ] **Trilateral Testing Mandate**: *Before* completing any task, the AI Agent must write a brief, ad-hoc python test script to definitively prove that the new variable/functionality behaves perfectly across all 3 input interfaces (CLI flag, YAML config, and Python dictionary override) in both Sandman and the affected modules. No task is complete without this verifiable proof.

---

## Task 1: Unify Verbosity Terminology
**Context Reference**: `nomenclature2.md` -> `## 1. Verbosity (verbose / verbocity / detail)`

**Objective**: Standardize all logging/output control to use the key `verbose` universally across all modules, completely deprecating `verbosity`.

**Acceptance Criteria:**
- [x] `core/config.py` in `jobs2md`, `reddit2md`, and Sandman orchestrator parse `verbose` as an integer (0, 1, 2) from YAML.
- [x] All CLI argument parsers (`argparse`) use `--verbose` and store the result in `args.verbose`.
- [x] Any existing references to `verbosity` in configuration parsers or Python logic are removed or aliased to throw a deprecation warning while falling back to `verbose`.
- [x] `jobs2md`: Passes `verbose` directly into JobSpy's configuration.
- [x] `reddit2md`: Implements `logging.getLogger().setLevel()` based on the `verbose` integer (0: ERROR, 1: WARNING, 2: INFO/DEBUG).

---

## Task 2: Implement Strict Age Restrictions
**Context Reference**: `nomenclature2.md` -> `## 2. Age Restrictions (min_age_hours & max_age_hours)`

**Objective**: Ensure full parity for `min_age_hours` and `max_age_hours` in both `jobs2md` and `reddit2md`.

**Acceptance Criteria:**
- [x] **`jobs2md`**: Maps `max_age_hours` to JobSpy's native `hours_old` parameter.
- [x] **`jobs2md`**: Implements post-scrape filtering on the resulting pandas DataFrame to drop any jobs that are younger than `min_age_hours`.
- [x] **`reddit2md`**: Continues to use `min_age_hours` to queue posts for future rescrapes via `rescrape_after`.
- [x] **`reddit2md`**: Implements a check against `created_utc` during iteration. If a post's age exceeds `max_age_hours`, it is immediately discarded/skipped.

---

## Task 3: Standardize Pagination via Offset
**Context Reference**: `nomenclature2.md` -> `## 3. Pagination & Offset (offset)`

**Objective**: Support skipping initial results across all modules using the `offset` parameter.

**Acceptance Criteria:**
- [x] The `offset` parameter (integer) is exposed in YAML configs and CLI parsers for all modules.
- [x] **`jobs2md`**: Passes the `offset` value natively to JobSpy's `offset` parameter during the `scrape()` call.
- [x] **`reddit2md`**: Implements standard Python list slicing (e.g., `rss_feed_items[offset:]`) to discard the first N items in the parsed RSS feed before initiating JSON fetch requests.

---

## Task 4: Clarify Sorting Mechanics
**Context Reference**: `nomenclature2.md` -> `## 4. Sorting (sort)`

**Objective**: Prevent false promises regarding job board sorting capabilities.

**Acceptance Criteria:**
- [x] Remove any backend implementation attempts to force `sort` into `jobs2md`, as it is unsupported by JobSpy.
- [x] Ensure `reddit2md` continues to support `sort` natively via PRAW/RSS paths.
- [x] Update `nomenclature.md` to explicitly document that `sort` is a `reddit2md`-only parameter, and `jobs2md` relies on the target site's default relevance algorithms.

---

## Task 5: Domain-Specific "Creator" Metadata
**Context Reference**: `nomenclature2.md` -> `## 5. Author/Poster Entity (author)`

**Objective**: Ensure the Markdown front-matter intuitively reflects the domain of the scraped data rather than forcing a universal key.

**Acceptance Criteria:**
- [ ] **`reddit2md`**: Continues to output the posting user under the key `author: `.
- [ ] **`jobs2md`**: Outputs the posting company under the key `employer: ` (mapped from JobSpy's `company` output).
- [ ] **`jobs2md`**: Verify if JobSpy returns a specific Company/Employer ID. If so, expose an `employer_id` parameter in the config/CLI allowing users to query jobs posted strictly by that specific ID. Ensure this behavior is documented. Attempt coherent naming with the rest of the project, as seen in nomenclature.md.

---

## Task 6: List-Based Categorization
**Context Reference**: `nomenclature2.md` -> `## 6. Categorization (category / label / flair)`

**Objective**: Prevent string concatenation in front-matter and utilize native YAML lists for granular categorization.

**Acceptance Criteria:**
- [ ] **`reddit2md`**: Continues mapping `link_flair_text` directly to `category: `.
- [ ] **`jobs2md`**: Does *not* generate a `category` key. 
- [ ] **`jobs2md`**: Generates a YAML list for `employment_type: ` (e.g., `[Full-time, Contract]`) mapped from JobSpy.
- [ ] **`jobs2md`**: Generates a YAML list for `workplace: ` (e.g., `[Remote, In-office, Hybrid]`) mapped from JobSpy's location/remote flags.

---

## Task 7: Universal "Source" and "Sources" Support
**Context Reference**: `nomenclature2.md` -> `## 7. Targeting Sources (source vs sources)`

**Objective**: Unify the configuration and execution layers to universally support both `source` (string) and `sources` (list) across Sandman, `jobs2md`, and `reddit2md`. This avoids breaking legacy configs while elegantly scaling multi-target routines.

**Implementation Plan & Investigation:**
- **Configuration Parsing (`core/config.py` in all modules):** When the `settings` or `routine` YAML block is parsed, the Config manager should act as a normalizer. If a routine block contains `sources: ["A", "B"]`, the config manager should dynamically duplicate that routine into two discrete jobs in the runtime queue—one for `source: A` and one for `source: B`. The underlying execution loop then remains oblivious; it simply processes a list of single-source jobs. 
- **CLI & Python kwargs:** 
  - *CLI*: Add `add_mutually_exclusive_group()` or alias logic in `argparse` to allow both `--source` and `--sources`. If a user passes `--sources A,B`, `argparse` splits it into a list. The initialization logic then iterates over this list, functionally queueing multiple single-source runs.
  - *Python calls*: Standardize the class constructors (e.g., `Scraper(source="A")` and `Scraper(sources=["A", "B"])`). The init method will intercept either argument, normalize it into an iterable list of sources, and process them sequentially.
- **Development Effort**: Low/Medium. It requires centralizing the normalization logic within the shared architecture blueprint (`core/config.py` and `argparse` setup) and replicating that standard across Sandman, `jobs2md`, and `reddit2md`.

**Acceptance Criteria:**
- [ ] **Configuration Expansion**: Update YAML parsing in Sandman, `jobs2md`, and `reddit2md` so that a single routine containing a `sources` list is automatically unrolled into multiple single-source jobs within the execution queue.
- [ ] **CLI Support**: Update `argparse` in all three projects to accept both `--source` and `--sources` flags seamlessly, routing them to the same normalization logic.
- [ ] **Python API**: Ensure the main orchestrator classes in all three projects gracefully accept both `source` (str) and `sources` (list) keyword arguments without failing.
- [ ] **Consistent Execution**: Confirm that `jobs2md`, `reddit2md`, and Sandman utilize the exact same underlying logic pattern to handle the expansion of sources, keeping the architecture unified.

---

## Task 8: Implicit CLI Routine Execution
**Context Reference**: `nomenclature2.md` -> `## 8. Naming Routines (name)`

**Objective**: Enable executing specific YAML routines cleanly via implicit positional CLI arguments.

**Acceptance Criteria:**
- [ ] Sandman and Module YAML parsers are updated to support the `routine` block as a dictionary of named keys (e.g., `routine: \n  my_job: \n    sources: [...]`).
- [ ] Update all `argparse` setups to accept an optional positional string argument (e.g., `args.routine_name`).
- [ ] If `routine_name` is provided (e.g., `python3 reddit2md "daily_news"`), the script searches the config's `routine` dictionary for that exact key. 
  - If found, it executes *only* that routine block.
  - If not found, it exits with a user-friendly error message.
- [ ] If `routine_name` is omitted, the script iterates through all keys in the `routine` dictionary sequentially.

---

## Task 9: Enforce `max_db_records` Nomenclature
**Context Reference**: `nomenclature2.md` -> `## 9. Database Footprint (max_db_records)`

**Objective**: Standardize database footprint configuration terminology.

**Acceptance Criteria:**
- [ ] Execute a global search and replace in the Python codebase: change `db_limit` (or similar variants) to `max_db_records`.
- [ ] Verify that all SQLite database pruning functions (`DELETE FROM ... WHERE id NOT IN (SELECT id ... LIMIT ?)`) in the `DatabaseManager` classes are strictly referencing `max_db_records` from the parsed configuration.

---

## Task 10: Robust Output Path Sanitization
**Context Reference**: `nomenclature2.md` -> `## 10. Output Paths Standardization (md_log, md_output_directory)`

**Objective**: Infer user intent based on variable names and defensively correct invalid path extensions in the config parser.

**Acceptance Criteria:**
- [ ] Standardize the configuration keys to exactly: `output_md`, `output_json`, `output_db`, `output_md_log`.
- [ ] Implement a path sanitization function in `core.config.Config` that runs upon loading the YAML.
- [ ] **Directory Validation**: If `output_md` or `output_json` contains a file extension (e.g., ends in `.json`), convert the `.` to an `_`, append a trailing slash `/`, and log a warning that a directory was expected.
- [ ] **File Validation**: If `output_db` or `output_md_log` ends with the *wrong* extension (e.g., `output_md_log: path.json`), forcibly swap the extension to `.md` (or `.db`), and log a warning.

---

## Task 11: Two-Way Queue via `rescrape_after` in jobs2md
**Context Reference**: `nomenclature2.md` -> `## 11. Jobs2md Specifics (Descriptions, Country, etc.) & Rescrape Logic`

**Objective**: Utilize the Markdown front-matter to queue shallow job listings for deeper "hydration" scrapes later, mimicking Reddit2md's queue functionality.

**Acceptance Criteria:**
- [ ] **`jobs2md`**: Standardize `detail` as a boolean flag (default `false`). Do not alter `reddit2md`'s enum-based `detail` implementation.
- [ ] **`jobs2md`**: During front-matter generation, always inject the `rescrape_after: ` key.
- [ ] **`jobs2md`**: If `detail` is `false` during the scrape, leave `rescrape_after:` empty.
- [ ] **Orchestrator Logic**: Implement a pre-run scan in `jobs2md` that checks existing Markdown files in the output directory. If a file has a populated `rescrape_after` timestamp that is in the past:
  - Extract the job's URL.
  - Execute a targeted JobSpy scrape for that specific URL with `detail: true` (mapping to `linkedin_fetch_description: True`).
  - Overwrite/update the markdown file with the full description and clear the `rescrape_after` field.
---

## Task 13: Decouple Age Filtering from Maturity Logic
**Context Reference**: Human Input on Age Filtering Consistency

**Objective**: Ensure `min_age_hours` behaves identically across all modules as a hard filter (ignoring posts newer than the limit). Move the existing reddit2md "queue for rescrape if young" logic to a newly named parameter: `rescrape_threshold_hours`.

**Acceptance Criteria:**
- [x] Add `rescrape_threshold_hours` to the configuration, CLI (`--rescrape-threshold-hours`), and Python interfaces across Sandman and reddit2md.
- [x] Refactor `reddit2md`: Modify the scrape loop to use `min_age_hours` as a strict filter (like `max_age_hours`). If a post's age in hours is less than `min_age_hours`, it should be completely discarded.
- [x] Refactor `reddit2md`: Ensure the `rescrape_after` timestamp logic is now entirely driven by `rescrape_threshold_hours` instead of `min_age_hours`.
- [x] Update `nomenclature2.md` and standard documentation (Task 0 workflow) to reflect this architectural shift.
