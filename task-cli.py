import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)

    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()

    # Generate new ID
    new_id = 1 if len(tasks) == 0 else tasks[-1]["id"] + 1

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_id})")

def list_tasks(filter_status=None):
    tasks = load_tasks()

    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]

    if not tasks:
        print("No tasks found.")
        return

    for t in tasks:
        print(f"{t['id']}. {t['description']} [{t['status']}]")

def update_task(task_id, new_description):
    tasks = load_tasks()

    for t in tasks:
        if t["id"] == task_id:
            t["description"] = new_description
            t["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return

    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()

    # Filter out the task with matching ID
    new_tasks = [t for t in tasks if t["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print(f"Task with ID {task_id} not found.")
        return

    save_tasks(new_tasks)
    print(f"Task {task_id} deleted successfully.")

def mark_in_progress(task_id):
    tasks = load_tasks()

    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "in-progress"
            t["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task_id} marked as in-progress.")
            return

    print(f"Task with ID {task_id} not found.")

def mark_done(task_id):
    tasks = load_tasks()

    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "done"
            t["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return

    print(f"Task with ID {task_id} not found.")

def main():
    args = sys.argv

    if len(args) < 2:
        print("No command provided.")
        return

    command = args[1]

    if command == "add":
        if len(args) < 3:
            print("Please provide a task description.")
        else:
            description = args[2]
            add_task(description)

    elif command == "list":
        if len(args) == 2:
            list_tasks()  # list all
        else:
            status = args[2]
            allowed = ["todo", "in-progress", "done"]
            if status not in allowed:
                print("Invalid status. Use: todo, in-progress, done")
            else:
                list_tasks(status)

    elif command == "update":
        if len(args) < 4:
            print("Usage: update <id> <new description>")
        else:
            try:
                task_id = int(args[2])
                new_description = args[3]
                update_task(task_id, new_description)
            except ValueError:
                print("Task ID must be a number.")

    elif command == "delete":
        if len(args) < 3:
            print("Usage: delete <id>")
        else:
            try:
                task_id = int(args[2])
                delete_task(task_id)
            except ValueError:
                print("Task ID must be a number.")

    elif command == "mark-in-progress":
        if len(args) < 3:
            print("Usage: mark-in-progress <id>")
        else:
            try:
                task_id = int(args[2])
                mark_in_progress(task_id)
            except ValueError:
                print("Task ID must be a number.")

    elif command == "mark-done":
        if len(args) < 3:
            print("Usage: mark-done <id>")
        else:
            try:
                task_id = int(args[2])
                mark_done(task_id)
            except ValueError:
                print("Task ID must be a number.")

    else:
        print("Unknown command.")

    
if __name__ == "__main__":
    main()
