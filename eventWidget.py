from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
import os


class MyEventWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyEventWidget, self).__init__(*args, **kwargs)
        self.ui = uic.loadUi(os.path.join(os.path.dirname(__file__), "UI/myEventWidget.ui"), self)
