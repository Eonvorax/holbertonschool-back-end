#!/usr/bin/python3
"""Gather data on employee progress for their respective tasks."""

import json
import requests


def get_progress_json(filename):
    """
    Retrieve employee progress on their tasks, based on their user ID.

    The data will be saved to a file named in the format:
        <filename>.json
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
        # Creating task list for this employee
        employees_progress[str(emp_id)] = []

        # Going through all tasks looking for user ID match
        for task in todos_data:
            if task.get("userId") == emp_id:
                # Found task for this employee, adding it to their task list
                employees_progress[str(emp_id)].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    # Dump dictionary into JSON file with given filename
    with open(filename, mode="w") as json_file:
        json.dump(employees_progress, json_file)


if __name__ == "__main__":
    json_filename = "todo_all_employees.json"
    get_progress_json(json_filename)
