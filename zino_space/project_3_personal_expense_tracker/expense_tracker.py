import json
import os

# File to save expenses
DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses():
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expenses(expenses):
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    description = input("Enter a description: ")

    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })
    save_expenses(expenses)
    print("Expenses added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nExpenses: ")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: {expense['amount']}, "
              f"Category: {expense['category']}, "
              f"Description: {expense['description']}")

def delete_expense(expense):
    view_expenses(expense)
    if not expenses:
        print("No expenses recorded.")
        return

    try:
        index = int(input("Enter the number of the expense to delete: "))
        if 1 <= index <= len(expenses):
            removed_expense = expense.pop(index - 1)
            save_expenses(expenses)
            print(f"Deleted expense: {removed_expense}")
        else:
            print("Invalid number")
    except ValueError:
        print("Please enter a valid number.")

# def summarize_expenses(expenses):
#     if not expenses:
#         print("No expenses recorded.")
#         return
#
#     summary = {}
#     for expense in expenses:
#         summary[expense['category']]