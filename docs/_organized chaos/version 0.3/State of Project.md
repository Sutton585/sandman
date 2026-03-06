# Current State of Project
## Current stage: MVP

As defined in our roadmap, the Phase 0 MVP is the "Manual Folder-Based Evaluation Loop."

Before we write complex scrapers, databases, or resume generators, we must prove that an AI can reliably read a job description and apply your specific "Arbitrage over Competition" mindset.

This MVP accomplishes one thing: It takes a raw job description, compares it against your `profile.md`, and outputs a brutally honest, strategically aligned assessment (with scores) so you can decide in 10 seconds if a job is worth your time.

# Dependencies
The requirements.txt file contains:

### `litellm`
This is the magic ingredient. Different AI companies (OpenAI, Anthropic/Claude, Google/Gemini) all require different, specific Python code to talk to them. litellm acts as a universal translator. It allows us to write the code once. If you want to switch from using Gemini to using Claude tomorrow, you don't rewrite the script; you just change one line in config.json.

### `google-genai`
This is simply the underlying Google package that litellm needs to talk to Gemini (which is currently set as our default in the config).


# Overall Organization
Here is the directory structure we just created inside the /operator/ folder:

```
 1 /operator/
 2 ├── inbox/                  # You drop raw job descriptions here (.md files)
 3 ├── evaluations/            # The script drops the scored reports here
 4 ├── prompts/
 5 │   └── evaluation_prompt.md # The exact instructions given to the AI
 6 ├── config.json             # Settings (tells the script which AI to use)
 7 ├── evaluate.py             # The engine that runs the process
 8 └── requirements.txt        # The list of external Python tools needed
```

# How It Works (Pseudocode Walkthrough)
Here is the logical flow of evaluate.py written in plain English pseudocode:

---

  # STEP 1: SETUP
  1. Load settings from config.json (Which AI to use? Where are the folders?)
  2. Read the master 'profile.md' into memory (This is the Source of Truth)
  3. Read the 'evaluation_prompt.md' into memory (This contains the JSON rules)

  # STEP 2: CHECK FOR WORK
  1. Look inside the 'operator/inbox/' folder.
  2. Find all markdown (.md) files.
  3. IF inbox is empty:
    - Stop and tell the user to add some files.

  # STEP 3: PROCESS EACH JOB
  FOR EACH job_description_file in the inbox:
    Check if this job has already been evaluated in 'operator/evaluations/'.
    IF it has:
      Skip it (unless the user forced a re-run).

  # STEP 4: ASSEMBLE THE INSTRUCTION
  Create the final message for the AI:
      Combine the 'evaluation_prompt'
      + The 'profile.md' text
      + The text of the 'job_description_file'

  # STEP 5: ASK THE AI
  Send the massive combined message to the AI (via litellm).
  Wait for the AI to reply with the required JSON data.

  # STEP 6: FORMAT THE OUTPUT
  Take the AI's raw JSON data (the scores, the red flags, the reasoning).
  Format it into a clean, easy-to-read Markdown file.
  Write that new file into the 'operator/evaluations/' folder.

  # STEP 7: FINISH
  Print "Done!" to the screen.

---

### The End Result
You drop a file called HVAC_office_manager.md into the inbox.
You run the script.
A few seconds later, eval_HVAC_office_manager.md appears in the evaluations folder. It looks like this:

```
---
traditional_fit_score: 20
arbitrage_score: 95
recommended_action: "apply"
primary_archetype: "STACKABLE_ARBITRAGE"
anti_pattern_flags: []
green_flags: ["vague process improvement scope", "direct access to owner"]

---

# Evaluation: HVAC_office_manager.md

## Reasoning
### Traditional Fit: 
Low. This doesn't utilize your UX UI design skills at all.
claiming 35 hours a week for other contracts.

### Arbitrage Potential:
Exceptional. This is a paper-based company. You could automate 90% of this role using Google Apps Script and SQLite in week two, reclaiming 35 hours a week for other contracts.

## Website Strategy
Do not use the UX portfolio. Direct them to the SMB Modernization landing page, or develop a specific landing page for this niche if there's sufficient opportunties that provide similar exploitability.

```
