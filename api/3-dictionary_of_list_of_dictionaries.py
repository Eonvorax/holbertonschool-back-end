#!/usr/bin/python3
"""Gather data from an API for a given employee
ID and store TODO list progress in a JSON file"""

import json
import requests


def get_progress_json(filename):
    """
    Retrieve employee information and TODO list progress based on the
    employee ID.
    The data will be save to a file named in format:
        <employee_ID>.json
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{url}/users"
    todos_url = f"{url}/todos"

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    employees_progress = {}
    for employee in employee_data:
        emp_id = employee.get("id")
        username = employee.get("username")
        employees_progress[str(emp_id)] = []
        for task in todos_data:
            if task.get("userId") == emp_id:
                employees_progress[str(emp_id)].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    # Generate filename and dump dictionary into JSON file
    with open(filename, mode="w") as json_file:
        json.dump(employees_progress, json_file)


if __name__ == "__main__":
    json_filename = "todo_all_employees.json"
    get_progress_json(json_filename)
