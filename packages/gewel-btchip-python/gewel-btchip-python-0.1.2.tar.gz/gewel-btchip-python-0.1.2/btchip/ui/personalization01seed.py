# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personalization-01-seed.ui'
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
        self.TitleLabel.setGeometry(QtCore.QRect(50, 20, 311, 31))
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
        self.NewWalletButton = QtGui.QRadioButton(Dialog)
        self.NewWalletButton.setGeometry(QtCore.QRect(20, 130, 94, 21))
        self.NewWalletButton.setChecked(True)
        self.NewWalletButton.setObjectName(_fromUtf8("NewWalletButton"))
        self.buttonGroup = QtGui.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.NewWalletButton)
        self.RestoreWalletButton = QtGui.QRadioButton(Dialog)
        self.RestoreWalletButton.setGeometry(QtCore.QRect(20, 180, 171, 21))
        self.RestoreWalletButton.setObjectName(_fromUtf8("RestoreWalletButton"))
        self.buttonGroup.addButton(self.RestoreWalletButton)
        self.seed = QtGui.QLineEdit(Dialog)
        self.seed.setEnabled(False)
        self.seed.setGeometry(QtCore.QRect(50, 210, 331, 21))
        self.seed.setEchoMode(QtGui.QLineEdit.Normal)
        self.seed.setObjectName(_fromUtf8("seed"))
        self.CancelButton = QtGui.QPushButton(Dialog)
        self.CancelButton.setGeometry(QtCore.QRect(10, 270, 75, 25))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.NextButton = QtGui.QPushButton(Dialog)
        self.NextButton.setGeometry(QtCore.QRect(320, 270, 75, 25))
        self.NextButton.setObjectName(_fromUtf8("NextButton"))
        self.mnemonicNotAvailableLabel = QtGui.QLabel(Dialog)
        self.mnemonicNotAvailableLabel.setGeometry(QtCore.QRect(130, 240, 171, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.mnemonicNotAvailableLabel.setFont(font)
        self.mnemonicNotAvailableLabel.setWordWrap(True)
        self.mnemonicNotAvailableLabel.setObjectName(_fromUtf8("mnemonicNotAvailableLabel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Gewel Chip setup - seed", None))
        self.TitleLabel.setText(_translate("Dialog", "Gewel Chip setup - seed (1/3)", None))
        self.IntroLabel.setText(_translate("Dialog", "Please select an option: either create a new wallet or restore an existing one", None))
        self.NewWalletButton.setText(_translate("Dialog", "New Wallet", None))
        self.RestoreWalletButton.setText(_translate("Dialog", "Restore wallet backup", None))
        self.seed.setPlaceholderText(_translate("Dialog", "Enter an hexadecimal seed or a BIP 39 mnemonic code", None))
        self.CancelButton.setText(_translate("Dialog", "Cancel", None))
        self.NextButton.setText(_translate("Dialog", "Next", None))
        self.mnemonicNotAvailableLabel.setText(_translate("Dialog", "Mnemonic API is not available", None))

