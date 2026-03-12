---
task: Task_1
status: Pending Review
target_terms: [verbosity, detail]
new_term: verbose
context: "Standardizing logging and output control to use 'verbose' as an integer (0, 1, 2) instead of 'verbosity'."
date_generated: 2026-03-10 15:23:32
---

# Documentation Scrubbing Report for Task_1

> **Instructions**: Review the `AI Analysis` and `Proposed Rewrite` for each block below. If accurate, apply the rewrite to the source file.

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

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #13)
**Original:**
```markdown
## File: `README.md` (Block #16)
**Original:**
```markdown
1.  **Project Overview:** Start with this `README.md` to understand the high-level vision and the "Orchestrator" deployment model.
2.  **Global Standards:** Read the [Unified Module Blueprint](modules/unified_module_blueprint.md). This document defines the mandatory architectural rules (The "5 Buckets"), schema baselines, and cross-module communication protocols shared by all scrapers.
3.  **Module Registry:** Review the `modules/` directory. Each subdirectory (e.g., `jobs2md`, `gmail2md`) is an independent GitHub repository with its own isolated virtual environment.
4.  **Specific Module Context:** Once you've identified a module to work on, read its local `README.md` and its `architecture.md` file. These documents detail the platform-specific strategies, unique metadata fields, and implementation progress for that specific scraper.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #19)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #52)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #55)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #88)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #28)
**Original:**
```markdown
### Human input:
- Reddit2md doesn't do anything like that. the "author" variable in reddit is limited to markdown output, not any particular user-facing parameter, as far as I am aware.
- Jobspy (i believe) allows us to querie by "author" or employer or whatever, so it COULD be a useful parameter to use in config files or python or CLI calls. "show me jobs posted by this employer". I'm still not sure if that's really how it works. but if we can run queries like that, then this parameter needs to be user-facing to some extent to allow for the detail to be used in their queries. 
  - If the employer returns `company` or `employerID` or something similar, we can just call it `employer: ` in the front-matter, but i still don't have clarity on the exact variable. I want to know how i'd use it in jobspy queries. empoloyer ID? company?
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #109)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #62)
**Original:**
```markdown
How we can use this for job2md:
When we are scraping from a source (linkedin) that doesn't give full details by default, then we can use the detail field. In reddit, it's something like XS, SM, MD, LG, and XL. for jobs2md it can just be a boolean. default value is false. if we run a scrape on linkedin where we need the full details, we just specify detail: true.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #112)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #115)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #65)
**Original:**
```markdown
### Human input:
don't touch detail in reddit2md. we are just establishing that in jobs2md it happens to be a boolean. No changes needed to reddit2md regarding this.
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

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #160)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #163)
**Original:**
```markdown
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

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #214)
**Original:**
```markdown
## File: `docs/nomenclature.md` (Block #45)
**Original:**
```markdown
- fetch_full_description
  * Used for: Fetching complete descriptions when not provided by default feeds.
  * Maps to JobSpy: linkedin_fetch_description
  This should all be in job2md concerns. What level of detail is returned by default? if not complete, we need to support the variable `detail` just like reddit2md. Does it depend on source? linkedIn doesn't give full detail by defualt. need to learn more here.
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

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #298)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #325)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #13)
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

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #28)
**Original:**
```markdown
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

## File: `workspace/feeds/reddit/MarvelStudiosSpoilers/MarvelStudiosSpoilers_1roulqx.md` (Block #24)
**Original:**
```markdown
- ==**u/Radiant-Debt-2533** (Score: 3)==
		That's what they should do with Champions.
	- ==**u/Fall_False** (Score: 2)==
		I wouldn't be shocked if in the future, we see the Disney+ slate being more a balance of live-action and animated content.
	- ==**u/Thevamps555** (Score: 2)==
		It’s also why they didn’t get a season 2 because of CGI costs, the actress even said this herself lol
- ==**u/sidmis** (Score: 10)==
	Can someone do black magic on john Campea and make him leak the entire Doomsday plot detail by detail 
- ==**u/chimichanga_3** (Score: 9)==
	https://nitter.net/Gabeb890/status/2030751517616324785#m
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

## File: `docs/readme_nomenclature adjustments.md` (Block #4)
**Original:**
```markdown
Wrong:
```
scraper.run(subreddit_name="MarvelComics", overrides={'post_limit': 5, 'comment_detail': 'XL'})
```
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/readme_nomenclature adjustments.md` (Block #5)
**Original:**
```markdown
Correct:
```
scraper.run(subreddit_name="MarvelComics", overrides={'max_results': 5, 'detail': 'XL'})
```
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/readme_nomenclature adjustments.md` (Block #6)
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

## File: `docs/readme_nomenclature adjustments.md` (Block #7)
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

## File: `docs/readme_nomenclature adjustments.md` (Block #9)
**Original:**
```markdown
correct:
```
### max_results
Description: The maximum number of new posts reddit2md will attempt to fetch from a subreddit (source) during a single run.
- Config: "max_results": 8
- CLI: --max_results 8
- Python: 'max_results': 8
```
wrong:
```
### Comment Detail Presets
Description: Presets to control the exact volume and depth of comments captured. 
- XS: Top 3 top-level comments, 0 replies (Literal: 3 total).
- SM: Top 5 top-level comments, 1 reply each (Literal: 5 + 5 = 10 max).
- MD (Default): Top 8 top-level comments, 2 replies each (Literal: 8 + 16 = 24 max).
- LG: Top 10 top-level comments, 3 depth (3 replies, 1 sub-reply) (Literal: 10 + 30 + 30 = 70 max).
- XL: No limits. Recursively captures every single comment and reply.
	- Config: "comment_detail": "MD"
	- CLI: --detail MD
	- Python: 'comment_detail': 'MD'
```
correct:
```
### Comment Detail Presets
Description: Presets to control the exact volume and depth of comments captured. 
- XS: Top 3 top-level comments, 0 replies (Literal: 3 total).
- SM: Top 5 top-level comments, 1 reply each (Literal: 5 + 5 = 10 max).
- MD (Default): Top 8 top-level comments, 2 replies each (Literal: 8 + 16 = 24 max).
- LG: Top 10 top-level comments, 3 depth (3 replies, 1 sub-reply) (Literal: 10 + 30 + 30 = 70 max).
- XL: No limits. Recursively captures every single comment and reply.
	- Config: "detail": "MD"
	- CLI: --detail MD
	- Python: 'detail': 'MD'
```
Wrong:
```
### Flair
Description: Categorizes the post based on its source metadata.
- Config: "flair": "Value"
- CLI: --flair Value
- Python: 'flair': 'Value'
```
Correct:
```
### Flair and Labels
Description: Categorizes the post based on its the reddit flair.
- Config: "label": "Value"
- CLI: --label Value
- Python: 'label': 'Value'
```
Wrong:
```
### Post Link
Description: Metadata field for links to external URLs or internal Obsidian links to related scraped posts. The first link will always be the primary link of the reddit post itself.
- Config: "post_link": "URL"
- CLI: --post-link URL
- Python: 'post_link': 'URL'
```
correct:
```
### post_links
Description: Metadata field for links to external URLs. The first link will always be the primary link of the reddit post itself.
- Config: "post_links": "URL"
- CLI: --post-links URL
- Python: 'post_links': 'URL'
```
### Save JSON
Description: Whether the sanitized JSON data fetched from Reddit is persisted to your data directory after the Markdown note is generated.
- Config: "save_json": true
- CLI: --save-json [True/False]
- Python: 'save_json': True
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #34)
**Original:**
```markdown
- detail
  - Used for: Controls the detail level of logging and data capture.
  - Confirmed consistent naming:
    - Job2md:     ? (unsure what level of control we have of our output)
    - reddit2md:  ✅
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #42)
**Original:**
```markdown
- fetch_full_description
  * Used for: Fetching complete descriptions when not provided by default feeds.
  * Maps to JobSpy: linkedin_fetch_description
  This should all be in job2md concerns. What level of detail is returned by default? if not complete, we need to support the variable `detail` just like reddit2md. Does it depend on source? linkedIn doesn't give full detail by defualt. need to learn more here.
```

**AI Analysis:** Skipped (No client)

---

## File: `docs/nomenclature.md` (Block #59)
**Original:**
```markdown
1.  **Settings (`settings`)**: This section establishes the baseline parameters for any execution (such as output directories, default logging verbosity, and standard timeouts).
2.  **Routine (`routine`)**: This section defines an ordered list of specific tasks to execute when the module is run without arguments.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #12)
**Original:**
```markdown
Used for persistent, automated, persistent setups. It must contain:
-  Settings (`settings`): This section establishes the baseline parameters for any execution (such as output directories, default logging verbosity, and standard timeouts).
-  Routine (`routine`): This section defines an ordered list of specific tasks to execute when the module is run without arguments.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #14)
**Original:**
```markdown
### B. The Command Line Interface (CLI)
Used for ad-hoc exploration, testing, and terminal-based automation (like recurring schedules).
- Must support targeting a specific origin entity (e.g., --target news) for one-off scrape tasks of entities not in the config.
- Must support explicit, typed overrides for every single parameter (e.g., --max-results 5, --detail XL, --save-json False).
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #32)
**Original:**
```markdown
### Layer 3: Markdown Notes (The Final Product)
- Path: md_output_directory/
- Purpose: The human-readable and LLM-parsable final output.
- Function: As detailed in the Core Philosophy, these are living documents that dictate state back to the SQLite cache during reconciliation.
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

## File: `modules/reddit2md/README.md` (Block #13)
**Original:**
```markdown
scraper = RedditScraper(config_path="config.yml")
scraper.run(source="Python", overrides={'max_results': 5, 'detail': 'XL'})
```
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #16)
**Original:**
```markdown
routine:
  - source: "MarvelComics"
    sort: "top"
  - source: "MarvelComics"
    detail: "XL"
```
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #29)
**Original:**
```markdown
### Typical Workflow Example
1. Test: Set "debug": true in your config. Experiment with new subreddits or detail settings. Verify the results in the local /data/markdown/ directory.
2. Deploy: Once satisfied, set "debug": false and point your md_output_directory to the live directory, (ie. your Obsidian Vault). All future runs will now populate your vault with beautifully formatted notes organized by subreddit.
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/reddit2md/README.md` (Block #35)
**Original:**
```markdown
### Comment Detail Presets
Description: Presets to control the exact volume and depth of comments captured. 
- XS: Top 3 top-level comments, 0 replies (Literal: 3 total).
- SM: Top 5 top-level comments, 1 reply each (Literal: 5 + 5 = 10 max).
- MD (Default): Top 8 top-level comments, 2 replies each (Literal: 8 + 16 = 24 max).
- LG: Top 10 top-level comments, 3 depth (3 replies, 1 sub-reply) (Literal: 10 + 30 + 30 = 70 max).
- XL: No limits. Recursively captures every single comment and reply.
- Config: "detail": "MD"
- CLI: --detail MD
- Python: 'detail': 'MD'
```

**AI Analysis:** Skipped (No client)

---

