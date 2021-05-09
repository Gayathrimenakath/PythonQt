from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *


sampleData = {
  "Alloys":{
      "Aluminium":25,
      "Copper": 75
    },
    "Aluminium":{
      "Duralumin": 20,
      "Hydronalium":30,
      "Magnaliuim": 50,     
    },
    "Magnaliuim":{
      "aluminium":45,
      "magnesium": 55
    },
    "Duralumin":{
       "copper": 50,
       "aluminium":50
    },
    "Hydronalium":{
       "manganese": 1,
       "magnesium": 12,
       "aluminium": 87
    },
    "Copper":{
       "Beryllium copper": 30,
       "Billon": 45,
       "Copper–tungsten" :35
    },
    "Beryllium copper":{
       "Beryllium": 3,
       "copper":97
    },
    "Billon":{
       "gold": 13,
       "copper": 87
    },
    "Copper–tungsten":{
       "Tungsten": 40,
       "copper":60
    }
  }




class Chart(QWidget):
    def __init__(self, chartKey, parent=None):
        super(Chart, self).__init__(parent)
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
            
        for key, value in sampleData[key].items():
            print("adding series", str(key), value)
            slice_ = QPieSlice(str(key), value)
            self.series.append(slice_)
       
        self.chart.addSeries(self.series)
        self.series.doubleClicked.connect(self.handle_double_clicked)
             
        
          
    #Show the update chart with the distribution of the selected slice
    def handle_double_clicked(self, slice):
        slice.setExploded()
        slice.setLabelVisible()
     
        if slice.label() in sampleData.keys():
            print("slice",slice.label());
            self.addSeries(slice.label())
           
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        lay = QtWidgets.QHBoxLayout(widget)
        
        chart = Chart('Alloys', self)
        lay.addWidget(chart.chartview)

        # create main layout
        widget.setLayout(lay)
        
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(400,300)
    w.show()
    sys.exit(app.exec_())
    
