"""Define and configure the application's toolbar."""


from PySide6.QtWidgets import QToolBar


class MainToolBar(QToolBar):
    """Create main toolbar."""

    def __init__(self):
        super().__init__()
