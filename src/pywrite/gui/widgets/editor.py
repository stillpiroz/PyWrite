"""Define and configure the application's text editor (text area)."""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
)


class EditorWidget(QWidget):
    """Provide the main text editing area."""
    
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.text_edit = QTextEdit()

        self.layout.addWidget(self.text_edit)
