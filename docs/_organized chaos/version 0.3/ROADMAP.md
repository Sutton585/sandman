# ROADMAP: Operator Project
## Execution Phases and Milestones

### Phase 0: Manual Foundation (MVP - Current)
- **Goal:** Prove the evaluation logic and profile high-fidelity.
- **Milestone 1:** `profile.md` synthesis (Complete).
- **Milestone 2:** Folder-based evaluation loop (Complete/Testing).
- **Milestone 3:** `evaluate.py` handles manual JDs in `/inbox`.

### Phase 1: Persistent Intelligence (Near-term)
- **Goal:** Move from files to a central SQLite DB for deduplication and tracking.
- **Task JS-03:** Initialize `operator.db` schema.
- **Task JS-03.1:** Migrate manual folder ingestion to database ingestion.
- **Task JS-03.2:** Build Gmail integration for job alerts (JS-03 dependent).
- **Task DIG-01:** Integrate `Digestitor` logic into the `operator.db`.

### Phase 2: Application Acceleration (Mid-term)
- **Goal:** Automate the resume and cover letter tailoring bottleneck.
- **Task JS-04:** Build `resume_generator.py` using CAR bullet points from `profile.md`.
- **Task JS-04.1:** Implement "Employer Phrasing Translation" (Reframing logic).
- **Task JS-04.2:** Human-in-the-loop review interface for generated drafts.

### Phase 3: Opportunity Mining (Long-term)
- **Goal:** Proactively surface "Unknown Unknowns" and non-job income streams.
- **Task JS-05:** Build `opportunity_miner.py`.
- **Task JS-05.1:** SAM.gov micro-contract polling.
- **Task JS-05.2:** Marketplace (eBay/Surplus) scraper for hardware/deals.
- **Task JS-05.3:** "Creative Leverage" engine (New niche discovery).

### Phase 4: Conversational Interface (Final)
- **Goal:** Full MCP integration.
- **Task JS-06:** Expose all tools as MCP endpoints for use with Claude/Gemini.
- **Task JS-06.1:** Conversational job scoring and resume drafting.
- **Task JS-06.2:** AI-driven strategy adjustments (Suggesting new niches in chat).
