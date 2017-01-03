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
import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
app = QApplication(sys.argv)
try:
    due = QTime.currentTime()
    message = 'Alert'
    if len(sys.argv)<2:
        raise ValueError
    hours,mins = sys.argv[1].split(":")
    due = QTime(int(hours),int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv)>2:
        message = ''.join(sys.argv[2:])
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]"

while QTime.currentTime()<due:
    time.sleep(2)
label = QLabel("<font color=red size=72><b>{0}</b></font>"
               .format(message))
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(60000, app.quit) # 1 minute
app.exec_()

