#!/usr/bin/python3
"""Script that returns an employee's TODO list progress"""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    todo_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    )

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user = user_response.json()
    todos = todo_response.json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [
        task for task in todos if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):"
        .format(employee_name, len(done_tasks), total_tasks)
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
