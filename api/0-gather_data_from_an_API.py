import requests

def get_employee_info(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a request to get employee details
    employee_url = f"{base_url}/users/{employee_id}"
    response = requests.get(employee_url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve employee information for ID {employee_id}")
        return

    employee_data = response.json()
    employee_name = employee_data["name"]

    # Make a request to get the employee's TODO list
    todos_url = f"{base_url}/users/{employee_id}/todos"
    response = requests.get(todos_url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve TODO list for ID {employee_id}")
        return

    todos = response.json()

    # Calculate the number of completed tasks
    completed_tasks = [todo for todo in todos if todo["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todos)

    # Print the employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")
    
    # Print the titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_info(employee_id)
    