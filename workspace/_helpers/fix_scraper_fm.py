import re

with open('modules/reddit2md/reddit2md/scraper.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix frontmatter parsing
content = content.replace("frontmatter.get('post_date')", "frontmatter.get('date_posted')")
content = content.replace("frontmatter.get('flair')", "frontmatter.get('label')")

with open('modules/reddit2md/reddit2md/scraper.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated scraper.py again")
