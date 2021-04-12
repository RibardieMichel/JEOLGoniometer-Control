# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import time
import os
from PyQt4 import QtCore, QtGui, uic
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyJEM import TEM3

stage=TEM3.Stage3()
step=1

qtCreatorFile =  "GonioControl.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("GonioSet")
        position=stage.GetPos()
        #position=[20000, 80000, 25.2, 3, 2]  #FOR TEST
        "print(position)"
        #position=position[0:2]
        print(position)
        X=position[0]
        Y=position[1]
        Z=position[2]
        TX=position[3]
        TY=position[4]
        X=round((X/1000),2)
        Y=round((Y/1000),2)
        Z=round((Z/1000),2)
        TX=round((TX/1),3)
        TY=round((TY/1),3)
        self.Xvalue.setValue(X)
        self.Yvalue.setValue(Y)
        self.Zvalue.setValue(Z)
        self.TXvalue.setValue(TX)
        self.TYvalue.setValue(TY)
        
        print("stage:",X,Y,Z,TX,TY)
        
        #origin motors
        self.Neutralize.clicked.connect(self.Neutral)
        self.NSHIFT.clicked.connect(self.shiftN)
        self.NZ.clicked.connect(self.ZN)        
        self.NTX.clicked.connect(self.TXN)
        self.NTY.clicked.connect(self.TYN)        
        
        #mettre à jour les données
        self.RefreshButton.clicked.connect(self.getpos)
        #use of mouse wheel
        self.Xvalue.valueChanged.connect(self.setX)
        self.Yvalue.valueChanged.connect(self.setY)
        self.Zvalue.valueChanged.connect(self.setZ)
        self.TXvalue.valueChanged.connect(self.setTX)
        self.TYvalue.valueChanged.connect(self.setTY)
        #use of Shift arrows
        self.right.clicked.connect(self.Xplus)
        self.left.clicked.connect(self.Xminus)
        self.up.clicked.connect(self.Yplus)
        self.down.clicked.connect(self.Yminus)
        #Tilt step by step
        self.Txplus.clicked.connect(self.Txpos)
        self.Txmoins.clicked.connect(self.Txneg)
        self.Typlus.clicked.connect(self.Typos)
        self.Tymoins.clicked.connect(self.Tyneg)
        #Z step by step
        self.Zplus.clicked.connect(self.Zpos)
        self.Zmoins.clicked.connect(self.Zneg)
        
        #QtGui.QTextEdit.toPlainText
    def shiftN(self):
        stage.SetX(0)
        stage.SetY(0)
        time.sleep(1)
        self.Xvalue.setValue(0)
        self.Yvalue.setValue(0)  
        
    def TXN(self):
        stage.SetTiltXAngle(0)
        time.sleep(1)
        self.TXvalue.setValue(0)
        
    def TYN(self):
        stage.SetTiltYAngle(0)
        time.sleep(1)
        self.TXvalue.setValue(0)
        
    def ZN(self):
        stage.SetZ(0)
        time.sleep(1)
        self.Zvalue.setValue(0)
        
    def Neutral(self):
        stage.SetOrg()
        time.sleep(5)
        self.Xvalue.setValue(0)
        self.Yvalue.setValue(0)
        self.Zvalue.setValue(0)
        self.TXvalue.setValue(0)
        self.TYvalue.setValue(0)
        
    def Xplus(self):
        step=self.StepShift.value() *1
        step=float(step)
        X=self.Xvalue.value()*1
        #stage.SetXRel(step)
        self.Xvalue.setValue(X+step)
        
    def Xminus(self):
        step=self.StepShift.value()*1
        step=float(step)
        X=self.Xvalue.value()*1
        #stage.SetXRel(-step)
        self.Xvalue.setValue(X-step)
        
    def Yplus(self):
        step=self.StepShift.value()*1
        step=float(step)
        Y=self.Yvalue.value()*1
        #stage.SetYRel(step)
        self.Yvalue.setValue(Y+step)
    def Yminus(self):
        step=self.StepShift.value()*1
        step=float(step)
        Y=self.Yvalue.value()*1
        #stage.SetYRel(-step)
        self.Yvalue.setValue(Y-step)
        
    def Txpos(self):
        step=(self.StepTiltX.value())*1
        Tx=self.TXvalue.value()
        #stage.SetTXRel(step)
        self.TXvalue.setValue(Tx+step)
        
    def Txneg(self):
        step=(self.StepTiltX.value())*1
        Tx=self.TXvalue.value()
        Tx=float(Tx)
        #stage.SetTXRel(-step)
        self.TXvalue.setValue(Tx-step)
        
    def Typos(self):
        step=(self.StepTiltY.value())*1
        Ty=self.TYvalue.value()
        #stage.SetTYRel(step)
        self.TYvalue.setValue(Ty+step)
        
    def Tyneg(self):
        step=(self.StepTiltY.value())*1
        Ty=self.TYvalue.value()
        #stage.SetTYRel(-step)
        self.TYvalue.setValue(Ty-step)
        
        
    def Zneg(self):
        step=int(self.StepZ.text())*1
        #stage.SetZRel(-step)
        Z=self.Zvalue.value()
        Z=Z-step
        self.Zvalue.setValue(Z)
        
    def Zpos(self):
        step=int(self.StepZ.text())*1
        #stage.SetZRel(step)
        Z=self.Zvalue.value()
        Z=Z+step
        self.Zvalue.setValue(Z)
        
    def getpos(self):
        position=stage.GetPos()
        #position=[100000, 120000, 55.2, 10, 20]  #FOR TEST
        "print(position)"
        #position=position[0:2]
        print(position)
        X=position[0]
        Y=position[1]
        Z=position[2]
        TX=position[3]
        TY=position[4]
        X=round((X/1000),2)
        Y=round((Y/1000),2)
        Z=round((Z/1000),2)
        TX=round((TX/1),3)
        TY=round((TY/1),3)
        print("stage:",X,Y,Z,TX,TY)
        self.Xvalue.setValue(X)
        self.Yvalue.setValue(Y)
        self.Zvalue.setValue(Z)
        self.TXvalue.setValue(TX)
        self.TYvalue.setValue(TY)
        #QtGui.QSpinBox.setValue(X)
        
    def setX(self):
        position=stage.GetPos()
        #position=[200000, 180000, 25.2, 0.3, 0.0]  #FOR TEST
        X=self.Xvalue.value()
        print("SX:",X)
        X=X*1000
        #time.sleep(0.1)
        stage.SetX(X)
        
    def setY(self):
        position=stage.GetPos()
        #position=[200000, 180000, 25.2, 0.3, 0.0]  #FOR TEST
        Y=self.Yvalue.value()
        print("SY:",Y)
        Y=Y*1000
        #time.sleep(0.1)
        stage.SetY(Y)
        
    def setZ(self):
        position=stage.GetPos()
        #position=[200000, 180000.2, 25.2, 0.3, 0.0]  #FOR TEST
        Z=self.Zvalue.value()
        print("Z:",Z)
        Z=Z*1000
        #time.sleep(0.1)
        stage.SetZ(Z)        
        
    def setTX(self):
        position=stage.GetPos()
        #position=[200.5, 180.2, 25.2, 0.3, 0.0]  #FOR TEST
        TX=self.TXvalue.value()
        print("TX:",TX)
        TX=TX*1
        #time.sleep(0.1)
        stage.SetTiltXAngle(TX)
        
    def setTY(self):
        position=stage.GetPos()
        #position=[200.5, 180.2, 25.2, 0.3, 0.0]  #FOR TEST
        TY=self.TYvalue.value()
        print("TY:",TY)
        TY=TY*1
        #time.sleep(0.1)
        stage.SetTiltYAngle(TY)
        
        
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())