#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

For a given employee ID, returns information about
his/her TODO list progress.
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

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        sys.exit(1)

    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_done = len(done_tasks)

    # Print required format
    print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")

    for task in done_tasks:
        print("\t {}".format(task.get("title")))