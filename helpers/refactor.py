import os
import re

files_to_update = [
    'modules/reddit2md/README.md',
    'modules/reddit2md/config.json',
    'modules/reddit2md/reddit2md/scraper.py',
    'modules/reddit2md/reddit2md/core/config.py',
    'modules/reddit2md/reddit2md/core/processor.py',
    'modules/reddit2md/reddit2md/core/database.py',
    'modules/reddit2md/reddit2md/core/reddit_client.py',
    'modules/reddit2md/architecture.md',
    'sandman.py'
]

# replacements order matters to avoid partial overlaps
# Using word boundaries carefully
replacements = [
    (r'\bsubreddit_name\b', 'source'),
    (r'--subreddit\b', '--source'),
    
    (r'\bpost_limit\b', 'max_results'),
    (r'--limit\b', '--max-results'),
    
    (r'\bcomment_detail\b', 'detail'),
    # --detail is already --detail
    
    (r'\bflair\b', 'label'),
    (r'--flair\b', '--label'),
    
    (r'\bpost_link\b', 'post_links'),
    (r'--post-link\b', '--post-links'),
    
    (r'\bupdate_log\b', 'md_log'),
    (r'--update-log\b', '--md-log'),
    
    (r'\bmax_db_records\b', 'db_limit'),
    (r'--max-records\b', '--db-limit'),
    
    (r'\bmin_post_age_hours\b', 'min_age_hours'),
    (r'--age\b', '--min-age-hours'),
    
    (r'\bfilter_keywords\b', 'blacklist_terms'),
    (r'--filter\b', '--blacklist-terms'),
    
    (r'\burl_blacklist\b', 'blacklist_urls'),
    (r'--blacklist\b', '--blacklist-urls'),
    
    (r'\bgenerate_subreddit_folders\b', 'group_by_source'),
    (r'--folders\b', '--group-by-source'),
    
    # Specific replacements for config dictionary keys
    (r"config\.get\('name'", "config.get('source'"),
    (r"config\.get\('subreddit'", "config.get('source'"),
    (r'"name":', '"source":'),
]

for filepath in files_to_update:
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (does not exist)")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Refactor complete.")
