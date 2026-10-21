#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(emp_id)).json()
    todos = requests.get(url + "todos", params={"userId": emp_id}).json()
    username = user.get("username")
    with open("{}.csv".format(emp_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([emp_id, username,
                             t.get("completed"), t.get("title")])
