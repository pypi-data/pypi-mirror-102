# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personalization-03-config.ui'
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
        Dialog.resize(400, 243)
        self.TitleLabel = QtGui.QLabel(Dialog)
        self.TitleLabel.setGeometry(QtCore.QRect(30, 10, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName(_fromUtf8("TitleLabel"))
        self.IntroLabel = QtGui.QLabel(Dialog)
        self.IntroLabel.setGeometry(QtCore.QRect(20, 50, 351, 61))
        self.IntroLabel.setWordWrap(True)
        self.IntroLabel.setObjectName(_fromUtf8("IntroLabel"))
        self.qwertyButton = QtGui.QRadioButton(Dialog)
        self.qwertyButton.setGeometry(QtCore.QRect(50, 110, 94, 21))
        self.qwertyButton.setChecked(True)
        self.qwertyButton.setObjectName(_fromUtf8("qwertyButton"))
        self.keyboardGroup = QtGui.QButtonGroup(Dialog)
        self.keyboardGroup.setObjectName(_fromUtf8("keyboardGroup"))
        self.keyboardGroup.addButton(self.qwertyButton)
        self.qwertzButton = QtGui.QRadioButton(Dialog)
        self.qwertzButton.setGeometry(QtCore.QRect(50, 140, 94, 21))
        self.qwertzButton.setObjectName(_fromUtf8("qwertzButton"))
        self.keyboardGroup.addButton(self.qwertzButton)
        self.azertyButton = QtGui.QRadioButton(Dialog)
        self.azertyButton.setGeometry(QtCore.QRect(50, 170, 94, 21))
        self.azertyButton.setObjectName(_fromUtf8("azertyButton"))
        self.keyboardGroup.addButton(self.azertyButton)
        self.CancelButton = QtGui.QPushButton(Dialog)
        self.CancelButton.setGeometry(QtCore.QRect(10, 210, 75, 25))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.NextButton = QtGui.QPushButton(Dialog)
        self.NextButton.setGeometry(QtCore.QRect(320, 210, 75, 25))
        self.NextButton.setObjectName(_fromUtf8("NextButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Gewel Chip setup", None))
        self.TitleLabel.setText(_translate("Dialog", "Gewel Chip setup - config (3/3)", None))
        self.IntroLabel.setText(_translate("Dialog", "Please select your keyboard type to type the second factor confirmation", None))
        self.qwertyButton.setText(_translate("Dialog", "QWERTY", None))
        self.qwertzButton.setText(_translate("Dialog", "QWERTZ", None))
        self.azertyButton.setText(_translate("Dialog", "AZERTY", None))
        self.CancelButton.setText(_translate("Dialog", "Cancel", None))
        self.NextButton.setText(_translate("Dialog", "Next", None))

