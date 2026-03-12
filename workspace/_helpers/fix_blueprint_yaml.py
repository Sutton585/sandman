import re

filepath = 'modules/unified_module_blueprint.md'
with open(filepath, 'r') as f:
    content = f.read()

# Add a specific paragraph clarifying our config approach.
# We will insert it under Section 4A where it talks about the config file.

old_section = """### A. The Configuration File (`config.yml`)
Used for persistent, automated, daily-driver setups. It must contain:
1.  **Global Defaults**: A block defining fallback behaviors (like output directories, default logging verbosity, etc).
2.  **Job Queue**: An array of specific target entities and any custom overrides for that specific target."""

new_section = """### A. The Configuration File (`config.yml`)
**YAML Configuration Standard:** All Sandman modules MUST use YAML (`config.yml`) for their configuration files. While JSON was considered for strict standard-library portability, YAML is the officially supported standard because it allows for inline comments (`#`), which is critical for user-facing configuration files where complex parameters need explanation.

Used for persistent, automated, daily-driver setups. It must contain:
1.  **Global Defaults (`settings`)**: A block defining fallback behaviors (like output directories, default logging verbosity, etc).
2.  **Job Queue (`jobs`)**: An array of specific target entities and any custom overrides for that specific target."""

content = content.replace(old_section, new_section)

with open(filepath, 'w') as f:
    f.write(content)
