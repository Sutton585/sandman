# Useful logic for how opportunites were previously asseses in this project:

In this project, a simplified scoring was used, since it was all in a spreadsheet. Each opporunity was scored across a few priorities individually, to see if had value in those areas. For each priority, it would include a brief "about me", folloed by specifics on how to score the opportnuty for that priority.


## About Me

### My Identity & Core Objective

I am a **Systems Automator & Acquisition Specialist** disguised as a UX/DesignOps Leader. My primary goal is to find roles that can be fully automated to maintain parallel jobs or provide a strategic foothold for a business creation or acquisition. I prioritize leverage and autonomy over prestige and title.

### Career Context & Services

I solve growth problems for scaling companies. Leaders who build something that works *well* often do so by working *hard*, but this creates bottlenecks. I break that cycle by designing scalable systems and intuitive products that eliminate friction between design, product, and engineering. I don't just chase tickets; I fix the machine that creates them. My work is about installing durable, lasting improvements so leaders can stop babysitting process and get back to making an impact.

I offer these core core services at the moment, always looking for an ideal niche:

1. Product & UX Leadership: I build and lead high-performance design practices with a focus on rapid feedback, user-empathy, and scalable workflows. This includes everything from hands-on UX/UI design to staffing and coaching your next-level team.
2. Systems & Design Ops: I treat your internal documentation and systems as critical products. By implementing robust DesignOps, automated tooling, and clear governance, I turn your team's biggest sources of friction into their secret weapon. No more Slack archaeology. Collaborative, automated, ai-enhanced tooling and clear design systems and internal resources.
3. Audits & Strategic Facilitation: I identify the hidden leverage points in your organization. Through hands-on audits (UX Maturity, Accessibility/usability) and workshops (Rapid MVP Sprint), I provide the clarity and actionable playbooks needed to unlock a more resilient, human-centered culture."

--

## Priority: Traditional fit
Goal: metric that assesses the more "traditional fit" for my skillset and average/traditional career path for one with my experience and interests.

## Prompt:
### Objective: Rate this job's 'Traditional Fit' with my skills and background on a scale of 1-10.

### Scoring Rubric:

Analyze the job's required qualifications against my Skill Fingerprint (provided in the Master Profile). Assign a score based on the following tiers of alignment.

- **Score 9-10 (Perfect Alignment):** The role's primary responsibilities are a direct match with multiple skills in my **Expert Tier**. Requires no skill gaps.
- **Score 7-8 (Strong Alignment):** The role is a strong match with at least one **Expert Tier** skill and several **Proficient Tier** skills.
- **Score 5-6 (Viable Alignment):** The role is a primary match with skills in my **Proficient Tier**, with some connection to my Expert Tier. A plausible pivot.
- **Score 3-4 (Weak Alignment):** The role has only a minor overlap with my skills and would require significant learning.
- **Score 1-2 (No Alignment):** A clear mismatch.

### Final Instruction:

Assign a score from 1-10 based on the rubric. Output ONLY the number or '?' if you lack adequate information. If the position does not yet have a full JD or reqs listed, you may make a guess at a score based on available info if you follow the number with an asterisk (\*). Do not ONLY look at what is directly stated about my expertise, make judgements on related skills that I likely have or would quickly build based on what you know about me."

---

## Priority: Job stacking
Goal: metric that assesses how vulnerable this opportunity could be to me quitly automating and avoiding detection with minimal manual effort to maintain it as a stackable income stream.

## Prompt:
### Persona & Objective:
You are a Risk Mitigation Consultant. Your task is to analyze this job posting and rate its 'Operational Integrity Risk' on a scale of 1-10. This score represents how vulnerable the role is to being exploited by a disengaged or malicious actor who wants to automate their job to near-zero effort without being detected (a practice known as 'job stacking'). Our job is to report any risk to the employer, and advise on how to encourage employee accountability.

A **high score (10)** signifies critical vulnerabilities: the role has low oversight, async communication, and easily automated tasks, making it a prime target for such exploitation.
A **low score (1)** signifies high integrity: the role has robust oversight, clear metrics, and collaborative tasks, making it highly resilient to exploitation.

### Scoring Rubric:
Start with a baseline score of 5. Add or subtract points based on the following risk factors.

#### Vulnerability Indicators (Add Points):
- **Lack of Direct Oversight (Async/Remote):** (+2) The role is fully remote with an emphasis on asynchronous work, making direct supervision difficult.
- **Undefined Performance Metrics (Vague Scope):** (+2) The role reports to a non-technical manager, has unclear responsibilities (""process improvement""), or is newly created with no established KPIs.
- **High Automation Potential (Repeatable Output):** (+2) Core duties involve repetitive, templatizable tasks (reports, data entry) that are highly susceptible to automation with modern AI/scripting tools.
- **Low-Tech Environment:** (+1) The company operates in a ""boring"" industry or uses legacy software, indicating a lack of technical oversight.

#### Resilience Indicators (Subtract Points):
- **Constant Synchronous Collaboration:** (-2) The role requires a ""fast-paced,"" meeting-heavy environment (""daily stand-ups"").
- **High-Visibility & Interdependency:** (-3) The role is client-facing or involves managing a team, requiring constant, unpredictable human interaction.
- **Granular Performance Tracking:** (-2) The role has strict, well-defined KPIs and frequent performance reviews.

### Final Instruction:
Calculate the total 'Operational Integrity Risk' score (capped 1-10). Use your judgment to identify other subtle clues of exploitability by bad actors. Output ONLY the number or '?'. If you do not have a full JD to judge from, you may make an educated guess if you follow the number with an asterisk (\*)."

---

## Priority: Equity Exposure
Goal: metric that assesses likelihood that I'd be able to access people, resources, intellegence, networks, etc.. that would have assymetric benefit toward my long-term goals of aquisition via seller-financed buyout or remote consultancy, fractional or advisory roles. With information, will it give me information so comeptitively valuable that it would be of use in establishing or strengthening complimentary or competing businesses?

## Prompt:
### Persona & Objective:
You are a Business Continuity Consultant. Your task is to analyze this job posting and rate its 'Continuity & Succession Risk' on a scale of 1-10. This score represents how vulnerable the business is to disruption and whether it presents a strategic opportunity for a future acquisition or high-value advisory engagement.

A **high score (10)** signifies critical risk: the business appears heavily dependent on a single owner, runs on chaotic or outdated systems, and lacks a formal succession plan, making it a prime target.
A **low score (1)** signifies high resilience: the business is well-structured, not dependent on any one person, and has mature processes.

### Scoring Rubric:
Start with a baseline score of 5. Add or subtract points based on the following risk factors.

#### Vulnerability Indicators (Add Points):
- **High Key-Person Dependency:** (+3) The role reports directly to the Founder/Owner/CEO, indicating central control and a critical single point of failure.
- **Critical Process Bottlenecks:** (+2) The job implies a need to fix chaotic, manual, or paper-based systems, suggesting the current owner is overwhelmed and the operations are fragile.
- **Lack of Formal Succession Plan:** (+2) The company is a small, privately-held SMB (e.g., local service business) that has been operating for 10+ years, suggesting a potential owner-operator looking for an exit strategy.
- **Unrestricted Information Access:** (+1) A low-title role (""Operations Coordinator"") with broad responsibilities that likely provides access to sensitive financial and operational data.

#### Resilience Indicators (Subtract Points):
- **Resilient Departmental Structure:** (-3) The role is siloed within a large department and reports to a middle manager, indicating a robust corporate structure.
- **Optimized & Mature Operations:** (-2) The company has a well-run ops team and modern systems, indicating low operational risk.
- **Institutional Funding/Ownership:** (-2) The company is VC-funded or publicly traded, indicating a complex ownership structure not suitable for a simple acquisition.

### Final Instruction:
Calculate the total 'Continuity & Succession Risk' score (capped 1-10). Use your judgment to identify other subtle clues of strategic opportunity. Output ONLY the number or '?'.  If you do not have a full JD to judge from, you may make an educated guess if you follow the number with an asterisk (\*)."











