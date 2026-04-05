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
# IMPORTANT: This is NOT a separate request! When you POST, the server does
# two things in ONE round-trip:
#   1. Creates the resource
#   2. Sends back a confirmation response with the created data
#
# Think of ordering food:
#   You:     "I'd like a burger with cheese"   (POST — your data)
#   Waiter:  "Order #47: burger + cheese"       (Response — confirmation)
# You're not going back to check — the waiter immediately confirms.
#
# So response.json() reads the server's REPLY to your POST,
# not a separate GET request.

# Status 201 means "Created" — the server successfully made the new resource.
# (Remember: 200 = OK for GET, 201 = Created for POST)
print(f"Status Code: {response.status_code}")  # 201 = Created

# The server sends back the created resource, usually with a new ID assigned.
# WHAT IS response.json() HERE?
# It's the server's confirmation — the data it created, sent back to you.
# This typically includes everything you sent PLUS a new ID the server assigned.
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

# WHAT ARE REQUEST HEADERS?
# Headers are metadata you send WITH your request — info ABOUT the data.
# Think of it like a shipping label on a package:
#
#   ┌─────────────────────────────────┐
#   │  LABEL (headers)                │  ← info ABOUT the package
#   │    Content-Type: application/json
#   │    Authorization: Bearer abc123  │  ← (for APIs that need a key)
#   ├─────────────────────────────────┤
#   │  PACKAGE CONTENTS (body/data)   │  ← the actual data
#   │    {"title": "Hello"}           │
#   └─────────────────────────────────┘
#
# The server reads headers first to know HOW to read the data.
# "Content-Type: application/json" tells the server:
#   "The data I'm sending is in JSON format — parse it as JSON."
headers = {
    # This tells the server: "I'm sending JSON data encoded in UTF-8"
    "Content-Type": "application/json; charset=UTF-8",
}

# WHAT IS "payload"?
# It's just a variable name — it holds the data you want to send.
# There's nothing special about the word. You could call it anything:
#   payload = {"title": "Hello"}
#   my_data = {"title": "Hello"}
#   banana  = {"title": "Hello"}   ← works, but bad name!
# Developers commonly use "payload" to mean "the data carried by a request"
# — like the contents inside a shipping package.
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

# WHAT IS json.dumps()?
# It converts a Python dict INTO a JSON string:
#   Before (Python dict):  {"title": "Hello", "userId": 1}
#   After (JSON string):   '{"title": "Hello", "userId": 1}'
# They LOOK the same, but one is a Python object, the other is a text string.
# APIs receive text, not Python objects — so you must convert first.
# (The opposite is json.loads() — converts a JSON string back to a dict)

# COMPARISON — json= vs data=json.dumps()
#
# WHY did Example 1 use json=new_post but Example 2 uses data=json.dumps(payload)?
# They accomplish the SAME THING — sending JSON to the server.
# The difference is how much work YOU do vs how much requests does for you.
#
#   ┌──────────────────────────────────────────────────────────────┐
#   │  METHOD 1: json=payload  (AUTOMATIC — Example 1)            │
#   │    requests.post(url, json=payload)                         │
#   │                                                             │
#   │    What requests does FOR you:                              │
#   │      ✓ Converts your dict to a JSON string                 │
#   │      ✓ Sets Content-Type to application/json               │
#   │    You just pass the dict — done!                           │
#   ├──────────────────────────────────────────────────────────────┤
#   │  METHOD 2: data=json.dumps(payload)  (MANUAL — Example 2)  │
#   │    requests.post(url, data=json.dumps(payload), headers=h)  │
#   │                                                             │
#   │    What YOU must do yourself:                               │
#   │      • Convert dict to JSON string with json.dumps()       │
#   │      • Set Content-Type header yourself                    │
#   │    More work, but you have full control over headers.       │
#   └──────────────────────────────────────────────────────────────┘
#
# WHEN WOULD YOU NEED THE MANUAL WAY?
#   1. Adding an API key:
#        headers = {
#            "Content-Type": "application/json",
#            "Authorization": "Bearer YOUR_API_KEY"   ← can't do this with json=
#        }
#      (Actually, you CAN still use json= AND pass headers= too — but some
#       developers prefer the manual way for full visibility.)
#
#   2. Custom Content-Type:
#        headers = {"Content-Type": "application/json; charset=UTF-8"}
#      (json= always sets it to "application/json" — no charset.)
#
#   3. When an API expects a specific format that json= doesn't support.
#
# BOTTOM LINE:
#   Use json=  for 90% of cases — it's cleaner and less error-prone.
#   Use data=json.dumps() when you need precise control over headers.

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
#
# REAL-WORLD USE CASES FOR FORM DATA:
#   1. Login forms — many websites accept username/password as form data:
#        data={"username": "john", "password": "secret123"}
#
#   2. File uploads — when you upload a profile picture or document,
#      it's sent as form data (multipart form data)
#
#   3. Payment gateways — some older payment APIs (like PayPal's classic API)
#      expect form-encoded data, not JSON
#
#   4. OAuth token requests — when your app exchanges a code for an access token:
#        data={"grant_type": "authorization_code", "code": "abc123"}
#
#   5. Legacy/older APIs — APIs built before JSON became the standard
#      still expect form data
#
# WHEN TO USE WHICH?
#   Modern API (most cases)  →  json=   (sends JSON)
#   Website login/form       →  data=   (sends form-encoded)
#   File upload              →  files=  (sends multipart form data)
#
# Think of it this way:
#   json=   →  talking to a modern API (machine-to-machine)
#   data=   →  mimicking what a browser does when you click "Submit"

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

# WHAT IS response.request?
# response        = what the server SENT BACK to you (the reply)
# response.request = what YOU SENT to the server (your original request)
#
# This is useful for debugging — you can see exactly what headers and data
# you sent, to make sure everything looks right.
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
