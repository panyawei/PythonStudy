# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1019, 756)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(330, 60, 421, 191))
        self.tableWidget.setMinimumSize(QtCore.QSize(421, 191))
        self.tableWidget.setMaximumSize(QtCore.QSize(421, 191))
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(1, 5, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(2, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(2, 4, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(2, 5, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(3, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(3, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(3, 4, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(3, 5, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(4, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(4, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(4, 4, item)
        item = QtGui.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(4, 5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(39)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(35)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(32)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 241, 201))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "肺实变/GGO", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "树芽征/腺泡结节", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "支气管扩张", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "肺气肿", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "气管/支气管", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "有", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "右上", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "右中", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "右下", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "左上", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "左下", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "肺实质/气管/支气管异常", None))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "胸腔/胸膜异常", None))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "心脏/大血管异常", None))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "纵隔/肺门/其他部位淋巴结", None))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "纵隔病变", None))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "胸壁病变", None))
        item = self.listWidget.item(6)
        item.setText(_translate("Form", "椎体异常", None))
        item = self.listWidget.item(7)
        item.setText(_translate("Form", "乳腺病变", None))
        item = self.listWidget.item(8)
        item.setText(_translate("Form", "上腹部病变", None))
        item = self.listWidget.item(9)
        item.setText(_translate("Form", "拟诊", None))
        item = self.listWidget.item(10)
        item.setText(_translate("Form", "随诊建议", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

