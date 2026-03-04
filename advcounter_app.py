import json
from datetime import datetime, date
import matplotlib.pyplot as plt
import os

DATA_FILE = "tasks.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        tasks = json.load(f)
else:
    tasks = {}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task_count():
    task_name = input("Enter task name: ").strip()
    input_date = input("Enter date (DD-MM-YYYY) or leave blank for today: ").strip()
    if input_date == "":
        input_date = date.today().strftime("%d-%m-%Y")
    else:
        try:
            dt = datetime.strptime(input_date, "%d-%m-%Y")
            input_date = dt.strftime("%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Using today instead.")
            input_date = date.today().strftime("%d-%m-%Y")
    try:
        value = float(input("Enter hours/reps for this task: "))
    except ValueError:
        value = 1
    if task_name not in tasks:
        tasks[task_name] = {}
    tasks[task_name][input_date] = tasks[task_name].get(input_date, 0) + value
    save_data()
    print(f"{task_name} updated for {input_date} with {value} units.\n")

def view_task_stats():
    task_name = input("Enter task name: ").strip()
    if task_name not in tasks:
        print(f"No records found for task '{task_name}'.\n")
        return
    task_data = tasks[task_name]
    for d, v in sorted(task_data.items(), key=lambda x: datetime.strptime(x[0], "%d-%m-%Y")):
        print(f"{d}: {v}")
    dates = sorted(task_data.keys(), key=lambda x: datetime.strptime(x, "%d-%m-%Y"))
    values = [task_data[d] for d in dates]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o', linestyle='-', color='b')
    plt.title(f"Progress of {task_name}")
    plt.xlabel("Date")
    plt.ylabel("Hours / Reps")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\n1. Add Task Count/Hours")
        print("2. View Task Stats/Graph")
        print("3. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            add_task_count()
        elif choice == "2":
            view_task_stats()
        elif choice == "3":
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()