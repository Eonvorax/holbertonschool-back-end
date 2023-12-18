#!/usr/bin/python3

"""
Gather data from an API for a given employee
ID and display TODO list progress.
"""

import requests
import sys


def get_employee_progress(employee_ID):
    """
    For a given employee ID, returns information about
    their TODO list progress
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{url}/users/{employee_ID}"
    todos_url = f"{url}/todos?userId={employee_ID}"

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if employee_response.status_code == 200:
        employee_name = employee_data.get('name')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    if todos_response.status_code == 200:
        total_tasks = len(todos_data)
        completed_tasks = 0
    for task in todos_data:
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
