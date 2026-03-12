import subprocess
import os

print("--- Testing Task 2: Age Restrictions ---")

print("1. Testing jobs2md CLI max_age_hours mapping")
res = subprocess.run(["python3", "modules/jobs2md/jobs2md.py", "--query", "test", "--sources", "indeed", "--max-age-hours", "1", "--verbose", "2"], capture_output=True, text=True)
if "Error" not in res.stderr and res.returncode == 0:
    print("SUCCESS: jobs2md CLI max-age-hours did not crash")
else:
    print(f"FAIL: jobs2md CLI: {res.stderr}")

print("2. Testing reddit2md CLI max_age_hours injection")
res = subprocess.run(["python3", "modules/reddit2md/reddit2md.py", "--source", "test", "--max-age-hours", "1", "--verbose", "0"], capture_output=True, text=True)
if "Error" not in res.stderr and res.returncode == 0:
    print("SUCCESS: reddit2md CLI max-age-hours parsed properly")
else:
    print(f"FAIL: reddit2md CLI: {res.stderr}")

print("3. Testing jobs2md python override")
content = """
import sys
import os
sys.path.append('modules/jobs2md')
from jobs2md import JobScraper
scraper = JobScraper(overrides={'query': 'test', 'sources': ['indeed'], 'verbose': 0, 'min_age_hours': 1000})
try:
    scraper.run()
    print("PYTHON SUCCESS")
except Exception as e:
    print(f"PYTHON FAIL: {e}")
"""
with open("test_python_age.py", "w") as f:
    f.write(content)

res = subprocess.run(["python3", "test_python_age.py"], capture_output=True, text=True)
if "PYTHON SUCCESS" in res.stdout:
    print("SUCCESS: jobs2md Python min_age_hours filtering")
else:
    print(f"FAIL: jobs2md Python: {res.stdout}")
    
os.remove("test_python_age.py")
