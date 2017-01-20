#-------------------------------------------------------------------------------
# Name:        QT_traverse
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

import os
import sys
from PyQt4.QtCore import (QString, Qt,QVariant)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QBoxLayout, QDialog,
        QDialogButtonBox, QGridLayout, QLabel, QLineEdit, QTextEdit,
        QVBoxLayout, QWidget,QPushButton,QFileDialog)

class Dialog(QDialog):
    exe_file=u'D:\ZSDicoms\ConverterEXE\dcm2niiConverter.exe '

    StyleSheet = """
QComboBox { color: darkblue; }
QLineEdit { color: darkgreen; }
QLineEdit[mandatory="true"] {
    background-color: rgb(255, 255, 127);
    color: darkblue;
}
"""
    def __init__(self,parent=None):
        super(Dialog,self).__init__(parent)
        self.SourcePathLabel=QLabel('&SourcePath:')
        self.SourcePathLineEdit=QLineEdit()
        self.SourcePathLabel.setBuddy(self.SourcePathLineEdit)
        self.SourceSelectButton=QPushButton('&SourceSelect')
        self.SavePathLabel=QLabel('&SavePath')
        self.SavePathLineEdit=QLineEdit()
        self.SavePathLabel.setBuddy(self.SavePathLineEdit)
        self.SaveSelectButton=QPushButton('&SaveSelect')
        self.SaveNameLabel=QLabel('&SaveName')
        self.SaveNameLineEdit=QLineEdit()
        self.SaveNameLabel.setBuddy(self.SaveNameLineEdit)
        self.buttonBox=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        convertButton=self.buttonBox.button(QDialogButtonBox.Ok)
        convertButton.setText('&Convert')
        convertButton.setEnabled(False)

        self.setStyleSheet(Dialog.StyleSheet)
        self.setWindowTitle('DCM==>NII')

        grid=QGridLayout()
        grid.addWidget(self.SourcePathLabel,0,0)
        grid.addWidget(self.SourcePathLineEdit,0,1)
        grid.addWidget(self.SourceSelectButton,0,2)
        grid.addWidget(self.SavePathLabel,1,0)
        grid.addWidget(self.SavePathLineEdit,1,1)
        grid.addWidget(self.SaveSelectButton,1,2)
        grid.addWidget(self.SaveNameLabel,2,0)
        grid.addWidget(self.SaveNameLineEdit,2,1,1,2)

        layout=QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

        self.lineEdits = (self.SourcePathLineEdit,self.SavePathLineEdit,self.SaveNameLineEdit)
        for lineEdit in self.lineEdits:
            lineEdit.setProperty("mandatory", QVariant(True))
            lineEdit.textEdited.connect(self.updateUi)
        self.SourceSelectButton.clicked.connect(self.sourcefile)
        self.SaveSelectButton.clicked.connect(self.savefile)
        self.buttonBox.accepted.connect(self.convert)
        self.buttonBox.rejected.connect(self.reject)

    def sourcefile(self):
        source_absolute_path=QFileDialog.getExistingDirectory(self,'Open Dir',os.getcwd())
        self.SourcePathLineEdit.setText(QString(source_absolute_path))


    def savefile(self):
        save_absolute_path=QFileDialog.getExistingDirectory(self,'Open Dir',os.getcwd())
        self.SavePathLineEdit.setText(QString(save_absolute_path))

    def updateUi(self):
        enable = True
        for lineEdit in self.lineEdits:
            if (lineEdit.property("mandatory").toBool() and lineEdit.text().isEmpty()):
                enable = False
                break
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)


    def convert(self):
        import subprocess
        for lineEdit in self.lineEdits:
            if not lineEdit.text().isEmpty():
                file=[x for x in os.listdir(self.SourcePathLineEdit.text())]
                for files in file:
                    if(len(files)>1):
                        cmd=self.exe_file+' '+str(self.SourcePathLineEdit.text())+'\\'+files+' '+str(self.SavePathLineEdit.text())+' '+"%s" % str(self.SaveNameLineEdit.text())+files
                    else:
                        cmd=self.exe_file+' '+str(self.SourcePathLineEdit.text())+'\\'+files+' '+str(self.SavePathLineEdit.text())+' '+"%s" % str(self.SaveNameLineEdit.text())+'0'+files
                    print (cmd)
                    process = subprocess.Popen(cmd, shell=True)
                    process.communicate()
            else:break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Dialog()
    form.show()
    app.exec_()



