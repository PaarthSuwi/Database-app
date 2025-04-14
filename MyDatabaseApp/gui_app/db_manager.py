import os
from PyQt5.QtSql import QSqlDatabase

def create_connection():
    # Construct absolute path to databases/siu_library.db
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "databases", "siu_library.db")

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(db_path)

    if not db.open():
        print("❌ Cannot establish a database connection.")
        return False

    print(f"✅ Connected to DB at: {db_path}")
    return True
