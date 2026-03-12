import sys

filepath = 'tasks.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_task = """
---

## Task 13: Decouple Age Filtering from Maturity Logic
**Context Reference**: Human Input on Age Filtering Consistency

**Objective**: Ensure `min_age_hours` behaves identically across all modules as a hard filter (ignoring posts newer than the limit). Move the existing reddit2md "queue for rescrape if young" logic to a newly named parameter: `rescrape_threshold_hours`.

**Acceptance Criteria:**
- [ ] Add `rescrape_threshold_hours` to the configuration, CLI (`--rescrape-threshold-hours`), and Python interfaces across Sandman and reddit2md.
- [ ] Refactor `reddit2md`: Modify the scrape loop to use `min_age_hours` as a strict filter (like `max_age_hours`). If a post's age in hours is less than `min_age_hours`, it should be completely discarded.
- [ ] Refactor `reddit2md`: Ensure the `rescrape_after` timestamp logic is now entirely driven by `rescrape_threshold_hours` instead of `min_age_hours`.
- [ ] Update `nomenclature2.md` and standard documentation (Task 0 workflow) to reflect this architectural shift.
"""

if "Task 13" not in content:
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(new_task)
    print("Successfully appended Task 13 to tasks.md")
else:
    print("Task 13 already exists.")
