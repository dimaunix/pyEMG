# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgetUpdate.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widgetDownload(object):
    def setupUi(self, widgetDownload):
        widgetDownload.setObjectName("widgetDownload")
        widgetDownload.resize(349, 196)
        self.verticalLayout = QtWidgets.QVBoxLayout(widgetDownload)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(widgetDownload)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(widgetDownload)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lblOldVersion = QtWidgets.QLabel(widgetDownload)
        self.lblOldVersion.setObjectName("lblOldVersion")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblOldVersion)
        self.lblNewVersion = QtWidgets.QLabel(widgetDownload)
        self.lblNewVersion.setObjectName("lblNewVersion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lblNewVersion)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.label = QtWidgets.QLabel(widgetDownload)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(400, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(widgetDownload)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.labelStatus = QtWidgets.QLabel(widgetDownload)
        self.labelStatus.setText("")
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.verticalLayout_2.addWidget(self.labelStatus)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCancel = QtWidgets.QPushButton(widgetDownload)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.btnDownload = QtWidgets.QPushButton(widgetDownload)
        self.btnDownload.setObjectName("btnDownload")
        self.horizontalLayout.addWidget(self.btnDownload)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(widgetDownload)
        QtCore.QMetaObject.connectSlotsByName(widgetDownload)

    def retranslateUi(self, widgetDownload):
        _translate = QtCore.QCoreApplication.translate
        widgetDownload.setWindowTitle(_translate("widgetDownload", "Update pyEMG"))
        self.label_4.setText(_translate("widgetDownload", "New version:"))
        self.label_5.setText(_translate("widgetDownload", "Old version:"))
        self.lblOldVersion.setText(_translate("widgetDownload", "0.0.0.0"))
        self.lblNewVersion.setText(_translate("widgetDownload", "0.0.0.0"))
        self.label.setText(_translate("widgetDownload", "Please wait until update process will be finished"))
        self.btnCancel.setText(_translate("widgetDownload", "Cancel"))
        self.btnDownload.setText(_translate("widgetDownload", "Download"))
