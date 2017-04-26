#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     20/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import sys
from PyQt4.QtCore import (QString, Qt)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QBoxLayout, QDialog,
        QDialogButtonBox, QGridLayout, QLabel, QLineEdit, QTextEdit,
        QVBoxLayout, QWidget)

class Dialog(QDialog):
    def __init__(self,parent=None):
        super(Dialog,self).__init__(parent)
        self.userNameLabel=QLabel('&userName:')
        self.userNameEdit=QLineEdit()
        self.userNameLabel.setBuddy(self.userNameEdit)
        self.userNameEdit.setAlignment(Qt.AlignLeft)

        self.userPasswdLabel=QLabel(raw_input())
        self.userPasswdLabel.setAlignment(Qt.AlignRight)

        grid=QGridLayout()
        grid.addWidget(self.userNameLabel,0,0)
        grid.addWidget(self.userNameEdit,0,1)
        grid.addWidget(self.userPasswdLabel,1,0,1,2)
        self.setLayout(grid)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Dialog()
    form.show()
    app.exec_()

