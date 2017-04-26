# -*- coding:utf-8 -*-
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
        QVBoxLayout,QHBoxLayout, QWidget,QPushButton,QFileDialog)
from PyQt4 import QtGui

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

        self.NIInum=[]
        self.RightTitleLabel=QLabel('DCM==>NII')
        self.RightTitleLabel.setAlignment(Qt.AlignCenter)
        self.NIISourcePathLabel=QLabel('&SourcePath:')
        self.NIISourcePathLineEdit=QLineEdit()
        self.NIISourcePathLabel.setBuddy(self.NIISourcePathLineEdit)
        self.NIISourceSelectButton=QPushButton('&SourceSelect')
        self.NIISavePathLabel=QLabel('&SavePath')
        self.NIISavePathLineEdit=QLineEdit()
        self.NIISavePathLabel.setBuddy(self.NIISavePathLineEdit)
        self.NIISaveSelectButton=QPushButton('&SaveSelect')
        self.NIISaveNameLabel=QLabel('&SaveName')
        self.NIISaveNameLineEdit=QLineEdit()
        self.NIISaveNameLabel.setBuddy(self.NIISaveNameLineEdit)
        self.NIInputLineEdit=QLineEdit()

        self.NIInputLineEdit.setFixedSize(65,25)

        self.NIIStopButton=QPushButton('&Stop')
        self.NIIbuttonBox=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        NIIconvertButton=self.NIIbuttonBox.button(QDialogButtonBox.Ok)
        NIIconvertButton.setText('&NiiConvert')
        NIIconvertButton.setEnabled(False)

        self.setStyleSheet(Dialog.StyleSheet)
        self.setWindowTitle('Traverse')

        grid=QGridLayout()
        grid.addWidget(self.RightTitleLabel,0,0,1,3)
        grid.addWidget(self.NIISourcePathLabel,1,0)
        grid.addWidget(self.NIISourcePathLineEdit,1,1)
        grid.addWidget(self.NIISourceSelectButton,1,2)
        grid.addWidget(self.NIISavePathLabel,2,0)
        grid.addWidget(self.NIISavePathLineEdit,2,1)
        grid.addWidget(self.NIISaveSelectButton,2,2)
        grid.addWidget(self.NIISaveNameLabel,3,0)
        grid.addWidget(self.NIISaveNameLineEdit,3,1,1,2)
        grid .addWidget(self.NIInputLineEdit,4,0)
        grid.addWidget(self.NIIStopButton,4,1)
        grid.addWidget(self.NIIbuttonBox,4,2)

        Hlayout=QHBoxLayout()
        Hlayout.addLayout(grid)
        self.setLayout(Hlayout)

        self.NIISourceSelectButton.clicked.connect(self.Niisourcefile)
        self.NIISaveSelectButton.clicked.connect(self.Niisavefile)
        self.NIIStopButton.clicked.connect(self.NiiStop)
        self.NIIlineEdits = (self.NIISourcePathLineEdit,self.NIISavePathLineEdit)
        for lineEdit in self.NIIlineEdits:
            lineEdit.setProperty("mandatory", QVariant(True))
            lineEdit.textChanged.connect(self.NiiupdateUi)

        self.NIISaveNameLineEdit.textEdited.connect(self.NiiupdateUi)
        self.NIIbuttonBox.accepted.connect(self.Niiconvert)
        self.NIIbuttonBox.rejected.connect(self.reject)

    def NiiStop(self):
        if self.ii==self.files[self.num]:
            self.NIInputLineEdit.setText(u'已暂停')
            self.NIInputLineEdit.setStyleSheet("color:red")
            self.process.kill()


    def Niisourcefile(self):
        self.NIInum=[]
        source_absolute_path=QFileDialog.getExistingDirectory(self,'Open Dir',os.getcwd())
        self.NIISourcePathLineEdit.setText(QString(source_absolute_path))


    def Niisavefile(self):
        save_absolute_path=QFileDialog.getExistingDirectory(self,'Open Dir',os.getcwd())
        self.NIISavePathLineEdit.setText(QString(save_absolute_path))


    def NiiupdateUi(self):
        enable=True

        if not self.NIISourcePathLineEdit.text().isEmpty() and not self.NIISavePathLineEdit.text().isEmpty() and not self.NIISaveNameLineEdit.text().isEmpty():
            self.NIIbuttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)
        else:
            enable=False
            self.NIIbuttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)

    def Niiconvert(self):
        import subprocess
        self.files=[x for x in os.listdir(self.NIISourcePathLineEdit.text())]
        print (self.files)
        self.num=0
        for i in range(0,len(self.files)):
            self.num=i
            self.ii=self.files[i]

            if(len(self.ii)>1):
                self.cmd=self.exe_file+' '+str(self.NIISourcePathLineEdit.text())+'\\'+self.ii+' '+str(self.NIISavePathLineEdit.text())+' '+"%s" % str(self.NIISaveNameLineEdit.text())+self.ii
            else:
                self.cmd=self.exe_file+' '+str(self.NIISourcePathLineEdit.text())+'\\'+self.ii+' '+str(self.NIISavePathLineEdit.text())+' '+"%s" % str(self.NIISaveNameLineEdit.text())+'0'+self.ii
            print (self.cmd)
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
            if self.ii==self.files[-1]:
                self.NIInputLineEdit.setText(u'转换完毕')
                self.NIInputLineEdit.setStyleSheet("color:red")
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Dialog()
    form.show()
    app.exec_()



