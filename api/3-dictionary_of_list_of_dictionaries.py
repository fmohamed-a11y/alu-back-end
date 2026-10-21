#!/usr/bin/python3
"""Export all employees' TODO list to a JSON file."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    data = {}
    for user in users:
        uid = user.get("id")
        todos = requests.get(url + "todos", params={"userId": uid}).json()
        data[str(uid)] = [{"username": user.get("username"),
                           "task": t.get("title"),
                           "completed": t.get("completed")} for t in todos]
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
