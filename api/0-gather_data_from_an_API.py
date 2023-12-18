#!/usr/bin/python3

"""
Gather data from an API for a given employee
ID and display TODO list progress.
"""

import requests
import sys


def get_employee_progress(employee_id):
    """
    For a given employee ID, returns information about
    their TODO list progress
    """
    # API endpoint URLs
    url_base = f"https://jsonplaceholder.typicode.com/"
    url_employee = url_base + f"users/{employee_id}"
    url_todos = url_base + f"todos?userId={employee_id}"

    # Send GET request to the API for employee name
    employee_response = requests.get(url_employee)
    employee_data = employee_response.json()

    if employee_response.status_code != 200:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        sys.exit(1)

    employee_name = employee_data.get('name')

    # Send GET request to the API for employee tasks
    todos_response = requests.get(url_todos)
    todos_data = todos_response.json()

    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        sys.exit(1)

    total_tasks = len(todos_data)
    completed_tasks = 0
    for task in todos_data:
        # Counting booleans
        completed_tasks += task['completed']

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks, total_tasks))

    for task in todos_data:
        if task['completed']:
            print("\t {}".format(task['title']))


if __name__ == "__main__":
    # Checking correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <id>")
        sys.exit(1)

    # Converting string ID to integer
    employee_id = int(sys.argv[1])
    get_employee_progress(employee_id)
