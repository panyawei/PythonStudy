# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paymentdlg.ui'
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

class Ui_PaymentDlg(object):
    def setupUi(self, PaymentDlg):
        PaymentDlg.setObjectName(_fromUtf8("PaymentDlg"))
        PaymentDlg.resize(399, 276)
        self.gridlayout = QtGui.QGridLayout(PaymentDlg)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonBox = QtGui.QDialogButtonBox(PaymentDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(381, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 2, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(PaymentDlg)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.hboxlayout = QtGui.QHBoxLayout(self.tab)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.paidCheckBox = QtGui.QCheckBox(self.tab)
        self.paidCheckBox.setObjectName(_fromUtf8("paidCheckBox"))
        self.hboxlayout.addWidget(self.paidCheckBox)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridlayout1 = QtGui.QGridLayout(self.tab_2)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.sortCodeLineEdit = QtGui.QLineEdit(self.tab_2)
        self.sortCodeLineEdit.setObjectName(_fromUtf8("sortCodeLineEdit"))
        self.gridlayout1.addWidget(self.sortCodeLineEdit, 1, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridlayout1.addWidget(self.label_8, 1, 2, 1, 1)
        self.bankLineEdit = QtGui.QLineEdit(self.tab_2)
        self.bankLineEdit.setObjectName(_fromUtf8("bankLineEdit"))
        self.gridlayout1.addWidget(self.bankLineEdit, 0, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridlayout1.addWidget(self.label_7, 0, 2, 1, 1)
        self.accountNumLineEdit = QtGui.QLineEdit(self.tab_2)
        self.accountNumLineEdit.setObjectName(_fromUtf8("accountNumLineEdit"))
        self.gridlayout1.addWidget(self.accountNumLineEdit, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout1.addWidget(self.label_6, 1, 0, 1, 1)
        self.checkNumLineEdit = QtGui.QLineEdit(self.tab_2)
        self.checkNumLineEdit.setObjectName(_fromUtf8("checkNumLineEdit"))
        self.gridlayout1.addWidget(self.checkNumLineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout1.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridlayout2 = QtGui.QGridLayout(self.tab_3)
        self.gridlayout2.setMargin(9)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.creditCardLineEdit = QtGui.QLineEdit(self.tab_3)
        self.creditCardLineEdit.setObjectName(_fromUtf8("creditCardLineEdit"))
        self.gridlayout2.addWidget(self.creditCardLineEdit, 0, 1, 1, 3)
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridlayout2.addWidget(self.label_11, 0, 0, 1, 1)
        self.expiryDateEdit = QtGui.QDateEdit(self.tab_3)
        self.expiryDateEdit.setAlignment(QtCore.Qt.AlignRight)
        self.expiryDateEdit.setObjectName(_fromUtf8("expiryDateEdit"))
        self.gridlayout2.addWidget(self.expiryDateEdit, 1, 3, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridlayout2.addWidget(self.label_10, 1, 2, 1, 1)
        self.validFromDateEdit = QtGui.QDateEdit(self.tab_3)
        self.validFromDateEdit.setAlignment(QtCore.Qt.AlignRight)
        self.validFromDateEdit.setObjectName(_fromUtf8("validFromDateEdit"))
        self.gridlayout2.addWidget(self.validFromDateEdit, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridlayout2.addWidget(self.label_9, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridlayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridlayout3 = QtGui.QGridLayout()
        self.gridlayout3.setMargin(0)
        self.gridlayout3.setSpacing(6)
        self.gridlayout3.setObjectName(_fromUtf8("gridlayout3"))
        self.label_3 = QtGui.QLabel(PaymentDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout3.addWidget(self.label_3, 0, 2, 1, 1)
        self.amountSpinBox = QtGui.QDoubleSpinBox(PaymentDlg)
        self.amountSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.amountSpinBox.setMaximum(999999.0)
        self.amountSpinBox.setObjectName(_fromUtf8("amountSpinBox"))
        self.gridlayout3.addWidget(self.amountSpinBox, 1, 3, 1, 1)
        self.label = QtGui.QLabel(PaymentDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout3.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(PaymentDlg)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout3.addWidget(self.label_5, 1, 0, 1, 1)
        self.surnameLineEdit = QtGui.QLineEdit(PaymentDlg)
        self.surnameLineEdit.setObjectName(_fromUtf8("surnameLineEdit"))
        self.gridlayout3.addWidget(self.surnameLineEdit, 0, 3, 1, 1)
        self.forenameLineEdit = QtGui.QLineEdit(PaymentDlg)
        self.forenameLineEdit.setObjectName(_fromUtf8("forenameLineEdit"))
        self.gridlayout3.addWidget(self.forenameLineEdit, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(PaymentDlg)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridlayout3.addWidget(self.label_4, 1, 2, 1, 1)
        self.invoiceNumSpinBox = QtGui.QSpinBox(PaymentDlg)
        self.invoiceNumSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.invoiceNumSpinBox.setMaximum(999999999)
        self.invoiceNumSpinBox.setMinimum(1000000)
        self.invoiceNumSpinBox.setProperty("value", 1000000)
        self.invoiceNumSpinBox.setObjectName(_fromUtf8("invoiceNumSpinBox"))
        self.gridlayout3.addWidget(self.invoiceNumSpinBox, 1, 1, 1, 1)
        self.gridlayout.addLayout(self.gridlayout3, 0, 0, 1, 1)
        self.label_8.setBuddy(self.sortCodeLineEdit)
        self.label_7.setBuddy(self.bankLineEdit)
        self.label_6.setBuddy(self.accountNumLineEdit)
        self.label_2.setBuddy(self.checkNumLineEdit)
        self.label_11.setBuddy(self.creditCardLineEdit)
        self.label_10.setBuddy(self.expiryDateEdit)
        self.label_9.setBuddy(self.validFromDateEdit)
        self.label_3.setBuddy(self.surnameLineEdit)
        self.label.setBuddy(self.forenameLineEdit)
        self.label_5.setBuddy(self.invoiceNumSpinBox)
        self.label_4.setBuddy(self.amountSpinBox)

        self.retranslateUi(PaymentDlg)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PaymentDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PaymentDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(PaymentDlg)
        PaymentDlg.setTabOrder(self.forenameLineEdit, self.surnameLineEdit)
        PaymentDlg.setTabOrder(self.surnameLineEdit, self.invoiceNumSpinBox)
        PaymentDlg.setTabOrder(self.invoiceNumSpinBox, self.amountSpinBox)
        PaymentDlg.setTabOrder(self.amountSpinBox, self.tabWidget)
        PaymentDlg.setTabOrder(self.tabWidget, self.paidCheckBox)
        PaymentDlg.setTabOrder(self.paidCheckBox, self.checkNumLineEdit)
        PaymentDlg.setTabOrder(self.checkNumLineEdit, self.accountNumLineEdit)
        PaymentDlg.setTabOrder(self.accountNumLineEdit, self.bankLineEdit)
        PaymentDlg.setTabOrder(self.bankLineEdit, self.sortCodeLineEdit)
        PaymentDlg.setTabOrder(self.sortCodeLineEdit, self.creditCardLineEdit)
        PaymentDlg.setTabOrder(self.creditCardLineEdit, self.validFromDateEdit)
        PaymentDlg.setTabOrder(self.validFromDateEdit, self.expiryDateEdit)

    def retranslateUi(self, PaymentDlg):
        PaymentDlg.setWindowTitle(_translate("PaymentDlg", "Payment Form", None))
        self.paidCheckBox.setText(_translate("PaymentDlg", "&Paid", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PaymentDlg", "Cas&h", None))
        self.label_8.setText(_translate("PaymentDlg", "S&ort Code:", None))
        self.label_7.setText(_translate("PaymentDlg", "&Bank:", None))
        self.label_6.setText(_translate("PaymentDlg", "A&ccount No.:", None))
        self.label_2.setText(_translate("PaymentDlg", "Check &No.:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PaymentDlg", "Chec&k", None))
        self.label_11.setText(_translate("PaymentDlg", "&Number:", None))
        self.expiryDateEdit.setDisplayFormat(_translate("PaymentDlg", "MMM yyyy", None))
        self.label_10.setText(_translate("PaymentDlg", "E&xpiry Date", None))
        self.validFromDateEdit.setDisplayFormat(_translate("PaymentDlg", "MMM yyyy", None))
        self.label_9.setText(_translate("PaymentDlg", "&Valid From:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("PaymentDlg", "Credit Car&d", None))
        self.label_3.setText(_translate("PaymentDlg", "&Surname:", None))
        self.amountSpinBox.setPrefix(_translate("PaymentDlg", "$ ", None))
        self.label.setText(_translate("PaymentDlg", "&Forename:", None))
        self.label_5.setText(_translate("PaymentDlg", "&Invoice No.:", None))
        self.label_4.setText(_translate("PaymentDlg", "&Amount:", None))

