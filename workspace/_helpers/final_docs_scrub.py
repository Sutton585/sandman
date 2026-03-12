import os
import re

def update_file(filepath, mapping):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content
    for old, new in mapping:
        new_content = re.sub(old, new, new_content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

# 1. reddit2md/architecture.md mapping fixes
reddit_arch_fixes = [
    (r'time_scraped', 'date_scraped'),
    (r'time_posted', 'date_posted'),
    (r'metadata_label', 'label'),
]
update_file('modules/reddit2md/architecture.md', reddit_arch_fixes)

# 2. reddit2md/README.md typo fix
reddit_readme_fixes = [
    (r'--blacklist-urls-terms', '--blacklist-terms'),
    (r'nightly', 'automated'),
    (r'Weekly', 'Recurring'),
]
update_file('modules/reddit2md/README.md', reddit_readme_fixes)

# 3. jobs2md/architecture.md sources pluralization
job_arch_fixes = [
    (r'\bsource\b', 'sources'),
    (r'--source\b', '--sources'),
]
update_file('modules/jobs2md/architecture.md', job_arch_fixes)

# 4. Global terminology scrub
global_scrub = [
    (r'(?i)nightly', 'recurring'),
    (r'(?i)weekly', 'periodic'),
    (r'(?i)daily', 'regular'),
    (r'(?i)digest', 'collection'),
]
for root, dirs, files in os.walk('.'):
    if any(ignore in root for ignore in ['.git', 'venv', 'node_modules', 'data']):
        continue
    for file in files:
        if file.endswith('.md'):
            update_file(os.path.join(root, file), global_scrub)

