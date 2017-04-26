#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     08/02/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import (QApplication, QDialog)
from ui_tabelWindow import Ui_Form

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False


class Table(QtGui.QMainWindow):
    def __init__(self):
        super(Table, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
##        Ui_Form.setupUi(self)
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Table()
    main.show()
    sys.exit(app.exec_())

