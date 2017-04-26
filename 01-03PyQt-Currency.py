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
import urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        self.create_connections()
        self.prepare()
        self.setWindowTitle('Currency')

    def create_widgets(self):
        self.dateLabel=QLabel()
        self.fromComboBox=QComboBox()
        self.fromSpinBox=QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01,10000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox=QComboBox()
        self.toLabel=QLabel('1.00')

    def layout_widgets(self):
        grid=QGridLayout()
        grid.addWidget(self.dateLabel,0,0)
        grid.addWidget(self.fromComboBox,1,0)
        grid.addWidget(self.fromSpinBox,1,1)
        grid.addWidget(self.toComboBox,2,0)
        grid.addWidget(self.toLabel,2,1)
        self.setLayout(grid)

    def create_connections(self):
##        self.connect(self.fromComboBox,SIGNAL("currentIndexChange(int)"),self.updateUi)
##        self.connect(self.toComboBox,SIGNAL("currentIndexChange(int)"),self.updateUi)
##        self.connect(self.fromSpinBox,SIGNAL("valueChange(double)"),self.updateUi)
        print "fromComboBox signal"
        self.fromComboBox.currentIndexChanged.connect(self.updateUi)
        print "toComboBox signal"
        self.toComboBox.currentIndexChanged.connect(self.updateUi)
        print "fromSpinBox signal"
        self.fromSpinBox.valueChanged.connect(self.updateUi)


    def prepare(self):
        date=self.getdata()
        self.dateLabel.setText(date)
        rates=sorted(self.rates.keys())
        self.fromComboBox.addItems(rates)
        self.toComboBox.addItems(rates)

    def updateUi(self):
        print "a"
        to=unicode(self.toComboBox.currentText())
        from_=unicode(self.fromComboBox.currentText())

##        print self.rates[from_]
##        print self.rates[to]
        if to==unicode(''):
            to=unicode('Argentine peso')
        amount=(self.rates[from_]/self.rates[to])*self.fromSpinBox.value()
        self.toLabel.setText("%0.2f" % amount)


    def getdata(self): # Idea taken from the Python Cookbook
        print "b"
        self.rates = {}
        try:
            date = "Unknown"
            fh = urllib2.urlopen("http://www.bankofcanada.ca"
                                 "/en/markets/csv/exchange_eng.csv")
            for line in fh:
##                line = line.rstrip()
                if not line or line.startswith(("#", "Closing ")):
                    continue
                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]
                else:
                    try:
                        value = float(fields[-1])
                        self.rates[unicode(fields[0])] = value

                    except ValueError:
                        pass
            return "Exchange Rates Date: " + date
        except Exception, e:
            return "Failed to download:\n%s" % e

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=Form()
    form.show()
    app.exec_()

