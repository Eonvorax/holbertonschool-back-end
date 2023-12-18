#!/usr/bin/python3
"""Gather data from an API for a given employee
ID and store TODO list progress in a JSON file"""

import json
import requests
import sys


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

    employee_list = []
    for employee in employee_data:
        employee_list.append({
        "id" : employee.get("id"),
        "username" : employee.get("username")
        })

    print(employee_list)

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # TODO replace the following by a for loop going through employee_list
    return
    # Create base dictionary and list to contain tasks
    tasks_dict = {}
    tasks_list = []

    # Fill list with dictionaries in requested format for JSON
    for task in todos_data:
        tasks_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_username
            })

    # Add list to the dictionary
    tasks_dict[str(employee_ID)] = tasks_list

    # Generate filename and dump dictionary into JSON file
    with open(filename, mode="w") as json_file:
        json.dump(tasks_dict, json_file)


if __name__ == "__main__":
    json_filename = "todo_all_employees.json"
    get_progress_json(json_filename)
