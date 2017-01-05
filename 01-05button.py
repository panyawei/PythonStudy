#-------------------------------------------------------------------------------
# Name:        button
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     05/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import sys
from PyQt4.QtCore import (QStringList, Qt)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QDialog, QHBoxLayout,
        QInputDialog, QLineEdit, QListWidget, QMessageBox, QPushButton,
        QVBoxLayout)

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class Button(QDialog):
    acceptedList=Signal(QStringList)
    def __init__(self,name,stringList=None,parent=None):
        super(Button,self).__init__(parent)
        self.name=name
        self.create_widgets(stringList)
        self.layout_widgets()
        self.setWindowTitle("{0}".format(self.name))

    def create_widgets(self,stringList):
        self.listWidget=QListWidget()
        if stringList is not None:
            self.listWidget.addItems(stringList)
            self.listWidget.setCurrentRow(0)

    def layout_widgets(self):
        buttonLayout=QVBoxLayout()
        for i,j in (("&ADD",self.add),
                    ("&REMOVE",self.remove),
                    ("&SORT",self.listWidget.sortItems),
                    ("&CLOSE",self.accept)):
            button=QPushButton(i)
            if not MAC:
                button.setFocusPolicy(Qt.NoFocus)
            if i == "CLOSE":
                buttonLayout.addStretch()
            buttonLayout.addWidget(button)
            button.clicked.connect(j)
        layout=QHBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def add(self):
        row=self.listWidget.currentRow()
        title="ADD {0}".format(self.name)
        string, ok = QInputDialog.getText(self, title, title)
        if ok and not string.isEmpty():
            self.listWidget.insertItem(row, string)

    def remove(self):
        row=self.listWidget.currentRow()
        item=self.listWidget.item(row)
        if item is None:
            return
        reply = QMessageBox.question(self, "Remove {0}".format(
                self.name), "Remove {0} `{1}'?".format(
                self.name, unicode(item.text())),
                QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item

    def accept(self):
        self.stringlist = QStringList()
        for row in range(self.listWidget.count()):
            self.stringlist.append(self.listWidget.item(row).text())
        self.acceptedList.emit(self.stringlist)
        QDialog.accept(self)


if __name__ == '__main__':
    select=['D','E','F','G','A','B','C','D','E','F','G']
    app=QApplication(sys.argv)
    button=Button("select",select)
    button.show()
    app.exec_()
