import sqlite3
import os

# Get absolute path to siu_library.db
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FOLDER = os.path.join(BASE_DIR, "databases")
os.makedirs(DB_FOLDER, exist_ok=True)  # Create 'databases' folder if missing

db_path = os.path.join(DB_FOLDER, "siu_library.db")

def execute_sql_script(file_path, connection):
    with open(file_path, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    connection.executescript(sql_script)

# Create and connect to database
conn = sqlite3.connect(db_path)

# Execute scripts
execute_sql_script(os.path.join(DB_FOLDER, "create_tables.sql"), conn)
execute_sql_script(os.path.join(DB_FOLDER, "insert_dummy_data.sql"), conn)

conn.commit()
conn.close()

print("✅ siu_library.db created successfully at:", db_path)
