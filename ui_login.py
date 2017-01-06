# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_register(object):
    def setupUi(self, register):
        register.setObjectName(_fromUtf8("register"))
        register.resize(370, 238)
        self.cancelButton = QtGui.QPushButton(register)
        self.cancelButton.setGeometry(QtCore.QRect(210, 140, 75, 28))
        self.cancelButton.setMaximumSize(QtCore.QSize(15777215, 16777215))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.widget = QtGui.QWidget(register)
        self.widget.setGeometry(QtCore.QRect(64, 31, 243, 80))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.username = QtGui.QLabel(self.widget)
        self.username.setObjectName(_fromUtf8("username"))
        self.horizontalLayout.addWidget(self.username)
        self.userlineEdit = QtGui.QLineEdit(self.widget)
        self.userlineEdit.setObjectName(_fromUtf8("userlineEdit"))
        self.horizontalLayout.addWidget(self.userlineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(13, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.password = QtGui.QLabel(self.widget)
        self.password.setObjectName(_fromUtf8("password"))
        self.horizontalLayout.addWidget(self.password)
        self.passwordlineEdit = QtGui.QLineEdit(self.widget)
        self.passwordlineEdit.setText(_fromUtf8(""))
        self.passwordlineEdit.setObjectName(_fromUtf8("passwordlineEdit"))
        self.horizontalLayout.addWidget(self.passwordlineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.loginButton = QtGui.QPushButton(register)
        self.loginButton.setGeometry(QtCore.QRect(71, 140, 75, 28))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.username.raise_()
        self.password.raise_()
        self.userlineEdit.raise_()
        self.passwordlineEdit.raise_()
        self.loginButton.raise_()
        self.cancelButton.raise_()
        self.loginButton.raise_()
        self.passwordlineEdit.raise_()
        self.password.raise_()
        self.username.setBuddy(self.userlineEdit)
        self.password.setBuddy(self.passwordlineEdit)

        self.retranslateUi(register)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), register.reject)
        QtCore.QMetaObject.connectSlotsByName(register)

    def retranslateUi(self, register):
        register.setWindowTitle(_translate("register", "register", None))
        self.cancelButton.setText(_translate("register", "取消", None))
        self.username.setText(_translate("register", "用户名：", None))
        self.password.setText(_translate("register", "密  码：", None))
        self.loginButton.setText(_translate("register", "登录", None))

