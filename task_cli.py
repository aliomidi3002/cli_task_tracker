import sys
import json
import os
from datetime import datetime

from click import command

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")


def list_tasks(status=None):
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    filtered = tasks if status is None else [t for t in tasks if t["status"] == status]
    
    if not filtered:
        print(f"No tasks with status: {status}")
        return
    
    for task in filtered:
        print(f"[{task['id']}] {task['description']} - {task['status']} (created: {task['createdAt']})")


def update_task(task_id, new_description):
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == int(task_id):
            task["description"] = new_description
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    
    print(f"Task {task_id} not found.")


def delete_task(task_id):
    tasks = load_tasks()
    
    filtered = [t for t in tasks if t["id"] != int(task_id)]
    
    if len(filtered) == len(tasks):
        print(f"Task {task_id} not found.")
        return
    
    save_tasks(filtered)
    print(f"Task {task_id} deleted successfully.")

def mark_task(task_id, status):
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == int(task_id):
            task["status"] = status
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    
    print(f"Task {task_id} not found.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py add <description>")
        else:
            add_task(sys.argv[2])

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python task_cli.py update <id> <description>")
        else:
            update_task(sys.argv[2], sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py delete <id>")
        else:
            delete_task(sys.argv[2])

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py mark-in-progress <id>")
        else:
            mark_task(sys.argv[2], "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py mark-done <id>")
        else:
            mark_task(sys.argv[2], "done")
            
    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
