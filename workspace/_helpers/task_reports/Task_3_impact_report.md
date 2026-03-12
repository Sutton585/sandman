---
task: Task_3
status: Pending Review
target_terms: [offset, pagination]
new_term: offset
context: "Implementing an offset parameter across all modules to discard the first N items in a feed/query before starting the scrape."
date_generated: 2026-03-10 16:22:09
---

# Documentation Scrubbing Report for Task_3

> **Instructions**: Review the `AI Analysis` and `Proposed Rewrite` for each block below. If accurate, apply the rewrite to the source file.

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #28)
**Original:**
```markdown
## File: `tasks.md` (Block #18)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] The `offset` parameter (integer) is exposed in YAML configs and CLI parsers for all modules.
- [ ] **`jobs2md`**: Passes the `offset` value natively to JobSpy's `offset` parameter during the `scrape()` call.
- [ ] **`reddit2md`**: Implements standard Python list slicing (e.g., `rss_feed_items[offset:]`) to discard the first N items in the parsed RSS feed before initiating JSON fetch requests.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #64)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #15)
**Original:**
```markdown
**Investigation & Guidance:**
- **JobSpy**: Supports a numeric `offset`. 
- **PRAW (Reddit)**: Uses cursor-based pagination (`after` and `before` IDs), not numeric offsets. To support a numeric `offset` in reddit2md, we would have to fetch `offset + max_results` and slice the array (discarding the first `N`). This is inefficient but standardizes the UX.
- **Code Change Strategy**: Add `offset` to all CLI parsers. In `jobs2md.py` `execute_task`, pass `offset` to `self.client.scrape`. In `reddit2md.py`, implement list slicing to skip the first `offset` items.
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

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #70)
**Original:**
```markdown
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #46)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #55)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #58)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #61)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #124)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #142)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #157)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #160)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #163)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #172)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #178)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #292)
**Original:**
```markdown
## File: `modules/unified_module_blueprint.md` (Block #19)
**Original:**
```markdown
1. Config (Settings Management): Handles the logic for merging `settings` with task-specific settings and applying CLI/Python overrides based on the Precedence Order. Validates parameter types.
2. Client (Network Operations): Strictly isolates API and network logic. Manages authentication, headers (e.g., browser-mimicking), rate limiting, and pagination. It should return raw or semi-raw data.
3. Processor (Data Sanitization & Translation): The pure data translation layer. It takes the messy API response from the Client and strictly maps it to the "Standard Schema". It also handles the logic for internal Obsidian link resolution.
4. DatabaseManager (State Tracking): Manages the SQLite index. Responsible for cache pruning, maintaining the `rescrape_after` maturity logic, and executing the State Reconciliation Flow on startup.
5. Scraper / Orchestrator (The Execution Loop): The main entry point. Iterates through the routine queue, coordinates the Config, Client, Processor, and DatabaseManager, and ultimately writes the final Markdown and JSON files to the disk using a Theme Engine / Templates.
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

## File: `docs/nomenclature.md` (Block #39)
**Original:**
```markdown
- offset
  - Used for: Starting a search from a specific pagination index.
  - Confirmed consistent naming:
    - Sandman:    N/A
    - Job2md:     ✅
    - reddit2md:  ✅
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

