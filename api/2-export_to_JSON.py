#!/usr/bin/python3
"""Exports an employee's TODO list to a JSON file. """
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(emp_id)).json()
    todos = requests.get(url + "todos", params={"userId": emp_id}).json()
    username = user.get("username")
    data = {emp_id: [{"task": t.get("title"),
                      "completed": t.get("completed"),
                      "username": username} for t in todos]}
    with open("{}.json".format(emp_id), "w") as f:
        json.dump(data, f)
