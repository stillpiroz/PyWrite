"""Main application status bar."""


from PySide6.QtWidgets import QStatusBar


class MainStatusBar(QStatusBar):
    """Create and configure the main application status bar."""

    def __init__(self):
        super().__init__()

        self.showMessage("Ready")
