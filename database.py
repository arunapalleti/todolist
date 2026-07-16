import os
import json
from datetime import datetime
import uuid

# Define paths relative to this file
DB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database")
TASKS_FILE = os.path.join(DB_DIR, "tasks.json")
HISTORY_FILE = os.path.join(DB_DIR, "history.json")

def init_db():
    """Initializes the database directory and JSON files if they don't exist."""
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
    
    for file_path in [TASKS_FILE, HISTORY_FILE]:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

# Call on import to ensure database setup
init_db()

def load_tasks():
    """Loads current active tasks from tasks.json."""
    init_db()
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback if file is corrupted
        return []

def save_tasks(tasks):
    """Saves active tasks to tasks.json."""
    init_db()
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

def load_history():
    """Loads archived/completed tasks from history.json."""
    init_db()
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback if file is corrupted
        return []

def save_history(history):
    """Saves history items to history.json."""
    init_db()
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)

def add_task(title, description, priority, category, deadline):
    """Creates a new task and appends it to active tasks."""
    tasks = load_tasks()
    new_task = {
        "id": str(uuid.uuid4()),
        "title": title.strip(),
        "description": description.strip(),
        "priority": priority,
        "category": category,
        "deadline": str(deadline),
        "status": "Pending",
        "created_at": datetime.now().isoformat(),
        "completed_at": None
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def update_task(task_id, title, description, priority, category, deadline, status):
    """Updates fields of an existing task. Handles auto-archiving if status is changed to Completed."""
    if status == "Completed":
        return mark_task_completed(task_id)
        
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = title.strip()
            t["description"] = description.strip()
            t["priority"] = priority
            t["category"] = category
            t["deadline"] = str(deadline)
            t["status"] = status
            save_tasks(tasks)
            return True
    return False

def delete_task(task_id):
    """Deletes a task from the active tasks database."""
    tasks = load_tasks()
    initial_length = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) < initial_length:
        save_tasks(tasks)
        return True
    return False

def mark_task_completed(task_id):
    """Moves a task from tasks.json into history.json and marks it completed with timestamp."""
    tasks = load_tasks()
    task_to_complete = None
    remaining_tasks = []
    
    for t in tasks:
        if t["id"] == task_id:
            task_to_complete = t
        else:
            remaining_tasks.append(t)
            
    if not task_to_complete:
        return False
        
    # Mark task as completed
    task_to_complete["status"] = "Completed"
    task_to_complete["completed_at"] = datetime.now().isoformat()
    
    # Save the updated active tasks
    save_tasks(remaining_tasks)
    
    # Save to history database
    history = load_history()
    history.append(task_to_complete)
    save_history(history)
    
    return True

def delete_history_item(task_id):
    """Removes a single task item from history.json."""
    history = load_history()
    initial_length = len(history)
    history = [h for h in history if h["id"] != task_id]
    if len(history) < initial_length:
        save_history(history)
        return True
    return False

def clear_all_history():
    """Deletes all items from history.json."""
    save_history([])
    return True
