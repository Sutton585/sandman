import re

with open('modules/reddit2md/reddit2md/core/processor.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update clean_json
content = content.replace(
    "'author': post_data.get('author'),",
    "'poster': post_data.get('author'),"
)
content = content.replace(
    "'subreddit': post_data.get('subreddit_name_prefixed'),",
    "'source': post_data.get('subreddit_name_prefixed'),"
)
content = content.replace(
    "'link_flair_text': post_data.get('link_flair_text'),",
    "'label': post_data.get('link_flair_text'),"
)

# Also for comments author
content = content.replace(
    "'author': data.get('author', 'N/A'),",
    "'poster': data.get('author', 'N/A'),"
)

# 2. Update usages in the file
content = content.replace("cleaned_post['subreddit']", "cleaned_post['source']")
content = content.replace("cleaned_post['author']", "cleaned_post['poster']")
content = content.replace("cleaned_post.get('link_flair_text')", "cleaned_post.get('label')")
content = content.replace("c['author']", "c['poster']")

# 3. Update fm_data
old_fm = """        # Prepare Frontmatter
        fm_data = {
            'tags': '[reddit, scraped]',
            'source_url': f"https://reddit.com{cleaned_post['permalink']}",
            'subreddit': cleaned_post['source'],
            'author': cleaned_post['poster'],
            'post_date': datetime.fromtimestamp(cleaned_post['post_timestamp']).strftime("%Y-%m-%d"),
            'scrape_date': datetime.now().strftime("%Y-%m-%d"),
            'post_id': post_id,
            'score': cleaned_post['score'],
            'type': post_type,
            'flair': flair,
        }
        if rescrape_after: fm_data['rescrape_after'] = rescrape_after
        if resolved_post_links: fm_data['post_link'] = ", ".join(resolved_post_links)"""

new_fm = """        # Prepare Frontmatter
        fm_data = {
            'post_URL': f"https://reddit.com{cleaned_post['permalink']}",
            'source': cleaned_post['source'],
            'poster': cleaned_post['poster'],
            'date_posted': datetime.fromtimestamp(cleaned_post['post_timestamp']).strftime("%Y-%m-%d"),
            'date_scraped': datetime.now().strftime("%Y-%m-%d"),
            'post_id': post_id,
            'score': cleaned_post['score'],
            'module': 'reddit2md',
            'label': flair,
        }
        if rescrape_after: fm_data['rescrape_after'] = rescrape_after
        if resolved_post_links: fm_data['post_links'] = ", ".join(resolved_post_links)"""

content = content.replace(old_fm, new_fm)

with open('modules/reddit2md/reddit2md/core/processor.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated processor.py")
