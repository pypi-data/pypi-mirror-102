# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personalization-00-start.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 231)
        self.TitleLabel = QtGui.QLabel(Dialog)
        self.TitleLabel.setGeometry(QtCore.QRect(120, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName(_fromUtf8("TitleLabel"))
        self.IntroLabel = QtGui.QLabel(Dialog)
        self.IntroLabel.setGeometry(QtCore.QRect(20, 60, 351, 61))
        self.IntroLabel.setWordWrap(True)
        self.IntroLabel.setObjectName(_fromUtf8("IntroLabel"))
        self.NextButton = QtGui.QPushButton(Dialog)
        self.NextButton.setGeometry(QtCore.QRect(310, 200, 75, 25))
        self.NextButton.setObjectName(_fromUtf8("NextButton"))
        self.arningLabel = QtGui.QLabel(Dialog)
        self.arningLabel.setGeometry(QtCore.QRect(20, 120, 351, 81))
        self.arningLabel.setWordWrap(True)
        self.arningLabel.setObjectName(_fromUtf8("arningLabel"))
        self.CancelButton = QtGui.QPushButton(Dialog)
        self.CancelButton.setGeometry(QtCore.QRect(20, 200, 75, 25))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Gewel Chip setup", None))
        self.TitleLabel.setText(_translate("Dialog", "Gewel Chip setup", None))
        self.IntroLabel.setText(_translate("Dialog", "Your Gewel Chip dongle is not set up - you\'ll be able to create a new wallet, or restore an existing one, and choose your security profile.", None))
        self.NextButton.setText(_translate("Dialog", "Next", None))
        self.arningLabel.setText(_translate("Dialog", "Sensitive information including your dongle PIN will be exchanged during this setup phase - it is recommended to execute it on a secure computer, disconnected from any network, especially if you restore a wallet backup.", None))
        self.CancelButton.setText(_translate("Dialog", "Cancel", None))

