import os
import re

# Terminology replacements mapping
replacements = [
    # 1. Schedule & Purpose Neutrality
    (r'Sandman Sandman Orchestrator', 'Sandman Orchestrator'),
    (r'Sandman Orchestrator', 'Orchestrator'),
    (r'execution cycle', 'Standard Cycle'),
    (r'execution cycle', 'execution cycle'),
    (r'Knowledge Collection', 'knowledge collection'),
    (r'Recurring digest', 'curated feed'),
    (r'Knowledge Collection', 'Knowledge Collection'),
    (r'Recurring Digest', 'Curated Feed'),
    (r'personalized Knowledge Collections', 'high-fidelity knowledge feeds'),
    (r'for use in Knowledge Collections', 'for research and archival'),
    (r'daily or Recurring digest', 'curated data stream'),
    (r'daily-driver', 'persistent'),
    (r'every Monday morning via cron', 'whenever needed'),
    (r'cron schedule', 'recurring schedule'),
    (r'cron tasks', 'automated tasks'),
    (r'cron schedules', 'automated schedules'),
    
    # 2. jobs2md: source -> sources (when referring to job boards)
    # This is tricky because "source" is used generically too.
    # In config.yml and jobs2md code, we'll be surgical.
]

def update_file(filepath, mapping):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for pattern, replacement in mapping:
        new_content = re.sub(pattern, replacement, new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

# Process all markdown files for terminology
for root, dirs, files in os.walk('.'):
    if any(ignore in root for ignore in ['.git', 'venv', 'node_modules', 'data']):
        continue
    for file in files:
        if file.endswith('.md'):
            update_file(os.path.join(root, file), replacements)

# Specifically update sandman.py and config.yml
update_file('sandman.py', replacements)
update_file('config.yml', replacements)

# 2. Update jobs2md specifically for sources pluralization
jobs2md_replacements = [
    (r'\bsource\b', 'sources'),
    (r'--source\b', '--sources'),
]

# Surgery on jobs2md files
update_file('modules/jobs2md/jobs2md.py', jobs2md_replacements)
update_file('modules/jobs2md/core/config.py', jobs2md_replacements)
update_file('modules/jobs2md/config.yml', jobs2md_replacements)
# Root config.yml jobs section also needs "sources" for jobs2md
update_file('config.yml', [
    (r'module: \"jobs\"\n    source:', 'module: \"jobs\"\n    sources:'),
    (r'module: \"jobs\"\n    sources: \"indeed\"', 'module: \"jobs\"\n    sources: [\"indeed\"]'), # fix accidental string if it happens
])

# 3. reddit2md JSON purge
if os.path.exists('modules/reddit2md/config.json'):
    os.remove('modules/reddit2md/config.json')
    print("Deleted modules/reddit2md/config.json")

# Ensure reddit2md code uses "routine" and "config.yml"
# (Wait, I already updated core/config.py and scraper.py in previous turn, 
# but let's double check specific strings like "jobs" in dict keys)
reddit_cleanup = [
    (r'\"jobs\":', '\"routine\":'),
    (r'config\.json', 'config.yml'),
]
update_file('modules/reddit2md/reddit2md/core/config.py', reddit_cleanup)
update_file('modules/reddit2md/reddit2md/scraper.py', reddit_cleanup)

print("Final Terminology Cleanup Script execution complete.")
