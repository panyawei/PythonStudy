#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     06/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import re
import sys
from PyQt4.QtCore import (Qt, QString)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtCore import pyqtSlot as Slot
from PyQt4.QtGui import (QApplication, QDialog)
import ui_login

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class login(QDialog,ui_login.Ui_register):

    found = Signal(int)
    notfound = Signal()

    def __init__(self, text, parent=None):
        super(login, self).__init__(parent)
        self.__text = unicode(text)
        self.__index = 0
        self.setupUi(self)
        if not MAC:
            self.loginButton.setFocusPolicy(Qt.NoFocus)
        self.updateUi()

    def updateUi(self):
        enable = not self.userlineEdit.text().isEmpty()
        self.loginButton.setEnabled(enable)

    def text(self):
        return self.__text




app=QApplication(sys.argv)
l=login('a')
l.show()
app.exec_()

