"""
=== LESSON 4: Practice Challenge ===

Now it's your turn! This script has exercises for you to complete.
Each exercise has a TODO section — fill in the code to make it work.

All exercises use free public APIs, no API key needed.

Run this file to check your answers — it will tell you if you got it right!
"""

import requests

score = 0
total = 5

# ============================================================
# Challenge 1: Fetch a user by ID
# ============================================================
print("Challenge 1: Fetch user #5's name")
print("-" * 40)

# TODO: Make a GET request to fetch user #5 from JSONPlaceholder
# API: https://jsonplaceholder.typicode.com/users/5
# Store the user's name in the variable below

user_name = None  # Replace None with your code

# --- Check ---
if user_name == "Chelsey Dietrich":
    print(f"  PASS — Got: {user_name}")
    score += 1
else:
    print(f"  FAIL — Expected 'Chelsey Dietrich', got: {user_name}")
    print("  Hint: requests.get(url).json()['name']")
print()


# ============================================================
# Challenge 2: Count items from an API
# ============================================================
print("Challenge 2: How many todos does user 1 have?")
print("-" * 40)

# TODO: Fetch all todos for userId=1
# API: https://jsonplaceholder.typicode.com/todos?userId=1
# Store the count in the variable below

todo_count = None  # Replace None with your code

# --- Check ---
if todo_count == 20:
    print(f"  PASS — Count: {todo_count}")
    score += 1
else:
    print(f"  FAIL — Expected 20, got: {todo_count}")
    print("  Hint: len(requests.get(url, params={...}).json())")
print()


# ============================================================
# Challenge 3: Create a new resource
# ============================================================
print("Challenge 3: Create a new post via POST")
print("-" * 40)

# TODO: Send a POST request to create a new post
# API: https://jsonplaceholder.typicode.com/posts
# Send JSON with: title="My Post", body="Hello API!", userId=1
# Store the status code in the variable below

status_code = None  # Replace None with your code

# --- Check ---
if status_code == 201:
    print(f"  PASS — Status: {status_code} (Created)")
    score += 1
else:
    print(f"  FAIL — Expected 201, got: {status_code}")
    print("  Hint: requests.post(url, json={...}).status_code")
print()


# ============================================================
# Challenge 4: Use a different free API
# ============================================================
print("Challenge 4: Fetch a random dog fact")
print("-" * 40)

# TODO: Fetch a dog fact from this free API (no key needed)
# API: https://dogapi.dog/api/v2/facts
# The response has this structure: {"data": [{"attributes": {"body": "the fact..."}}]}
# Store the fact text in the variable below

dog_fact = None  # Replace None with your code

# --- Check ---
if dog_fact and isinstance(dog_fact, str) and len(dog_fact) > 10:
    print(f"  PASS — Fact: {dog_fact[:60]}...")
    score += 1
else:
    print(f"  FAIL — Expected a string with a dog fact, got: {dog_fact}")
    print("  Hint: response.json()['data'][0]['attributes']['body']")
print()


# ============================================================
# Challenge 5: Handle an error properly
# ============================================================
print("Challenge 5: Handle a 404 error")
print("-" * 40)

# TODO: Try to GET a post that doesn't exist (ID 99999)
# API: https://jsonplaceholder.typicode.com/posts/99999
# If the status code is 404, set error_handled to True
# Otherwise set it to False

error_handled = None  # Replace None with your code

# --- Check ---
if error_handled is True:
    print("  PASS — Correctly detected the 404!")
    score += 1
else:
    print(f"  FAIL — Expected True, got: {error_handled}")
    print("  Hint: response.status_code == 404")
print()


# ============================================================
# Results
# ============================================================
print("=" * 50)
print(f"SCORE: {score}/{total}")
print("=" * 50)
if score == total:
    print("Perfect! You've mastered the basics of REST API calls!")
elif score >= 3:
    print("Great job! Review the ones you missed and try again.")
else:
    print("Keep practicing! Re-read the lesson files for help.")
