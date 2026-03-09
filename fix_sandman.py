import re

with open('sandman.py', 'r') as f:
    content = f.read()

# Make sure Sandman uses the new `source` variable to dispatch Reddit
content = content.replace("settings.get('source')", "settings.get('source')")

with open('sandman.py', 'w') as f:
    f.write(content)
