# SYSTEM ARCHITECTURE: Scraping and Monitoring Suite
## The Operator Technical Design

### 1. Conceptual Design
The system is a collection of modular tools focused on discovery, ingestion, and evaluation. It acts as an intelligence layer on top of a unified database.

```text
SCRAPERS & INGESTION   ->   CENTRAL STORAGE   ->   INTELLIGENCE   ->   INTERFACE
(Modules)                   (SQLite DB)            (LLM/Scoring)        (Output)

Jobber Scrapers        ->   Job Postings table ->   Evaluator     ->   Daily Digest
Digestitor (Reddit)    ->   Market Trends table ->  Summarizer    ->   Abridged MD
Market Monitor (eBay)  ->   Surplus table      ->   Scorer        ->   Markdown Log
SAM.gov / RFPs         ->   Contracts table    ->   Miner         ->   Agent Tasks
```

### 2. Core Components

#### A. Central Database (`operator.db`)
A single SQLite database acts as the system's "memory." This enables:
- Deduplication of opportunities.
- Tracking of application status.
- Analysis of what "Unknown Unknowns" have been surfaced.
- **Key Tables:** `opportunities`, `user_history`, `application_tracking`, `market_items`, `digests`.

#### B. Modules (`/modules`)
Each discovery source is a separate module with a consistent interface:
- **`jobber`**: Scrapes job boards (LinkedIn/Indeed), monitors Gmail job alerts.
- **`digestitor`**: Scrapes Reddit (Rochester/Upstate NY), TikTok, and niche news feeds.
- **`market_monitor`**: Monitors eBay, FB Marketplace, and Gov Surplus (e.g., Monroe County, NYS).
- **`contracts`**: Polls SAM.gov and local RFP sites for micro-contracts.

#### C. The Intelligence Engine (`/core`)
- **`evaluator.py`**: Uses `profile.md` and `logic.md` to score entries in the database.
- **`resume_generator.py`**: Uses high-fidelity CAR bullet points from `profile.md` to tailor application materials.
- **`opportunity_miner.py`**: Proactively generates "Unknown Unknown" suggestions.

#### D. The Digest Generator
A weekly or daily task that aggregates the latest:
- High-scoring jobs (by arbitrage and fit score).
- Flips/deals found in the market.
- Relevant news trends from Digestitor.
- Suggested "creative leverage" plays.

### 3. Data Flow
1. **Modules** ingest raw data into the Central DB.
2. **Intelligence Engine** polls for un-scored entries in the DB and populates `arbitrage_score`, `fit_score`, and `reasoning`.
3. **Digest Generator** pulls the best entries from the DB and generates a clean, abridged Markdown report for the user.
4. **User** reviews the Digest and triggers actions (e.g., `generate_resume --job_id 123`).

### 4. Integration Logic (The "Digestitor" Loop)
- The Reddit scraper identifies localized trends or news.
- The AI interprets these trends into *opportunities* (e.g., "A local hospital is modernizing; look for IT admin roles").
- These opportunities are injected into the discovery engine as new search terms or target industries.
