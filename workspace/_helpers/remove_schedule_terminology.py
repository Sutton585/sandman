import os
import re

replacements = [
    (r'execution cycle', 'execution cycle'),
    (r'on a recurring schedule', 'on a recurring schedule'),
    (r'for later review', 'for later review'),
    (r'Sandman Orchestrator', 'Sandman Orchestrator'),
    (r'execution cycle', 'Standard Cycle'),
    (r'Knowledge Collection', 'Knowledge Collection'),
    (r'Knowledge Collection', 'knowledge collection'),
    (r'personalized Knowledge Collections', 'individual knowledge feeds'),
    (r'periodically', 'periodically'),
    (r'recurring automations', 'recurring automations'),
    (r'curated feeds', 'curated feeds'),
    (r'Recurring', 'Recurring'),
]

files_to_process = []
for root, dirs, files in os.walk('.'):
    if any(ignore in root for ignore in ['.git', 'venv', 'node_modules', 'data']):
        continue
    for file in files:
        if file.endswith('.md') or file.endswith('.py') or file.endswith('.yml'):
            files_to_process.append(os.path.join(root, file))

for filepath in files_to_process:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for pattern, replacement in replacements:
        new_content = re.sub(pattern, replacement, new_content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Scrubbed schedule terminology from {filepath}")

# Final JSON purge
gmail_json = 'modules/gmail2md/config.json'
if os.path.exists(gmail_json):
    os.remove(gmail_json)
    print(f"Removed legacy JSON config: {gmail_json}")

