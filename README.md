# 📚 MyDatabaseApp — GUI-Based SQLite Library Management

A PyQt5-based GUI application for managing a library database using SQLite. Designed for simplicity and ease of use, this project allows users to create tables, insert dummy data, run SQL queries, and interact with a prebuilt library database through a visually intuitive interface.

---

## 🗂️ Project Structure

MyDatabaseApp/ │ 
├── databases/ # SQL-related resources │ 
├── create_tables.sql # SQL script to create database schema │ 
├── insert_dummy_data.sql # SQL script to populate with sample data │ 
├── queries.sql # Common SQL query templates │ 
└── siu_library.db # Main SQLite database file │ 
├── gui_app/ # GUI application folder │ 
├── pycache/ # Compiled Python cache │ 
├── db_manager.py # Core DB interaction logic │ 
├── eg_csv.csv # Example CSV for data import/export │ 
├── initialize_db.py # One-time DB setup using SQL scripts │ 
├── main.py # Main GUI launcher │ 
├── siu_library.db # GUI-side duplicate DB (if needed) │ 
├── styles.qss # Qt stylesheet for styling the GUI │ 
└── ui_main.py # Auto-generated PyQt5 UI Python file │ 
├── requirements.txt # Python dependencies


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


