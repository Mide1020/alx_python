import requests
import csv
import sys

def export_employee_tasks_to_csv(employee_id):
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Create the URL to retrieve employee details
    employee_url = f"{base_url}/users/{employee_id}"

    # Send a GET request to get the employee details
    employee_response = requests.get(employee_url)

    # Check if the request was successful (status code 200)
    if employee_response.status_code == 200:
        employee_data = employee_response.json()
        user_id = employee_data['id']
        username = employee_data['username']

        # Create the URL to retrieve TODO items for the employee
        todos_url = f"{base_url}/todos?userId={user_id}"

        # Send a GET request to get the TODO list for the employee
        todos_response = requests.get(todos_url)

        # Check if the request was successful (status code 200)
        if todos_response.status_code == 200:
            todo_list = todos_response.json()

            # Create a CSV file with the user_id as the filename
            filename = f"{user_id}.csv"

            # Write tasks to the CSV file
            with open(filename, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
                for todo in todo_list:
                    task_completed_status = "True" if todo['completed'] else "False"
                    task_title = todo['title']
                    csv_writer.writerow([user_id, username, task_completed_status, task_title])

            print(f"Tasks for User {user_id} ({username}) have been exported to {filename}")
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
    
    export_employee_tasks_to_csv(employee_id)
