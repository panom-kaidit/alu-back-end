#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

For a given employee ID, returns information about
his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} emp_id", file=sys.stderr)
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("the id must be vaild (int type)", file=sys.stderr)
        sys.exit(1)

    base = "https://jsonplaceholder.typicode.com"

    url_response = requests.get(f"{base}/users/{emp_id}")
    if url_response.status_code != 200:
        sys.exit(1)
    user = url_response.json()
    emp_name = user.get("name")

    todo_list_response = requests.get(
        f"{base}/todos", params={"userId": emp_id})
    if todo_list_response.status_code != 200:
        sys.exit(1)
    todo_list = todo_list_response.json()

    success = [task for task in todo_list if task.get("completed") is True]

    f_line = (
        f"Employee {emp_name} is done with tasks"
        f"({len(success)}/{len(todo_list)}):"
    )
    print(f_line)

    for task in success:
        title = task.get("title")
        print("\t {}".format(title))