#-------------------------------------------------------------------------------
# Name:        SigmaLabelGUI.py
# Purpose:     A tool for doctor's labeling
#
# Author:      ChunBo Liu (12SigmaTech)
#
# Created:     19/10/2016
# Copyright:   (c) 12SigmaTech 2016

# Changed Version:  0.11.01
#-------------------------------------------------------------------------------

#coding=utf-8
import slicer
import qt, ctk, vtk
import os
import logging
import time

from slicer.util import VTKObservationMixin
libPath=os.path.dirname(os.path.realpath(__file__))+'/modules'
import sys
sys.path.insert(0, libPath)

import LabelEditorLib
from LabelEditorLib.EditUtil import EditUtil
from LabelEditorLib.ColorBox import ColorBox
from LabelEditorLib.WinLevelPresetToolBar import WinLevelPresetToolBar

#
# global variable
#
previousVolumeNode=None

defaultFilePath="D:\SigmaLabel\Labels"

lungDiseaseList=["Lung Nodule(Solid)","Lung Nodule(Part-solid)","Lung Nodule(GGO)",\
                    "Emphysema","Pulmonary Fibrosis","Air Space Disease",\
                    "Pulmonary Effusion","Rib Fracture","Lymphoadenopathy","Pneumothorax" ,"Pulmonary Edema"]

brainDiseaseList=["Intraparenchymal Hemorrhage","Intraventricular Hemorrhage",\
                            "Subarachnoid Hemorrhage","Epidural Hemorrhage","Focal Encephalomalacia","Subdural Hemorrhage",\
                            "Hydrocephalus","Venous Sinus Thrombosis","Focal Mass","Midline Shift" ]

colorNoList=[1,9,100,26,299,32,110,258,287,303,30]




#Lable
class SigmaLabelGUI:
  def __init__(self, parent):
    import string
    parent.title = "SigmaLabel"
    parent.categories = ["12Sigma"]
    parent.contributors = ["ChunBo Liu (12SigmaTech)"]
    parent.helpText = """
     A label markup tool for 12Sigma Tech.
    """
    parent.acknowledgementText = """
"""
    self.parent = parent

class SigmaLabelGUIWidget(VTKObservationMixin):
    def __init__(self,parent=None):
        VTKObservationMixin.__init__(self)
        if not parent:
            self.parent = slicer.qMRMLWidget()
            self.parent.setLayout(qt.QVBoxLayout())
            self.parent.setMRMLScene(slicer.mrmlScene)
            self.layout=self.parent.layout()
            self.setup()
            self.parent.show()
        else:
            self.parent = parent
            self.layout = parent.layout()

    def setup(self):
      global lungDiseaseList
      self.volumes = ctk.ctkCollapsibleButton(self.parent)
      self.volumes.objectName = 'VolumeCollapsibleButton'
      self.volumes.setLayout(qt.QVBoxLayout())
      self.volumes.setText("Select Volumes")
      self.layout.addWidget(self.volumes)
      #Added a helper to verify the function
      self.helper = LabelEditorLib.HelperBox(self.volumes)

      self.editLabelMapsFrame = ctk.ctkCollapsibleButton(self.parent)
      self.editLabelMapsFrame.objectName = 'EditLabelMapsFrame'
      self.editLabelMapsFrame.setLayout(qt.QVBoxLayout())
      self.editLabelMapsFrame.setText("Label Selected Volume")
      self.layout.addWidget(self.editLabelMapsFrame)
      self.editLabelMapsFrame.collapsed = False

      #create the frame for Label type
      self.labelTypeFrame=qt.QFrame(self.editLabelMapsFrame)
      self.labelTypeFrame.setLayout(qt.QHBoxLayout())

      self.bodyPartLabel=qt.QLabel("Body Part:",self.labelTypeFrame)
      self.bodyPartLabel.setToolTip("Select Brain or Lung.")
      self.labelTypeFrame.layout().addWidget(self.bodyPartLabel)

      self.bodyPartSelector=qt.QComboBox(self.labelTypeFrame)
      self.bodyPartSelector.addItem("None")
      self.bodyPartSelector.addItem("Brain")
      self.bodyPartSelector.addItem("Lung")

      self.bodyPartSelector.setCurrentIndex(0)

      self.labelTypeFrame.layout().addWidget(self.bodyPartSelector)
      self.bodyPartSelector.connect('currentIndexChanged(QString)',self.onBodyPartSelect)
      self.diseaseLabel = qt.QLabel("   Label Type:",self.labelTypeFrame)
      self.diseaseLabel.setToolTip( "Display all of the diseases.")
      self.labelTypeFrame.layout().addWidget(self.diseaseLabel)

      self.diseaseSelector = qt.QComboBox(self.labelTypeFrame)
      self.diseaseSelector.setMinimumContentsLength(25)
      self.diseaseSelector.addItem("None")
      lungDiseaseIndex=0
      lungListLen=len(lungDiseaseList)
      while(lungDiseaseIndex<lungListLen):
        self.diseaseSelector.addItem(lungDiseaseList[lungDiseaseIndex])
        lungDiseaseIndex=lungDiseaseIndex+1

      self.diseaseSelector.setCurrentIndex(0)
      EditUtil.setLabel(1)

      self.diseaseColorLabel=qt.QLabel(self.labelTypeFrame)
      self.diseaseColorLabel.setToolTip("Show the selected label's color.")
      self.diseaseColorLabel.setFixedWidth(30)

      self.labelTypeFrame.layout().addWidget(self.diseaseSelector)
      self.labelTypeFrame.layout().addWidget(self.diseaseColorLabel)


      #add a color label for
      self.showColorLabel=qt.QLabel(self.labelTypeFrame)
      self.showColorLabel.setToolTip("Display the selected label's color.")
      self.showColorLabel.setFixedWidth(30)
      #default color
      rgb=[128,174,128]
      self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0] , rgb[1] , rgb[2] ))
      self.labelTypeFrame.layout().addWidget(self.showColorLabel)
      self.editLabelMapsFrame.layout().addWidget(self.labelTypeFrame)
      self.diseaseSelector.connect('currentIndexChanged(QString)',self.onDiseaseSelect)   ##TODO:Here need a function to do something!!!

      # add  start
      self.editLabelMapsFrame2 = ctk.ctkCollapsibleButton(self.parent)
      self.editLabelMapsFrame2.objectName = 'EditLabelMapsFrame2'
      self.editLabelMapsFrame2.setLayout(qt.QVBoxLayout())
      self.editLabelMapsFrame2.setText("Label Selected Volume")
      self.layout.addWidget(self.editLabelMapsFrame2)
      self.editLabelMapsFrame2.collapsed = False

      self.labelTypeFlu=qt.QFrame(self.editLabelMapsFrame2)
      self.labelTypeFlu.setLayout(qt.QHBoxLayout())
      self.FluPartLabel=qt.QLabel("Flu Part:",self.labelTypeFlu)
      self.FluPartLabel.setToolTip('Select Fowl smallpox virus or Monkey smallpox virus.')


      self.FluPartSelector=qt.QComboBox(self.labelTypeFlu)
      self.FluPartSelector.addItem("None")
      self.FluPartSelector.addItem("Fowl smallpox virus")
      self.FluPartSelector.addItem("Monkey smallpox virus")

      self.FluPartSelector.setCurrentIndex(0)


    ##      self.FluPartSelector.connect('currentIndexChanged(QString)',self.onBodyPartSelect)
      self.disFluLabel = qt.QLabel("   Label Type:",self.labelTypeFlu)
      self.disFluLabel.setToolTip( "Display all of the diseases.")

      self.disFluSelector = qt.QComboBox(self.labelTypeFlu)
      self.disFluSelector.setMinimumContentsLength(25)
      self.disFluSelector.addItem("None")
    ##self.labelTypeFlu.layout().addStretch(1)
      self.labelTypeFlu.layout().addWidget(self.FluPartLabel)
      self.labelTypeFlu.layout().addWidget(self.FluPartSelector)
      self.labelTypeFlu.layout().addWidget(self.disFluLabel)
      self.labelTypeFlu.layout().addWidget(self.disFluSelector)




      self.effectsToolsFrame = qt.QFrame(self.editLabelMapsFrame)
      self.effectsToolsFrame.objectName = 'EffectsToolsFrame'
      self.effectsToolsFrame.setLayout(qt.QHBoxLayout())
      self.editLabelMapsFrame.layout().addStretch(1)
      self.effectsToolsFrame.setMinimumWidth(300)
      self.editLabelMapsFrame.layout().addWidget(self.effectsToolsFrame)

      self.effectOptionsFrame = qt.QFrame(self.editLabelMapsFrame)
      self.effectOptionsFrame.objectName = 'EffectOptionsFrame'
      self.effectOptionsFrame.setLayout(qt.QVBoxLayout())
      self.effectOptionsFrame.setMinimumWidth(300)

      self.editBoxFrame = qt.QFrame(self.effectsToolsFrame)
      self.editBoxFrame.objectName = 'EditBoxFrame'
      self.editBoxFrame.setLayout(qt.QVBoxLayout())
      self.effectsToolsFrame.layout().addWidget(self.editBoxFrame)
      self.editLabelMapsFrame.layout().addWidget(self.effectOptionsFrame)

      self.toolsBox = LabelEditorLib.EditBox(self.editBoxFrame, optionsFrame=self.effectOptionsFrame)  #this will call the EditBox()
      self.layout.addStretch(1)
      self.saveAndLoadBtnFrame=qt.QFrame(self.editLabelMapsFrame)
      self.saveAndLoadBtnFrame.setLayout(qt.QHBoxLayout())
      self.widgetLabel1 = qt.QLabel("",self.labelTypeFrame)
      self.LoadButton = qt.QPushButton("Load Labels")
      self.LoadButton.toolTip = "Load the previous label volumes from some folders"
      self.LoadButton.connect('clicked(bool)', self.onLoadButtonClicked)
      self.widgetLabel = qt.QLabel("",self.labelTypeFrame)

      SaveButton=qt.QPushButton("Save Labels")
      SaveButton.toolTip = "Save current label volumes from some folders"
      SaveButton.connect('clicked(bool)', self.onSaveButtonClicked)
      self.widgetLabel2 = qt.QLabel("",self.labelTypeFrame)
      ResetButton=qt.QPushButton("Reset Labels")
      ResetButton.toolTip="Delete all of the previous labels of current Volume."
      ResetButton.connect('clicked(bool)',self.onResetButtonClicked)
      self.widgetLabel3 = qt.QLabel("",self.labelTypeFrame)

      self.saveAndLoadBtnFrame.layout().addWidget(self.widgetLabel1)
      self.saveAndLoadBtnFrame.layout().addWidget(self.LoadButton)
      self.saveAndLoadBtnFrame.layout().addWidget(self.widgetLabel)
      self.saveAndLoadBtnFrame.layout().addWidget(SaveButton)
      self.saveAndLoadBtnFrame.layout().addWidget(self.widgetLabel2)
      self.saveAndLoadBtnFrame.layout().addWidget(ResetButton)
      self.saveAndLoadBtnFrame.layout().addWidget(self.widgetLabel3)
      self.editLabelMapsFrame.layout().addWidget(self.saveAndLoadBtnFrame)

      # Set the layout to be WideScreen with 1(red) + 3(yellow, green, 3d)
      sigmalLabelViewLayoutDescription ="""<layout type="horizontal" split="true" >
         <item>
          <view class="vtkMRMLSliceNode" singletontag="Red">
           <property name="orientation" action="default">Axial</property>
           <property name="viewlabel" action="default">R</property>
           <property name="viewcolor" action="default">#F34A33</property>
          </view>
         </item>
         <item>
          <layout type="vertical">
           <item>
            <view class="vtkMRMLSliceNode" singletontag="Yellow">
             <property name="orientation" action="default">Sagittal</property>
             <property name="viewlabel" action="default">Y</property>
             <property name="viewcolor" action="default">#EDD54C</property>
            </view>
           </item>
           <item>
            <view class="vtkMRMLSliceNode" singletontag="Green">
             <property name="orientation" action="default">Coronal</property>
             <property name="viewlabel" action="default">G</property>
             <property name="viewcolor" action="default">#6EB04B</property>
            </view>
           </item>
           <item>
            <view class="vtkMRMLViewNode" singletontag="1">
             <property name="viewlabel" action="default">1</property>
            </view>
           </item>
          </layout>
         </item>
        </layout>"""
      layoutManager = slicer.app.layoutManager()
      layoutNode = layoutManager.layoutLogic().GetLayoutNode()
      sigmaLayout = slicer.vtkMRMLLayoutNode.SlicerLayoutUserView + 99;
      layoutNode.AddLayoutDescription(sigmaLayout, sigmalLabelViewLayoutDescription);
      layoutManager.setLayout(sigmaLayout)

      # disable automatic updates to slice views when datasets are loaded into Slicer
      self.helper.masterSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSwitchVolume)
      ####################################
      '''
      Winow Levels Preset Toolbar
      '''
      ####################################
      winleveltoolbar = WinLevelPresetToolBar()
      winleveltoolbar.findOrAddToolbar()

    def onDiseaseSelect(self,disease):
        if(disease=="Lung Nodule(Solid)" or disease=="Intraparenchymal Hemorrhage"):
            self.colorNo=1          #="purple"  #color no=205
            rgb=[128,174,128]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0] , rgb[1] , rgb[2] ))
        elif(disease=="Lung Nodule(Part-solid)" or disease=="Intraventricular Hemorrhage"):
            self.colorNo=9      #12         #="yellow"  #color no=12
            rgb=[230,220,70]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0] , rgb[1] , rgb[2] ))
        elif(disease=="Lung Nodule(GGO)" or disease=="Subarachnoid Hemorrhage"):
            self.colorNo=100         #="blue"    #color no=16
            rgb=[64,123,147]   # was rgb=[0,151,206]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0] , rgb[1] , rgb[2]))
        elif(disease=="Emphysema" or disease=="Epidural Hemorrhage"):
            self.colorNo=26         #"green"   #color no=26
            rgb=[0,145,30]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0] , rgb[1] , rgb[2]))
        elif(disease=="Air Space Disease" or disease=="Subdural Hemorrhage"):
            self.colorNo=32        #"red"     #color no=32
            rgb=[188,65,28]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0], rgb[1], rgb[2]))
        elif(disease=="Pulmonary Effusion" or disease=="Hydrocephalus"):
            self.colorNo=110
            rgb=[88,106,215]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0], rgb[1], rgb[2]))
        elif(disease=="Rib Fracture" or disease=="Venous Sinus Thrombosis"):
            self.colorNo=258
            rgb=[177,122,101]  #[255,255,220]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0], rgb[1], rgb[2]))
        elif(disease=="Lymphoadenopathy" or disease=="Focal Mass"):
            self.colorNo=287
            rgb=[0,147,202]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0], rgb[1], rgb[2]))
        elif(disease=="Pneumothorax" or disease=="Midline Shift"):
            self.colorNo=303
            rgb=[164,36,155]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0], rgb[1], rgb[2]))
        elif(disease=="Pulmonary Edema"):
            self.colorNo=30
            rgb=[170,250,250]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0], rgb[1], rgb[2]))
        elif(disease=="Pulmonary Fibrosis" or disease=="Focal Encephalomalacia"):
            self.colorNo=299
            rgb=[191,143,0]
            self.showColorLabel.setStyleSheet("background-color: rgb(%s,%s,%s)" % (rgb[0], rgb[1], rgb[2]))

        EditUtil.setLabel(self.colorNo)



    def onSaveButtonClicked(self):
      global defaultFilePath
      import os
      masterNode = None
      if self.helper is not None:
        filename_Suffix=".nrrd"
        labelVolume = EditUtil.getLabelVolume()
        labelFileName=labelVolume.GetName()
        masterVolume = EditUtil.getBackgroundVolume()
        snode = masterVolume.GetStorageNode()
        #get the current path of master volume.
        [filepath, volume_file]= os.path.split(snode.GetFileName())

        if(labelVolume):
            file_to_write=defaultFilePath+"/"+str(labelFileName)+filename_Suffix
            if slicer.util.saveNode(labelVolume,file_to_write) == False:
                logging.debug ('ERROR: failed to save label map: ', labelVolume.GetName())
            else:

                warningMessageDialog=qt.QMessageBox(slicer.util.mainWindow())#slicer.util.mainWindow()
                warningMessageDialog.setText("\n**Labels Saved Successfully!**\n\n")##                warningMessageDialog.setInformativeText("Labels Saved Successfully!")
                warningMessageDialog.setStandardButtons(qt.QMessageBox.Ok)
                warningMessageDialog.setDefaultButton(qt.QMessageBox.Ok)
                warningMessageDialog.exec_()

        EditUtil.setLabelOutline(True)
        labelVolume.GetDisplayNode().SetSliceIntersectionThickness(2)
        self.LoadButton.enabled = True

    def onLoadButtonClicked(self):

        # ------------------------------------------------------------------------------
        # TODO:
        ### We may need some logic here to make sure the current label map is saved
        # ------------------------------------------------------------------------------
        global defaultFilePath

        loadLabelsDialog=qt.QMessageBox(slicer.util.mainWindow())#slicer.util.mainWindow()
        loadLabelsDialog.setText("**WARNING**\n\n Unsaved labels will be LOST.Continue to LOAD?\n\n")
##        loadLabelsDialog.setInformativeText()
        loadLabelsDialog.setStandardButtons(qt.QMessageBox.Yes | qt.QMessageBox.Cancel)
        loadLabelsDialog.setDefaultButton(qt.QMessageBox.Cancel)
        ret = loadLabelsDialog.exec_()
        if ret==qt.QMessageBox.Cancel:
            return
        #Load the previous labels now,we should check if current label file is existed.
        oldLabelVolume = EditUtil.getLabelVolume()
##        print "1102 oldLabelVolume name is:",oldLabelVolume.GetName()
        masterVolume = EditUtil.getBackgroundVolume()
        snode = masterVolume.GetStorageNode()
        labelFileName=oldLabelVolume.GetName()
        #get the current path of master volume.
        [filepath, volume_file]= os.path.split(snode.GetFileName())
        file_to_load=defaultFilePath+"/"+str(labelFileName)+".nrrd"
##        print "###file to load in load button is:",file_to_load
        if(os.path.exists(file_to_load)):
            #remove current lables
##            print 'previous label name: ' + oldLabelVolume.GetName()
            slicer.mrmlScene.RemoveNode(oldLabelVolume)
            self.toolsBox.undoRedo.clearState()
            properties = {}
            self.setPropogateVolumeSelection(1)
            [success, labelVolume] = slicer.util.loadLabelVolume(file_to_load, properties, True)
            if success == True and labelVolume:
##                print "+++++Load the previous labels successfully when click the load button."
                labelVolume.SetName(labelFileName)
##                print labelVolume.GetName()
                # Set the newly loaded label to be active
                EditUtil.setActiveVolumes(masterVolume, labelVolume)
                EditUtil.setLabelOutline(True)
                labelVolume.GetDisplayNode().SetSliceIntersectionThickness(2)
##            else:
##                self.helper.select()
            self.setPropogateVolumeSelection(0)
        else:
##            print "Files not exist!!"
            warningMessageDialog=qt.QMessageBox(slicer.util.mainWindow())#slicer.util.mainWindow()
            warningMessageDialog.setText("\n \n**WARNING** \n Label file does not Exist! \n\n")
##            warningMessageDialog.setInformativeText("Label file does not Exist!")
            warningMessageDialog.setStandardButtons(qt.QMessageBox.Ok)
            warningMessageDialog.setDefaultButton(qt.QMessageBox.Ok)
            warningMessageDialog.exec_()

    def onResetButtonClicked(self):
        resetLabelsDialog=qt.QMessageBox(slicer.util.mainWindow())#slicer.util.mainWindow()
        resetLabelsDialog.setText("\n**WARNING** \n \n Do you want to delete all of your new labels now?\n\n")
        resetLabelsDialog.setStandardButtons(qt.QMessageBox.Yes | qt.QMessageBox.Cancel)
        resetLabelsDialog.setDefaultButton(qt.QMessageBox.Cancel)
        ret = resetLabelsDialog.exec_()
        if ret==qt.QMessageBox.Yes:  #will delete the previous labels now!!
            import os
            import sys
            #get the current directory
            masterVolume = EditUtil.getBackgroundVolume()
            if(masterVolume is None):
                return
            snode = masterVolume.GetStorageNode()
            [filepath, volume_file]= os.path.split(snode.GetFileName())
            labelVolume = EditUtil.getLabelVolume()
            if(labelVolume):
              labelFilePath=filepath

              labelFileName=labelVolume.GetName()
              file_to_delete=defaultFilePath+"/"+str(labelFileName)+".nrrd"
              if os.path.isfile(file_to_delete):
                  os.remove(file_to_delete)
              # Remove label volume from mrml scene
              slicer.mrmlScene.RemoveNode(labelVolume)
              #Clear the unDo/reDo list
              self.toolsBox.undoRedo.clearState()
              self.setPropogateVolumeSelection(1)
              #create new label volume
              newMerge=self.helper.select()
              self.setPropogateVolumeSelection(0)
              self.LoadButton.enabled = False

    def onSwitchVolume(self,node):
##        print "Switch to new node is:",node
        self.helper.getCurrentUserName()
        global previousVolumeNode
        if node is not None:
            if previousVolumeNode is not  None and previousVolumeNode!=node:
                self.saveCurrentLabels()
            previousVolumeNode=node
            # enable updates to slice views for selected volume
            self.setPropogateVolumeSelection(1)
            self.resetView(node)
            # enable updates to slice views for selected volume
            previousLabelExisted=self.helper.onSelect(node)
            # again disable automatic updates to slice views when datasets are loaded into Slicer
            self.setPropogateVolumeSelection(0)
            if(previousLabelExisted):
                self.LoadButton.enabled=True
            else:
                self.LoadButton.enabled=False

    def setPropogateVolumeSelection(self, doPropagate):
        compositeNode = EditUtil.getCompositeNode('Red')
        compositeNode.SetDoPropagateVolumeSelection(doPropagate)
        compositeNode = EditUtil.getCompositeNode('Green')
        compositeNode.SetDoPropagateVolumeSelection(doPropagate)
        compositeNode = EditUtil.getCompositeNode('Yellow')
        compositeNode.SetDoPropagateVolumeSelection(doPropagate)

    def saveCurrentLabels(self):
        global defaultFilePath
        import os
        self.checkSaveDialog=qt.QMessageBox(slicer.util.mainWindow())
        self.checkSaveDialog.setText("**WARNING:Volume Changed!** \n \n Do you want to save all of your new labels now? \n \n")
##        self.checkSaveDialog.setInformativeText("Do you want to save all of your labels of current volume?")
        self.checkSaveDialog.setStandardButtons(qt.QMessageBox.Yes | qt.QMessageBox.No)
        self.checkSaveDialog.setDefaultButton(qt.QMessageBox.Yes)
        ret=self.checkSaveDialog.exec_()

        filename_Suffix=".nrrd"
        labelVolume = EditUtil.getLabelVolume()
        masterVolume = EditUtil.getBackgroundVolume()
        snode = masterVolume.GetStorageNode()
        #get the current path of master volume.
        [filepath, volume_file]= os.path.split(snode.GetFileName())

        if(labelVolume):
            labelFilePath=defaultFilePath
            labelFileName=labelVolume.GetName()#labelVolume.GetName()
        if  ret==qt.QMessageBox.Yes: #save the current labels now.
            if(labelVolume):
                file_to_write=labelFilePath+"/"+str(labelFileName)+filename_Suffix
                slicer.util.saveNode(labelVolume,file_to_write)
##                print "Saved the labels successfully when swcitching the volumes."
                self.toolsBox.undoRedo.clearState()

        else:    # user select No,this will clear all of the current labels firstly.
           labelVolume = EditUtil.getLabelVolume()
           slicer.mrmlScene.RemoveNode(labelVolume)
           #reset the undo list
           self.toolsBox.undoRedo.clearState()
            #check if there is already has a label volume of  current volume


    def onBodyPartSelect(self,bodypart):
        global lungDiseaseList,brainDiseaseList
        masterVolume = EditUtil.getBackgroundVolume()
        if(bodypart=="Lung"):  #order of labels
            self.diseaseSelector.blockSignals(True)
            self.diseaseSelector.clear()
            self.diseaseSelector.blockSignals(False)
            i=0
            while(i<len(lungDiseaseList)):
                self.diseaseSelector.addItem(lungDiseaseList[i])
                i=i+1
            diseaseSelected=0
            self.diseaseSelector.setCurrentIndex(diseaseSelected)
            #call the resetView()
            self.resetView(masterVolume)
        elif(bodypart=="Brain"):
            self.diseaseSelector.blockSignals(True)
            self.diseaseSelector.clear()
            self.diseaseSelector.blockSignals(False)
            j=0
            while(j<len(brainDiseaseList)):
                self.diseaseSelector.addItem(brainDiseaseList[j])
                j=j+1
            diseaseSelected=0
            self.diseaseSelector.setCurrentIndex(diseaseSelected)
            self.resetView(masterVolume)
        else:
            self.diseaseSelector.blockSignals(True)
            self.diseaseSelector.clear()
            self.diseaseSelector.blockSignals(False)

        self.saveDiseaseColor()


    def resetView(self,node):
        self.grayscaleNode = node
        activeNode = slicer.app.applicationLogic().GetSelectionNode()
        activeNode.SetReferenceActiveVolumeID(self.grayscaleNode.GetID())
        slicer.app.applicationLogic().PropagateVolumeSelection(0)
        volumeRenderingWidgetRep = slicer.modules.volumerendering.widgetRepresentation()
        volumeRenderingWidgetRep.setMRMLVolumeNode(node)
        presetsScene = slicer.modules.volumerendering.logic().GetPresetsScene()

        if self.bodyPartSelector.currentIndex==2:
            node.GetDisplayNode().SetAutoWindowLevel(False)
            node.GetDisplayNode().SetWindowLevel(1400., -500.)
##            print "Selected the CT-Lung",self.bodyPartSelector
            ctLung = presetsScene.GetFirstNodeByName('CT-Lung')
            volumeRenderingWidgetRep.applyPreset(ctLung)
        elif(self.bodyPartSelector.currentIndex==1):
            node.GetDisplayNode().SetAutoWindowLevel(False)
            node.GetDisplayNode().SetWindowLevel(100., 50.)
            ctBrain=presetsScene.GetFirstNodeByName("CT-Brain")  #todo:check with Yumin about this preset type
            volumeRenderingWidgetRep.applyPreset(ctBrain)
        volumeRenderingNode = slicer.mrmlScene.GetFirstNodeByName('VolumeRendering')
        volumeRenderingNode.SetVisibility(1)

        #center the slicer
        layoutManager = slicer.app.layoutManager()
        layoutManager.resetThreeDViews()
        threeDWidget = layoutManager.threeDWidget(0)
        threeDView = threeDWidget.threeDView()
        #threeDView.resetFocalPoint()
        layoutManager.resetSliceViews()
        threeDView.setOrientationWidgetVisible(1)

        #Adjust the size of 3D view
        vol=self.grayscaleNode;
        self.spacing=vol.GetSpacing()
        self.origin=vol.GetOrigin()
        self.extent=vol.GetImageData().GetExtent()
        self.dimension = vol.GetImageData().GetDimensions()
        sceneCenter=[0,0,0]
        sceneCenter[0]=self.origin[0]-self.dimension[0]*0.5*self.spacing[0]
        sceneCenter[1]=self.origin[1]+self.dimension[1]*0.5*self.spacing[1]
        sceneCenter[2]=self.origin[2]+self.dimension[2]*0.5*self.spacing[2]

        cameraPos=[0,0,0]
        cameraPos[0]=sceneCenter[0]
        cameraPos[1]=sceneCenter[1]+1.5*self.dimension[1]*self.spacing[1]
        cameraPos[2]=sceneCenter[2]

        cameraNode=slicer.util.getNode('*Camera*')
        camera=cameraNode.GetCamera()
        camera.SetPosition(cameraPos)
        camera.SetViewUp(0,0,1)
        camera.SetFocalPoint(sceneCenter)
        camera.SetViewAngle(35)
        cameraNode.ResetClippingRange()
        EditUtil.setLabelOutline(True)


    def turnOnMIP(self):
        sliceNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
        appLogic = slicer.app.applicationLogic()
        sliceLogic = appLogic.GetSliceLogic(sliceNode)
        sliceLayerLogic = sliceLogic.GetBackgroundLayer()
        reslice = sliceLayerLogic.GetReslice()
        reslice.SetSlabModeToMax()
        reslice.SetSlabNumberOfSlices(900)
        reslice.SetSlabSliceSpacingFraction(0.5)
        sliceNode.Modified()


    def saveDiseaseColor(self):
        global lungDiseaseList,brainDiseaseList,colorNoList
        #create the lundDiseaseColor dictionary
        lungDiseaseLen=len(lungDiseaseList)
        colorNoLen=len(colorNoList)
        lungColorNoDic={}
        lungIndex=0
        while(lungIndex<lungDiseaseLen):
            lungColorNoDic.setdefault(lungIndex,{})['diseaseName']=lungDiseaseList[lungIndex]
            lungColorNoDic.setdefault(lungIndex,{})['diseaseColorNo']=colorNoList[lungIndex]
            lungIndex=lungIndex+1

        #create the brainColorNo dictionary
        brainDiseaseLen=len(brainDiseaseList)
        brainColorNoDic={}
        brainIndex=0
        while(brainIndex<brainDiseaseLen):
            brainColorNoDic.setdefault(brainIndex,{})['diseaseName']=brainDiseaseList[brainIndex]
            brainColorNoDic.setdefault(brainIndex,{})['diseaseColorNo']=colorNoList[brainIndex]
            brainIndex=brainIndex+1
        #get current label volume's name
        labelVolume = EditUtil.getLabelVolume()
        labelFileName=labelVolume.GetName()

        file_to_write=defaultFilePath+"/"+str(labelFileName)+".txt"

        fp=file(file_to_write,'a')
        fp.write("LabelName is:"+str(labelFileName)+'\n')
        fp.write("Version is:"+"1.0"+"\n")
        if(self.bodyPartSelector.currentIndex==1):  #bodypart is brain now
            fp.write("BodyPart is:Brain"+"\n")
            outputIndex=0
            while(outputIndex<brainIndex):
                fp.write(str(brainColorNoDic[outputIndex]))
                fp.write('\n')
                outputIndex=outputIndex+1

        elif(self.bodyPartSelector.currentIndex==2):  #bodypart is lung now
            fp.write("BodyPart is:Lung"+"\n")
            outputIndex=0
            while(outputIndex<lungIndex):
##                print "outputIndex=",outputIndex
                fp.write(str(lungColorNoDic[outputIndex]))
                fp.write('\n')
                outputIndex=outputIndex+1
        fp.close()


