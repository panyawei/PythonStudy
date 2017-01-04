#-------------------------------------------------------------------------------
# Name:        addinTimer
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     04/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import division
import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.browser=QTextBrowser()
        self.lineedit=QLineEdit('Enter time')
        self.lineedit.selectAll()

        layout=QHBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)

        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle('AddinTimer')

    def updateUi(self):
        try:
            text=unicode(self.lineedit.text())
            self.browser.append('%s' %text)
            lis=text.split(':')
            print type(lis)
##            print '1'
            due=QTime(int(lis[0]),int(lis[1]))

            print due
            print QTime.currentTime()

            if not due.isValid():
                raise ValueError
            print len(lis)
            if len(lis)==3:
                message=''.join(lis[2:])
            while QTime.currentTime()<due:
                time.sleep(5)

            self.browser.append('<font color=green>%s </font>' %message)

            QTimer.singleShot(3000, app.quit) # 1 minute

        except ValueError:
            self.browser.append('<font color=red>%s is invalid</font>' %text)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=Form()
    form.show()
    app.exec_()

