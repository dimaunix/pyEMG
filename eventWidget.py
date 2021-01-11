from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, QTime, QDate, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout, QLabel, QLineEdit, QDateTimeEdit


class MyEventWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(MyEventWidget, self).__init__(*args, **kwargs)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formEvent = QFormLayout(self)
        self.formEvent.setObjectName(u"formEvent")
        self.label_7 = QLabel(self)
        self.label_7.setText("Datetime:")
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(10)
        self.label_7.setFont(font)

        self.formEvent.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self)
        self.label_8.setText(u"Name:")
        self.label_8.setFont(font)

        self.formEvent.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.inputEventName = QLineEdit(self)
        self.inputEventName.setObjectName(u"inputEventName")
        font1 = QFont()
        font1.setFamily(u"Verdana")
        font1.setPointSize(8)
        self.inputEventName.setFont(font1)

        self.formEvent.setWidget(1, QFormLayout.FieldRole, self.inputEventName)

        self.label_9 = QLabel(self)
        self.label_9.setText(u"Reddit URL:")
        self.label_9.setFont(font)

        self.formEvent.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.inputEventURL = QLineEdit(self)
        self.inputEventURL.setObjectName(u"inputEventURL")
        self.inputEventURL.setFont(font1)

        self.formEvent.setWidget(2, QFormLayout.FieldRole, self.inputEventURL)

        self.label_10 = QLabel(self)
        self.label_10.setText(u"Host:")
        self.label_10.setFont(font)

        self.formEvent.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.inputHost = QLineEdit(self)
        self.inputHost.setObjectName(u"inputHost")
        self.inputHost.setFont(font1)

        self.formEvent.setWidget(3, QFormLayout.FieldRole, self.inputHost)

        self.dateTimeEvent = QDateTimeEdit(self)
        self.dateTimeEvent.setObjectName(u"dateTimeEvent")
        self.dateTimeEvent.setFont(font1)
        self.dateTimeEvent.setDateTime(QDateTime(QDate(2021, 1, 10), QTime(16, 0, 0)))
        self.dateTimeEvent.setDate(QDate(2021, 1, 10))
        self.dateTimeEvent.setTime(QTime(16, 0, 0))
        self.dateTimeEvent.setDisplayFormat(u"dd.MM.yyyy HH:mm")
        self.dateTimeEvent.setCalendarPopup(True)
        self.dateTimeEvent.setTimeSpec(Qt.UTC)

        self.formEvent.setWidget(0, QFormLayout.FieldRole, self.dateTimeEvent)

        self.verticalLayout.addLayout(self.formEvent)
        self.setLayout(self.verticalLayout)
