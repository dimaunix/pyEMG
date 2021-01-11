from PyQt5.QtWidgets import QWidget
import pyperclip
from UI.widgetMessage import Ui_widgetMessage


class WidgetMessage(QWidget):
    def __init__(self,  *args, **kwargs):
        super(WidgetMessage, self).__init__(*args, **kwargs)
        self.ui = Ui_widgetMessage()
        self.ui.setupUi(self)
        self.ui.btnCopy.clicked.connect(self.copyToClipboard)

    def copyToClipboard(self):
        pyperclip.copy(self.ui.editMessage.toPlainText())
