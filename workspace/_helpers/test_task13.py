import subprocess
import os

print("--- Testing Task 13: Decouple Age Filtering ---")

print("1. Testing reddit2md CLI min-age filtering")
res = subprocess.run(["python3", "modules/reddit2md/reddit2md.py", "--source", "test", "--min-age-hours", "1000", "--verbose", "0"], capture_output=True, text=True)
if "Error" not in res.stderr and res.returncode == 0:
    print("SUCCESS: reddit2md CLI min-age filtering parsed properly")
else:
    print(f"FAIL: reddit2md CLI: {res.stderr}")

print("2. Testing reddit2md CLI rescrape-threshold parsing")
res = subprocess.run(["python3", "modules/reddit2md/reddit2md.py", "--source", "test", "--rescrape-threshold-hours", "24", "--verbose", "0"], capture_output=True, text=True)
if "Error" not in res.stderr and res.returncode == 0:
    print("SUCCESS: reddit2md CLI rescrape_threshold_hours parsed properly")
else:
    print(f"FAIL: reddit2md CLI: {res.stderr}")

print("3. Testing reddit2md python override")
content = """
import sys
sys.path.append('modules/reddit2md')
from reddit2md.scraper import RedditScraper
scraper = RedditScraper(overrides={'verbose': 0, 'rescrape_threshold_hours': 24, 'min_age_hours': 12})
try:
    scraper.run(source='news')
    print("PYTHON SUCCESS")
except Exception as e:
    print(f"PYTHON FAIL: {e}")
"""
with open("test_python_task13.py", "w") as f:
    f.write(content)

res = subprocess.run(["python3", "test_python_task13.py"], capture_output=True, text=True)
if "PYTHON SUCCESS" in res.stdout:
    print("SUCCESS: reddit2md Python threshold overrides")
else:
    print(f"FAIL: reddit2md Python: {res.stdout}\n{res.stderr}")
    
os.remove("test_python_task13.py")
