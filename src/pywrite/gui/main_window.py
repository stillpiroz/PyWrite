"""Define and configure the application's main window."""


from PySide6.QtWidgets import QMainWindow

from pywrite.gui.widgets.editor import EditorWidget
from pywrite.gui.widgets.status_bar import MainStatusBar
from pywrite.gui.widgets.toolbar import MainToolBar


class MainWindow(QMainWindow):
    """Create and manage the main application window."""
    
    def __init__(self):
        super().__init__()

        # Configure the main window.
        self.setWindowTitle("PyWrite")
        self.resize(1000, 700)
        
        # Initialize and set the text editor as the central widget.
        self.editor = EditorWidget()
        self.setCentralWidget(self.editor)

        # Initialize and add the toolbar.
        self.toolbar = MainToolBar(self.editor.text_edit)
        self.addToolBar(self.toolbar)

        # Initialize and set the status bar.
        self.status_bar = MainStatusBar()
        self.setStatusBar(self.status_bar)
