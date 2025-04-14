from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QComboBox,
    QTableView, QMessageBox, QHBoxLayout, QLabel, QTextEdit, QFileDialog
)
from PyQt5.QtSql import QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import Qt
import csv
import matplotlib.pyplot as plt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("📚 SIU Library Manager")
        self.resize(1000, 750)
        self.setStyleSheet("font-family: 'Segoe UI'; font-size: 14px;")

        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.main_layout = QVBoxLayout(self.central)

        heading = QLabel("📘 SIU Library Database Interface")
        heading.setAlignment(Qt.AlignCenter)
        heading.setStyleSheet("font-size: 22px; font-weight: bold; color: #2c3e50; padding: 10px;")
        self.main_layout.addWidget(heading)

        self.table_selector = QComboBox()
        self.table_selector.addItems([
            "Books", "Authors", "Categories", "Members",
            "Borrow_Records", "Reservations", "Librarians", "Fines"
        ])
        self.table_selector.setFixedHeight(35)
        self.table_selector.currentIndexChanged.connect(self.load_table)
        self.main_layout.addWidget(self.table_selector)

        self.table = QTableView()
        self.table.setSortingEnabled(True)
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet("""
            QTableView {
                background-color: #ffffff;
                alternate-background-color: #f2f2f2;
                gridline-color: #dcdcdc;
                selection-background-color: #aed6f1;
                selection-color: #000000;
            }
            QHeaderView::section {
                background-color: #ecf0f1;
                font-weight: bold;
                border: 1px solid #dcdcdc;
            }
        """)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.main_layout.addWidget(self.table)

        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("➕ Add Row")
        self.del_btn = QPushButton("🗑️ Delete Selected")
        self.save_btn = QPushButton("💾 Save Changes")
        for btn in [self.add_btn, self.del_btn, self.save_btn]:
            btn.setFixedHeight(38)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border-radius: 5px;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
                QPushButton:pressed {
                    background-color: #1f618d;
                }
            """)
            btn_layout.addWidget(btn)
        self.main_layout.addLayout(btn_layout)

        self.add_btn.clicked.connect(self.add_row)
        self.del_btn.clicked.connect(self.delete_row)
        self.save_btn.clicked.connect(self.save_changes)

        self.query_mode_btn = QPushButton("🛠️ Toggle SQL Query Mode")
        self.query_mode_btn.setCheckable(True)
        self.query_mode_btn.setFixedHeight(35)
        self.query_mode_btn.toggled.connect(self.toggle_query_mode)
        self.main_layout.addWidget(self.query_mode_btn)

        self.query_input = QTextEdit()
        self.query_input.setPlaceholderText("Write your SQL query here...")
        self.query_input.setFixedHeight(120)
        self.query_input.hide()

        self.run_query_btn = QPushButton("▶️ Run SQL Query")
        self.run_query_btn.setFixedHeight(35)
        self.run_query_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        self.run_query_btn.clicked.connect(self.run_sql_query)
        self.run_query_btn.hide()

        self.export_csv_btn = QPushButton("⬇️ Export Results to CSV")
        self.export_csv_btn.setFixedHeight(35)
        self.export_csv_btn.clicked.connect(self.export_query_to_csv)
        self.export_csv_btn.hide()

        self.visualize_btn = QPushButton("📊 Visualize Results (Pie)")
        self.visualize_btn.setFixedHeight(35)
        self.visualize_btn.clicked.connect(self.visualize_query_results)
        self.visualize_btn.hide()

        self.query_output = QTableView()
        self.query_output.hide()

        self.main_layout.addWidget(self.query_input)
        self.main_layout.addWidget(self.run_query_btn)
        self.main_layout.addWidget(self.export_csv_btn)
        self.main_layout.addWidget(self.visualize_btn)
        self.main_layout.addWidget(self.query_output)

        self.load_table()

    def load_table(self):
        selected_table = self.table_selector.currentText()
        self.model = QSqlTableModel(self)
        self.model.setTable(selected_table)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.table.setModel(self.model)

    def add_row(self):
        row = self.model.rowCount()
        self.model.insertRow(row)

    def delete_row(self):
        selected = self.table.selectionModel().selectedRows()
        for index in selected:
            self.model.removeRow(index.row())
        self.model.submitAll()

    def save_changes(self):
        if self.model.submitAll():
            QMessageBox.information(self, "✅ Saved", "Changes saved to the database.")
        else:
            QMessageBox.warning(self, "⚠️ Error", "Failed to save changes.")

    def toggle_query_mode(self, checked):
        self.query_input.setVisible(checked)
        self.run_query_btn.setVisible(checked)
        self.query_output.setVisible(checked)
        self.export_csv_btn.setVisible(checked)
        self.visualize_btn.setVisible(checked)

    def run_sql_query(self):
        raw_sql = self.query_input.toPlainText().strip()
        if not raw_sql:
            QMessageBox.warning(self, "Empty Query", "Please write a SQL query to run.")
            return

        self.query_model = QSqlQueryModel()
        self.query_model.setQuery(raw_sql)

        if self.query_model.lastError().isValid():
            QMessageBox.critical(self, "SQL Error", self.query_model.lastError().text())
        else:
            self.query_output.setModel(self.query_model)
            QMessageBox.information(self, "Success", "Query executed successfully.")

    def export_query_to_csv(self):
        model = self.query_output.model()
        if not model:
            QMessageBox.warning(self, "No Data", "No query results to export.")
            return

        path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv)")
        if not path:
            return

        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            headers = [model.headerData(i, Qt.Horizontal) for i in range(model.columnCount())]
            writer.writerow(headers)

            for row in range(model.rowCount()):
                writer.writerow([model.data(model.index(row, col)) for col in range(model.columnCount())])

        QMessageBox.information(self, "Exported", f"Results exported to:\n{path}")

    def visualize_query_results(self):
        model = self.query_output.model()
        if not model or model.columnCount() < 2:
            QMessageBox.warning(self, "Invalid", "Need at least 2 columns to create a pie chart.")
            return

        labels = []
        sizes = []

        try:
            for row in range(model.rowCount()):
                labels.append(str(model.data(model.index(row, 0))))
                sizes.append(float(model.data(model.index(row, 1))))
        except ValueError:
            QMessageBox.warning(self, "Error", "Second column must be numeric.")
            return

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("📊 SQL Query Result - Pie Chart")
        plt.tight_layout()
        plt.show()
