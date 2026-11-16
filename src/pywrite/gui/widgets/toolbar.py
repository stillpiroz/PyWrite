"""Define and configure the application's toolbar."""


from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QToolBar

from pywrite.resources import resources_rc


class MainToolBar(QToolBar):
    """Create main toolbar."""

    def __init__(self):
        super().__init__()

        # --- Add formatting actions ---
        self.bold_action = BoldAction()
        self.italic_action = ItalicAction()
        self.underline_action = UnderlineAction()

        self.addActions([
            self.bold_action,
            self.italic_action,
            self.underline_action,
        ])


class ToolbarAction(QAction):
    """Base class for toolbar actions."""

    def __init__(self, callback, icon):
        super().__init__()

        self.setIcon(QIcon(icon))
        self.triggered.connect(callback)


# ----- Toolbar action definitions -----
class BoldAction(ToolbarAction):
    """Action for applying bold formatting."""

    def __init__(self):
        super().__init__(self.bold, ":/icons/bold.svg")

    def bold(self):
            """Apply bold formatting."""
            pass


class ItalicAction(ToolbarAction):
    """Action for applying italic formatting."""

    def __init__(self):
        super().__init__(self.italic, ":/icons/italic.svg")

    def italic(self):
            """Apply italic formatting."""
            pass


class UnderlineAction(ToolbarAction):
    """Action for applying underline formatting."""

    def __init__(self):
        super().__init__(self.underline, ":/icons/underline.svg")

    def underline(self):
            """Apply underline formatting."""
            pass
