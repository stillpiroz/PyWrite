"""Define and configure the application's main window."""


import sys

from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """Create main window."""
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyWrite")
        self.resize(1000, 700)
