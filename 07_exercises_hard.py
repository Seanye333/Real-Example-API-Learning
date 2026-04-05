"""
=== EXERCISES: Hard Level ===

10 advanced exercises that test real-world API skills.
These involve sessions, retries, building helpers, and combining APIs.

APIs used (all free, no key needed):
- JSONPlaceholder: https://jsonplaceholder.typicode.com
- Cat Facts: https://catfact.ninja
- HTTPBin: https://httpbin.org (returns specific status codes)
- Open Meteo: https://api.open-meteo.com
"""

import requests
import time

score = 0
total = 10


# ============================================================
# Exercise 1: Use a Session for multiple requests
# ============================================================
print("Exercise 1: Use requests.Session for efficiency")
print("-" * 40)

# TODO: Create a requests.Session() with a custom User-Agent header
#       Then use that session to GET posts #1, #2, and #3
#       Store the titles in a list
#
# Why sessions? They reuse the TCP connection — faster for multiple
# requests to the same server. They also persist headers/cookies.

# Example:
#   session = requests.Session()
#   session.headers.update({"User-Agent": "API-Learner/1.0"})
#   response = session.get(url)

titles = None  # Should be a list of 3 titles

# --- Check ---
if (titles and isinstance(titles, list) and len(titles) == 3
        and titles[0] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"):
    print(f"  PASS — Got 3 titles using a session")
    score += 1
else:
    print(f"  FAIL — Expected 3 specific titles, got: {titles}")
    print("  Hint: Use session.get() in a loop for ids 1, 2, 3")
print()


# ============================================================
# Exercise 2: Retry on failure
# ============================================================
print("Exercise 2: Implement retry logic")
print("-" * 40)

# TODO: Write a function that retries a GET request up to 3 times
#       if it fails. Wait 1 second between retries.
#       Return the response JSON on success, or None after all retries fail.

def get_with_retry(url, max_retries=3):
    # Your code here
    return None

# --- Check (we test with a working URL) ---
result = get_with_retry("https://jsonplaceholder.typicode.com/posts/1")
if result and result.get("id") == 1:
    print("  PASS — Retry function works")
    score += 1
else:
    print(f"  FAIL — Expected post data, got: {result}")
    print("  Hint: Loop max_retries times, use try/except, time.sleep(1)")
print()


# ============================================================
# Exercise 3: Build a mini API client class
# ============================================================
print("Exercise 3: Build a JSONPlaceholder client class")
print("-" * 40)

# TODO: Create a class with these methods:
#   - __init__(self): set self.base_url
#   - get_post(self, post_id) -> dict
#   - get_user(self, user_id) -> dict
#   - create_post(self, title, body, user_id) -> dict

class JSONPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_post(self, post_id):
        # Your code here
        pass

    def get_user(self, user_id):
        # Your code here
        pass

    def create_post(self, title, body, user_id):
        # Your code here
        pass

# --- Check ---
client = JSONPlaceholderClient()
post = client.get_post(1)
user = client.get_user(1)
new = client.create_post("Test", "Body", 1)

if (post and post.get("id") == 1
        and user and user.get("name") == "Leanne Graham"
        and new and new.get("id") == 101):
    print("  PASS — Client class works for all 3 methods")
    score += 1
else:
    print(f"  FAIL — post={post}, user={user}, new={new}")
    print("  Hint: Each method should use requests.get/post and return .json()")
print()


# ============================================================
# Exercise 4: Collect all pages (pagination)
# ============================================================
print("Exercise 4: Collect ALL cat facts across all pages")
print("-" * 40)

# TODO: The cat facts API paginates results.
# GET https://catfact.ninja/facts?page=1 returns:
#   {"data": [...], "last_page": N, "current_page": 1, ...}
# Loop through all pages and collect every fact.
# Store the total count.
# IMPORTANT: Limit to first 5 pages max to avoid slow requests.

all_facts_count = None  # Your code here

# --- Check ---
if all_facts_count and isinstance(all_facts_count, int) and all_facts_count > 40:
    print(f"  PASS — Collected {all_facts_count} facts across pages")
    score += 1
else:
    print(f"  FAIL — Expected > 40 facts, got: {all_facts_count}")
    print("  Hint: Loop page=1 to 5, extend a list with each page's data")
print()


# ============================================================
# Exercise 5: Build a user activity report
# ============================================================
print("Exercise 5: Build an activity report for user #1")
print("-" * 40)

# TODO: For user #1, fetch their:
#   - posts (GET /posts?userId=1)
#   - todos (GET /todos?userId=1)
#   - albums (GET /albums?userId=1)
# Build a report dict like:
#   {"name": "...", "post_count": N, "todo_count": N, "album_count": N}

report = None  # Your code here

# --- Check ---
if (report and isinstance(report, dict)
        and report.get("post_count") == 10
        and report.get("todo_count") == 20
        and report.get("album_count") == 10):
    print(f"  PASS — Report: {report}")
    score += 1
else:
    print(f"  FAIL — Expected post=10, todo=20, album=10, got: {report}")
print()


# ============================================================
# Exercise 6: Find related data across endpoints
# ============================================================
print("Exercise 6: Find all commenters on user #1's posts")
print("-" * 40)

# TODO: Step 1 — Get all posts by user #1
#       Step 2 — For each post, get its comments
#       Step 3 — Collect all unique commenter emails
#       NOTE: To keep it fast, only check the first 3 posts

unique_emails = None  # Should be a set or its length as int

# --- Check ---
if unique_emails and isinstance(unique_emails, (set, int)):
    count = len(unique_emails) if isinstance(unique_emails, set) else unique_emails
    if count == 15:
        print(f"  PASS — Found {count} unique commenter emails")
        score += 1
    else:
        print(f"  FAIL — Expected 15, got: {count}")
else:
    print(f"  FAIL — Expected a set of emails or count, got: {unique_emails}")
    print("  Hint: Loop through first 3 posts, get comments, collect emails into a set")
print()


# ============================================================
# Exercise 7: Handle different HTTP status codes
# ============================================================
print("Exercise 7: Map status codes to their meanings")
print("-" * 40)

# TODO: Use https://httpbin.org/status/{code} to request these status codes:
#   200, 201, 301, 404, 500
# Build a dict mapping each code to the response reason phrase
# Example: {200: "OK", 201: "Created", ...}
# IMPORTANT: Add timeout=5 and allow_redirects=False for 301

status_map = None  # Your code here

# --- Check ---
if (status_map and isinstance(status_map, dict)
        and status_map.get(200) == "OK"
        and status_map.get(404) == "Not Found"):
    print(f"  PASS — {status_map}")
    score += 1
else:
    print(f"  FAIL — Expected status map, got: {status_map}")
    print("  Hint: response.reason gives you 'OK', 'Not Found', etc.")
print()


# ============================================================
# Exercise 8: Get weather data
# ============================================================
print("Exercise 8: Get current temperature in Tokyo")
print("-" * 40)

# TODO: Use the Open-Meteo API (free, no key needed)
# API: https://api.open-meteo.com/v1/forecast
# Params: latitude=35.6762, longitude=139.6503, current_weather=true
# Store the current temperature

tokyo_temp = None  # Your code here (should be a number)

# --- Check ---
if tokyo_temp is not None and isinstance(tokyo_temp, (int, float)):
    print(f"  PASS — Tokyo temperature: {tokyo_temp}°C")
    score += 1
else:
    print(f"  FAIL — Expected a number, got: {tokyo_temp}")
    print("  Hint: response.json()['current_weather']['temperature']")
print()


# ============================================================
# Exercise 9: Batch operations
# ============================================================
print("Exercise 9: Create 5 posts in a batch")
print("-" * 40)

# TODO: Use a loop to create 5 posts via POST
# Each post should have: title=f"Post {i}", body=f"Body {i}", userId=1
# Collect all the returned IDs in a list

created_ids = None  # Should be a list of 5 IDs

# --- Check ---
if created_ids and isinstance(created_ids, list) and len(created_ids) == 5:
    print(f"  PASS — Created IDs: {created_ids}")
    score += 1
else:
    print(f"  FAIL — Expected 5 IDs, got: {created_ids}")
    print("  Hint: Loop range(1, 6), POST each, append response.json()['id']")
print()


# ============================================================
# Exercise 10: Build a search function
# ============================================================
print("Exercise 10: Search posts by keyword")
print("-" * 40)

# TODO: Write a function that:
#   1. GETs all posts from JSONPlaceholder
#   2. Filters posts where the keyword appears in the title (case-insensitive)
#   3. Returns a list of matching post titles

def search_posts(keyword):
    # Your code here
    return []

# --- Check ---
results = search_posts("qui")
if results and isinstance(results, list) and len(results) > 3:
    print(f"  PASS — Found {len(results)} posts matching 'qui'")
    print(f"         First: '{results[0][:50]}...'")
    score += 1
else:
    print(f"  FAIL — Expected multiple matches, got: {results}")
    print("  Hint: [p['title'] for p in posts if keyword.lower() in p['title'].lower()]")
print()


# ============================================================
# Results
# ============================================================
print("=" * 50)
print(f"HARD EXERCISES SCORE: {score}/{total}")
print("=" * 50)
if score == total:
    print("AMAZING! You've mastered Python API calls!")
    print("Next steps: Try building a real project that uses APIs.")
elif score >= 7:
    print("Impressive! You're nearly at expert level.")
elif score >= 4:
    print("Good progress! Review sessions, pagination, and error handling.")
else:
    print("Try the medium exercises first (06_exercises_medium.py).")
