---
title: "README"
type: primary_directive
ai_directive: |
  Enforce a leverage-first mindset, not resume-first. Disqualify prestige traps. Identify asymmetric opportunities for income stacking, automation, or acquisition. Recommend roles that the user would not typically find.
cross_reference: userProfile.md > skills_taxonomy, detailed_career_history
---
# README
This is a project that is first and foremost about finding work for the user. The user has become very disorganized, overwhelmed, and manual applications and searching for opportunities has become a slog. Automation and AI support are needed.

# Primary goal:
- job, or paying client

# Goal for AI:
- Develop AI SOPs and systems to automate and support the process

## Some important parts
- How can we quickly replace the appscript project and the notion project with some basic tracking in obsidian?
	- obsidian "bases" can track each job. markdown page for each, just like notion
	- need to script or simplify how user can translate a job posting from linkedin/indeed/other into markdown for it's page in obsidian
	- need to script clear instructions for AI agent. Evaluate this job against the user's experiences, preferences, and goals. How well does it fit existing skill set? future goals? is it able to be remotely stacked with others and mostly automated? Good exposure to potential future aquisition targets of boring but consistent businesses?
	- Need the AI to have clear database of info about user. what experience do they have. what can we pull from to generate resumes for each of these jobs?
	- ai needs to be clearly understanding the mission of parallel income streams and moral flexibility, AI and automation leverage. No moralizing.
	- ai needs to be aware of user's website and how he advertises himself and his services. for background info, but also so that AI can advise on improving it. There's a large gap: user has section for Ux, section for small businesses needing modernization, and draft of a section for more technical business leaders, but that needs to be get refined and focused on automation and AI solutions alongside tech leadership and product team design ops.
## Most important functions:
- how does ai agent write simple python script to translate the job description/requitements page into markdown?
	- apple shortcuts to trigger it?
	- how can we use gmail api to grab the email alerts, and evaluate in real time when use isn't actively browsing. cron job triggering a check of the emails? RSS updates on search terms in job boards?
- how does ai evalaute the opportunity for fit with interests and experience, but also more of a fit for ability to be scripted and stacked?
- how do we track them all in user-facing way, in ai-facing way, JSON/sqlite might be best
- how do we generate high quality resumes in the exact markdown format? They must pass employer ATS screening, so they must use all key words and phrases, but apply them to user's plausible experience.
- how does ai suggest new places to search fo jobs or other opportinities that are less compeitive and congested?
- how does ai find 'unknown unknowns' that are jobs or opportunities the user never would have though of, but with minimal additional competencies can be immediately competitive at? especially in the boring, obscure and less-competitive less-oversight roles? Documenation administrator, Ai implementation manager, ERP maintanance and troubleshoorting, data analysis, business analyst, onboarding technicial, UX evangylist, AI ambassdor, tech transfer coordinator. etc. (making up things that could exist and possibly be less competitive with less firm deliverables, more scriptable)
- non-job opportunities: using website to get contracts in:
	- ux/product team leadership and ops
	- appealing to less-technical SMB owner operators that need modernization
	- more technical hands-on roles like fractional CTO, head of UX, AI Initiatives advisor: high level roles specialising in automating and integrating AI into businesses
- non-job opportunities:
	- public contracts that are easy to middle-man
	- flippping gov surplus stock for profit, business hardware into LLM home lab, improve amount of automated LLM workflows can be done around the clock, have it constantly looking for flippable surplus or contracts that are easy to middle-man.
	- etc.

# Existing Resources:
## Directories:
- Larger Scale Project
  This directory has the documentation from the agents working on the larger project. This will show larger scope of what's happening. In summary: This job search optimization, automation and AI enhanced tool we are creating is a combination of several items that have been implemented in various ways in the past. It should ultimately be a part of the "sandman" MCP and automation project. Able to constantly run automations and respond to user instruction. Since component parts of this have been implmented to varying degrees, this project here is being given this large directory of files. They are not currently built to work well together, so we will first need to figure out how to create optimally useful versions of whatever important information can be extracted from these files. Existing scripts can be mostly ported to python and adjusted for these use cases and hardware considerations.
- Original AI Guidance Files:
  This directory was what was used in the past to guide the AI support chat. It contains very important info on the user's preferences and background.
	- userProfile.md: info on user's experience and background. very important
  - logic.md: how to prioritize and selct jobs that align with user's goals
  - Directory: Skills Database: this contains the csv files of a database that was being used for keeping track of experiences, skills, past roles, etc. It's very useful for AI when trying to create a resume using the terms and phrasing in a job description, ensuring to use CAR or STAR format accomplihsments based in real situations from my experience. Probably one of the best resources to use as a starting point when we develop our own optimized data for this project. It's originally a google sheet, but this is just raw CSV values.
  - communications.md: how to navigate negotiation and sales, trying to secure jobs and navigate communications. Might not be very helpful to this project.
  - voice.md: output requirements. mostly to remove LLM red flags. things that make it obvious you're reading something from an AI. not very important to this project at this stage.
  - newContent.md: I don't remember, i think it was things to ad to userProfile for at-a-galnce reference for certain skills and experience. not sure.
  - Personal Career Outline Document: Longer-form details on career. Older document, probably better optimized in more recent files like userProfile.md
  - Summary:
		- User wants low oversight, easy-to-automate work that can be done remote and stacked with other jobs and clients. Highly able to learn and script AI solutions. Very experienced in all realms of UX. 
			- Field of interest UX, expertise in deep figma design ops and design systems. 
			- Field of interest: helping smaller businesses scale up technology, automation and AI integration. This is an opportuntity to find potential acquisition targets by prioritizing aging less-modern owners looking for retirement path, willing to entertain seller-financed buyout.
			- Field of interest: Overlooked, boring, non-competitive roles that aren't what user would know to look for. Remote roles. Examples: data entry, data analysis, ERP support, sales. anything that's easy to script and integrate AI, performing remotely. Jobs where there's little competition or oversight, and automating the job;s bare minimum and avoiding detection are possible. This is an area of "unknown unknowns" for the user and they need help discovering the opportunities, especially where there is overlap in existing skills/interests and/or overlap with potential aging owners in need of modernization.
- Notion DB of job applications (illustrative of process, mine for background experience)
	- The previous process involved taking each job application, creating a new notion DB entry. that entry would contain:
		- job description
		- ATS keywords (the terms/phrases AI suggested are important to use in resume to match highly in ATS filtering)
		- strategizing and notes on how to essentially rephrase job requirements into bulletpoints for resume
		- drafting of resumes that would rank high for employer ATS.
		- front-matter on status of application or discussion/interviewing process.
- Old resumes 
	- resumes used for job applications in pdf
	- markdown version of resumes
- Jobs with potential
  - mostly empty now, but a good place to store jobs that I come accross that i might not have known to look for, but now that I lucked into them, they look like the kind of jobs I want my portfolio to make me look like a perfect candidate for, I want to be able to apply to these jobs with aboslute confidence despite it not being a traditional fit. These are areas worth pivoting into. I'd rather lead hybrid/remote AI implementation and coordination than be another mid-level UX designer stuffed into an uncomfortable office that's always under the microscope from 8 levels of management above me to close out increasing amounts of vague jira tickets.
- Appscript Project: 
  - Automated job alert emails where automatically scraped via appscript into a google sheets file. each job link was extracted and rated according to user prefernce. This no longer works, and needs to be re-done in python with something like sqlite.
  - user could also trigger apple shortcut on mac when viewing a job on indeed or on linkedin, and the page would be scraped and uploaded to this spreadsheet, allowing for more detialed info on jobs of particular interest.
  - simple to script. most complexity is in formatting the markdown or plain text from json or html.
  - important note: there's a file "useful logic from this project" that is immediately useful for job evaluation. Between that and logic.md, a solid reubric can be developed.





---

## Improving How we document developing and validating skills for use in the Job Search automation project

The current approach used in LEARNER.md tracks fluency in topics. For job search purposes you need a second dimension: **leverage**. A skill has two independent values — how well you know it, and what asymmetric advantage it creates in which contexts.

Add a new section to LEARNER.md called `SKILLS INVENTORY` with a different structure than the fluency matrix:

```markdown
## SKILLS INVENTORY
### Format:
SKILL | FLUENCY | TRADITIONAL ROLES | ARBITRAGE OPPORTUNITIES | EVIDENCE

### Example entries:

Agentic AI workflow scripting | [familiar] |
  TRADITIONAL: AI Engineer, Automation Engineer, DevOps
  ARBITRAGE: Any ops-heavy role where 40% of work is 
    repetitive data handling. Operations analyst, 
    marketing coordinator, project manager at a 
    company that hasn't discovered automation yet.
    You automate your job in week 2 and stack capacity.
  EVIDENCE: Digestitor pipeline, Sandman platform,
    Reddit-to-markdown workflow

HTML scraping + structured data extraction | [familiar] |
  TRADITIONAL: Data Engineer, Web Scraper, ETF Developer
  ARBITRAGE: Market research roles, competitive 
    intelligence, any job where "research" means 
    a human manually browses websites all day
  EVIDENCE: Digestitor trafilatura pipeline

SQLite + structured local databases | [familiar] |
  TRADITIONAL: Backend developer, data analyst
  ARBITRAGE: Any role that currently tracks things 
    in spreadsheets. Office manager, operations 
    coordinator, project tracker roles at SMBs
  EVIDENCE: Digestitor database layer, LL database work

LLM prompt engineering + output structuring | [familiar] |
  TRADITIONAL: AI Product Manager, Prompt Engineer,
    ML Operations
  ARBITRAGE: Legal document review, grant writing,
    RFP response writing, any role where the output
    is structured text produced from research inputs
  EVIDENCE: This project's AI workflow design

Government contract solicitation awareness | [none] |
  TRADITIONAL: Government contractor, BD analyst
  ARBITRAGE: SAM.gov lists thousands of small data
    analysis, research, and reporting contracts 
    under $25k that go unfilled or underleveraged.
    Scriptable discovery + LLM fulfillment for 
    simple deliverables is realistic.
  EVIDENCE: (not yet built)
```

The `ARBITRAGE` field is the key addition. It's not "what jobs use this skill" — it's "where does having this skill when nobody expects it change the game entirely."



This system, particularly JS-05's opportunity mining, is genuinely valuable and under-built in the market. Most job search tools optimize for finding jobs that match your resume. This is a system that finds roles where your actual capability exceeds what the job description even knows to ask for. That's a fundamentally different and more powerful framing.

The big arbitrage plays possible here (boring local company, PowerPoint job, automate it in week 2, stack another, maybe go 10-99 instead of w2, build a agency) are real. The government contract angle is also wide open and almost nobody from a non-traditional background thinks to look there. SAM.gov has thousands of small research and analysis contracts that are exactly the kind of work an LLM pipeline handles well.

This project is the foundation everything else depends on. That's where I'd start — before writing a single line of scraper code.



# What we are trying to build
# The Job Search Automation Platform
### A personal intelligence system for career arbitrage

---

## What This Is

Operator is a personal job search intelligence platform. It ingests job postings from
multiple sources, evaluates them against a detailed personal profile, and produces
tailored application materials. More importantly, it surfaces opportunities that
traditional job search methods miss entirely — roles where the user's skill combination
creates a disproportionate, non-obvious advantage.

The guiding philosophy is arbitrage over competition. The goal is never to compete
on the same terms as everyone else applying to the same role. The goal is to find
situations where your presence is unexpected, your capabilities are unrecognized by
the job description, and your ability to automate, accelerate, or transform the role
makes you disproportionately valuable — or disproportionately efficient.

This includes traditional career fits, but also: automatable roles at companies with
no technical sophistication, government contract opportunities in low-competition
categories, small business acquisition candidates, middleman plays on outsourceable
contracts, and any situation where showing up with modern AI tooling to a room that
has never seen it creates a structural advantage.

---

## The Problem Being Solved

Standard job searching is manual, inefficient, and optimized for average candidates.
It treats every job posting as equally worthy of attention, evaluates fit
superficially, produces generic application materials, and completely ignores the
universe of non-obvious opportunities that don't appear on LinkedIn.

Specifically:

- Job alert emails pile up unread because manually evaluating each one is tedious
- Resume tailoring is time-consuming and rarely done well
- Keyword matching by ATS systems filters out strong candidates with non-standard
  phrasing before a human ever sees the application
- The most interesting opportunities — arbitrage plays, underserved niches,
  government micro-contracts, automatable roles — require research patterns that
  humans don't naturally do but machines do well
- Nobody tells you what jobs you'd be exceptional at that you've never heard of

Operator solves all of these.

---

## Desired End State

A system where the user's daily job search workflow is:

1. Open a morning digest showing new postings scored against personal priorities
2. For any interesting posting, one command generates a fully tailored resume and
   cover letter using the job's exact terminology and phrasing
3. Periodically, the system surfaces a set of non-obvious opportunity categories
   the user hadn't considered — with specific reasoning for why each is a fit
4. The user maintains a single source-of-truth profile document that drives all
   output — update it once, all future applications reflect the change
5. A human reviews all generated materials before submission — the system drafts,
   the human refines and approves

The system never automates the human out of the loop on final decisions. It
handles the research, evaluation, and drafting. The user handles judgment and
submission.

---

## Core Principles

**Arbitrage over competition.** The most valuable output is identifying where the
user's skill combination is rare and unexpected, not just where it matches the
job description.

**Human in the loop.** All generated materials are drafts for human review.
The system never submits anything autonomously. Plausibility and authenticity
are the user's responsibility to verify.

**Honest reframing, not fabrication.** The resume generator translates real
experience into the employer's terminology. "Built automated data pipeline" and
"developed ETL workflow" describe the same thing. The tool finds the right
phrasing. It never invents experience that doesn't exist.

**Profile as source of truth.** One document — profile.md — drives everything.
The quality of all outputs is directly proportional to the quality of this document.
Investment in maintaining it pays compound returns.

**Unknown unknowns matter most.** The most valuable job the user gets might be
one they never would have searched for. The system must actively surface
opportunity categories the user hasn't considered.

---

## User Profile Context

The user has a background in software and UX. They are building competency in: Linux administration, Docker, Python scripting, agentic AI workflows, automated data pipelines, SQLite database management, and LLM prompt engineering.

They are interested in opportunities where these skills create leverage in non-technical environments — operations roles, local businesses, government contracting, and any situation where showing up with automation capability in a room that has never seen it creates structural advantage.

They are explicitly interested in the /r/overemployed model: finding roles that can be performed at a high level in reduced hours through automation, creating capacity to stack income sources or simply reclaim time.

They are not exclusively interested in tech roles. A boring local business that generates reliable income and can be partially automated is more interesting than a prestigious tech role with high surveillance and low autonomy.

---

## What the System Knows

The system maintains a personal profile covering:

- Work history with specific achievements and measurable outcomes
- Technical skills with evidence (not just claimed — demonstrated)
- Soft skills and working style preferences
- Career goals and non-negotiables (remote, salary floor, management style)
- Known arbitrage skills — capabilities that create advantage in non-obvious contexts
- Anti-patterns — things to actively avoid despite appearing attractive on surface
  (example: UX leadership role, good salary, but indicators of micromanagement
  and activity tracking — traditional fit but wrong culture)

---

## Opportunity Categories the System Should Surface

Beyond standard job matching, the system should reason about:

**Automatable local roles.** Small and medium businesses in stable industries
with ops-heavy roles and no internal technical sophistication. The user automates
most of the job within weeks, maintains baseline performance, and recaptures time.

**Government micro-contracting.** SAM.gov and USAJobs list thousands of small
data analysis, research, reporting, and administrative contracts that are
under-competed and often fulfillable with LLM assistance. Low barrier to entry,
reliable payment, non-traditional path.

**Middleman contract plays.** Identifying government or commercial contracts where
the user can fulfill the deliverable by orchestrating tools and subcontractors,
without necessarily having the domain expertise themselves. The skill is in
finding and operationalizing the contract, not necessarily executing the
technical work directly.

**Small business acquisition.** Some owner-operators of stable local businesses
are willing to seller-finance a buyout to the right person. A technically
capable buyer who can modernize operations without disrupting them is rare.
Identifying these candidates is a research automation problem.

**Unknown job titles.** Roles that exist in large numbers but are invisible to
someone who has only searched within their industry vertical. Operations analyst,
business systems analyst, revenue operations, process improvement specialist,
intelligence analyst — many of these reward technical automation skills that
the job description never explicitly asks for.

**Roles where AI literacy is a decade ahead of the room.** Any industry where
competitors are not yet using LLM tooling for their core workflows. The user
arrives already operating at a level the company won't reach for years.

---

## Anti-Patterns to Screen Against

The system should flag roles that match the following patterns as low-priority
regardless of other fit signals:

- High surveillance / activity tracking indicators in the job description
- Mandatory in-office at location incompatible with user's constraints
- Language suggesting low autonomy or high approval-chain overhead
- Company size and structure that would eliminate any automation advantage
  (large enterprise with locked-down systems and IT approval for all tooling)
- Roles where the explicit requirements significantly exceed realistic opportunity
  (10 years experience for entry-level compensation)

---

## MVP Definition

The MVP is intentionally minimal. It should be usable within days, not weeks.

A folder of job descriptions in markdown format. A profile.md file. A single
LLM call that reads both and returns:

- Is this a traditional fit? Score and reasoning.
- Is this an arbitrage play? Score and reasoning.
- Does this have anti-pattern flags? What are they?
- Recommended action: apply, skip, monitor, research further.

That's it. No scraping, no database, no resume generation. Just the evaluation
loop running on files the user drops in manually. This proves the prompt and
the profile document work before building any infrastructure around them.

Everything else is built on top of a working evaluation loop.

---

## Phases

### Phase 0 — Manual MVP
Folder-based. User drops JD markdown files into a folder. LLM evaluates against
profile.md. Returns scored evaluation. No automation, no database, no resume
generation. Goal: validate the evaluation prompt and profile document quality.

### Phase 1 — Persistent Pipeline
Job postings stored in SQLite. Gmail integration reads job alert emails and
extracts postings automatically. Basic deduplication. Scheduled evaluation runs.
Morning digest output. Goal: eliminate manual file management.

### Phase 2 — Application Materials
Resume generator. Takes scored job + profile, produces tailored resume and cover
letter using job's terminology. Human reviews before use. Goal: eliminate the
tailoring bottleneck.

### Phase 3 — Opportunity Mining
Active surfacing of non-obvious opportunities. SAM.gov integration. Job title
expansion suggestions. Arbitrage play identification. Small business candidate
research. Goal: find opportunities the user wouldn't have found manually.

### Phase 4 — MCP Integration
All tools exposed as MCP endpoints. User can interact conversationally via Claude
or other MCP-compatible client. "Score this posting" with a URL returns full
analysis. "Generate resume for job 47" returns a document. Goal: conversational
interface over the entire system.

---

## Open Questions

These are not decisions to make now. They are questions to answer during
implementation, recorded here so they are not forgotten.

- What is the right format for profile.md to maximize LLM comprehension without
  becoming unwieldy to maintain?
- How should the system handle skills the user is actively learning but cannot
  yet claim as current competencies? Separate section? Confidence ratings?
- What is the right threshold for arbitrage potential flagging to avoid
  surfacing noise?
- How does the resume generator handle gaps between job requirements and user
  experience without fabricating? What is the right fallback behavior?
- Should the system maintain a feedback loop — tracking which applications
  got responses — to improve scoring over time?
- How does the human review step get implemented in a way that doesn't
  recreate the friction the system is meant to eliminate?

---

## What This Is Not

- Not a fully automated application submitter. Human approval is always required.
- Not a fabrication tool. Every claim in generated materials must be grounded
  in real experience documented in profile.md.
- Not a replacement for human judgment on culture fit and role quality.
  The system scores and surfaces. The human decides.
- Not dependent on any single LLM provider. The evaluation and generation
  prompts should work with Claude, Gemini, or a local model.



# Initial Tasks Outline:
A starting point to adjust as we develop a final README.MD and TASKS.MD for this project

## PHASE 2.5-J — Operator: Job Search Automation Platform

### Overview
Operator is a personal job search intelligence system. It evaluates job postings
against a detailed personal profile, generates tailored application materials,
and surfaces non-obvious opportunities where the user's skills create
disproportionate, unexpected advantage. See JOB_SEARCH_README.md for full vision,
principles, and open questions.

Architecture mirrors the Sandman tool pattern: each capability is a standalone
tool with a clean interface, a SQLite database, and markdown output. Tools are
built in order of dependency. The evaluation loop (JS-01 through JS-02) must
work and be validated before any other phase begins.

---

## JS-01 : Build profile.md — personal source of truth
STATUS: TODO
ACCEPTANCE CRITERIA:
  - Single markdown file at defined path in repo
  - Sections defined and populated:
    - Work history: each role with specific outcomes, not responsibilities
    - Projects: what was built, what stack, what it demonstrates
    - Technical skills: each with evidence reference, not just claimed
    - Soft skills and working style preferences
    - Goals: what good looks like in 1 year, 3 years
    - Constraints: salary floor, location, remote requirements
    - Anti-patterns: specific things to screen against regardless of fit score
    - Arbitrage skills: capabilities that create non-obvious advantage in
      non-technical environments, each with a specific scenario description
  - Format validated: an LLM given only this file can answer specific
    questions about experience without hallucinating details
  - Reviewed and confirmed accurate before any tooling is built on top of it
NOTES:
  This is the most important task in the entire phase. Every downstream output
  is only as good as this document. Do not skip or rush it.
  The arbitrage skills section is the novel piece. It should describe not just
  what the user can do but where that capability is rare and unexpected.
  Example: "Agentic AI workflow scripting: advantage in ops-heavy roles at
  non-technical companies. User can automate significant portions of the role
  within weeks of starting without drawing attention."

### JS-02 : Build Phase 0 MVP — folder-based evaluation loop
STATUS: TODO
BLOCKED BY: JS-01
ACCEPTANCE CRITERIA:
  - A folder: /operator/inbox/ — user drops JD markdown files here manually
  - A single script: evaluate.py — reads all files in inbox, reads profile.md,
    calls LLM, writes scored evaluation for each
  - Output per job: markdown file with frontmatter containing:
    - traditional_fit_score (0-100)
    - arbitrage_score (0-100)
    - recommended_action: apply / skip / monitor / research
    - anti_pattern_flags: list, empty if none
    - fit_reasoning: 2-3 sentences
    - arbitrage_reasoning: 2-3 sentences, present even when score is low
    - missing_skills: list
    - transferable_skills: list of existing skills with non-obvious application
  - Prompt template stored as separate markdown file, not hardcoded in script
  - LLM backend configurable via config file, not hardcoded to one provider
  - Idempotent: re-running skips already-scored files unless --force is passed
  - Output is human-readable and designed to be reviewed, not just logged
NOTES:
  This is the validation phase. If evaluation output is not useful and accurate,
  nothing else is worth building. Iterate on the prompt and profile document
  until output quality is consistently good before proceeding to JS-03.
  anti_pattern_flags should fire on signals like: mandatory in-office, activity
  tracking language, excessive approval chains, requirements-to-compensation
  mismatch, or cultural indicators incompatible with autonomous working style.
  arbitrage_reasoning should never be empty even for low scores. It should
  explicitly explain why this is or is not an arbitrage play.

### JS-03 : Build job database and ingestion layer
STATUS: TODO
BLOCKED BY: JS-02 validated and working
ACCEPTANCE CRITERIA:
  - SQLite database stores all job records
  - Schema: id, title, company, url, date_posted, source, salary_range,
    location, remote_ok, status, traditional_fit_score, arbitrage_score,
    recommended_action, anti_pattern_flags, full_text, date_evaluated
  - Status lifecycle: new > scored > reviewed > applied > response > closed
  - Ingestion from manual file drop (extends Phase 0 folder approach)
  - Ingestion from Gmail job alert emails (depends on TS-04 gmail_tool)
  - Deduplication by URL: re-ingesting same posting updates record, no duplicate
  - User can add a posting by URL: system fetches, stores, and queues for scoring
  - Morning digest output: markdown report of new scored postings since last run,
    sorted by combined fit and arbitrage score, anti-pattern flags shown prominently
NOTES:
  Gmail integration depends on TS-04. Stub with manual file drop initially
  and add email ingestion when gmail_tool exists. Do not block on it.
  The status lifecycle enables a feedback loop later: which scored postings
  got interviews? That data can improve scoring calibration over time.

### JS-04 : Build resume generator
STATUS: TODO
BLOCKED BY: JS-01, JS-02
ACCEPTANCE CRITERIA:
  - Takes a job record and profile.md as input
  - Extracts and ranks requirements from job posting by inferred priority:
    order of appearance, frequency, phrasing strength (must vs preferred),
    known norms for similar roles
  - Rewrites profile bullet points using job's exact terminology and phrasing
    while grounding every claim in documented real experience
  - Ensures complete coverage of required skills in output language
  - Never fabricates experience: if a required skill is missing, flags it
    rather than inventing a claim
  - Outputs: tailored resume as markdown
  - Outputs: cover letter variant as markdown
  - Outputs: skills gap analysis noting what to address in cover letter
    or interview rather than resume
  - Human review is a required step before use: output is clearly marked as draft
  - Transparency check: flags phrases that are too directly copied from the JD
    and suggests paraphrase alternatives to avoid pattern-matching detection
NOTES:
  The reframing principle: "built automated data pipeline" and "developed ETL
  workflow" describe the same thing. The tool finds the employer's phrasing.
  This is translation, not fabrication. The line is: real experience reframed
  vs invented experience claimed. System should never cross that line.
  The transparency check is the human-in-the-loop mechanism. Output that
  reads like it was written by someone who memorized the job description is
  a red flag. The generator should flag this and suggest natural alternatives.

### JS-05 : Build opportunity mining tool
STATUS: TODO
BLOCKED BY: JS-01
ACCEPTANCE CRITERIA:
  - Given profile.md, generates a structured opportunity report containing:
    - Non-obvious job title suggestions with reasoning for each
    - Contract and freelance opportunity categories worth investigating
    - Arbitrage plays: specific role types at specific company sizes and
      contexts where user's skill combination is rare and valuable
    - Unknown unknowns: job categories the user likely has not searched
      due to career path bias
  - Integrates with SAM.gov API to surface active government contract
    opportunities matching user's capabilities
  - Output stored as dated markdown report
  - Re-runnable as profile.md is updated: fresh suggestions reflect new skills
NOTES:
  Examples of what this should surface:
  "Operations analyst at 50-200 person company with no dedicated tech team:
  user automates the role and has capacity to stack a second within 90 days"
  "Government micro-purchase data analysis contracts under $25k on SAM.gov:
  low competition, reliable payment, LLM-fulfillable for simple deliverables"
  "Series A startups hiring first ops role: need someone who builds the
  infrastructure, not just runs it. Technical ops background is rare here."
  "Local service businesses with stable revenue and aging owner-operators:
  candidate for seller-financed acquisition to technically capable buyer."
  Government surplus and resale opportunities should also be scoped here
  if SAM.gov integration surfaces relevant contract vehicle types.

### JS-06 : Wire Operator into MCP server
STATUS: TODO
BLOCKED BY: JS-02, JS-03, JS-04, TS-06
ACCEPTANCE CRITERIA:
  - job_scorer exposed as MCP tool
  - resume_generator exposed as MCP tool
  - opportunity_miner exposed as MCP tool
  - User can paste a job URL into Claude and receive full scored evaluation
  - User can request resume generation for a specific job ID
  - User can request fresh opportunity mining report
  - All tool calls return structured output, not raw text
NOTES:
  This is the milestone where Operator becomes conversational. The full
  research-to-draft workflow happens in one Claude conversation without
  switching tools or manually running scripts.



