import sys

filepath = 'nomenclature2.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_section = """

## 13. NEW TASK: Decouple Age Filtering from Maturity Logic
**Reference**: Human Input on Age Filtering Consistency

### AI Analysis & Updated Plan:
- **Understanding**: Re-using `min_age_hours` as a trigger for queuing a "young" post for future re-scrapes in reddit2md breaks the mental model established in jobs2md, where `min_age_hours` is a strict filter that ignores young posts entirely. 
- **Review**: The user expects filtering parameters to actually filter. We must move the "queue for maturity rescrape" logic into a dedicated, explicitly named parameter to preserve consistency across the suite.
- **New Plan**: 
  - Standardize `min_age_hours` as a hard filter across all modules (discard any post younger than X hours).
  - Introduce `rescrape_threshold_hours` specifically for `reddit2md` (and eventually `jobs2md` detail hydration). If a post is scraped and its age is less than this threshold, it receives a `rescrape_after` timestamp.
"""

if "13. NEW TASK: Decouple Age Filtering" not in content:
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(new_section)
    print("Successfully appended to nomenclature2.md")
