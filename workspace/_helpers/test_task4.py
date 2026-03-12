import subprocess
import os

print("--- Testing Task 4: Sorting Clarification ---")

print("1. Testing jobs2md rejects or ignores sorting")
res = subprocess.run(["python3", "modules/jobs2md/jobs2md.py", "--query", "test", "--sources", "indeed", "--sort", "new", "--verbose", "0"], capture_output=True, text=True)
if "unrecognized arguments" in res.stderr:
    print("SUCCESS: jobs2md CLI correctly rejects --sort flag")
else:
    print(f"FAIL: jobs2md CLI did not reject sort: {res.stderr}")

print("2. Testing reddit2md accepts sort")
res = subprocess.run(["python3", "modules/reddit2md/reddit2md.py", "--source", "test", "--sort", "top", "--verbose", "0"], capture_output=True, text=True)
if "unrecognized arguments" not in res.stderr:
    print("SUCCESS: reddit2md CLI accepted --sort flag")
else:
    print(f"FAIL: reddit2md CLI rejected sort: {res.stderr}")

