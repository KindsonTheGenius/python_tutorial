#To Do List

tasks = []

def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete task")
    print("5. Exit")

def add_task():
    description = input("Enter the task description: ")
    tasks.append({"description": description, "completed": False})
   # print(f"Task "{description}"added!")

def view_tasks():
    if not tasks:
        print("No tasks available in the list")
        return

    print("Tasks:")
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{i+1}. {task['description']} - {status}")

def mark_task_complete():
    view_tasks()
    task_number = int(input("Enter the number to mark as complete: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number-1]["completed"] = True
        print(f"Task {task_number} has been marked as complete")
    else:
        print(f"Please enter a number between 1 and {len(tasks)}.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the number to delete: "))
    if 1 <= task_number <= len(tasks):
        deleted = tasks.pop(task_number-1)
        print(f"Task {deleted['description']} has been successfully removed")
    else:
        print(f"Please enter a number between 1 and {len(tasks)}.")
