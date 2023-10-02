import requests
import sys

def get_employee_info(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to the employee details endpoint
    employee_url = f"{base_url}/users/{employee_id}"
    response = requests.get(employee_url)

    if response.status_code != 200:
        print(f"Failed to retrieve employee information for ID {employee_id}")
        return

    employee_data = response.json()
    employee_name = employee_data.get("name")

    # Make a GET request to the employee's TODO list endpoint
    todo_url = f"{base_url}/users/{employee_id}/todos"
    response = requests.get(todo_url)

    if response.status_code != 200:
        print(f"Failed to retrieve TODO list for ID {employee_id}")
        return

    todo_list = response.json()

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todo_list if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todo_list)

    # Print the employee information
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")

    # Print the titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
