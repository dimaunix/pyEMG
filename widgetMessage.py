from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
import pyperclip
from UI.widgetMessage import Ui_widgetMessage


class WidgetMessage(QWidget):
    def __init__(self,  parent=None):
        super(WidgetMessage, self).__init__(parent)
        self.dialog = QWidget()
        self.dialog.ui = Ui_widgetMessage()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.ui.btnCopy.clicked.connect(self.copyToClipboard)

    def copyToClipboard(self):
        pyperclip.copy(self.dialog.ui.editMessage.toPlainText())
