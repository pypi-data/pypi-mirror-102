# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personalization-seedbackup-01.ui'
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
        Dialog.resize(400, 300)
        self.TitleLabel = QtGui.QLabel(Dialog)
        self.TitleLabel.setGeometry(QtCore.QRect(30, 20, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName(_fromUtf8("TitleLabel"))
        self.NextButton = QtGui.QPushButton(Dialog)
        self.NextButton.setGeometry(QtCore.QRect(320, 270, 75, 25))
        self.NextButton.setObjectName(_fromUtf8("NextButton"))
        self.IntroLabel = QtGui.QLabel(Dialog)
        self.IntroLabel.setGeometry(QtCore.QRect(10, 100, 351, 31))
        self.IntroLabel.setWordWrap(True)
        self.IntroLabel.setObjectName(_fromUtf8("IntroLabel"))
        self.IntroLabel_2 = QtGui.QLabel(Dialog)
        self.IntroLabel_2.setGeometry(QtCore.QRect(10, 140, 351, 31))
        self.IntroLabel_2.setWordWrap(True)
        self.IntroLabel_2.setObjectName(_fromUtf8("IntroLabel_2"))
        self.IntroLabel_3 = QtGui.QLabel(Dialog)
        self.IntroLabel_3.setGeometry(QtCore.QRect(10, 180, 351, 41))
        self.IntroLabel_3.setWordWrap(True)
        self.IntroLabel_3.setObjectName(_fromUtf8("IntroLabel_3"))
        self.TitleLabel_2 = QtGui.QLabel(Dialog)
        self.TitleLabel_2.setGeometry(QtCore.QRect(90, 60, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleLabel_2.setFont(font)
        self.TitleLabel_2.setObjectName(_fromUtf8("TitleLabel_2"))
        self.IntroLabel_4 = QtGui.QLabel(Dialog)
        self.IntroLabel_4.setGeometry(QtCore.QRect(10, 220, 351, 41))
        self.IntroLabel_4.setWordWrap(True)
        self.IntroLabel_4.setObjectName(_fromUtf8("IntroLabel_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Gewel Chip setup", None))
        self.TitleLabel.setText(_translate("Dialog", "Gewel Chip setup - seed backup", None))
        self.NextButton.setText(_translate("Dialog", "Next", None))
        self.IntroLabel.setText(_translate("Dialog", "A new seed has been generated for your wallet.", None))
        self.IntroLabel_2.setText(_translate("Dialog", "You must backup this seed and keep it out of reach of hackers (typically by keeping it on paper).", None))
        self.IntroLabel_3.setText(_translate("Dialog", "You can use this seed to restore your dongle if you lose it or access your funds with any other compatible wallet.", None))
        self.TitleLabel_2.setText(_translate("Dialog", "READ CAREFULLY", None))
        self.IntroLabel_4.setText(_translate("Dialog", "Press Next to start the backuping process.", None))

