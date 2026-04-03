"""
=== LESSON 2: POST Requests ===

POST requests are used to SEND/CREATE new data on a server.
Think of it like filling out a form and submitting it.

REAL WORLD ANALOGY:
    Imagine you're at a restaurant and you fill out an order form:
        Name: "Burger", Extras: "Cheese", Quantity: 2
    You hand the form (your data) to the waiter (the server).
    The waiter processes it and hands you back a receipt (the response)
    with a confirmation and an order number (the new ID).
    That's a POST request — you SEND data, and the server creates something.

GET vs POST — What's the difference?
    GET  →  "Give me data"        (you send nothing, server sends data back)
    POST →  "Here's new data"     (you send data, server creates something)

    GET is like reading a book.
    POST is like writing a new page in the book.

WHAT IS A REQUEST BODY?
    When you POST, you include a "body" — the data you're sending.
    This is usually in JSON format:
        {"title": "My Post", "body": "Hello!", "userId": 1}
    The server reads this body and uses it to create the new resource.

JSONPlaceholder simulates creating resources — it accepts your data
and returns it back with a new ID, but doesn't actually save it.
(It's a fake API for learning — real APIs would save it to a database.)
"""

import requests

# ============================================================
# Example 1: Simple POST — Create a new post
# ============================================================
print("=" * 50)
print("Example 1: Create a new post")
print("=" * 50)

# Step 1: Prepare the data you want to send, as a Python dictionary.
# This is the "body" of your request — the data the server will use
# to create a new post.
new_post = {
    "title": "My First API Post",
    "body": "Learning how to make POST requests with Python!",
    "userId": 1,
}

# Step 2: Send the POST request.
# requests.post() is like requests.get(), but it also SENDS data.
#
# The key difference is the json= parameter:
#   json=new_post  does TWO things automatically:
#     1. Converts your Python dict to a JSON string
#     2. Sets the "Content-Type" header to "application/json"
#        (this tells the server "hey, I'm sending you JSON data")
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post,  # <-- this converts dict to JSON and sets Content-Type header
)

# Step 3: Read the response.
# Status 201 means "Created" — the server successfully made the new resource.
# (Remember: 200 = OK for GET, 201 = Created for POST)
print(f"Status Code: {response.status_code}")  # 201 = Created

# The server sends back the created resource, usually with a new ID assigned.
created_post = response.json()
print(f"Server assigned ID: {created_post['id']}")
print(f"Title: {created_post['title']}")
print()


# ============================================================
# Example 2: POST with manual headers
# ============================================================
print("=" * 50)
print("Example 2: POST with explicit headers")
print("=" * 50)

import json  # Python's built-in JSON library

# WHY SET HEADERS MANUALLY?
# In Example 1, we used json= which handles everything automatically.
# But sometimes you need more control — for example:
#   - The API requires a specific Content-Type format
#   - You need to add an Authorization header (for APIs with API keys)
#   - You need custom headers the API expects
#
# This example shows the "manual" way, so you understand what json= does
# behind the scenes.

headers = {
    # This tells the server: "I'm sending JSON data encoded in UTF-8"
    "Content-Type": "application/json; charset=UTF-8",
}

payload = {
    "title": "Custom Headers Post",
    "body": "This request sets headers manually.",
    "userId": 2,
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    # data= sends raw data (doesn't auto-convert), so we must:
    #   1. Convert dict to JSON string ourselves using json.dumps()
    #   2. Set the Content-Type header ourselves
    data=json.dumps(payload),  # <-- manually convert dict → JSON string
    headers=headers,           # <-- manually tell server it's JSON
)

# COMPARISON:
#   json=payload           →  automatic (preferred, cleaner)
#   data=json.dumps(payload) + headers  →  manual (for when you need control)
# Both do the same thing!

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
print()


# ============================================================
# Example 3: POST form data (like an HTML form)
# ============================================================
print("=" * 50)
print("Example 3: POST form-encoded data")
print("=" * 50)

# WHAT IS FORM DATA?
# When you fill out a form on a website and click "Submit", the browser
# sends the data as "form-encoded" — NOT as JSON.
#
# Form-encoded looks like this: title=Hello&body=World&userId=1
# JSON looks like this:         {"title": "Hello", "body": "World", "userId": 1}
#
# Most modern APIs use JSON, but some older ones or file upload APIs
# expect form data. You should know both!

form_data = {
    "title": "Form Data Post",
    "body": "Sent as application/x-www-form-urlencoded",
    "userId": 3,
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    # data= WITHOUT json.dumps() sends as form-encoded (not JSON!)
    # This is the KEY difference:
    #   data=some_dict              →  form-encoded  (Content-Type: application/x-www-form-urlencoded)
    #   data=json.dumps(some_dict)  →  raw JSON string (you set Content-Type yourself)
    #   json=some_dict              →  automatic JSON  (Content-Type: application/json)
    data=form_data,  # <-- sends as form data, NOT JSON
)

print(f"Status Code: {response.status_code}")

# response.request gives you info about what was SENT (not received)
# This is useful for debugging — you can see exactly what headers you sent
print(f"Content-Type sent: {response.request.headers['Content-Type']}")
print(f"Response: {response.json()}")
print()


# ============================================================
# Example 4: Handling POST errors
# ============================================================
print("=" * 50)
print("Example 4: Handling POST errors")
print("=" * 50)

# WHY IS ERROR HANDLING MORE IMPORTANT FOR POST?
# - GET just reads data — if it fails, nothing bad happens
# - POST creates data — if it fails mid-way, you might get duplicates
#   or partial data. Always handle errors in POST requests!
#
# WHAT IS A TIMEOUT?
# A timeout is the maximum time you're willing to wait for a response.
# Without a timeout, your code could hang forever if the server is slow.
# timeout=5 means "give up if no response after 5 seconds".

try:
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "Test"},
        timeout=5,  # <-- always set a timeout in real apps!
    )
    # raise_for_status() throws an error if status is 4xx or 5xx
    response.raise_for_status()
    print(f"Success! Created: {response.json()['id']}")

except requests.exceptions.Timeout:
    # This runs if the server didn't respond within 5 seconds
    print("Request timed out!")

except requests.exceptions.HTTPError as e:
    # This runs if the server returned an error status (4xx or 5xx)
    print(f"HTTP Error: {e}")

except requests.exceptions.ConnectionError:
    # This runs if your code can't reach the server at all
    # (e.g., no internet, wrong URL, server is completely down)
    print("Could not connect to the server!")

# TIP: In a real app, you'd also want to:
#   - Log the error for debugging
#   - Retry the request (maybe the server was temporarily busy)
#   - Show a user-friendly message instead of crashing
print()

print("Lesson 2 complete! Run 03_put_delete_requests.py next.")
