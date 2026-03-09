import re
import os

files_to_update = [
    'modules/reddit2md/README.md',
    'modules/reddit2md/architecture.md',
    'modules/job2md/README.md',
    'modules/job2md/architecture.md',
    'modules/unified_module_blueprint.md',
    'README.md'
]

replacements = [
    (r'\bconfig\.json\b', 'config.yml'),
    (r'--save-json', '--save-json'), # Not strictly yaml config related but double check
    # Let's fix specific JSON config references to YAML config references
    (r'The Configuration File \(config\.yml\)', 'The Configuration File (`config.yml`)'),
    (r'\bconfig\.yml defines', '`config.yml` defines'),
]

for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Replace config.json with config.yml
        content = re.sub(r'\bconfig\.json\b', 'config.yml', content)
        
        # Update specific blueprint rules regarding YAML precedence over JSON for config
        if 'unified_module_blueprint.md' in filepath:
            content = content.replace('The Configuration File (config.yml)', 'The Configuration File (`config.yml`)')
            
        with open(filepath, 'w') as f:
            f.write(content)

