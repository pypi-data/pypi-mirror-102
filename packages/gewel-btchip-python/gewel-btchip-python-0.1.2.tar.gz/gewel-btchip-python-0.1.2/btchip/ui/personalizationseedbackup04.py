# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personalization-seedbackup-04.ui'
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
        Dialog.resize(554, 190)
        self.TitleLabel = QtGui.QLabel(Dialog)
        self.TitleLabel.setGeometry(QtCore.QRect(30, 10, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName(_fromUtf8("TitleLabel"))
        self.IntroLabel = QtGui.QLabel(Dialog)
        self.IntroLabel.setGeometry(QtCore.QRect(10, 50, 351, 51))
        self.IntroLabel.setWordWrap(True)
        self.IntroLabel.setObjectName(_fromUtf8("IntroLabel"))
        self.seedOkButton = QtGui.QPushButton(Dialog)
        self.seedOkButton.setGeometry(QtCore.QRect(20, 140, 501, 25))
        self.seedOkButton.setObjectName(_fromUtf8("seedOkButton"))
        self.seedKoButton = QtGui.QPushButton(Dialog)
        self.seedKoButton.setGeometry(QtCore.QRect(20, 110, 501, 25))
        self.seedKoButton.setObjectName(_fromUtf8("seedKoButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Gewel Chip setup", None))
        self.TitleLabel.setText(_translate("Dialog", "Gewel Chip setup - seed backup", None))
        self.IntroLabel.setText(_translate("Dialog", "Did you see the seed correctly displayed and did you backup it properly?", None))
        self.seedOkButton.setText(_translate("Dialog", "Yes, the seed is backed up properly and kept in a safe place, move on", None))
        self.seedKoButton.setText(_translate("Dialog", "No, I didn\'t see the seed. Wipe the dongle and start over", None))

