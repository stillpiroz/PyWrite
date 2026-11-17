"""Define and configure the application's text editor (text area)."""


from PySide6.QtGui import QTextCharFormat
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


class CursorFormatter:
    """Manage text cursor formatting."""

    def __init__(
        self,
        editor,
        format_method,
        format_setter,
        target_format,
        default_format,
    ):
        self._editor = editor
        self._get = format_method
        self._set = format_setter
        self._target = target_format
        self._default = default_format

    def _all_match_target(self, cursor):
        """Return True only if every selected char has the target format."""

        start, end = cursor.selectionStart(), cursor.selectionEnd()

        block = self._editor.document().findBlock(start)  # Find the first block containing the selection.

        # Iterate through all blocks that overlap with the selection.
        while block.isValid() and block.position() < end:
            it = block.begin()

            # Check each text fragment within the current block.
            while not it.atEnd():
                fragment = it.fragment()

                if fragment.isValid():
                    f_start = fragment.position()
                    f_end = f_start + fragment.length()

                    # Check whether the fragment overlaps with the selected text.
                    if f_start < end and f_end > start:
                        # A single mismatching fragment means the selection doesn't match the target.
                        if self._get(fragment.charFormat()) != self._target:
                            return False
                it += 1
            block = block.next()

        return True

    def toggle(self):
        """Toggle the target format on the selected text."""

        cursor = self._editor.textCursor()

        # Formatting is only applied to an existing selection.
        if not cursor.hasSelection():
            return

        # Toggle between the target format and the default format.
        if self._all_match_target(cursor):
            value = self._default
        else:
            value = self._target

        # Create a character format containing only the requested change.
        fmt = QTextCharFormat()
        self._set(fmt, value)

        cursor.mergeCharFormat(fmt)
        self._editor.mergeCurrentCharFormat(fmt)  # Keep the editor's current format in sync.
