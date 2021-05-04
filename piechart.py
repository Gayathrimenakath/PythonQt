from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

sample = {
   "Alloys":{
      "aluminium":25,
      "Copper": 75
    },
    "aluminium":{
      "Duralumin": 20,
      "Hydronalium":30,
      "magnaliuim": 50,     
    },
    "magnaliuim":{
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

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("DonutChart Example")
        self.setGeometry(100,100, 400,600)
        self.create_donutchart('Alloys')
        self.show()
       
    @pyqtSlot()
    def on_click(self):
        self.labl.setText('some text')
        self.labl.adjustSize()
        

    def create_donutchart(self, chartKey):
        series = QPieSeries()
        series.setHoleSize(0.35)
        
        for key, value in sample[chartKey].items():
            series.append(key, value)
       

        slice = QPieSlice()
     
        chart = QChart()
        #chart.legend().hide()
        chart.addSeries(series)

	# for the background and title
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("DonutChart Example")
        chart.setTheme(QChart.ChartThemeBlueCerulean)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        
        # creating a widget object
        widget = QWidget()
        
        # Creating a grid layout
        layout = QGridLayout()
  
        # setting this layout to the widget
        widget.setLayout(layout)
  
        self.setCentralWidget(chartview)
        
        series.doubleClicked.connect(self.handle_double_clicked)
        
        
    #Show the update chart with the distribution of the selected slice
    def handle_double_clicked(self, slice):
        slice.setExploded()
        slice.setLabelVisible()
        
        if slice.label() in sample:
            #print(slice.series().label());
            self.create_donutchart(slice.label())
   


App = QApplication(sys.argv)
app = QApplication([])
window = Window()
window.show()
sys.exit(App.exec_())

