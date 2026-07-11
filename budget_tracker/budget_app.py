# budget_tracker/budget_app.py
import json


def get_safe_integer(prompt_message):
    while True:
        try:
            value = int(input(prompt_message))
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def show_expenses():
    try:
        with open("budget.json", "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        print("No expenses recorded.")
        return

    total_spent = 0
    for expense in content:
        print(f"[{expense['category']}] {expense['item']}: ${expense['amount']}")
        total_spent += expense["amount"]
    print(f"Total spending: ${total_spent}")


def add_expense(item_name: str, amount: int, category: str):
    try:
        with open("budget.json", "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        content = []

    new_dict = {
        "item": item_name,
        "amount": amount,
        "category": category
    }
    content.append(new_dict)

    with open("budget.json", "w") as file:
        json.dump(content, file)
    print(f"Successfully logged: {item_name} (${amount})")


def delete_expense(target_item_name: str):
    try:
        with open("budget.json", "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        print("No expenses found.")
        return

    for row in content:
        if row['item'] == target_item_name:
            content.remove(row)
            break

    with open("budget.json", "w") as file:
        json.dump(content, file)
    print(f"Successfully deleted: {target_item_name}")


# --- Menu Loop ---
while True:
    print("\n--- Personal Budget Tracker ---")
    print("1. View expenses & Total")
    print("2. Add Expense")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_expenses()
    elif choice == "2":
        item = input("Enter item name: ")
        amount = get_safe_integer("Enter amount: $")
        category = input("Enter category (e.g. Food, Bill): ")
        add_expense(item, amount, category)
    elif choice == "3":
        item = input("Enter item name to delete: ")
        delete_expense(item)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid number (1-4)")
