"""Define and configure the application's toolbar."""


import sys

from PySide6.QtWidgets import QToolBar


class MainToolBar(QToolBar):
    """Create main toolbar."""

    def __init__(self):
        super().__init__()
