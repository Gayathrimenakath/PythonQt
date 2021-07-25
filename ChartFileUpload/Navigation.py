from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QApplication, QStackedWidget, QLabel, QGroupBox
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtGui import *
import sys
import sip

from tableView import TableView
from chart import Chart


json_data = {
  "pie1":{
    "lib":{
        "libgcc":["magnesium", "aluminium"],
        "libc":["magnesium", "manganese", "aluminium"],
        "libmiosix":["copper", "aluminium"],
        "libstdc++":["Beryllium", "copper"],
       },
    "nonlib":{
         "Beryllium copper":["Beryllium", "copper"],
   	 "Billon":["gold", "copper"],
         "Copper tungsten":["Tungsten","copper"],
     }
}}



def dict_to_model(item, d):
    print('...........................................................',d)
    if isinstance(d, dict):
        for k, v in d.items():
            it = QtGui.QStandardItem(k)
            item.appendRow(it)
            dict_to_model(it, v)
    elif isinstance(d, list):
        for v in d:
            dict_to_model(item, v)
    else:
        item.appendRow(QtGui.QStandardItem(str(d)))

class Navigation(QtCore.QObject):
    #clicked = QtCore.pyqtSignal(QtCore.QModelIndex)
    def __init__(self, data, parent=None):
        super(Navigation, self).__init__(parent)
    
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
     
        #self.gridLayout.addWidget(self.listview, 0, 0, 2, 1)
        
        self.frame = QtWidgets.QFrame()
        self.chart = Chart('pie1', data, self)
        
        self.parent().addToolBar(self.chart.navigationBar(data))
                     
        self.ly = QtWidgets.QVBoxLayout()
        self.frame.setLayout(self.ly)
                
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.addWidget(self.frame)
        
        self.gridLayout2 = QtWidgets.QGridLayout()
        self.gridLayout2.addWidget(self.chart.chartview)    
        
        self.gridLayout.addLayout(self.gridLayout2, 0, 2, 0, 1)
        self.gridLayout.addLayout(self.gridLayout1, 0, 2, 0, 1)  
        
        self.horizontalGroupBox = QGroupBox()
        self.horizontalGroupBox.setLayout(self.gridLayout)

        



