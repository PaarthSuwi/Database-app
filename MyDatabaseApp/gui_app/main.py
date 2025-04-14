import sys
from PyQt5.QtWidgets import QApplication
from ui_main import MainWindow
from db_manager import create_connection

def main():
    app = QApplication(sys.argv)
    if not create_connection():
        sys.exit(1)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
