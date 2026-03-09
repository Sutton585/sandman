import json
import urllib.request

req = urllib.request.Request(
    "https://www.reddit.com/r/MachineLearning/comments/1ro7zez/d_simtoreal_in_robotics_what_are_the_actual/.json?limit=1000",
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
)
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print("Score:", data[0]['data']['children'][0]['data'].get('score'))
except Exception as e:
    print(e)
