---
TO-AI: |
  This is a master coordination prompt for the Sandman Unified Nomenclature & YAML Initiative. 
  Your mission is to synchronize the codebases of Sandman, reddit2md, and jobs2md with the newly established documentation, nomenclature and config functionality and format standards.

FILE_MAP:
  sandman:
    - path: sandman.py
      action: Update config loader to strictly use YAML; rename 'jobs' list processing to 'routine'; ensure dispatch dictionary matches Universal Nomenclature.
    - path: config.yml
      action: Ensure structure follows 'settings' and 'routine' (using 'routine' as the key instead of 'jobs').
  
  reddit2md:
    - path: modules/reddit2md/reddit2md/core/config.py
      action: Swap json.load for yaml.safe_load; rename internal keys from 'jobs' to 'routine'.
    - path: modules/reddit2md/reddit2md/scraper.py
      action: Update the main execution loop to iterate over the 'routine' key; ensure all local variables match nomenclature.md.
    - path: modules/reddit2md/reddit2md.py
      action: Update CLI help text and arguments if any underscores survived the hyphenation initiative.
  
  jobs2md:
    - path: modules/jobs2md/core/config.py
      action: Swap json/yaml loading logic to be strictly YAML; implement the translation layer between Sandman Standard (e.g. 'source') and JobSpy (e.g. 'site_names').
    - path: modules/jobs2md/jobs2md.py
      action: Update the execution loop to process the 'routine' key; ensure the output mapping matches the Standard Markdown Schema.
    - path: modules/jobs2md/core/client.py
      action: Verify that Sandman Standard variables are correctly mapped to the JobSpy dependency.

ACCEPTANCE_CRITERIA:
  - No .json files are used for configuration.
  - The key 'jobs' does not appear in any config.yml or configuration-handling logic (replaced by 'routine').
  - 'sandman.py' can execute a full cycle of both reddit2md and jobs2md using only the root config.yml.
  - All Markdown front-matter generated uses the names defined in nomenclature.md (e.g., 'post_URL', 'poster', 'label').
  - Every change is verified by a successful execution run.

CONFIG Examples:
  - "sandman is the orchestrator of the modules. it uses the same language. the config files will follow the same patterns."
  - "notice how sandman can name each part of it's routine, and specify which module it is using to perform that part of it's routine. The language is universal, so the translation of these instructions into the module should be straight-forward."
  sandman config yaml file:
      settings:
        debug: false
        md_output_directory: "workspace/feeds/"
        json_output_directory: "workspace/data/log.md"
        data_output_directory: "sandman_config/data"
        group_by_source: true
        min_age_hours: 12
        max_results: 8
        md_log: true
      
      routine: # The routine: Executed in order when called
        - name: "regular MarvelStudiosSpoilers Updates"
          module: "reddit"
          source: "MarvelStudiosSpoilers"
          group_by_source: true

        - name: "regular Comic-related LeaksUpdates"
          module: "reddit"
          source: "LeaksAndRumors"
          limit: 3
          
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
      
      settings:
        debug: false
        md_output_directory: "workspace/feeds/reddit"
        json_output_directory: "workspace/data/log_reddit.md"
        data_output_directory: "sandman_config/data/reddit"
        group_by_source: true
        min_age_hours: 12
        max_results: 8
        md_log: true
      
      routine: # The routine: Executed in order when called
        - name: "regular MarvelStudiosSpoilers Updates"
          module: "reddit"
          source: "MarvelStudiosSpoilers"
          group_by_source: true

        - name: "regular Comic-related LeaksUpdates"
          module: "reddit"
          source: "LeaksAndRumors"
          limit: 3
      

---

# Progressive Execution Plan: Unified Nomenclature & YAML Sync

This document provides a rigorous, step-by-step path to move our codebase from "Draft Documentation" to "Live Functional Standard." Do not skip steps. Do not assume a task is done without running the script.

## Phase 1: The Core Orchestrator (Sandman)

1.  **Strict YAML Enforcement:** Update `sandman.py` to remove any fallback or legacy JSON loading. Use `yaml.safe_load`.
2.  **Terminology Migration:** In `sandman.py`, rename the variable `jobs` to `routine`. Update the config parsing logic to look for the `routine:` key in `config.yml`.
3.  **Path Verification:** Ensure `sandman.py` looks for `config.yml` in the project root by default.

## Phase 2: Tier 1 Synchronization (reddit2md)

1.  **Config Class Refactor:** Modify `modules/reddit2md/reddit2md/core/config.py` to use YAML. 
    - Ensure it correctly merges `settings` with the tasks defined in the `routine`.
2.  **Scraper Loop Refactor:** Update `modules/reddit2md/reddit2md/scraper.py`.
    - Change `self.config_manager.get_jobs()` to `self.config_manager.get_routine()`.
    - Ensure the loop `for task in routine:` is used throughout.
3.  **Nomenclature Audit:** Check `processor.py` one last time to ensure the keys it writes to Markdown perfectly match the "Front-Matter Schema" in `nomenclature.md`.

## Phase 3: Tier 2 Synchronization (jobs2md)

1.  **Nomenclature Translation Layer:** This is the most critical task. Update `modules/jobs2md/core/config.py` to translate:
    - `source` -> `site_names`
    - `query` -> `search_term`
    - `max_results` -> `results_wanted`
    - This allows the user to write "Standard Sandman" in the config, while the module handles the "Legacy JobSpy" names internally.
2.  **YAML Integration:** Ensure `jobs2md` no longer looks for a `.json` file.
3.  **Routine Loop:** Update `jobs2md.py` to iterate through the `routine` key.

## Phase 4: Validation & Lazy-Proofing

1.  **The "Empty Call" Test:** Run `python3 sandman.py` with no arguments.
    - **Pass Condition:** It successfully executes all tasks in the `routine` section of the root `config.yml`.
    - **Pass Condition:** reddit2md creates files with the correct front-matter.
    - **Pass Condition:** jobs2md creates files with the correct front-matter.
2.  **The "Manual Override" Test:** Run `python3 modules/reddit2md/reddit2md.py --source news --max-results 1`.
    - **Pass Condition:** The CLI arguments still work and override the `config.yml` correctly.
3.  **Blueprint Check:** Open `modules/unified_module_blueprint.md`. If you encountered a weird edge case or needed a new variable during this refactor, **add it to the blueprint now.** Do not let the documentation rot.

## Verification Checklist for Agents
- [ ] Did you rename `jobs` to `routine` in the code?
- [ ] Did you rename `config.json` references to `config.yml` in the code?
- [ ] Did you run the code to see if it actually works?
- [ ] Does the generated Markdown front-matter match `nomenclature.md` exactly?
- [ ] Is `yaml.safe_load` used instead of `json.load` for configs?
