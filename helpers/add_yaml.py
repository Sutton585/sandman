import os

filepath = 'modules/reddit2md/readme_nomenclature adjustments.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

yaml_frontmatter = """---
TO-AI: |
  Your task is to comprehensively update the codebase and README.md of the reddit2md module to adhere to the new universal nomenclature outlined below.

  Changes to Execute Across `README.md`, `scraper.py`, `core/config.py`, and `core/processor.py`:
  1. Source: Change `subreddit_name`, config `name`, config `subreddit`, and CLI `--subreddit` to `source` (CLI: `--source`).
  2. Max Results: Change `post_limit` and CLI `--limit` to `max_results` (CLI: `--max_results`).
  3. Detail: Change `comment_detail` to `detail` (CLI: `--detail`).
  4. Label: Change config `flair` and CLI `--flair` to `label` (CLI: `--label`).
  5. Post Links: Change `post_link` to `post_links` (CLI: `--post_links`).
  6. Markdown Log: Change `update_log` to `md_log` (CLI: `--md_log`).
  7. DB Limit: Change `max_db_records` and CLI `--max-records` to `db_limit` (CLI: `--db_limit`).
  8. Age: Change `min_post_age_hours` and CLI `--age` to `min_age_hours` (CLI: `--min_age_hours`).
  9. Blacklist Terms: Change `filter_keywords` and CLI `--filter` to `blacklist_terms` (CLI: `--blacklist_terms`).
  10. Blacklist URLs: Change `url_blacklist` and CLI `--blacklist` to `blacklist_urls` (CLI: `--blacklist_urls`).
  11. Source Grouping: Change `generate_subreddit_folders` and CLI `--folders` to `group_by_source` (CLI: `--group_by_source`).

  Corrections & Optimizations Noticed in Your Notes:
  - Correction 1: In the "Correct" Python resource example, you wrote `scraper.run(subreddit_name="MarvelComics", overrides=...)`. To be fully consistent, `subreddit_name` should also be changed to `source`.
  - Optimization 1 (CLI Flags): Your notes mix hyphens and underscores for CLI flags (e.g., `--md-log` vs `--max_results`). Standard POSIX conventions use hyphens (`--max-results`), which Python's `argparse` automatically translates to variables with underscores (`args.max_results`). While I will implement exactly what you requested in your corrected blocks, you may want to standardize the CLI flags to exclusively use hyphens in the future for a cleaner user experience.
---
"""

if not content.startswith('---'):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(yaml_frontmatter + content)
    print("Added YAML frontmatter.")
else:
    print("File already has YAML frontmatter.")
