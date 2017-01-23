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
        self.PYnum=[]
        self.NIInum=[]
        self.LeftTitleLabel=QLabel('China==>PinYin')
        self.LeftTitleLabel.setAlignment(Qt.AlignCenter)
        self.PYSourcePathLabel=QLabel('&SourcePath')
        self.PYSourcePathLineEdit=QLineEdit()
        self.PYSourcePathLabel.setBuddy(self.PYSourcePathLineEdit)
        self.PYSourceSelectButton=QPushButton('&SourceSelect')
        self.PYSavePathLabel=QLabel('&SavePath')
        self.PYSavePathLineEdit=QLineEdit()
        self.PYSavePathLabel.setBuddy(self.PYSavePathLineEdit)
        self.PYSaveSelectButton=QPushButton('&SaveSelect')
        self.PYConvertButton=QPushButton('&PyConvert')
        self.PYConvertButton.setEnabled(False)


        self.line = QtGui.QFrame()
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
##        self.hboxlayout.addWidget(self.line)

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
        self.NIIbuttonBox=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        NIIconvertButton=self.NIIbuttonBox.button(QDialogButtonBox.Ok)
        NIIconvertButton.setText('&NiiConvert')
        NIIconvertButton.setEnabled(False)

        self.setStyleSheet(Dialog.StyleSheet)
        self.setWindowTitle('Traverse')


        grid1=QGridLayout()
        grid1.addWidget(self.LeftTitleLabel,0,0,1,3)
        grid1.addWidget(self.PYSourcePathLabel,1,0)
        grid1.addWidget(self.PYSourcePathLineEdit,1,1)
        grid1.addWidget(self.PYSourceSelectButton,1,2)
        grid1.addWidget(self.PYSavePathLabel,2,0)
        grid1.addWidget(self.PYSavePathLineEdit,2,1)
        grid1.addWidget(self.PYSaveSelectButton,2,2)
        grid1.addWidget(self.PYConvertButton,3,2)


        grid2=QGridLayout()
        grid2.addWidget(self.RightTitleLabel,0,0,1,3)
        grid2.addWidget(self.NIISourcePathLabel,1,0)
        grid2.addWidget(self.NIISourcePathLineEdit,1,1)
        grid2.addWidget(self.NIISourceSelectButton,1,2)
        grid2.addWidget(self.NIISavePathLabel,2,0)
        grid2.addWidget(self.NIISavePathLineEdit,2,1)
        grid2.addWidget(self.NIISaveSelectButton,2,2)
        grid2.addWidget(self.NIISaveNameLabel,3,0)
        grid2.addWidget(self.NIISaveNameLineEdit,3,1,1,2)
        grid2.addWidget(self.NIIbuttonBox,4,2)

        Hlayout=QHBoxLayout()
        Hlayout.addLayout(grid1)
        Hlayout.addWidget(self.line)
        Hlayout.addLayout(grid2)
        self.setLayout(Hlayout)

        self.NIIlineEdits = (self.NIISourcePathLineEdit,self.NIISavePathLineEdit)
        for lineEdit in self.NIIlineEdits:
            lineEdit.setProperty("mandatory", QVariant(True))
            lineEdit.textChanged.connect(self.NiiupdateUi)
        self.NIISaveNameLineEdit.textEdited.connect(self.NiiupdateUi)
        self.PYlineEdits = (self.PYSavePathLineEdit,self.PYSourcePathLineEdit)
        for lineEdit in self.PYlineEdits:
            lineEdit.setProperty("mandatory", QVariant(True))
            lineEdit.textChanged.connect(self.PyupdateUi)


        self.PYSourceSelectButton.clicked.connect(self.Pysourcefile)
        self.NIISourceSelectButton.clicked.connect(self.Niisourcefile)

        self.PYSaveSelectButton.clicked.connect(self.Pysavefile)
        self.NIISaveSelectButton.clicked.connect(self.Niisavefile)
        self.PYConvertButton.clicked.connect(self.PyConvert)
        self.NIIbuttonBox.accepted.connect(self.Niiconvert)
        self.NIIbuttonBox.rejected.connect(self.reject)


    def Pysourcefile(self):
        source_absolute_path=QFileDialog.getExistingDirectory(self,'Open Dir',os.getcwd())
        self.PYSourcePathLineEdit.setText(QString(source_absolute_path))
        if not self.PYSourcePathLineEdit.text().isEmpty():
            self.PYnum.append('')
            print ('Pysourcefile:',len(self.PYnum))

    def Pysavefile(self):
        save_absolute_path=QFileDialog.getExistingDirectory(self,'Open Dir',os.getcwd())
        self.PYSavePathLineEdit.setText(QString(save_absolute_path))
        if not self.PYSavePathLineEdit.text().isEmpty():
            self.PYnum.append('')
            print ('Pysavefile',len(self.PYnum))

    def Niisourcefile(self):
        source_absolute_path=QFileDialog.getExistingDirectory(self,'Open Dir',os.getcwd())
        self.NIISourcePathLineEdit.setText(QString(source_absolute_path))
        if not self.NIISourcePathLineEdit.text().isEmpty():
            self.NIInum.append('')


    def Niisavefile(self):
        save_absolute_path=QFileDialog.getExistingDirectory(self,'Open Dir',os.getcwd())
        self.NIISavePathLineEdit.setText(QString(save_absolute_path))
        if not self.NIISavePathLineEdit.text().isEmpty():
            self.NIInum.append('')

    def PyupdateUi(self):
        print ('updateUi',len(self.PYnum)+1)
        enable=True
        if len(self.PYnum)+1==2:
            self.PYConvertButton.setEnabled(enable)
        else:
            enable=False
            self.PYConvertButton.setEnabled(enable)

    def NiiupdateUi(self):
        enable=True
        if len(self.NIInum)==2 and not self.NIISaveNameLineEdit.text().isEmpty():
            self.NIIbuttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)
        else:
            enable=False
            self.NIIbuttonBox.button(QDialogButtonBox.Ok).setEnabled(False)


    def PyConvert(self):
        import shutil
        import pypinyin
        import re
        for lineEdit in self.PYlineEdits:
            if not lineEdit.text().isEmpty():
                files=[x for x in os.listdir(unicode(self.PYSourcePathLineEdit.text()))]
                for ii in files:
                    filess = re.split(r'(\W+)',ii)
                    name=filess[1]
                    for num in range(1,1236):
                        if str(filess).startswith('[u\'%s\'' % num) :
                            if filess[0]==str(num):
                                while(len(name))==3:
                                    for i in range(len(name)):
                                        if i==0:
                                            name1= list(name)[i]
                                            a1= pypinyin.slug(name1)
                                            namelist=list(a1)
                                            b1=namelist[0]+namelist[1]
                                        if i==1:
                                            name2= list(name)[i]
                                            a2= pypinyin.slug(name2)
                                            namelist=list(a2)
                                            b2=namelist[0]
                                        if i==2:
                                            name3= list(name)[i]
                                            a3= pypinyin.slug(name3)
                                            namelist=list(a3)
                                            b3=namelist[0]
                                    nameUpper=(b1+b2+b3).upper()
                                    path=r"%s/%s%s/" %(unicode(self.PYSavePathLineEdit.text()),filess[0],nameUpper)
                                    isExists=os.path.exists(path)
                                    if not isExists:
                                        os.mkdir(path)
                                        shutil.copy(unicode(self.PYSourcePathLineEdit.text())+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                                    shutil.copy(unicode(self.PYSourcePathLineEdit.text())+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                                    break
                                while(len(name))==2:
                                    for i in range(len(name)):
                                        if i==0:
                                            name1= list(name)[i]
                                            a1= pypinyin.slug(name1)
                                            namelist=list(a1)
                                            b1=namelist[0]+namelist[1]
                                        if i==1:
                                            name2= list(name)[i]
                                            a2= pypinyin.slug(name2)
                                            namelist=list(a2)
                                            b2=namelist[0]+namelist[1]
                                    nameUpper= (b1+b2).upper()
                                    path=r"%s/%s%s/" %(unicode(self.PYSavePathLineEdit.text()),filess[0],nameUpper)
                                    isExists=os.path.exists(path)
                                    if not isExists:
                                        os.mkdir(path)
                                        shutil.copy(unicode(self.PYSourcePathLineEdit.text())+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                                    shutil.copy(unicode(self.PYSourcePathLineEdit.text())+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                                    break
                                while(len(name))==4:
                                    for i in range(len(name)):
                                        if i==0:
                                            name1= list(name)[i]
                                            a1= pypinyin.slug(name1)
                                            namelist=list(a1)
                                            b1=namelist[0]
                                        if i==1:
                                            name2= list(name)[i]
                                            a2= pypinyin.slug(name2)
                                            namelist=list(a2)
                                            b2=namelist[0]
                                        if i==2:
                                            name3= list(name)[i]
                                            a3= pypinyin.slug(name3)
                                            namelist=list(a3)
                                            b3=namelist[0]
                                        if i==3:
                                            name4= list(name)[i]
                                            a4= pypinyin.slug(name4)
                                            namelist=list(a4)
                                            b4=namelist[0]
                                    nameUpper= (b1+b2+b3+b4).upper()
                                    path=r"%s/%s%s/" %(unicode(self.PYSavePathLineEdit.text()),filess[0],nameUpper)
                                    isExists=os.path.exists(path)
                                    if not isExists:
                                        os.mkdir(path)
                                        shutil.copy(unicode(self.PYSourcePathLineEdit.text())+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                                    shutil.copy(unicode(self.PYSourcePathLineEdit.text())+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                                    break

    def Niiconvert(self):
        import subprocess
        for lineEdit in self.NIIlineEdits:
            if not lineEdit.text().isEmpty():
                files=[x for x in os.listdir(self.NIISourcePathLineEdit.text())]
                for ii in files:
                    if(len(ii)>1):
                        cmd=self.exe_file+' '+str(self.NIISourcePathLineEdit.text())+'\\'+ii+' '+str(self.NIISavePathLineEdit.text())+' '+"%s" % str(self.NIISaveNameLineEdit.text())+ii
                    else:
                        cmd=self.exe_file+' '+str(self.NIISourcePathLineEdit.text())+'\\'+ii+' '+str(self.NIISavePathLineEdit.text())+' '+"%s" % str(self.NIISaveNameLineEdit.text())+'0'+ii
                    print (cmd)
                    process = subprocess.Popen(cmd, shell=True)
                    process.communicate()
            else:break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Dialog()
    form.show()
    app.exec_()



