#!/usr/bin/python3
"""
Script that, using a REST API, returns information about
an employee's TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    # Check if employee ID is provided
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch data
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Convert JSON responses
    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Print required output
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")
