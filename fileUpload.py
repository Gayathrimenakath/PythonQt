from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QApplication, QStackedWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setText('Welcome to PyQt5 example')
        self.label1.setAutoFillBackground(True)
        self.label1.setFont(QtGui.QFont("Times", 20,weight=QtGui.QFont.Bold))
        self.label1.setAlignment(Qt.AlignCenter)
        
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(10, 210, 500, 23)
        self.label3.setObjectName("label3")
        
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.addWidget(self.label1, 0, 0)
        
        self.frame = QtWidgets.QFrame()
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.gridLayout2 = QtWidgets.QGridLayout()
        self.gridLayout2.setObjectName("gridLayout2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout2.addWidget(self.label_2, 0, 0, 0, 1)
        
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout2.addWidget(self.pushButton, 0, 2, 1, 1)
        
        self.gridLayout.addLayout(self.gridLayout2, 0, 0, 7, 2)
        self.gridLayout.addLayout(self.gridLayout1, 0, 0, 1, 2)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect( self.file_open)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("fileUpload", "File Name"))
        self.pushButton.setText(_translate("fileUpload", "Browse"))
        

    def file_open(self):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', options=QtWidgets.QFileDialog.DontUseNativeDialog)
        file = open(name, 'r')
        with file:
            text = file.read()
            self.lineEdit.setText(name)
            self.label3.setText('File Uploaded, check console for its contents')
            print(text)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
