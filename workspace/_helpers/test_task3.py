import subprocess
import os

print("--- Testing Task 3: Offset ---")

print("1. Testing jobs2md CLI offset parameter")
res = subprocess.run(["python3", "modules/jobs2md/jobs2md.py", "--query", "test", "--sources", "indeed", "--offset", "5", "--verbose", "0"], capture_output=True, text=True)
if "Error" not in res.stderr and res.returncode == 0:
    print("SUCCESS: jobs2md CLI offset parsed successfully")
else:
    print(f"FAIL: jobs2md CLI: {res.stderr}")

print("2. Testing reddit2md CLI offset injection")
res = subprocess.run(["python3", "modules/reddit2md/reddit2md.py", "--source", "test", "--offset", "5", "--verbose", "0"], capture_output=True, text=True)
if "Error" not in res.stderr and res.returncode == 0:
    print("SUCCESS: reddit2md CLI offset parsed properly")
else:
    print(f"FAIL: reddit2md CLI: {res.stderr}")

print("3. Testing reddit2md python override")
content = """
import sys
sys.path.append('modules/reddit2md')
from reddit2md.scraper import RedditScraper
scraper = RedditScraper(overrides={'verbose': 0, 'offset': 5, 'max_results': 1})
try:
    scraper.run(source='news')
    print("PYTHON SUCCESS")
except Exception as e:
    print(f"PYTHON FAIL: {e}")
"""
with open("test_python_offset.py", "w") as f:
    f.write(content)

res = subprocess.run(["python3", "test_python_offset.py"], capture_output=True, text=True)
if "PYTHON SUCCESS" in res.stdout:
    print("SUCCESS: reddit2md Python offset overrides")
else:
    print(f"FAIL: reddit2md Python: {res.stdout}\n{res.stderr}")
    
os.remove("test_python_offset.py")
