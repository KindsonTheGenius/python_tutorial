tasks = []

def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete task")
    print("5. Exit")

def add_task():
    description = input("Enter the task description")
    tasks.append({"description": description, "completed": False})
   # print(f"Task "{description}"added!")

def view_task():
    return

def mark_task_complete():
    return

def delete_task():
    return