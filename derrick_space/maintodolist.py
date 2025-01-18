from todolist import display_menu, add_task, view_tasks, mark_task_complete, delete_task

def main():
    while True:
        #try:
            display_menu()
            choice = input("\nEnter Your Choice (1-5): ")
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                mark_task_complete()
            elif choice == "4":
                delete_task()
            elif choice == "5":
                print("Exiting To Do list. Goodbye!")
                break
            else:
                print("Wrong choice.")
        #except:
            #print("Please enter a valid number")
if __name__ == "__main__":
    main()