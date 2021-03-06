# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myEventWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyEventWidget(object):
    def setupUi(self, MyEventWidget):
        MyEventWidget.setObjectName("MyEventWidget")
        MyEventWidget.setEnabled(True)
        MyEventWidget.resize(248, 118)
        MyEventWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MyEventWidget.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(MyEventWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formEvent = QtWidgets.QFormLayout()
        self.formEvent.setObjectName("formEvent")
        self.label_7 = QtWidgets.QLabel(MyEventWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formEvent.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(MyEventWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formEvent.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.inputEventName = QtWidgets.QLineEdit(MyEventWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.inputEventName.setFont(font)
        self.inputEventName.setObjectName("inputEventName")
        self.formEvent.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputEventName)
        self.label_9 = QtWidgets.QLabel(MyEventWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formEvent.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.inputEventURL = QtWidgets.QLineEdit(MyEventWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.inputEventURL.setFont(font)
        self.inputEventURL.setObjectName("inputEventURL")
        self.formEvent.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inputEventURL)
        self.label_10 = QtWidgets.QLabel(MyEventWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formEvent.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.inputHost = QtWidgets.QLineEdit(MyEventWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.inputHost.setFont(font)
        self.inputHost.setObjectName("inputHost")
        self.formEvent.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inputHost)
        self.dateTimeEvent = QtWidgets.QDateTimeEdit(MyEventWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.dateTimeEvent.setFont(font)
        self.dateTimeEvent.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 10), QtCore.QTime(16, 0, 0)))
        self.dateTimeEvent.setDate(QtCore.QDate(2021, 1, 10))
        self.dateTimeEvent.setTime(QtCore.QTime(16, 0, 0))
        self.dateTimeEvent.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.dateTimeEvent.setCalendarPopup(True)
        self.dateTimeEvent.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEvent.setObjectName("dateTimeEvent")
        self.formEvent.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateTimeEvent)
        self.verticalLayout.addLayout(self.formEvent)

        self.retranslateUi(MyEventWidget)
        QtCore.QMetaObject.connectSlotsByName(MyEventWidget)

    def retranslateUi(self, MyEventWidget):
        _translate = QtCore.QCoreApplication.translate
        self.label_7.setText(_translate("MyEventWidget", "Datetime:"))
        self.label_8.setText(_translate("MyEventWidget", "Name:"))
        self.label_9.setText(_translate("MyEventWidget", "Reddit URL:"))
        self.label_10.setText(_translate("MyEventWidget", "Host:"))
