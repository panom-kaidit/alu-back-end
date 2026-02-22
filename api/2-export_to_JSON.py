#!/usr/bin/python3
"""
Retrieve an employee's tasks from the API and export them
to a JSON file named USER_ID.json using the required format.
"""

import json
import requests
import sys


def fetch_user(user_id):
    """Fetch user information."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def fetch_todos(user_id):
    """Fetch todos for a user."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id}, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    try:
        user = fetch_user(employee_id)
        todos = fetch_todos(employee_id)
    except requests.RequestException:
        sys.exit(1)

    username = user.get("username")

    data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    filename = f"{employee_id}.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


if __name__ == "__main__":
    main()