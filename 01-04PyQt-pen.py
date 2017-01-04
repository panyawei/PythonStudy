#-------------------------------------------------------------------------------
# Name:        pen
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     04/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import sys
from PyQt4.QtCore import Qt
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QCheckBox, QComboBox, QDialog,
        QGridLayout, QHBoxLayout, QLabel, QPushButton, QSpinBox,
        QVBoxLayout)


class PenPropertiesDlg(QDialog):

    def __init__(self, parent=None):
        super(PenPropertiesDlg, self).__init__(parent)

        widthLabel = QLabel("&Width:")
        self.widthSpinBox = QSpinBox()
        widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.widthSpinBox.setRange(0, 24)
        self.beveledCheckBox = QCheckBox("&Beveled edges")
        styleLabel = QLabel("&Style:")
        self.styleComboBox = QComboBox()
        styleLabel.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(["Solid", "Dashed", "Dotted",
                                     "DashDotted", "DashDotDotted"])
        okButton = QPushButton("&OK")
        cancelButton = QPushButton("Cancel")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(self.beveledCheckBox, 0, 2)
        layout.addWidget(styleLabel, 1, 0)
        layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)
        self.setLayout(layout)

        okButton.clicked.connect(self.accept)
        cancelButton.clicked.connect(self.reject)
        self.setWindowTitle("Pen Properties")


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.width = 1
        self.beveled = False
        self.style = "Solid"

        penButtonInline = QPushButton("Set Pen... (Dumb &inline)")
        penButton = QPushButton("Set Pen... (Dumb &class)")
        self.label = QLabel("The Pen has not been set")
        self.label.setTextFormat(Qt.RichText)

        layout = QVBoxLayout()
        layout.addWidget(penButtonInline)
        layout.addWidget(penButton)
        layout.addWidget(self.label)
        self.setLayout(layout)

        penButtonInline.clicked.connect(self.setPenInline)
        penButton.clicked.connect(self.setPenProperties)
        self.setWindowTitle("Pen")
        self.updateData()


    def updateData(self):
        bevel = ""
        if self.beveled:
            bevel = "<br>Beveled"
        self.label.setText("Width = {0}<br>Style = {1}{2}".format(
                           self.width, self.style, bevel))


    def setPenInline(self):
        widthLabel = QLabel("&Width:")
        widthSpinBox = QSpinBox()
##        widthLabel.setBuddy(widthSpinBox)
        widthSpinBox.setAlignment(Qt.AlignLeft)
        widthSpinBox.setRange(0, 24)
        widthSpinBox.setValue(self.width)
        beveledCheckBox = QCheckBox("&Beveled edges")
        beveledCheckBox.setChecked(self.beveled)
        styleLabel = QLabel("&Style:")
        styleComboBox = QComboBox()
        styleLabel.setBuddy(styleComboBox)
        styleComboBox.addItems(["Solid", "Dashed", "Dotted",
                                "DashDotted", "DashDotDotted"])
        styleComboBox.setCurrentIndex(styleComboBox.findText(self.style))
        okButton = QPushButton("&OK")
        cancelButton = QPushButton("Cancel")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(widthSpinBox, 0, 1)
        layout.addWidget(beveledCheckBox, 0, 2)
        layout.addWidget(styleLabel, 1, 0)
        layout.addWidget(styleComboBox, 1, 1, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)

        form = QDialog()
        form.setLayout(layout)
        okButton.clicked.connect(form.accept)
        cancelButton.clicked.connect(form.reject)
        form.setWindowTitle("Pen Properties")

        if form.exec_():
            self.width = widthSpinBox.value()
            self.beveled = beveledCheckBox.isChecked()
            self.style = unicode(styleComboBox.currentText())
            self.updateData()


    def setPenProperties(self):
        dialog = PenPropertiesDlg(self)
        dialog.widthSpinBox.setValue(self.width)
        dialog.beveledCheckBox.setChecked(self.beveled)
        dialog.styleComboBox.setCurrentIndex(
                dialog.styleComboBox.findText(self.style))
        if dialog.exec_():
            self.width = dialog.widthSpinBox.value()
            self.beveled = dialog.beveledCheckBox.isChecked()
            self.style = unicode(dialog.styleComboBox.currentText())
            self.updateData()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()