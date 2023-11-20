# custom_line_edit.py
from PyQt5.QtWidgets import QLineEdit

class CustomLineEdit(QLineEdit):
    def __init__(self, placeholder_text, parent=None):
        super().__init__(parent)
        self.placeholder_text = placeholder_text
        self.setPlaceholderText(placeholder_text)

    def focusInEvent(self, event):
        self.setPlaceholderText('')
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        if self.text() == '':
            self.setPlaceholderText(self.placeholder_text)
        super().focusOutEvent(event)
