from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QDialog
import helper
from UI.auth import Ui_widgetAuth


class WidgetAuth(QDialog):
    def __init__(self, params):
        super(WidgetAuth, self).__init__(params.get("parent"))
        self.widget = QDialog()
        self.widget.setWindowIcon(helper.get_icon())
        self.widget.ui = Ui_widgetAuth()
        self.widget.ui.setupUi(self.widget)
        self.widget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.db = params.get("db")
        self.widget.ui.btnLogin.clicked.connect(self.authenticate)

    def authenticate(self):
        if self.db.sign_in(self.widget.ui.inputEmail.text(), self.widget.ui.inputPassword.text()):
            self.widget.close()

