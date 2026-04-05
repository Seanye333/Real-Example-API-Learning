"""
=== EXERCISES: Medium Level ===

10 intermediate exercises that combine multiple concepts.
These require you to chain requests, process data, and think more.

APIs used (all free, no key needed):
- JSONPlaceholder: https://jsonplaceholder.typicode.com
- Cat Facts: https://catfact.ninja
- Universities API: http://universities.hipolabs.com
"""

import requests

score = 0
total = 10


# ============================================================
# Exercise 1: Filter and count
# ============================================================
print("Exercise 1: How many completed todos does user #1 have?")
print("-" * 40)

# TODO: GET all todos for user 1, then count how many have completed=True
# API: https://jsonplaceholder.typicode.com/todos?userId=1

response = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1")
todos = response.json()
# WAY 1
# count = 0
# for todo in todos:
#     if todo['completed'] == True:
#         count += 1
# completed_count = count
# WAY2
completed_count = len([todo for todo in todos if todo['completed'] == True])
# --- Check ---
if completed_count == 11:
    print(f"  PASS — {completed_count} completed todos")
    score += 1
else:
    print(f"  FAIL — Expected 11, got: {completed_count}")
    print("  Hint: Get all todos for userId=1, then filter where todo['completed'] == True")
print()


# ============================================================
# Exercise 2: Get data from a nested URL
# ============================================================
print("Exercise 2: Get comments for post #3 using nested route")
print("-" * 40)

# TODO: Use the nested route to get comments for post #3
# API: https://jsonplaceholder.typicode.com/posts/3/comments
# Store the email of the FIRST comment

response = requests.get("https://jsonplaceholder.typicode.com/posts/3/comments")

first_comment_email = response.json()[0]['email']
#You don't need ['postId'] — you already filtered by post #3 in the URL (/posts/3/comments).
# --- Check ---
if first_comment_email and "@" in first_comment_email:
    print(f"  PASS — {first_comment_email}")
    score += 1
else:
    print(f"  FAIL — Expected an email address, got: {first_comment_email}")
print()


# ============================================================
# Exercise 3: Search universities by country
# ============================================================
print("Exercise 3: Find universities in Singapore")
print("-" * 40)

# TODO: Search for universities in Singapore
# API: http://universities.hipolabs.com/search?country=Singapore
# Store the total number of universities found

response = requests.get("http://universities.hipolabs.com/search", params = {'country':'Singapore'})
uni_count = len(response.json())  # Your code here

# --- Check ---
if uni_count and isinstance(uni_count, int) and uni_count > 0:
    print(f"  PASS — Found {uni_count} universities")
    score += 1
else:
    print(f"  FAIL — Expected a positive number, got: {uni_count}")
    print("  Hint: len(requests.get(url, params={'country': 'Singapore'}).json())")
print()


# ============================================================
# Exercise 4: Collect data from multiple requests
# ============================================================
print("Exercise 4: Get the titles of all albums by user #2")
print("-" * 40)

# TODO: GET all albums where userId=2
# API: https://jsonplaceholder.typicode.com/albums?userId=2
# Store all titles in a list

response = requests.get("https://jsonplaceholder.typicode.com/albums", params = {'userId':2})
# Way 1
# albums = response.json()
# album_titles = []
# for album in albums:
#     album_titles.append(album['title'])
#way 2
album_titles = [album['title'] for album in response.json()]
# --- Check ---
if album_titles and isinstance(album_titles, list) and len(album_titles) == 10:
    print(f"  PASS — Got {len(album_titles)} album titles")
    print(f"         First: '{album_titles[0]}'")
    score += 1
else:
    print(f"  FAIL — Expected a list of 10 titles, got: {album_titles}")
    print("  Hint: [album['title'] for album in response.json()]")
print()


# ============================================================
# Exercise 5: Chain two API calls
# ============================================================
print("Exercise 5: Get the name of the user who wrote post #42")
print("-" * 40)

# TODO: Step 1 — GET post #42 to find its userId
#       Step 2 — GET that user to find their name
# API: https://jsonplaceholder.typicode.com/posts/42
# API: https://jsonplaceholder.typicode.com/users/{userId}
response1 = requests.get('https://jsonplaceholder.typicode.com/posts/42')
userId = response1.json()['userId']
response2 = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
author_name = response2.json()['name'] # Your code here

# --- Check ---
if author_name == "Chelsey Dietrich":
    print(f"  PASS — {author_name}")
    score += 1
else:
    print(f"  FAIL — Expected 'Chelsey Dietrich', got: {author_name}")
    print("  Hint: First get the post, then use its userId to fetch the user")
print()


# ============================================================
# Exercise 6: Aggregate data
# ============================================================
print("Exercise 6: Which user has the most posts?")
print("-" * 40)

# TODO: GET all posts, count posts per userId, find who has the most
# API: https://jsonplaceholder.typicode.com/posts
# Store the userId with the most posts
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

# counts = {}
# for post in posts:
#     uid = post['userId']
#     if uid in counts:
#         counts[uid] += 1    # already seen this user, add 1
#     else:
#         counts[uid] = 1     # first time seeing this user, start at 1
counts = {}
for post in posts:
    uid = post['userId']
    counts[uid] = counts.get(uid, 0) + 1

top_poster_id = max(counts, key=counts.get)


# --- Check ---
# All users have 10 posts each, so userId=1 should be first when tied
if top_poster_id and isinstance(top_poster_id, int) and 1 <= top_poster_id <= 10:
    print(f"  PASS — User {top_poster_id} (all users have 10 posts each)")
    score += 1
else:
    print(f"  FAIL — Expected a userId (1-10), got: {top_poster_id}")
    print("  Hint: Use a dict to count posts per userId, then find the max")
print()


# ============================================================
# Exercise 7: Pagination with cat facts
# ============================================================
print("Exercise 7: Get cat facts from page 2")
print("-" * 40)

# TODO: GET cat facts from page 2 (the API paginates results)
# API: https://catfact.ninja/facts?page=2
# Store the number of facts returned on that page
#
# WHAT IS PAGINATION?
# Pagination means the API splits results into PAGES instead of
# sending everything at once — like a book with chapters.
#
# Imagine the API has 100 cat facts. Instead of sending all 100:
#   Page 1: facts 1-20    ← ?page=1
#   Page 2: facts 21-40   ← ?page=2
#   Page 3: facts 41-60   ← ?page=3
#   ...and so on
#
# WHY? Sending thousands of results at once would be slow.
# Pages keep responses small and fast.
#
# The response looks like this:
#   {
#       "current_page": 2,         ← which page you're on
#       "data": [                  ← the actual facts for THIS page
#           {"fact": "Cats sleep 16 hours...", "length": 30},
#           {"fact": "A group of cats...", "length": 35},
#           ...
#       ],
#       "last_page": 5,            ← total number of pages
#       "total": 100               ← total facts across ALL pages
#   }
#
# The facts are inside ['data'], so we use len() to count them.
response = requests.get('https://catfact.ninja/facts', params = {'page':2})
page2_count = len(response.json()['data'])

# --- Check ---
if page2_count and isinstance(page2_count, int) and page2_count > 0:
    print(f"  PASS — Page 2 has {page2_count} facts")
    score += 1
else:
    print(f"  FAIL — Expected a positive number, got: {page2_count}")
    print("  Hint: len(response.json()['data'])")
print()


# ============================================================
# Exercise 8: Create and then verify
# ============================================================
print("Exercise 8: POST a new post and verify it has the right title")
print("-" * 40)

# TODO: POST a new post with title="Verification Test", body="test", userId=1
# Then check that the RESPONSE contains title="Verification Test"
# API: https://jsonplaceholder.typicode.com/posts
my_post = {
    'title':'Verification Test', 
    'body':'test', 
    'userId':1
}
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json=my_post
)
verified = response.json()['title'] == 'Verification Test'


# --- Check ---
if verified is True:
    print("  PASS — POST response matches what we sent")
    score += 1
else:
    print(f"  FAIL — Expected True, got: {verified}")
    print("  Hint: response.json()['title'] == 'Verification Test'")
print()


# ============================================================
# Exercise 9: Extract unique values
# ============================================================
print("Exercise 9: How many unique userIds posted comments on post #1?")
print("-" * 40)

# TODO: GET all comments on post #1
# API: https://jsonplaceholder.typicode.com/comments?postId=1
# Count how many unique email domains (part after @) are in the comments
response = requests.get('https://jsonplaceholder.typicode.com/comments', params={'postId':1})
comments = response.json()
unique_domains = len({comment['email'].split('@')[1] for comment in comments})

# --- Check ---
if unique_domains == 5:
    print(f"  PASS — {unique_domains} unique email domains")
    score += 1
else:
    print(f"  FAIL — Expected 5, got: {unique_domains}")
    print("  Hint: {comment['email'].split('@')[1] for comment in comments}")
print()


# ============================================================
# Exercise 10: Robust request with timeout and error handling
# ============================================================
print("Exercise 10: Make a safe request with error handling")
print("-" * 40)

# TODO: Write a function that:
#   1. Makes a GET request to the given URL
#   2. Uses a timeout of 5 seconds
#   3. Returns the JSON data if successful (status 200)
#   4. Returns None if ANY error occurs (timeout, connection, bad status)
#
# WHY DO WE NEED ERROR HANDLING?
# When calling APIs, many things can go wrong:
#   - Server is down              → ConnectionError
#   - Server takes too long       → Timeout
#   - URL doesn't exist           → 404 status code
#   - Server has a bug            → 500 status code
#   - No internet connection      → ConnectionError
#
# Without error handling, your program would CRASH.
# With try/except, it fails GRACEFULLY (returns None instead).
#
# HOW try/except WORKS:
#   try:
#       # Code that MIGHT break goes here
#       risky_code()
#   except:
#       # If ANYTHING in try breaks, jump here instead of crashing
#       handle_the_error()
#
# HOW timeout WORKS:
#   requests.get(url, timeout=5)
#   → "Wait up to 5 seconds for a response. If no response, give up."
#   → Without timeout, your program could hang FOREVER waiting.
#
# WHAT THE FUNCTION DOES:
#   safe_get("good_url")  → returns {"id": 1, "title": "..."}  (JSON data)
#   safe_get("bad_url")   → returns None                        (no crash!)
#   safe_get("slow_url")  → returns None                        (timeout, no crash!)

def safe_get(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()     # Success! Return the data
        return None                    # Bad status (404, 500, etc.) → None
    except:
        return None                    # Any error (timeout, no internet) → None

# --- Check ---
good = safe_get("https://jsonplaceholder.typicode.com/posts/1")
bad = safe_get("https://jsonplaceholder.typicode.com/posts/99999")

if good and good.get("id") == 1 and bad is None:
    print("  PASS — Function handles both success and failure")
    score += 1
else:
    print(f"  FAIL — good={good is not None}, bad={bad}")
    print("  Hint: Use try/except, check status_code, use timeout=5")
print()


# ============================================================
# Results
# ============================================================
print("=" * 50)
print(f"MEDIUM EXERCISES SCORE: {score}/{total}")
print("=" * 50)
if score == total:
    print("Excellent! Move on to 07_exercises_hard.py!")
elif score >= 7:
    print("Great work! Fix the remaining ones and try again.")
elif score >= 4:
    print("Solid progress! Review your logic and retry.")
else:
    print("Try the easy exercises first (05_exercises_easy.py).")
