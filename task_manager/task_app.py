import json


def show_tasks():
    try:
        with open("tasks.json", "r") as file:
            content = json.load(file)
        for task in content:
            if task["completed"] == True:
                print(f"[X] {task['task']}")
            else:
                print(f"[] {task['task']}")
    except FileNotFoundError:
        print("No tasks found.")


def add_task(new_task_name: str):
    try:
        with open("tasks.json", "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        content = []

    new_item = {
        "task": new_task_name,
        "completed": False
    }
    content.append(new_item)

    with open("tasks.json", "w") as file:
        json.dump(content, file)
    print(f"Added task: {new_task_name}")


def complete_task(target_task_name: str):
    try:
        with open("tasks.json", "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        print('No tasks found')
        return

    for item in content:
        if item["task"] == target_task_name:
            item["completed"] = True
            break

    with open("tasks.json", "w") as file:
        json.dump(content, file)
    print(f"Completed task: {target_task_name}")


def delete_task(target_task_name: str):
    try:
        with open("tasks.json", "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        print("No tasks found.")
        return

    for item in content:
        if item["task"] == target_task_name:
            content.remove(item)
            break

    with open("tasks.json", "w") as file:
        json.dump(content, file)
    print(f"Deleted task: {target_task_name}")


# --- Menu Loop ---
while True:
    print("\n--- Task Manager Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        ask = input("Enter new task name: ")
        add_task(ask)
    elif choice == "3":
        ask = input("Which task did you complete? ")
        complete_task(ask)
    elif choice == "4":
        ask = input("Which task did you want to delete? ")
        delete_task(ask)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-5.")
