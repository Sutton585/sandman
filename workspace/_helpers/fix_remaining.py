import re

# Update README.md
with open('README.md', 'r') as f:
    content = f.read()

content = re.sub(r'Scrapes subreddits', 'Scrapes subreddits (sources)', content)

with open('README.md', 'w') as f:
    f.write(content)

# Update reddit2md/architecture.md
with open('modules/reddit2md/architecture.md', 'r') as f:
    content = f.read()

replacements = [
    (r'\bflair\b', 'label'),
    (r'\bsubreddit\b', 'source'),
    (r'\bpost_limit\b', 'max_results'),
    (r'\bcomment_detail\b', 'detail'),
    (r'\bmin_post_age_hours\b', 'min_age_hours'),
    (r'\bfilter_keywords\b', 'blacklist_terms'),
    (r'\burl_blacklist\b', 'blacklist_urls'),
    (r'\bgenerate_subreddit_folders\b', 'group_by_source'),
    (r'\bmax_db_records\b', 'db_limit')
]

for old, new in replacements:
    content = re.sub(old, new, content)

# Fix link_label_text (doesn't make sense, it is link_flair_text in reddit api)
content = re.sub(r'link_label_text', 'link_flair_text', content)
# Fix sub_name_prefixed
content = re.sub(r'source_name_prefixed', 'subreddit_name_prefixed', content)

with open('modules/reddit2md/architecture.md', 'w') as f:
    f.write(content)
