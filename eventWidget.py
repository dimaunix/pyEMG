from PyQt5.QtWidgets import QWidget
from UI.myEventWidget import Ui_MyEventWidget


class MyEventWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyEventWidget, self).__init__(*args, **kwargs)
        self.ui = Ui_MyEventWidget()
        self.ui.setupUi(self)
