import requests
import sys
import csv

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct URLs for employee details and TODO list
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        # Fetch employee details
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()

        # Fetch TODO list
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        # Calculate progress
        total_tasks = len(todo_list)
        completed_tasks = sum(1 for task in todo_list if task["completed"])

        # Display the progress in the correct format
        print(f"Employee {employee_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

        # Display the titles of completed tasks
        completed_task_titles = [task["title"] for task in todo_list if task["completed"]]
        for title in completed_task_titles:
            print(f"\t{title}")

        # Export data to CSV
        csv_filename = f"employee_{employee_id}_todo.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Employee Name", "Total Tasks", "Completed Tasks"])
            csv_writer.writerow([employee_data['name'], total_tasks, completed_tasks])
            csv_writer.writerow(["Completed Task Titles"])
            csv_writer.writerows([[title] for title in completed_task_titles])
        
        print(f"Data exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
