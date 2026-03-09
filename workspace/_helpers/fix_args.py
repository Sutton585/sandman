import re

filepath = 'modules/reddit2md/reddit2md/scraper.py'
with open(filepath, 'r') as f:
    content = f.read()

replacements = [
    (r'args\.limit', 'args.max_results'),
    (r'args\.age', 'args.min_age_hours'),
    (r'args\.folders', 'args.group_by_source'),
    (r'args\.max_records', 'args.db_limit'),
    (r'args\.filter', 'args.blacklist_terms'),
    (r'args\.blacklist', 'args.blacklist_urls'),
    (r'args\.subreddit', 'args.source'),
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open(filepath, 'w') as f:
    f.write(content)

