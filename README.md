# 📚 MyDatabaseApp — GUI-Based SQLite Library Management

A PyQt5-based GUI application for managing a library database using SQLite. Designed for simplicity and ease of use, this project allows users to create tables, insert dummy data, run SQL queries, and interact with a prebuilt library database through a visually intuitive interface.

---

## 🗂️ Project Structure
MyDatabaseApp/
│
├── databases/                            # SQL resources and main database
│   ├── create_tables.sql                 # SQL script to define DB schema
│   ├── insert_dummy_data.sql             # Preloaded sample data
│   ├── queries.sql                       # Collection of SQL query examples
│   └── siu_library.db                    # Main SQLite database file
│
├── gui_app/                              # GUI application logic and assets
│   ├── __pycache__/                      # Python bytecode cache
│   ├── db_manager.py                     # DB access and operations
│   ├── eg_csv.csv                        # Sample CSV for import/export
│   ├── initialize_db.py                  # DB setup script using SQL files
│   ├── main.py                           # Entry point for launching the GUI
│   ├── siu_library.db                    # Duplicate DB used by GUI (optional)
│   ├── styles.qss                        # Qt stylesheet for UI customization
│   └── ui_main.py                        # PyQt5 UI layout (auto-generated)
│
├── requirements.txt                      # Python package dependencies


---

## 🚀 Features

- ✅ GUI to interact with SQLite database
- 🛠 Create and populate tables using `.sql` scripts
- 🔍 View, insert, update, and delete records
- 📤 Import/export data via CSV
- 🎨 Styled with custom `.qss` for clean UI design

---

## 🖥️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/MyDatabaseApp.git
cd MyDatabaseApp

```
## Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

##  Install Requirements
```bash
pip install -r requirements.txt
```

## Initialize the Database
```bash
python gui_app/initialize_db.py
```

## python gui_app/main.py
```bash
python gui_app/main.py
```

Developed by Paarth Suwi
Inspired by academic DBMS projects and GUI-based database tools.

Happy coding! 💻📊


