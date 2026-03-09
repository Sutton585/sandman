import yaml
import re

with open('config.yml', 'r') as f:
    content = f.read()

replacements = [
    (r'update_log:', 'md_log:'),
    (r'subreddit:', 'source:'),
    (r'limit:', 'max_results:'),
    (r'min_post_age_hours:', 'min_age_hours:'),
    (r'generate_folders:', 'group_by_source:'),
    (r'search_term:', 'query:'),
    (r'sources:', 'source:') # wait, for jobs it was 'sources: ["indeed"...]' -> 'source: ["indeed"...]'
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open('config.yml', 'w') as f:
    f.write(content)

