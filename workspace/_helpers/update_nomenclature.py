import os
import re

# Define the root directory of the project
root_dir = "."

# Define the files to ignore (e.g., hidden directories, venv, etc.)
ignore_dirs = [".git", "venv", "__pycache__", "node_modules", "data", "archive"]

# Define the replacements
# Note: We use specific regex to avoid replacing "job" in the context of employment
replacements = [
    # 1. Terminology replacements
    (r'\bjob queue\b', 'routine'),
    (r'\bJob Queue\b', 'Routine'),
    (r'\bjob-specific\b', 'task-specific'),
    (r'\bJob-Specific\b', 'Task-Specific'),
    (r'\bdefault jobs\b', 'default routine'),
    (r'\bscrape jobs\b', 'scrape tasks'),
    (r'\bconfigured jobs\b', 'configured routine'),
    (r'\bJob Loop\b', 'Routine Loop'),
    (r'\bjob array\b', 'routine array'),
    
    # 2. Config file replacements
    (r'config\.json', 'config.yml'),
    
    # 3. YAML key replacements (careful with these)
    (r'\bjobs:\s*\[', 'routine: ['),
    (r'\bjobs:\s*\n', 'routine:\n'),
    (r'\b\"jobs\":\s*\[', '\"routine\": ['),
]

def update_markdown_files():
    for dirpath, dirs, filenames in os.walk(root_dir):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = os.path.join(dirpath, filename)
                print(f"Processing: {file_path}")
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for pattern, replacement in replacements:
                    new_content = re.sub(pattern, replacement, new_content, flags=re.IGNORECASE if "config" not in pattern else 0)
                
                # Special handling for job2md specific cases to ensure we don't break employment references
                # Actually, the regex \b (word boundary) should handle most cases.
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")

if __name__ == "__main__":
    update_markdown_files()
