from expense_tracker import load_expenses, save_expenses, add_expenses, view_expenses, delete_expense

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Delete Expense")
        print("4. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            add_expenses()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            delete_expense()
        elif choice == 4:
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()