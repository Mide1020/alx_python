import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Create the URL to retrieve employee details
    employee_url = f"{base_url}/users/{employee_id}"

    # Send a GET request to get the employee details
    employee_response = requests.get(employee_url)

    # Check if the request was successful (status code 200)
    if employee_response.status_code == 200:
        employee_data = employee_response.json()
        employee_name = employee_data['name']

        # Create the URL to retrieve TODO items for the employee
        todos_url = f"{base_url}/users/{employee_id}/todos"

        # Send a GET request to get the TODO list for the employee
        todos_response = requests.get(todos_url)

        # Check if the request was successful (status code 200)
        if todos_response.status_code == 200:
            todo_list = todos_response.json()
            
            # Count completed and total tasks
            completed_tasks = 0
            total_tasks = len(todo_list)

            # Collect completed task titles
            completed_task_titles = []
            for todo in todo_list:
                if todo['completed']:
                    completed_tasks += 1
                    completed_task_titles.append(todo['title'])

            # Print the formatted output
            print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
            for title in completed_task_titles:
                print(f" {title}")

        else:
            print(f"Failed to fetch TODO list. Status code: {todos_response.status_code}")
    else:
        print(f"Failed to fetch employee details. Status code: {employee_response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
