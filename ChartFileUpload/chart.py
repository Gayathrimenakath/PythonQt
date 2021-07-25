from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel,QToolBar
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from tableView import TableView
#from Navigation import Navigation



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QApplication, QStackedWidget, QLabel, QGroupBox
import sys
import sip
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


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

'''def clearLayout(layout):
        if layout.takeAt(0) is not None:
        #widget = item.widget()
            if layout.takeAt(0).item.widget() is not None:
                layout.takeAt(0).item.widget().deleteLater()'''
        
        
class Chart(QWidget):
    def __init__(self, chartKey, data, frame, parent=None):
        super(Chart, self).__init__(parent)
        self.frame = frame
        self.data = data
        
        self.pt = self.parent()
        
        #add the to the main window
        #self.toolbar = QToolBar("Edit", self)
        #self.pt.addToolBar(self.toolbar)
        
        #ly = QtWidgets.QVBoxLayout()
        #self.frame = QtWidgets.QFrame()
        #self.frame.setLayout(ly)
        
        #self.layout = QtWidgets.QGridLayout()
        
        #print('----------------',self.frame)
        
        
        
        self.create_chart(chartKey)
        clicked = QtCore.pyqtSignal(QtCore.QModelIndex)
        #self.pt.addToolBar(self.navigationBar(data))
      
        
    def create_chart(self, chartKey):
        self.series = QPieSeries()
        self.series.setHoleSize(0.35)
        self.chart = QChart()
        
        
        
        #Add series to the chart
        self.addSeries(chartKey)

	# for the background and title
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("DonutChart Example")
        self.chart.setTheme(QChart.ChartThemeBlueCerulean)

        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        
        #navigation = Navigation(classObj, self)
        #self.addToolBar(navigation.toolbar)
        
        #clicked = QtCore.pyqtSignal(QtCore.QModelIndex)
        
        
        
        
    def navigationBar(self, data):
        self.toolbar = QtWidgets.QToolBar()
        self.toolbar.actionTriggered.connect(self.on_actionTriggered)     
        self.model =  QtGui.QStandardItemModel(self)
        dict_to_model(self.model.invisibleRootItem(), data)
        it = self.model.item(0, 0)
        ix = self.model.indexFromItem(it)
        root_action = self.toolbar.addAction(it.text())
        root_action.setData(QtCore.QPersistentModelIndex(ix))
        self.listview = QtWidgets.QListView()
        self.listview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        #self.series.doubleClicked.connect(self.on_clicked)
        self.listview.setModel(self.model)
        self.listview.setRootIndex(ix)
        self.a = 10
        
        return self.toolbar
        
        
       
    #make the listed items clickable
    #@QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_clicked(self, index):
        if not self.model.hasChildren(index):
            self.clicked.emit(index)
            return
        action = self.toolbar.addAction(index.data())
        action.setData(QtCore.QPersistentModelIndex(index))
        self.listview.setRootIndex(index)
        print(index.data())
        self.chart.addSeries(index.data())
        
        
    #make the breadcrumbs clickable in order to go back and forth
    #@QtCore.pyqtSlot(QtWidgets.QAction)
    def on_actionTriggered(self, action):
        ix = action.data()
        self.chart.addSeries(ix.data())
        model = ix.model()
        self.listview.setRootIndex(QtCore.QModelIndex(ix))
        self.toolbar.clear()
        ixs = []
        while  ix.isValid():
            ixs.append(ix)
            ix = ix.parent()
        for ix in reversed(ixs):
            action = self.toolbar.addAction(ix.data())
            action.setData(ix)    
    
    
        
    def addSeries(self, key):
        self.chart.removeAllSeries()
        self.series = QPieSeries()
        self.series.setHoleSize(0.35)
        
        
        #Show chartview only if the content length is less than 6. Otherwise show a table view    
        if len(self.data[key]) < 6:
            for key, value in self.data[key].items():
                slice_ = QPieSlice(str(key), value)
                self.series.append(slice_)
       
            for slice in self.series.slices():
                slice.setLabel(slice.label())
            
            self.chart.addSeries(self.series)
            self.frame.frame.hide()
            self.chart.show()
        else:
            for m, item in self.data[key].items():
                print(m,item)
            
            self.table = TableView(self.data[key], len(self.data[key]), 1)
     
            if self.frame.ly.count() > 0:
                self.frame.ly.itemAt(0).widget().setParent(None)
            
            self.frame.ly.addWidget(self.table)
            
            
            self.frame.frame.show()
            self.chart.hide()         
            
        self.series.doubleClicked.connect(self.handle_double_clicked)
          
    #Show the update chart with the distribution of the selected slice
    def handle_double_clicked(self, slice):
        slice.setExploded()
        slice.setLabelVisible()
     
        if slice.label() in self.data.keys():
            print("slice",slice.label());
            self.addSeries(slice.label())
           
