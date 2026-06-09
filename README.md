# Task Tracker CLI

A simple command line tool to track your tasks, built with Python.

## Usage

```bash
# Add a task
python task_cli.py add "Task description"

# List all tasks
python task_cli.py list

# List by status
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done

# Update a task
python task_cli.py update <id> "New description"

# Delete a task
python task_cli.py delete <id>

# Mark a task
python task_cli.py mark-in-progress <id>
python task_cli.py mark-done <id>
```

## Task Properties
- `id` - unique identifier
- `description` - task description
- `status` - todo | in-progress | done
- `createdAt` - creation timestamp
- `updatedAt` - last updated timestamp