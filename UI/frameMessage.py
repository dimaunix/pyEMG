# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgetMessage.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widgetMessage(object):
    def setupUi(self, widgetMessage):
        widgetMessage.setObjectName("widgetMessage")
        widgetMessage.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(widgetMessage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editMessage = QtWidgets.QTextEdit(widgetMessage)
        self.editMessage.setObjectName("editMessage")
        self.verticalLayout.addWidget(self.editMessage)
        self.btnCopy = QtWidgets.QPushButton(widgetMessage)
        self.btnCopy.setObjectName("btnCopy")
        self.verticalLayout.addWidget(self.btnCopy)

        self.retranslateUi(widgetMessage)
        QtCore.QMetaObject.connectSlotsByName(widgetMessage)

    def retranslateUi(self, widgetMessage):
        _translate = QtCore.QCoreApplication.translate
        widgetMessage.setWindowTitle(_translate("widgetMessage", "Generated Message for Jeeves"))
        self.btnCopy.setText(_translate("widgetMessage", "Copy"))