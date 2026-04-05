"""
=== EXERCISES: Easy Level ===

10 beginner exercises using free public APIs.
Fill in each TODO, then run this file to check your score.

APIs used (all free, no key needed):
- JSONPlaceholder: https://jsonplaceholder.typicode.com
- Dog API: https://dogapi.dog/api/v2
- Cat Facts: https://catfact.ninja
"""

import requests

score = 0
total = 10


# ============================================================
# Exercise 1: Get a specific post's title
# ============================================================
print("Exercise 1: Get the title of post #7")
print("-" * 40)

# TODO: GET post #7 and store its title
# API: https://jsonplaceholder.typicode.com/posts/7

response = requests.get("https://jsonplaceholder.typicode.com/posts/7")
title = response.json()['title']  # Your code here

# --- Check ---
if title == "magnam facilis autem":
    print(f"  PASS — {title}")
    score += 1
else:
    print(f"  FAIL — Expected 'magnam facilis autem', got: {title}")
    print("  Hint: requests.get('https://jsonplaceholder.typicode.com/posts/7').json()['title']")
print()


# ============================================================
# Exercise 2: Count all users
# ============================================================
print("Exercise 2: How many users are there?")
print("-" * 40)

# TODO: GET all users and count them
# API: https://jsonplaceholder.typicode.com/users

response = requests.get("https://jsonplaceholder.typicode.com/users")
user_count = len(response.json())  # Your code here

# --- Check ---
if user_count == 10:
    print(f"  PASS — {user_count} users")
    score += 1
else:
    print(f"  FAIL — Expected 10, got: {user_count}")
    print("  Hint: len(requests.get(url).json())")
print()


# ============================================================
# Exercise 3: Get a user's email
# ============================================================
print("Exercise 3: What is user #3's email?")
print("-" * 40)

# TODO: GET user #3 and store their email
# API: https://jsonplaceholder.typicode.com/users/3

response = requests.get("https://jsonplaceholder.typicode.com/users/3")

email = response.json()['email']  # Your code here

# --- Check ---
if email == "Nathan@yesenia.net":
    print(f"  PASS — {email}")
    score += 1
else:
    print(f"  FAIL — Expected 'Nathan@yesenia.net', got: {email}")
print()


# ============================================================
# Exercise 4: Get comments for a post
# ============================================================
print("Exercise 4: How many comments does post #1 have?")
print("-" * 40)

# TODO: GET all comments for post #1
# API: https://jsonplaceholder.typicode.com/comments?postId=1

# response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
response = requests.get('https://jsonplaceholder.typicode.com/comments', params = {'postId':1})
comment_count = len(response.json())
# --- Check ---
if comment_count == 5:
    print(f"  PASS — {comment_count} comments")
    score += 1
else:
    print(f"  FAIL — Expected 5, got: {comment_count}")
    print("  Hint: Use params={'postId': 1}")
print()


# ============================================================
# Exercise 5: Get a cat fact
# ============================================================
print("Exercise 5: Fetch a cat fact")
print("-" * 40)

# TODO: GET a random cat fact
# API: https://catfact.ninja/fact
# The response looks like: {"fact": "some cat fact...", "length": 50}
# Store the fact text

response = requests.get("https://catfact.ninja/fact")
cat_fact = response.json()['fact'] # Your code here

# --- Check ---
if cat_fact and isinstance(cat_fact, str) and len(cat_fact) > 5:
    print(f"  PASS — {cat_fact[:60]}...")
    score += 1
else:
    print(f"  FAIL — Expected a string, got: {cat_fact}")
    print("  Hint: requests.get('https://catfact.ninja/fact').json()['fact']")
print()


# ============================================================
# Exercise 6: Check a status code
# ============================================================
print("Exercise 6: What status code does a deleted resource return?")
print("-" * 40)

# TODO: Send a DELETE request to remove post #1
# API: https://jsonplaceholder.typicode.com/posts/1
# Store the status code

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
delete_status = response.status_code  # Your code here

# --- Check ---
if delete_status == 200:
    print(f"  PASS — Status: {delete_status}")
    score += 1
else:
    print(f"  FAIL — Expected 200, got: {delete_status}")
    print("  Hint: requests.delete(url).status_code")
print()


# ============================================================
# Exercise 7: Get nested data
# ============================================================
print("Exercise 7: What company does user #2 work for?")
print("-" * 40)

# TODO: GET user #2 and find their company name
# API: https://jsonplaceholder.typicode.com/users/2
# The company name is in user['company']['name']

response = requests.get("https://jsonplaceholder.typicode.com/users/2")
company = response.json()['company']['name']  # Your code here

# --- Check ---
if company == "Deckow-Crist":
    print(f"  PASS — {company}")
    score += 1
else:
    print(f"  FAIL — Expected 'Deckow-Crist', got: {company}")
print()


# ============================================================
# Exercise 8: Create a comment via POST
# ============================================================
print("Exercise 8: Create a new comment")
print("-" * 40)

# TODO: POST a new comment to post #1
# API: https://jsonplaceholder.typicode.com/comments
# Send JSON: postId=1, name="Me", email="me@test.com", body="Great post!"
# Store the ID returned by the server
my_post = {
    "postId": 1,
    "name": "Me",
    "email":"me@test.com",
    "body":"Great post!"
}
response = requests.post(
    "https://jsonplaceholder.typicode.com/comments",
    json=my_post
    )
new_comment_id = response.json()['id']  # Your code here

# --- Check ---
if new_comment_id == 501:
    print(f"  PASS — Created comment ID: {new_comment_id}")
    score += 1
else:
    print(f"  FAIL — Expected 501, got: {new_comment_id}")
    print("  Hint: requests.post(url, json={...}).json()['id']")
print()


# ============================================================
# Exercise 9: Use PATCH to update a field
# ============================================================
print("Exercise 9: Update only the title of post #5")
print("-" * 40)

# TODO: PATCH post #5 to change its title to "Updated Title"
# API: https://jsonplaceholder.typicode.com/posts/5
# Store the response's userId to prove other fields weren't lost
response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/5",
    json ={'title':'Updated Title'}
)
user_id_after_patch = response.json()['userId'] # Your code here

# --- Check ---
if user_id_after_patch == 1:
    print(f"  PASS — userId preserved: {user_id_after_patch}")
    score += 1
else:
    print(f"  FAIL — Expected userId=1, got: {user_id_after_patch}")
    print("  Hint: requests.patch(url, json={'title': 'Updated Title'}).json()['userId']")
print()


# ============================================================
# Exercise 10: Get the Content-Type header
# ============================================================
print("Exercise 10: What Content-Type does the API return?")
print("-" * 40)

# TODO: GET any post and read the Content-Type from response headers
# API: https://jsonplaceholder.typicode.com/posts/1
# Store just the content type string
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
content_type = response.headers['Content-Type']  # Your code here
#In Exercise 10, you read the response Content-Type — the server is telling you "the data I sent back is application/json", so you know to use response.json() to read it.
# --- Check ---
if content_type and "application/json" in content_type:
    print(f"  PASS — {content_type}")
    score += 1
else:
    print(f"  FAIL — Expected 'application/json...', got: {content_type}")
    print("  Hint: response.headers['Content-Type']")
print()


# ============================================================
# Results
# ============================================================
print("=" * 50)
print(f"EASY EXERCISES SCORE: {score}/{total}")
print("=" * 50)
if score == total:
    print("Perfect! Move on to 06_exercises_medium.py!")
elif score >= 7:
    print("Almost there! Fix the remaining ones and try again.")
elif score >= 4:
    print("Good start! Review the lesson files for help.")
else:
    print("Go back to 01-03 lessons and re-read them first.")
