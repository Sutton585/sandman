import re

filepath = 'modules/unified_module_blueprint.md'
with open(filepath, 'r') as f:
    content = f.read()

# Replace all old nomenclature references in the blueprint
replacements = [
    (r'--limit 5, --detail XL', '--max-results 5, --detail XL'),
    (r'update_log \(Boolean\)', 'md_log (Boolean)'),
    (r'max_db_records \(Integer\)', 'db_limit (Integer)'),
    (r'min_post_age_hours \(Integer\)', 'min_age_hours (Integer)'),
    (r'max_db_records integer setting', 'db_limit integer setting'),
    (r'min_post_age_hours to 0', 'min_age_hours to 0'),
    (r'project or flair', 'project or label'),
    (r'post_link: \(Formerly story_link\)', 'post_links: (Formerly story_link)'),
    (r'generate_subreddit_folders', 'group_by_source')
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open(filepath, 'w') as f:
    f.write(content)

