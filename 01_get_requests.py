"""
=== LESSON 1: GET Requests ===

GET requests are used to RETRIEVE data from a server.
Think of it like asking a question — you're requesting information.

REAL WORLD ANALOGY:
    Imagine you walk into a library and ask the librarian:
    "Can I see the book with ID #1?"
    The librarian (server) finds the book and hands it to you (response).
    That's exactly what a GET request does — you ask, the server answers.

HOW IT WORKS (step by step):
    1. Your code sends an HTTP GET request to a URL (the server's address)
    2. The server receives your request and processes it
    3. The server sends back a response containing:
       - A status code (200 = success, 404 = not found, etc.)
       - Headers (metadata like content type, size, etc.)
       - A body (the actual data, usually in JSON format)
    4. Your code reads the response and uses the data

WHAT IS JSON?
    JSON (JavaScript Object Notation) is a text format for sending data.
    It looks almost identical to a Python dictionary:
        {"name": "John", "age": 30, "city": "New York"}
    APIs use JSON because it's lightweight, readable, and universal —
    every programming language can read and write it.

WHAT IS requests?
    'requests' is a Python library that makes HTTP calls easy.
    Without it, you'd need 10+ lines of code just for a simple GET.
    Install it with: pip install requests

We'll use JSONPlaceholder (https://jsonplaceholder.typicode.com),
a free fake API for testing and learning. It has fake data for:
    /users    — 10 fake users
    /posts    — 100 fake blog posts
    /comments — 500 fake comments
    /todos    — 200 fake todo items
    /albums   — 100 fake albums
    /photos   — 5000 fake photos
"""

import requests  # First, we import the library

# ============================================================
# Example 1: Simple GET — Fetch a single user
# ============================================================
print("=" * 50)
print("Example 1: Fetch a single user")
print("=" * 50)

# requests.get(url) sends a GET request to the URL and returns a Response object.
# The URL "https://jsonplaceholder.typicode.com/users/1" means:
#   - https://jsonplaceholder.typicode.com  →  the server address (base URL)
#   - /users                                →  the resource type (we want users)
#   - /1                                    →  the specific user (ID = 1)
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# WHAT IS response?
# 'response' is an object that holds everything the server sent back.
# It has many useful properties:
#   response.status_code  →  HTTP status code (200, 404, 500, etc.)
#   response.json()       →  the body parsed as a Python dict/list
#   response.text         →  the body as a raw string
#   response.headers      →  metadata about the response
#   response.url          →  the URL that was actually requested
#   response.ok           →  True if status code is 200-299

# The status code tells you if the request succeeded
# 200 = OK (success), 404 = Not Found, 500 = Server Error
print(f"Status Code: {response.status_code}")

# .json() converts the response body from JSON into a Python dictionary.
# This is the most common way to read API data.
# Before: '{"name": "Leanne Graham", "email": "Sincere@april.biz"}'  (raw JSON string)
# After:  {"name": "Leanne Graham", "email": "Sincere@april.biz"}    (Python dict)
user = response.json()

# Now we can access fields using dictionary keys, just like a normal dict
print(f"Name:    {user['name']}")
print(f"Email:   {user['email']}")

# You can also access NESTED data — the address is a dict inside the user dict
# user['address'] = {"street": "Kulas Light", "city": "Gwenborough", ...}
print(f"City:    {user['address']['city']}")
print()


# ============================================================
# Example 2: GET a list — Fetch all posts
# ============================================================
print("=" * 50)
print("Example 2: Fetch all posts (showing first 3)")
print("=" * 50)

# When you request /posts (without an ID), the API returns ALL posts as a list.
# This time response.json() returns a Python LIST of dictionaries, not just one dict.
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()  # This is a list like: [{"id": 1, ...}, {"id": 2, ...}, ...]

# len() tells us how many items are in the list
print(f"Total posts returned: {len(posts)}")
print()

# posts[:3] is Python slicing — it gives us the first 3 items from the list.
# Same as: [posts[0], posts[1], posts[2]]
# We loop through them and print each post's ID and title.
for post in posts[:3]:
    # post['title'][:50] slices the title string to show only the first 50 characters
    print(f"  Post #{post['id']}: {post['title'][:50]}...")
print()


# ============================================================
# Example 3: GET with query parameters — Filter results
# ============================================================
print("=" * 50)
print("Example 3: GET with query parameters")
print("=" * 50)

# WHAT ARE QUERY PARAMETERS?
# They're extra info you add to a URL to filter or customize results.
# They come after a '?' in the URL:
#   https://jsonplaceholder.typicode.com/posts?userId=1
#                                              ^^^^^^^^
#                                              This is a query parameter!
#
# You CAN build the URL manually like above, but it's better to use
# the params= argument — it handles special characters and formatting for you.

params = {"userId": 1}  # Only get posts written by user #1
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params,  # requests adds "?userId=1" to the URL automatically
)
filtered_posts = response.json()

print(f"Posts by user 1: {len(filtered_posts)}")
# response.url shows the full URL that was actually sent — useful for debugging!
print(f"Request URL was: {response.url}")

# You can pass multiple params too:
# params = {"userId": 1, "id": 5}  →  ?userId=1&id=5  (& separates multiple params)
print()


# ============================================================
# Example 4: Checking response headers
# ============================================================
print("=" * 50)
print("Example 4: Inspecting response headers")
print("=" * 50)

# WHAT ARE HEADERS?
# Headers are metadata sent alongside the request/response.
# Think of them like the label on a package:
#   - The package contents = the response body (your data)
#   - The label = headers (info ABOUT the data — type, size, encoding, etc.)
#
# Common response headers:
#   Content-Type    →  What format the data is in (e.g., application/json)
#   Content-Length  →  How big the response is in bytes
#   Cache-Control   →  How long the browser can cache this response
#   Date            →  When the server sent the response

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Access headers like a dictionary
print(f"Content-Type:   {response.headers['Content-Type']}")

# response.content is the raw bytes of the response body
print(f"Response size:  {len(response.content)} bytes")

# response.encoding is the character encoding (usually utf-8)
print(f"Encoding:       {response.encoding}")
print()


# ============================================================
# Example 5: Handling errors gracefully
# ============================================================
print("=" * 50)
print("Example 5: Handling a bad request (404)")
print("=" * 50)

# WHY HANDLE ERRORS?
# APIs can fail for many reasons:
#   - The resource doesn't exist (404)
#   - The server is down (500)
#   - You're not authorized (401/403)
#   - Your internet is disconnected
# Good code always handles these cases instead of crashing!

# This URL requests post #99999 which doesn't exist
response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")

# METHOD 1: Check the status code manually with an if/else
if response.status_code == 200:
    print("Success! Got the data.")
else:
    print(f"Error! Status code: {response.status_code}")
    # response.text gives you the raw response body as a string
    # (useful for seeing error messages from the server)
    print(f"Response body: {response.text}")
print()

# METHOD 2: Use raise_for_status() inside a try/except block.
# raise_for_status() does nothing if the request succeeded (2xx status),
# but THROWS an exception if the status code indicates an error (4xx or 5xx).
# This is cleaner when you have multiple things that could go wrong.
try:
    response = requests.get("https://httpstat.us/500")  # This URL always returns 500
    response.raise_for_status()  # This will raise an HTTPError because status is 500
except requests.exceptions.HTTPError as e:
    # This block runs when the server returns an error status code
    print(f"Caught an HTTP error: {e}")

# TIP: You can also catch other types of errors:
#   requests.exceptions.ConnectionError  →  can't reach the server
#   requests.exceptions.Timeout          →  server took too long to respond
#   requests.exceptions.RequestException →  catches ALL request errors

print()
print("Lesson 1 complete! Run 02_post_requests.py next.")
