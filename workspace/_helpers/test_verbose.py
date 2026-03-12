import subprocess
import os

print("--- Testing CLI ---")
print("1. Testing jobs2md with --verbose 0")
res = subprocess.run(["python3", "modules/jobs2md/jobs2md.py", "--query", "test", "--sources", "indeed", "--verbose", "0"], capture_output=True, text=True)
if "Executing Task:" not in res.stdout:
    print("SUCCESS: CLI verbose 0 blocked standard output")
else:
    print("FAIL: CLI verbose 0 failed")

print("2. Testing jobs2md with --verbose 1")
res = subprocess.run(["python3", "modules/jobs2md/jobs2md.py", "--query", "test", "--sources", "indeed", "--verbose", "1"], capture_output=True, text=True)
if "Executing Task:" in res.stdout:
    print("SUCCESS: CLI verbose 1 allowed standard output")
else:
    print("FAIL: CLI verbose 1 failed")

print("\n--- Testing Python Overrides ---")
print("3. Testing jobs2md via Python with verbose=0")
content = """
import sys
import os
sys.path.append('modules/jobs2md')
from jobs2md import JobScraper
scraper = JobScraper(overrides={'query': 'test', 'sources': ['indeed'], 'verbose': 0})
scraper.run()
"""
with open("test_python_verbose.py", "w") as f:
    f.write(content)

res = subprocess.run(["python3", "test_python_verbose.py"], capture_output=True, text=True)
if "Executing Task:" not in res.stdout:
    print("SUCCESS: Python verbose 0 blocked standard output")
else:
    print("FAIL: Python verbose 0 failed")
    
os.remove("test_python_verbose.py")
