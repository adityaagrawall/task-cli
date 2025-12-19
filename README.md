Task Tracker CLI
A simple command-line Task Tracker application built using Python.
It lets you add, update, delete, and track tasks using a JSON file as storage.
Features
Add new tasks
Update task description
Delete tasks
Mark tasks as todo, in-progress, or done
List all tasks
List tasks by status (todo/in-progress/done)
Automatically creates tasks.json if missing or empty
Stores timestamps: createdAt, updatedAt
Commands
Add a task
python3 task-cli.py add "Buy milk"
Update a task
python3 task-cli.py update <id> "New description"
Delete a task
python3 task-cli.py delete <id>"
Mark as in-progress
python3 task-cli.py mark-in-progress <id>
Mark as done
python3 task-cli.py mark-done <id>
List all tasks
python3 task-cli.py list
List by status
python3 task-cli.py list todo
python3 task-cli.py list in-progress
python3 task-cli.py list done
Task Structure (JSON)
Each task is stored like this:
{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "2025-12-19 14:30:21",
  "updatedAt": "2025-12-19 14:30:21"
}
How it Works (Short Explanation)
The app reads and writes tasks to tasks.json
If the file doesn’t exist or is empty, it creates a new one with []
Each command is handled through sys.argv
IDs auto-increment based on the last task
Timestamps use Python’s datetime
Requirements
Python 3 installed
No external libraries used
Running the Project
Run commands using:
python3 task-cli.py <command> <arguments>
Why I Built This
To practice:
Working with the filesystem
JSON data handling
CLI arguments
Clean Python functions
Basic state management

https://roadmap.sh/projects/task-tracker
