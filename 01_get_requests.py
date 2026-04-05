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

# WHAT IS SLICING?
# posts[:3] gives us the first 3 items from the list.
# The syntax is:  list[start:end]
#   posts[:3]    →  first 3 items (index 0, 1, 2)
#   posts[2:5]   →  items at index 2, 3, 4
#   posts[:10]   →  first 10 items
#   posts[5:]    →  everything from index 5 onward
#   posts[-1]    →  the last item
# Same as: [posts[0], posts[1], posts[2]]

# HOW THE LOOP WORKS:
# "for post in posts[:3]" runs the indented code 3 times.
# Each time, 'post' becomes one dictionary from the list:
#   Loop 1: post = {"id": 1, "title": "sunt aut facere...", "body": "...", "userId": 1}
#   Loop 2: post = {"id": 2, "title": "qui est esse...",    "body": "...", "userId": 1}
#   Loop 3: post = {"id": 3, "title": "ea molestias...",    "body": "...", "userId": 1}
for post in posts[:3]:
    # post['title'][:50] uses the SAME slicing trick, but on a STRING.
    # It grabs only the first 50 characters so long titles don't mess up the output.
    # Example:
    #   title = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    #   title[:50] = "sunt aut facere repellat provident occaecati excep"
    #   Then we add "..." at the end to show it was cut off.
    print(f"  Post #{post['id']}: {post['title'][:50]}...")

# print() with no arguments just prints a BLANK LINE — adds spacing before the next example
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
# Think of it like a search filter:
#   amazon.com/search?category=books&price_max=20&sort=rating
#                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                     These are all query parameters!
#
# THE MANUAL WAY (don't do this):
#   response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
#   This works, but gets messy and error-prone with multiple params or special characters.
#
# THE CLEAN WAY (use params=):
#   Pass a dictionary — requests builds the URL for you.
#   It automatically:
#     1. Adds the '?' for you
#     2. Joins multiple params with '&'
#     3. Encodes special characters (spaces, symbols) so they don't break the URL

params = {"userId": 1}  # Only get posts written by user #1
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params,  # requests adds "?userId=1" to the URL automatically
)

# MULTIPLE PARAMS EXAMPLE:
# params = {"userId": 1, "id": 5}
# This builds: ?userId=1&id=5  (the & separates each parameter)
#
# You can pass as many as you need:
# params = {"category": "books", "price_max": 20, "sort": "rating"}
# This builds: ?category=books&price_max=20&sort=rating
filtered_posts = response.json()

print(f"Posts by user 1: {len(filtered_posts)}")

# WHAT IS response.url?
# It shows the FULL URL that requests actually sent to the server.
# This is useful for DEBUGGING — you can see exactly what was built from your params dict.
# If something isn't working, printing response.url is one of the first things to check —
# maybe a param was misspelled or missing.
#
# With our params = {"userId": 1}, this will print:
#   https://jsonplaceholder.typicode.com/posts?userId=1
#
# With multiple params like {"userId": 1, "id": 5}, it would show:
#   https://jsonplaceholder.typicode.com/posts?userId=1&id=5
print(f"Request URL was: {response.url}")

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
#
# WHAT IS try/except?
# It's a "safety net" for your code. Normally, when an error happens,
# Python CRASHES and stops running. try/except catches the error and
# lets your program recover instead of crashing.
#
# HOW IT WORKS:
#   try:
#       risky_code()      ← Python tries to run this
#       more_code()       ← If line above fails, this is SKIPPED
#   except SomeError:
#       handle_error()    ← This runs INSTEAD of crashing
#
#   next_code()           ← Program continues normally
#
# THE FLOW:
#   If NO error  → runs try block, SKIPS except block
#   If error     → STOPS try block, JUMPS to matching except block
#
# WHY is Method 2 better than Method 1?
#   Method 1 (if/else) only catches bad status codes (404, 500)
#   Method 2 (try/except) also catches:
#     - Server completely down (ConnectionError)
#     - No internet (ConnectionError)
#     - Server too slow (Timeout)
#     - SSL certificate issues (SSLError)
#   With Method 1, any of those would CRASH your program!

try:
    # We request a user that doesn't exist — this returns a 404 error
    response = requests.get("https://jsonplaceholder.typicode.com/users/99999")
    response.raise_for_status()  # This will raise an HTTPError because status is 404
    # ↑ If raise_for_status() throws an error, the next line is SKIPPED
    #   and Python jumps to the matching except block below

except requests.exceptions.HTTPError as e:
    # This block runs when the server returns an error status code (4xx or 5xx)
    # "as e" stores the error details in a variable called 'e'
    # so you can print it and see exactly what went wrong
    print(f"Caught an HTTP error: {e}")
    # Output: "Caught an HTTP error: 404 Client Error: Not Found for url: ..."

# You can catch MULTIPLE types of errors with separate except blocks.
# Only ONE except block runs — whichever matches the error first.
# If no error happens, ALL except blocks are skipped.
#
# COMMON ERRORS TO CATCH:
#   requests.exceptions.HTTPError       →  bad status code (404, 500, etc.)
#   requests.exceptions.ConnectionError →  can't reach the server / no internet
#   requests.exceptions.Timeout         →  server took too long to respond
#   requests.exceptions.SSLError        →  SSL certificate problem
#   requests.exceptions.RequestException →  catches ALL of the above (use as a fallback)
#
# EXAMPLE with multiple except blocks:
#   try:
#       response = requests.get(url, timeout=5)
#       response.raise_for_status()
#       data = response.json()
#   except requests.exceptions.Timeout:
#       print("Too slow!")         ← runs if server takes > 5 seconds
#   except requests.exceptions.HTTPError:
#       print("Bad status!")       ← runs if 404, 500, etc.
#   except requests.exceptions.ConnectionError:
#       print("Can't connect!")    ← runs if server is down / no internet

print()
print("Lesson 1 complete! Run 02_post_requests.py next.")
