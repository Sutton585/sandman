import requests
import sys
import json

url = "https://www.reddit.com/r/MachineLearning/comments/1ro7zez/d_simtoreal_in_robotics_what_are_the_actual/.json?limit=1"

def test_headers(headers, attempt_name):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"[{attempt_name}] SUCCESS! Score: {data[0]['data']['children'][0]['data'].get('score')}")
                return True
            except:
                print(f"[{attempt_name}] 200 OK, but not JSON (likely blocked HTML).")
        else:
            print(f"[{attempt_name}] FAILED with status {response.status_code}")
    except Exception as e:
        print(f"[{attempt_name}] ERROR: {e}")
    return False

# Attempt 1: Googlebot
headers_1 = {
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Accept': '*/*'
}

# Attempt 2: Bingbot
headers_2 = {
    'User-Agent': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Accept': '*/*'
}

# Attempt 3: Standard Browser with full headers
headers_3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}

# Attempt 4: Custom Python script spoofing (Reddit API requires specific format sometimes)
headers_4 = {
    'User-Agent': 'python:sandman.reddit2md:v3.0 (by /u/sutton585)',
}

# Attempt 5: Mobile User-Agent
headers_5 = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Accept': 'application/json, text/plain, */*'
}

# Attempt 6: Old Firefox
headers_6 = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

# Attempt 7: Minimalist curl
headers_7 = {
    'User-Agent': 'curl/7.81.0',
    'Accept': '*/*'
}

# Attempt 8: Empty User-Agent (sometimes bypasses naive filters)
headers_8 = {
    'User-Agent': '',
    'Accept': '*/*'
}

# Attempt 9: Valid API bot string
headers_9 = {
    'User-Agent': 'bot',
}

# Attempt 10: Googlebot with referer
headers_10 = {
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Referer': 'https://www.google.com/',
    'Accept': 'application/json'
}


attempts = [
    (headers_1, "1: Googlebot"),
    (headers_2, "2: Bingbot"),
    (headers_3, "3: Full Browser Headers"),
    (headers_4, "4: Reddit API Style UA"),
    (headers_5, "5: Mobile UA"),
    (headers_6, "6: Firefox UA"),
    (headers_7, "7: cURL UA"),
    (headers_8, "8: Empty UA"),
    (headers_9, "9: Generic Bot UA"),
    (headers_10, "10: Googlebot with Referer")
]

for headers, name in attempts:
    test_headers(headers, name)

