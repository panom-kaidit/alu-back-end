#!/usr/bin/python3
"""
Fetch all users and their TODO tasks from the JSONPlaceholder API
and export them to a single JSON file in a structured dictionary format.

Output structure:
{
    "USER_ID": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": BOOLEAN
        },
        ...
    ],
    ...
}

The file is saved as "todo_all_employees.json".
"""
import json
import urllib.request


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    with urllib.request.urlopen(f"{api}/users") as res:
        users = json.load(res)

    # Fetch all TODOs
    with urllib.request.urlopen(f"{api}/todos") as res:
        todos = json.load(res)

    # Map user IDs to usernames
    usernames = {u.get("id"): u.get("username") for u in users}

    # Build the result dictionary
    result = {}
    for t in todos:
        uid = str(t.get("userId"))
        result.setdefault(uid, []).append({
            "username": usernames.get(t.get("userId")),
            "task": t.get("title"),
            "completed": t.get("completed")
        })

    # Write to JSON file
    with open("todo_all_employees.json", "w") as f:
        json.dump(result, f)