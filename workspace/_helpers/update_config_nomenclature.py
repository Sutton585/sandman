import re
import os

files_to_update = [
    'README.md',
    'docs/nomenclature.md',
    'modules/unified_module_blueprint.md',
    'modules/reddit2md/README.md',
    'modules/reddit2md/architecture.md',
    'modules/jobs2md/README.md',
    'modules/jobs2md/architecture.md',
    'modules/gmail2md/README.md',
    'modules/gmail2md/architecture.md',
    'modules/web2md/README.md',
    'modules/web2md/architecture.md'
]

replacements = [
    (r'\bjob queue\b', 'routine'),
    (r'\bJob Queue\b', 'Routine'),
    (r'\bjobs:\b', 'routine:'),
    (r'\bjobs array\b', 'routine array'),
    (r'\bJobs array\b', 'Routine array'),
    (r'array of jobs', 'array of tasks in the routine'),
    (r'list of jobs', 'list of tasks in the routine'),
    (r'\bjobs defined in\b', 'routine defined in'),
    (r'multiple jobs for', 'multiple tasks for'),
    (r'test job to the master', 'test task to the master'),
    (r'job-specific settings', 'task-specific settings'),
    (r'Job-Specific Config', 'Task-Specific Config'),
    (r'one-off scrape jobs', 'one-off scrape tasks'),
    (r'default jobs\.', 'default routine.'),
    (r'Job Loop:', 'Routine Loop:'),
    (r'job config', 'task config'),
    (r'Job-Specific', 'Task-Specific')
]

# We don't want to replace the word "job" in the context of employment (especially in jobs2md).
# So we are very specific with our replacements above.

for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for old, new in replacements:
            # We use ignorecase for some, but others we explicitly specified case above.
            # To be safe, we'll do exact string replacements or regex without re.IGNORECASE.
            content = re.sub(old, new, content)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")
    else:
        print(f"File not found: {filepath}")

print("Markdown documentation update complete.")
