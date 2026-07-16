from datetime import datetime
import json


class HabitTracker():
    def __init__(self):
        self.file = "progress.json"

    def log_workout(self, exercise, weights):
        today = datetime.now().strftime("%Y-%m-%d")
        entry = {
            "date": today,
            "type": "workout",
            "exercise": exercise,
            "volumes": weights
        }
        try:
            with open(self.file, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        data.append(entry)

        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    def log_study(self, task, minutes):
        today = datetime.now().strftime("%Y-%m-%d")
        entry = {
            "date": today,
            "type": "study",
            "task": task,
            "minutes": minutes
        }
        try:
            with open(self.file, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        data.append(entry)

        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    def view_report(self):
        total_study = 0
        total_workout = 0
        try:
            with open(self.file, "r") as file:
                all_entries = json.load(file)
            for entry in all_entries:
                if entry.get('type', 'N/A') == "study":
                    total_study += entry["minutes"]
                elif entry.get('type', 'N/A') == "workout":
                    total_workout += sum(entry["volumes"])
        except FileNotFoundError:
            all_entries = []
        print(f"Total time spent studying is {total_study} minutes")
        print(f"Total volume lifted is {total_workout}")


tracker = HabitTracker()

while True:
    print("\n--- IRON LOGIC TRACKER ---")
    print("1. Log Workout")
    print("2. Log Study")
    print("3. View Report")
    print("4. Exit")

    choice = input("\n Choose an option: ")

    if choice == "1":
        ex = input("Exercise name: ")
        w_input = input("Enter weights seperated by commas (e.g. 135,145): ")
        weights = [int(w.strip()) for w in w_input.split(",")]
        tracker.log_workout(ex, weights)
        print("Workout Saved!")

    elif choice == "2":
        task = input("What did you study? ")
        mins = int(input("How many minutes? "))
        tracker.log_study(task, mins)
        print("Study Session Saved!")

    elif choice == "3":
        tracker.view_report()

    elif choice == "4":
        print("Stay Disciplined. See you tomorrow!")
        break
