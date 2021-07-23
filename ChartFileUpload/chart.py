from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from tableView import TableView


class Chart(QWidget):
    def __init__(self, chartKey, data, frame, parent=None):
        super(Chart, self).__init__(parent)
        self.frame = frame
      
        
        self.data = data
        self.create_chart(chartKey)
      
        
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
        
        
    def addSeries(self, key):
        self.chart.removeAllSeries()
        self.series = QPieSeries()
        self.series.setHoleSize(0.35)
            
        if len(self.data[key]) == 2:
            for key, value in self.data[key].items():
                #print("adding series", str(key), value)
                slice_ = QPieSlice(str(key), value)
                self.series.append(slice_)
       
            for slice in self.series.slices():
                slice.setLabel("{:.1f}%".format(100 * slice.percentage()))
            
            self.chart.addSeries(self.series)
            #self.frame.frame.hide()
            
            #self.frame.frame.removeWidget(self.table)
            
            self.frame.frame.hide()
            self.chart.show()
        else:
            print('hi')
            for m, item in self.data[key].items():
                print(m,item)
            
            self.table = TableView(self.data[key], 3, 1)
            #self.table = TableView(data, 4, 5)
            #self.model = TableModel(sampleData[key])
            #self.frame.table.setModel(self.model)
            
            if self.frame.ly.count() == 0:
                self.frame.ly.addWidget(self.table)
            '''if self.frame.ly.count() == 0:
                self.frame.ly.addWidget(self.frame.table)'''
            
            self.frame.frame.show()
            self.chart.hide()
            #print(frame)
            print('parent', self.parent())
       
        '''for key, value in self.data[key].items():
            print("adding series", str(key), value)
            slice_ = QPieSlice(str(key), value)
            self.series.append(slice_)
       
        self.chart.addSeries(self.series)
        self.series.doubleClicked.connect(self.handle_double_clicked)
             
          
    #Show the update chart with the distribution of the selected slice
    def handle_double_clicked(self, slice):
        slice.setExploded()
        slice.setLabelVisible()
     
        if slice.label() in self.data.keys():
            print("slice",slice.label());
            self.addSeries(slice.label())'''
           

