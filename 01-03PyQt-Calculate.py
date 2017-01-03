#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     03/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import division
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.browser=QTextBrowser()
        self.lineedit=QLineEdit('Type an excpression and press Enter')
        self.lineedit.selectAll()
        layout=QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)
##        self.connect(self.lineedit,SIGNAL("returnPressed()"),self.updateUi)
        self.setWindowTitle('Calculate')

    def updateUi(self):
        try:
            text=unicode(self.lineedit.text())
            self.browser.append("%s = <b>%s</b>" %(text,eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=Form()
    form.show()
    app.exec_()
