"""
=== LESSON 3: PUT, PATCH & DELETE Requests ===

PUT    = Replace an entire resource (full update)
PATCH  = Update only specific fields (partial update)
DELETE = Remove a resource

Together with GET and POST, these make up the main HTTP methods
used in REST APIs (aka "CRUD" operations):
  Create = POST
  Read   = GET
  Update = PUT / PATCH
  Delete = DELETE

REAL WORLD ANALOGY:
    Think of a contact in your phone:
        Name: John, Phone: 555-1234, Email: john@email.com

    PUT (full replace):
        You delete the entire contact and re-enter everything from scratch.
        If you forget to include the email, it's gone.

    PATCH (partial update):
        You tap on just the phone number and change it.
        Name and email stay exactly as they were.

    DELETE:
        You delete the contact entirely.

WHAT IS REST?
    REST (Representational State Transfer) is a set of rules for how
    APIs should work. A REST API organizes data into "resources" (like
    users, posts, comments) and uses HTTP methods to interact with them:

        POST   /posts        →  Create a new post
        GET    /posts        →  Get all posts
        GET    /posts/1      →  Get post #1
        PUT    /posts/1      →  Replace post #1 entirely
        PATCH  /posts/1      →  Update some fields of post #1
        DELETE /posts/1      →  Delete post #1

    The URL identifies WHAT resource, the HTTP method identifies WHAT ACTION.
"""

import requests

# ============================================================
# Example 1: PUT — Replace an entire post
# ============================================================
print("=" * 50)
print("Example 1: PUT — Full update (replace)")
print("=" * 50)

# PUT replaces the ENTIRE resource — you must send ALL fields.
# If you leave out a field, it gets erased/set to default!
#
# Think of it like overwriting a file:
#   Before: {"id": 1, "title": "Old Title", "body": "Old body", "userId": 1}
#   You send: {"id": 1, "title": "New Title", "body": "New body", "userId": 1}
#   After:  {"id": 1, "title": "New Title", "body": "New body", "userId": 1}
#
# WARNING: If you forget a field in PUT:
#   You send: {"id": 1, "title": "New Title", "userId": 1}  (missing "body"!)
#   After:  {"id": 1, "title": "New Title", "body": null, "userId": 1}
#   The body is GONE because PUT replaces everything!

updated_post = {
    "id": 1,
    "title": "Completely Updated Title",
    "body": "This body has been fully replaced.",
    "userId": 1,
}

# requests.put() works like requests.post() — same json= parameter
response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",  # /posts/1 = update post with ID 1
    json=updated_post,
)

print(f"Status Code: {response.status_code}")  # 200 = OK (successfully updated)
print(f"Updated post: {response.json()}")
print()


# ============================================================
# Example 2: PATCH — Partial update
# ============================================================
print("=" * 50)
print("Example 2: PATCH — Partial update")
print("=" * 50)

# PATCH only updates the fields you send — everything else stays the same.
# This is usually what you want when editing something.
#
# Think of it like editing a Word document:
#   You change one paragraph, save — everything else stays the same.
#
# Before: {"id": 1, "title": "Old Title", "body": "Old body", "userId": 1}
# You send: {"title": "Only the Title Changed"}
# After:  {"id": 1, "title": "Only the Title Changed", "body": "Old body", "userId": 1}
#                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                    Only this changed! Body and userId are untouched.

partial_update = {
    "title": "Only the Title Changed",
    # We're NOT sending body or userId — they'll stay as they were
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=partial_update,
)

print(f"Status Code: {response.status_code}")
result = response.json()
print(f"Title:  {result['title']}")   # Changed — our new title
print(f"Body:   {result['body'][:50]}...")  # Unchanged — still has original body
print(f"UserId: {result['userId']}")  # Unchanged — still the original userId
print()


# ============================================================
# Example 3: DELETE — Remove a resource
# ============================================================
print("=" * 50)
print("Example 3: DELETE — Remove a post")
print("=" * 50)

# DELETE is the simplest — you just tell the server which resource to remove.
# No body/data needed — the URL alone tells the server what to delete.
#
# IMPORTANT: In real APIs, DELETE is permanent! There's usually no "undo".
# That's why many apps show a confirmation dialog: "Are you sure?"
#
# Common DELETE responses:
#   200 → Deleted successfully, here's the deleted item
#   204 → Deleted successfully, no content to return (empty body)
#   404 → Can't delete — that resource doesn't exist

response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1"
    # Notice: no json= or data= needed! Just the URL.
)

print(f"Status Code: {response.status_code}")  # 200 = OK
print(f"Response body: {response.json()}")  # Usually empty {} on success
print()


# ============================================================
# Example 4: PUT vs PATCH — Understanding the difference
# ============================================================
print("=" * 50)
print("Example 4: PUT vs PATCH comparison")
print("=" * 50)

# Let's demonstrate the difference with a clear example.
# Original post #1 has: title, body, userId

# --- PATCH: Only send what you want to change ---
print("PATCH — sending only {title}:")
patch_response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"title": "Patched Title"},  # Only changing title
)
patch_result = patch_response.json()
print(f"  Title:  {patch_result['title']}")   # Changed
print(f"  Body:   {patch_result['body'][:40]}...")  # Still has original body!
print(f"  UserId: {patch_result['userId']}")   # Still has original userId!
print()

# --- PUT: Must send EVERYTHING ---
print("PUT — sending ALL fields:")
put_response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={
        "id": 1,
        "title": "Put Title",
        "body": "Must include body too",
        "userId": 1,
    },
)
put_result = put_response.json()
print(f"  Title:  {put_result['title']}")
print(f"  Body:   {put_result['body']}")
print(f"  UserId: {put_result['userId']}")
print()

print("""SUMMARY — When to use which:
  PUT:
    - You have the COMPLETE updated object
    - You want to replace everything
    - Example: User re-submits an entire edit form

  PATCH:
    - You only want to change 1 or 2 fields
    - You don't want to accidentally erase other fields
    - Example: User toggles a "completed" checkbox on a todo

  In practice:
    - Most modern APIs prefer PATCH for updates
    - Some APIs only support one or the other
    - Always check the API documentation!
""")


# ============================================================
# Example 5: Full CRUD cycle in one flow
# ============================================================
print("=" * 50)
print("Example 5: Complete CRUD cycle")
print("=" * 50)

# WHAT IS CRUD?
# CRUD stands for Create, Read, Update, Delete — the four basic
# operations you can do with any data. Almost every app uses CRUD:
#   - A todo app: create tasks, read them, update status, delete them
#   - Instagram: create posts, read feed, update captions, delete posts
#   - A bank: create accounts, read balance, update info, delete accounts
#
# Here we'll do all four operations in sequence, like a real app would:

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# 1. CREATE — Make a new post (POST)
print("1. CREATE (POST)")
response = requests.post(BASE_URL, json={
    "title": "My New Post",
    "body": "Created via API",
    "userId": 1,
})
post_id = response.json()["id"]
print(f"   Created post with ID: {post_id}")
print(f"   Status: {response.status_code} (201 = Created)")

# 2. READ — Fetch a post to see it (GET)
print("2. READ (GET)")
response = requests.get(f"{BASE_URL}/1")
print(f"   Read post title: {response.json()['title'][:40]}...")
print(f"   Status: {response.status_code} (200 = OK)")

# 3. UPDATE — Change the title (PATCH)
print("3. UPDATE (PATCH)")
response = requests.patch(f"{BASE_URL}/1", json={"title": "Updated!"})
print(f"   Updated title to: {response.json()['title']}")
print(f"   Status: {response.status_code} (200 = OK)")

# 4. DELETE — Remove the post (DELETE)
print("4. DELETE")
response = requests.delete(f"{BASE_URL}/1")
print(f"   Deleted! Status: {response.status_code} (200 = OK)")

print()
print("""
RECAP — All HTTP methods at a glance:
  ┌──────────┬────────────┬───────────────┬─────────────────┐
  │  Method  │  CRUD      │  Sends Data?  │  Common Status  │
  ├──────────┼────────────┼───────────────┼─────────────────┤
  │  GET     │  Read      │  No           │  200 OK         │
  │  POST    │  Create    │  Yes (body)   │  201 Created    │
  │  PUT     │  Update    │  Yes (full)   │  200 OK         │
  │  PATCH   │  Update    │  Yes (partial)│  200 OK         │
  │  DELETE  │  Delete    │  No           │  200 or 204     │
  └──────────┴────────────┴───────────────┴─────────────────┘
""")
print("Lesson 3 complete! Run 04_practice_challenge.py next.")
