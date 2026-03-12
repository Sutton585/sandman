import os
import re

def update_file(path, replacements):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return

    new_content = content
    for old, new in replacements:
        new_content = new_content.replace(old, new)
        
    if content != new_content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {path}")

# Note: We replaced job2md with jobs2md earlier in the filesystem but need to update references.
# We also need to update global_defaults -> settings, 
# output_directory -> md_output_directory
# data_directory -> data_output_directory (except in specific contexts where it's not a setting maybe, but usually it is)
# scrape_log_path -> md_log

replacements = [
    ('job2md', 'jobs2md'),
    ('global_defaults', 'settings'),
    ('output_directory', 'md_output_directory'),
    ('data_directory', 'data_output_directory'),
    ('scrape_log_path', 'md_log')
]

for root, dirs, files in os.walk('.'):
    # skip .git, venv, data, node_modules etc.
    if any(x in root for x in ['.git', 'venv', 'node_modules', '__pycache__', 'workspace/data', 'workspace/feeds', 'data/markdown']):
        continue
        
    for file in files:
        if file.endswith(('.py', '.yml', '.yaml', '.md', '.json')):
            # skip the helper scripts themselves to avoid recursion issues
            if 'workspace/_helpers' in root and file == 'apply_nomenclature.py':
                continue
            # avoid overwriting already correctly updated docs/nomenclature.md if possible
            if file == 'nomenclature.md' and 'docs' in root:
                continue
            
            filepath = os.path.join(root, file)
            update_file(filepath, replacements)

print("Done.")
