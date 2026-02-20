#!/usr/bin/python3
"""
Fetch and display TODO progress for a given employee ID.
"""

import sys
import requests


API_BASE_URL = "https://jsonplaceholder.typicode.com"


def get_employee(employee_id):
    """Get employee details."""
    response = requests.get(f"{API_BASE_URL}/users/{employee_id}")
    return response.json() if response.status_code == 200 else None


def get_employee_todos(employee_id):
    """Get employee TODO list."""
    response = requests.get(
        f"{API_BASE_URL}/todos",
        params={"userId": employee_id}
    )
    return response.json() if response.status_code == 200 else None


def main():
    # Check argument count
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID", file=sys.stderr)
        sys.exit(1)

    # Validate employee ID
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer", file=sys.stderr)
        sys.exit(1)

    # Fetch data
    employee = get_employee(employee_id)
    if not employee:
        sys.exit(1)

    todos = get_employee_todos(employee_id)
    if todos is None:
        sys.exit(1)

    # Filter completed tasks
    completed = [task for task in todos if task.get("completed")]

    # Print results
    print(
        f"Employee {employee.get('name')} is done with tasks"
        f"({len(completed)}/{len(todos)}):"
    )

    for task in completed:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    main()