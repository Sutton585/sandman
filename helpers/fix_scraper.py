import re

with open('modules/reddit2md/reddit2md/scraper.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Update DB rebuilt logic
content = content.replace("frontmatter.get('subreddit', 'N/A')", "frontmatter.get('source', 'N/A')")
content = content.replace("frontmatter.get('author', 'N/A')", "frontmatter.get('poster', 'N/A')")
content = content.replace("frontmatter.get('flair', 'N/A')", "frontmatter.get('label', 'N/A')")

# Update usages of cleaned_post
content = content.replace("cleaned_post['subreddit']", "cleaned_post['source']")
content = content.replace("cleaned_post['author']", "cleaned_post['poster']")

with open('modules/reddit2md/reddit2md/scraper.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated scraper.py")
