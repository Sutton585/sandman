---
task: Task_4
status: Pending Review
target_terms: [sort, sorting]
new_term: sort
context: "Clarifying that the 'sort' parameter is exclusively supported by reddit2md (new, hot, top). jobs2md does not support sorting natively via JobSpy and relies on the default relevance sorting of the scraped platforms."
date_generated: 2026-03-10 16:37:56
---

# Documentation Scrubbing Report for Task_4

> **Instructions**: Review the `AI Analysis` and `Proposed Rewrite` for each block below. If accurate, apply the rewrite to the source file.

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #31)
**Original:**
```markdown
## File: `tasks.md` (Block #22)
**Original:**
```markdown
**Acceptance Criteria:**
- [ ] Remove any backend implementation attempts to force `sort` into `jobs2md`, as it is unsupported by JobSpy.
- [ ] Ensure `reddit2md` continues to support `sort` natively via PRAW/RSS paths.
- [ ] Update `nomenclature.md` to explicitly document that `sort` is a `reddit2md`-only parameter, and `jobs2md` relies on the target site's default relevance algorithms.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #73)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #20)
**Original:**
```markdown
**Investigation & Guidance:**
- Reddit inherently supports complex sorting (hot, new, top, controversial).
- Job boards generally only support "relevance" vs "date" sorting.
- **Action**: Investigate JobSpy's native parameters. If JobSpy has no explicit `sort` argument, it likely defaults to relevance/date depending on the provider. 
- **Code Change Strategy**: We can allow `sort: date` vs `sort: relevance` at the Sandman level. If JobSpy does not support this natively via arguments, we may need to sort the resulting pandas DataFrame ourselves by date if `sort: new` is passed to jobs2md.
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #76)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #21)
**Original:**
```markdown
### Human input:
Forget about the sanman level. Think only about jobspy. is there any parameter than changes the way the results are listed? for example "show most recent first" or "show best results first" or "show recommended first"? or is there no use for a sort parameter in this module?
```
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #79)
**Original:**
```markdown
## File: `nomenclature2.md` (Block #22)
**Original:**
```markdown
### AI Analysis & Updated Plan:
- **Understanding**: You want to know if JobSpy actually exposes a sorting parameter that dictates what the job boards return, or if trying to support `sort` in `jobs2md` is pointless.
- **Review**: JobSpy does *not* expose a dedicated `sort` parameter natively. It relies entirely on the default sorting of the underlying job boards being scraped (which is usually a black-box mix of relevance and date). Trying to shoehorn `sort` into `jobs2md` would create a false promise to the user.
- **New Plan**: Deprecate the concept of `sort` for `job2md`. It will be strictly a `reddit2md` parameter. The Sandman documentation will explicitly state that `jobs2md` relies on the provider's default relevance sorting algorithm.
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

## File: `workspace/_helpers/task_reports/Task_8_impact_report.md` (Block #208)
**Original:**
```markdown
## File: `docs/nomenclature.md` (Block #43)
**Original:**
```markdown
- sort
  * Used for: Sorting method for the platform feed.
  * Maps to JobSpy: N/A
  * Maps to reddit2md: sort (new, hot, top, rising)
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

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #16)
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

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #19)
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

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #22)
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

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #25)
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

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #28)
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

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #34)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #37)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #40)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #43)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #46)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #49)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #52)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #55)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #58)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #61)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #67)
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

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #70)
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

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #73)
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

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #76)
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

## File: `workspace/_helpers/task_reports/Task_3_impact_report.md` (Block #79)
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

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #34)
**Original:**
```markdown
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

## File: `workspace/_helpers/task_reports/Task_9_impact_report.md` (Block #58)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #73)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #166)
**Original:**
```markdown
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #181)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #184)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #187)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #193)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #196)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #202)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #238)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #241)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #244)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #310)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #337)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #385)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #406)
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

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #448)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_2_impact_report.md` (Block #460)
**Original:**
```markdown
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

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #37)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #40)
**Original:**
```markdown
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

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #91)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #94)
**Original:**
```markdown
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

## File: `workspace/_helpers/task_reports/Task_1_impact_report.md` (Block #145)
**Original:**
```markdown
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
```

**AI Analysis:** Skipped (No client)

---

## File: `workspace/feeds/log.md` (Block #2)
**Original:**
```markdown
| Status | Label | Title | Score | Sort | Post Date | Last Scrape | Re-scrape After |
| :| :| :| :| :| :| :| :|
| ⏳ *Maturing* | N/A | [[news_1rq6bcg.md|War expands to central Beirut as Israeli strike kills Iranians in luxury hotel]] | 235 | N/A | 2026-03-10 19:13 | 2026-03-10 16:28 | 2026-03-11 07:13 |
| ⏳ *Maturing* | N/A | [[test_1rq3k1k.md|Test test]] | 1 | N/A | 2026-03-10 17:36 | 2026-03-10 16:28 | 2026-03-11 05:36 |
| ⏳ *Maturing* | N/A | [[test_1rq3z0r.md|Real Time Sinking]] | 1 | N/A | 2026-03-10 17:51 | 2026-03-10 16:28 | 2026-03-11 05:51 |
| ⏳ *Maturing* | N/A | [[test_1rq445k.md|yo guys here to test]] | 1 | N/A | 2026-03-10 17:56 | 2026-03-10 16:28 | 2026-03-11 05:56 |
| ⏳ *Maturing* | N/A | [[test_1rq461l.md|Marketer tools harness test - 2026-03-10T17:58:24.495Z]] | 1 | N/A | 2026-03-10 17:58 | 2026-03-10 16:28 | 2026-03-11 05:58 |
| ⏳ *Maturing* | N/A | [[test_1rq4a45.md|Marketer tools harness test - 2026-03-10T18:02:05.446Z]] | 1 | N/A | 2026-03-10 18:02 | 2026-03-10 16:12 | 2026-03-11 06:02 |
| ⏳ *Maturing* | test | [[test_1rq4awd.md|test]] | 1 | N/A | 2026-03-10 18:02 | 2026-03-10 16:12 | 2026-03-11 06:02 |
| ⏳ *Maturing* | N/A | [[test_1rq59y1.md|Come Join LinkBlaze Testers Group On Discord!]] | 1 | N/A | 2026-03-10 18:36 | 2026-03-10 16:12 | 2026-03-11 06:36 |
| ⏳ *Maturing* | N/A | [[test_1rq6bhx.md|test]] | 1 | N/A | 2026-03-10 19:13 | 2026-03-10 16:12 | 2026-03-11 07:13 |
| ⏳ *Maturing* | N/A | [[test_1rq74wk.md|test]] | 1 | N/A | 2026-03-10 19:42 | 2026-03-10 16:12 | 2026-03-11 07:42 |
| ⏳ *Maturing* | N/A | [[test_1rq79va.md|Yilin's Reddit Post Title]] | 1 | N/A | 2026-03-10 19:47 | 2026-03-10 16:12 | 2026-03-11 07:47 |
| ⏳ *Maturing* | N/A | [[test_1rq7g2g.md|HELP!!! Urine sample sent to the lab]] | 1 | N/A | 2026-03-10 19:53 | 2026-03-10 16:12 | 2026-03-11 07:53 |
| ⏳ *Maturing* | N/A | [[test_1rq7vfj.md|Post Teste]] | 1 | N/A | 2026-03-10 20:08 | 2026-03-10 16:12 | 2026-03-11 08:08 |
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

## File: `docs/readme_nomenclature adjustments.md` (Block #11)
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

## File: `docs/nomenclature.md` (Block #40)
**Original:**
```markdown
- sort
  * Used for: Sorting method for the platform feed.
  * Maps to JobSpy: N/A
  * Maps to reddit2md: sort (new, hot, top, rising)
```

**AI Analysis:** Skipped (No client)

---

## File: `modules/unified_module_blueprint.md` (Block #42)
**Original:**
```markdown
### Automated Folder Organization
Modules must support a generate_folders (e.g., group_by_source) boolean toggle.
- True: Files are sorted into subdirectories based on their origin (e.g., md_output_directory/OriginEntity/File.md).
- False: All files are placed directly in the root of the md_output_directory.
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

## File: `modules/reddit2md/README.md` (Block #42)
**Original:**
```markdown
### Reddit Sort Method
Description: Choice of sort determines the flavor of your research: new (Default) for real-time tracking, hot for discovery, top for historical quality, or rising for momentum.
- Config: "sort": "new"
- CLI: --sort new
- Python: 'sort': 'new'
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

