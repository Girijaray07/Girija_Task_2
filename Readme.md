# [![📝 Python To-Do List CLI App](./Images/Header.png)](https://github.com/Girijaray07/Girija_Task_2)

A **Command Line Interface (CLI)** based To-Do List application in Python that allows users to **add**, **remove**, **update**, **view**, **save**, and **load** tasks with their statuses. Ideal for basic task tracking via terminal.

---

## 🚀 Features

* ✅ Add task with custom status
* ✅ Update existing tasks
* ✅ Delete specific tasks
* ✅ View all tasks in tabular format
* ✅ Automatically loads tasks from a file on startup
* ✅ Saves tasks to a file upon exiting
* ✅ Aligned display for better readability

---

## 📂 File Structure

```
Task2/
├── Files/
│   └── Tasks.txt         # Stores saved tasks
├── todo.py               # Main Python source file
└── Readme.md             # Project documentation
```

---

## 🛠 How to Run

```bash
python -u todo.py
```

Make sure you're inside the correct directory before running the script.

---

## 💡 Example Menu

```
***** Welcome to Python To-Do-List App *****

Select from Below Option:
1. Add a Task.
2. Remove a Task.
3. Update a Task.
4. View all Tasks.
5. Exit.
```

---

## 📄 Sample Task Display

```
    Task        |   Status
1. Finish Code |  Pending
2. Review PR   |  Completed
```

---

## 📦 Data Persistence

Tasks are automatically loaded from `Files/Tasks.txt` at startup and saved to it on exit. Each line follows the format:

```
<task> | <status>
```

---

## 📌 Notes

* Handles invalid inputs gracefully using try-except blocks.
* Dynamically adjusts column spacing based on longest task and status.
* Easy to extend with features like due dates, priorities, or task IDs.

---

## 📬 Contributions

Want to contribute?

1. Fork the repository
2. Add new features or improve formatting
3. Submit a pull request 🚀

---

**Happy Tasking! ✅**
