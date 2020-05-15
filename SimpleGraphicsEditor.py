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
        # Signal作成
        self.ui.pushButton.clicked.connect(self.clickbtn)

        self.ui.action_Open.triggered.connect(self.open)
        self.ui.action_Save.triggered.connect(self.save)
        self.ui.actionExit.triggered.connect(self.Exit)
        #self.ui.toolButton.clicked.connect(self.clicktoolbtn)
        #self.ui.lineEdit.setText("Hello World")
    def clickbtn(self):
        print("Push")
        print(self.file[0])
        img=cv2.imread(self.file[0])
        testcv=OpencvProcessing()
        img=testcv.gain(img,2.0)
        height,width,channels=img.shape
        bytesPerLine = channels * width
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        Qtimage=QtGui.QImage(img.data,width,height,bytesPerLine, QtGui.QImage.Format_RGB888)
        scene=QtWidgets.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap.fromImage(Qtimage))
        self.ui.graphicsView.setScene(scene)
    def clicktoolbtn(self):
        path = QtWidgets.QFileDialog().getOpenFileName()
        #if path != "":
            #self.ui.lineEdit.setText(path)
    def open(self):
        #cv_testopen=OpencvProcessing()
        self.file = QtWidgets.QFileDialog().getOpenFileName()
        
        pic_Item=QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(self.file[0]))
        print(self.file[0])
        img=cv2.imread(self.file[0])
        height,width,channels=img.shape
        bytesPerLine = channels * width
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        Qtimage=QtGui.QImage(img.data,width,height,bytesPerLine, QtGui.QImage.Format_RGB888)
        scene=QtWidgets.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap.fromImage(Qtimage))
        self.ui.graphicsView.setScene(scene)
        #img=c(self.file[0])
        # height,width,channels=img.shape
        # bytesPerLine = channels * width
        # img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # Qtimage=QtGui.QImage(img.data,width,height,bytesPerLine, QtGui.QImage.Format_RGB888)
        # scene=QtWidgets.QGraphicsScene()
        # scene.addPixmap(QtGui.QPixmap.fromImage(Qtimage))
        # self.ui.graphicsView.setScene(scene)
    def save(self):
        print("save")
    def Exit(self):
        self.close()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UIGraphicsEditorWidget()
    #window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
    #window.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    #import stylesheet
    #style_filename="SimpleGraphicsEditor.qss"
    open_file=open(os.path.join(CURRENT_PATH, 'SimpleGraphicsEditor.qss'), 'r')
    style_data = open_file.read()
    open_file.close
    window.setStyleSheet(style_data)

    window.show()
    sys.exit(app.exec_())