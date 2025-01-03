import todo_list

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6)")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting To-Do list. Goodbye!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()