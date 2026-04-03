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

completed_count = None  # Your code here

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

first_comment_email = None  # Your code here

# --- Check ---
if first_comment_email == "Nikita@garfield.biz":
    print(f"  PASS — {first_comment_email}")
    score += 1
else:
    print(f"  FAIL — Expected 'Nikita@garfield.biz', got: {first_comment_email}")
print()


# ============================================================
# Exercise 3: Search universities by country
# ============================================================
print("Exercise 3: Find universities in Singapore")
print("-" * 40)

# TODO: Search for universities in Singapore
# API: http://universities.hipolabs.com/search?country=Singapore
# Store the total number of universities found

uni_count = None  # Your code here

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

album_titles = None  # Your code here (should be a list of strings)

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

author_name = None  # Your code here

# --- Check ---
if author_name == "Mrs. Dennis Schulist":
    print(f"  PASS — {author_name}")
    score += 1
else:
    print(f"  FAIL — Expected 'Mrs. Dennis Schulist', got: {author_name}")
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

top_poster_id = None  # Your code here

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

page2_count = None  # Your code here

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

verified = None  # Set to True if the returned title matches, False otherwise

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

unique_domains = None  # Your code here (should be an int)

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

def safe_get(url):
    # Your code here
    return None

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
