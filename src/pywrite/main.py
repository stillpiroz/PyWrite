"Main App Endpoint"


import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from pywrite.gui.main_window import MainWindow


def main():
    """Initialize and run the application."""

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()
    sys.exit(app.exec())
