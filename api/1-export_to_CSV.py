#!/usr/bin/python3
"""
get all the data from file that gather the data then
export in format of csv.
"""
import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    emp_id = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
        "{}/users/{}".format(api, emp_id)
    ) as res:
        user = json.load(res)

    with urllib.request.urlopen(
        "{}/todos?userId={}".format(api, emp_id)
    ) as res:
        todos = json.load(res)

    with open("{}.csv".format(emp_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                user.get("username"),
                str(task.get("completed")),
                task.get("title")
            ])