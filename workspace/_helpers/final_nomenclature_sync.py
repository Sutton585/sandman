import os
import re

def replace_in_file(filepath, old, new):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace(old, new)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

# 1. Update nomenclature.md to be precise
nomenclature_standard = """## 3. Configuration File Architecture & Philosophy

The Sandman ecosystem relies on YAML configuration files (`config.yml`) to dictate behavior. The architecture of these files is split into two distinct sections:

1.  **Global Defaults (`global_defaults`)**: This section establishes the baseline parameters for any execution (such as output directories, default logging verbosity, and standard timeouts).
2.  **Routine (`routine`)**: This section defines an ordered list of specific tasks to execute when the module is run without arguments. 

The routine is a to-do list for calls to this script that don't have any specific parameters. You can have multiple entries in this queue targeting the exact same source with completely different parameters if you choose. It is the default automated routine, enabling the user to run the script without arguments on a cron schedule and retrieve their customized source of data."""

with open('docs/nomenclature.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # Find the "## Configuration File Architecture & Philosophy" header
    for i, line in enumerate(lines):
        if "## Configuration File Architecture & Philosophy" in line:
            new_lines = lines[:i] + [nomenclature_standard + "\n"]
            with open('docs/nomenclature.md', 'w', encoding='utf-8') as f2:
                f2.writelines(new_lines)
            print("Cleaned up docs/nomenclature.md")
            break

# 2. Update unified_module_blueprint.md
blueprint_replacements = [
    ("simple cron jobs", "simple cron schedules"),
    ("## 4. The Execution Architecture: The Job Model", "## 4. The Execution Architecture: The Routine Model"),
    ("Iterates through the Routine", "Iterates through the routine queue"),
    ("array of tasks in the routine", "array of tasks in the routine section of the config"),
    ("default jobs.", "default routine."),
    ("default jobs.", "default routine."),
]
for old, new in blueprint_replacements:
    replace_in_file('modules/unified_module_blueprint.md', old, new)

# 3. Update reddit2md README
reddit_yaml_example = """### Using the Configuration File
The config.yml file allows you to set global defaults and then define a list of specific tasks in the routine. This is the best way to manage a large list of scrape tasks for a daily digest. Note that you can have multiple tasks for the same subreddit with different settings.

```yaml
global_defaults:
  output_directory: "My Vault/Reddit"
  min_score: 50
  data_directory: "data"
  group_by_source: true

routine:
  - source: "MarvelComics"
    sort: "top"
  - source: "MarvelComics"
    detail: "XL"
```"""

with open('modules/reddit2md/README.md', 'r', encoding='utf-8') as f:
    content = f.read()
    # Find the section to replace
    pattern = r"### Using the Configuration File.*?\n\n```json.*?```"
    new_content = re.sub(pattern, reddit_yaml_example, content, flags=re.DOTALL)
    if new_content != content:
        with open('modules/reddit2md/README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated modules/reddit2md/README.md example")

# 4. Update job2md README
job_yaml_example = """## Proof of concept usage from Sandman layer
Sandman layer uses the same interfaces (python, CLI, config files, etc.) so just like we can queue our default routine and global settings defaults in our config file in the module, we can do the same in sandman like so:

```yaml
global_defaults:
  debug: false
  md_output_directory: "../../workspace/feeds/reddit"
  md_log: true
  data_directory: "../../workspace/data/reddit/"
  group_by_source: true
  min_age_hours: 0
  min_score: 20
  max_results: 10

routine:
  - name: "Python-related jobs from indeed and glassdoor"
    module: "job2md"
    source: ["indeed", "glassdoor"]
    query: "python"
    max_age_hours: 336
    is_remote: true
  - name: "Docker-related jobs from indeed and glassdoor"
    module: "job2md"
    source: ["linkedIn"]
    query: "Docker"
    max_results: 10
    is_remote: true
```"""

with open('modules/job2md/README.md', 'r', encoding='utf-8') as f:
    content = f.read()
    # Find the section to replace
    pattern = r"## Proof of concept usage from Sandman layer.*?\n\n```json.*?```"
    new_content = re.sub(pattern, job_yaml_example, content, flags=re.DOTALL)
    
    # Also replace "queue:" with "routine:" if any remained
    new_content = new_content.replace('"queue":', 'routine:')
    
    if new_content != content:
        with open('modules/job2md/README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated modules/job2md/README.md example")

