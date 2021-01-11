import os

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
import pyperclip


class MessageDialog(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = uic.loadUi(os.path.join(os.path.dirname(__file__), "frameMessage.ui"), self)
        self.btnCopy.clicked.connect(self.copyToClipboard)

    def copyToClipboard(self):
        pyperclip.copy(self.editMessage.toPlainText())
