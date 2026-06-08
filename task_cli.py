import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        print("add command recognized")
    elif command == "update":
        print("update command recognized")
    elif command == "delete":
        print("delete command recognized")
    elif command == "mark-in-progress":
        print("mark-in-progress command recognized")
    elif command == "mark-done":
        print("mark-done command recognized")
    elif command == "list":
        print("list command recognized")
    else:
        print(f"Unknown command: {command}")

    tasks = load_tasks()
    print(tasks)  # should print []
    save_tasks(tasks)  # should create tasks.json

if __name__ == "__main__":
    main()
