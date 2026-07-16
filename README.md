# SmartTodo

SmartTodo is a professional, modern To-Do List web application built using **Streamlit** and a local **JSON database**. Featuring a vibrant interface with custom card styling, smooth gradients, real-time status reporting, search capabilities, deep filtering, and full completion statistics.

---

## Key Features

- ⚡ **Interactive Dashboard**: High-level visual KPI metrics (Total, Completed, Pending, and Completion Rate), progress tracking bar, task distribution statistics (interactive charts), and recent task list.
- 📋 **Comprehensive Task Manager**: Full CRUD (Create, Read, Update, Delete) capability. Tasks can have Title, Description, Priority (High, Medium, Low), Category (Personal, Work, Study, Shopping, Health), and Deadline.
- 📜 **Completion History Archive**: Auto-archived log showing all completed tasks. Tracks Completion Date and calculates the completion time duration. Includes search, filter by month, pagination, single item deletion, and full history reset features.
- 📥 **CSV Export Utility**: Export active tasks or the complete historical logs into standard CSV sheets directly from the web interface.
- 🎨 **Premium Styling & Dark Mode**: Rounded card styles, clean elevation shadows, dynamic hover scaling transitions, clear badges, and a custom Dark Mode Toggle that saves preferences instantly in session state.
- 🔄 **Auto Refresh Option**: Configure the dashboard to sync data automatically every 30 seconds with a simple sidebar checkbox.
- 💾 **Reliable JSON Engine**: Auto-healing file database logic that automatically initializes database folder structure and JSON archives upon application boot if missing.

---

## Folder Structure

```text
SmartTodo/
│
├── app.py                      # Main entry point (Dashboard View)
├── requirements.txt            # Python environment dependencies
├── .env                        # Local configuration file
├── .gitignore                  # Git tracking exclusion list
├── README.md                   # User documentation
│
├── database/
│   ├── tasks.json              # Active tasks database
│   └── history.json            # Completed tasks archive
│
├── pages/
│   ├── Task_Page.py            # Active tasks manager page view
│   └── History_Page.py         # History logger and CSV exporter page view
│
├── utils/
│   ├── database.py             # CRUD database wrapper logic
│   ├── helper.py               # Field validation, uuid, and date formatters
│   └── styles.py               # CSS injectors, animations, and Dark Mode
│
└── assets/
    └── logo.png                # Brand asset (placeholder)
```

---

## Installation & Setup

### Prerequisites
- Python 3.11 or higher installed on your machine.

### 1. Clone or Copy Workspace Files
Ensure all project files are correctly structured in your desired folder.

### 2. Install Dependencies
Install all package requirements using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Streamlit application server:
```bash
streamlit run app.py
```

Streamlit will compile and launch the dashboard immediately in your default web browser (typically accessible at `http://localhost:8501`).

---

## UI Screenshots
*(Screenshots placeholder)*
- **Dashboard View**: View high level charts and task lists.
- **Active Tasks View**: Add new tasks and update existing ones.
- **History View**: Search history log and export files.
