"""Define and configure the application's toolbar."""


from PySide6.QtGui import (
    QAction,
    QFont,
    QIcon,
    QTextCharFormat,
)
from PySide6.QtWidgets import QToolBar

from pywrite.resources import resources_rc
from pywrite.gui.widgets.editor import CursorFormatter


class MainToolBar(QToolBar):
    """Create main toolbar."""

    def __init__(self, text_edit):
        super().__init__()

        self.bold_action = BoldAction(text_edit, self)
        self.italic_action = ItalicAction(text_edit, self)
        self.underline_action = UnderlineAction(text_edit, self)

        self.addActions([
            self.bold_action,
            self.italic_action,
            self.underline_action,
        ])


class ToolbarAction(QAction):
    """Base class for toolbar actions."""

    def __init__(self, text_edit, icon, parent=None):
        super().__init__(parent)

        self.text_edit = text_edit
        self.setIcon(QIcon(icon))


# ----- Toolbar action definitions -----
class BoldAction(ToolbarAction):
    def __init__(self, text_edit, parent=None):
        super().__init__(text_edit, ":/icons/bold.svg", parent)

        self.formatter = CursorFormatter(
            text_edit,
            format_method=QTextCharFormat.fontWeight,
            format_setter=QTextCharFormat.setFontWeight,
            target_format=QFont.Bold,
            default_format=QFont.Normal,
        )

        self.triggered.connect(self.formatter.toggle)


class ItalicAction(ToolbarAction):
    """Action for applying italic formatting."""

    def __init__(self, text_edit, parent=None):
        super().__init__(text_edit, ":/icons/italic.svg", parent)

        self.formatter = CursorFormatter(
            text_edit,
            format_method=QTextCharFormat.fontItalic,
            format_setter=QTextCharFormat.setFontItalic,
            target_format=True,
            default_format=False,
        )

        self.triggered.connect(self.formatter.toggle)


class UnderlineAction(ToolbarAction):
    """Action for applying underline formatting."""

    def __init__(self, text_edit, parent=None):
        super().__init__(text_edit, ":/icons/underline.svg", parent)

        self.formatter = CursorFormatter(
            text_edit,
            format_method=QTextCharFormat.fontUnderline,
            format_setter=QTextCharFormat.setFontUnderline,
            target_format=True,
            default_format=False,
        )

        self.triggered.connect(self.formatter.toggle)
