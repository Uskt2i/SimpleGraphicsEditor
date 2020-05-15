#!python3
# -*- coding: utf-8 -*-
import sys,glob,datetime
import os.path,cv2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
import numpy as np
#自作OpencvClass読み込み
from OpencvProcessing import OpencvProcessing

CURRENT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

height,width,channels=0,0,0
class UIGraphicsEditorWidget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UIGraphicsEditorWidget, self).__init__(parent)
 
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'SimpleGraphicsEditor.ui'))
        self.setCentralWidget(self.ui)
        self.setWindowTitle("Simple Graphics Editor")
        self.setCSS()

        self.ui.lineEditGain.setText('1.0')
        # Signal作成
        self.ui.pushButtonExcute.clicked.connect(self.clickbtn)

        self.ui.horizontalSliderGain.valueChanged.connect(self.sliderValueChangeGain)
        self.ui.lineEditGain.textChanged.connect(self.changeText)

        self.ui.action_Open.triggered.connect(self.open)
        self.ui.action_Save.triggered.connect(self.save)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionAbout.triggered.connect(self.about)
    def sliderValueChangeGain(self):
        view_num=float(self.ui.horizontalSliderGain.value())/100
        self.ui.lineEditGain.setText(str(view_num))
    def changeText(self,text):
        edit_num=float(text)*100
        #self.ui.horizontalSliderGain.value(int(edit_num))
    def clickbtn(self):

        gain_value=float(self.ui.lineEditGain.text())
        cv_test=OpencvProcessing()
        self.adjustimg=cv_test.gain(self.img,gain_value)
        self.updataImage(self.adjustimg)

    def open(self):
        self.file = QtWidgets.QFileDialog().getOpenFileName()
        self.img=cv2.imread(self.file[0])
        self.updataImage(self.img)

    def updataImage(self,updata_img):
        height,width,channels=updata_img.shape
        bytesPerLine = channels * width
        convert_img=cv2.cvtColor(updata_img,cv2.COLOR_BGR2RGB)
        Qtimage=QtGui.QImage(convert_img.data,width,height,bytesPerLine, QtGui.QImage.Format_RGB888)
        scene=QtWidgets.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap.fromImage(Qtimage))
        self.ui.graphicsView.setScene(scene)

    def save(self):
        print("save")
        file_name= QtWidgets.QFileDialog().getSaveFileName()
        print(file_name)
        save_file=file_name[0]
        cv2.imwrite(save_file,self.adjustimg)
        QMessageBox.information(self, "Message", "Save File [ "+save_file+" ]")

    def exit(self):
        self.close()
    def about(self):
        QMessageBox.information(self, "About", "Version 1.01")
    def setCSS(self):
        open_file=os.path.join(CURRENT_PATH, 'SimpleGraphicsEditor.css')
        with open(open_file,"r") as f:
            self.setStyleSheet("".join(f.readlines()))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UIGraphicsEditorWidget()
    window.show()
    sys.exit(app.exec_())