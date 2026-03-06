# OPERATOR: A Job Search Intelligence Platform
### Arbitrage over Competition

Operator is a personal intelligence system designed to transform the job search from a manual process into a high-leverage, automated operation. It identifies opportunities where your technical skills provide an unfair advantage over low-competition applicant pools.

---

## 🏗️ Project Framework

- **[MISSION.md](./MISSION.md)**: The core strategy, "Arbitrage over Competition" philosophy, and strategic pillars.
- **[SYSTEM_ARCHITECTURE.md](./SYSTEM_ARCHITECTURE.md)**: Technical design for the modular scraping and monitoring suite.
- **[ROADMAP.md](./ROADMAP.md)**: Phased execution plan from MVP to full automation.
- **[profile.md](./profile.md)**: Your "High-Fidelity Brain" (Source of Truth for experience and history).
- **[State of Project.md](./State_of_Project.md)**: Current status of the Phase 0 MVP.

---

## 🚀 Quick Start (Phase 0 MVP)

The current MVP handles a "Manual Folder-Based Evaluation Loop."

1. Drop a raw job description (Markdown) into `/operator/inbox/`.
2. Ensure `profile.md` is up to date.
3. Run the evaluator:
   ```bash
   python operator/evaluate.py
   ```
4. Check results in `/operator/evaluations/`.

---

## 📂 Project Structure

```text
/
├── MISSION.md               # Strategy & Philosophy
├── SYSTEM_ARCHITECTURE.md   # System design & Database schema
├── ROADMAP.md               # Task list & Milestones
├── profile.md               # User history (Source of Truth)
├── operator/                # Current MVP code
│   ├── inbox/               # Input JDs
│   └── evaluations/         # Scored reports
└── archive/                 # Legacy data and research
```

---

## 🤖 AI Agent Guidelines

1. **Surgical Edits Only:** Never rewrite an entire file. Edit minimally.
2. **AI.md Protocol:** Every directory should contain an `AI.md` file logging intent and advice for future agents.
3. **Session Logging:** Summarize sessions in `OPERATOR_LOG.md`.
4. **Git Protocol:** Always work in an `agent` branch. Never self-merge.
