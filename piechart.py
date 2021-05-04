from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        thisDict =  {
      "Protein": 4.2,
      "Fat": 15.6,
      "carbs": 23.8,
      "other": 56.4
   }
   
        self.thisDict =  {
      "Protein": {
      "carbs": 43.6,
      "other": 56.4
   },
      "Fat": {
      "calories": 43.6,
      "other": 56.4
   },
      "carbs": 23.8,
      "other": 56.4
   }
   
        self.setWindowTitle("DonutChart Example")
        self.setGeometry(100,100, 400,600)
        self.create_donutchart(thisDict)
        
        #self.labl = QLabel(self)
        #self.labl.setText('abc')
        
        #button = QPushButton('button', self)        
        #button.move(50,50)
        #button.clicked.connect(self.on_click)

        self.show()
       
    @pyqtSlot()
    def on_click(self):
        self.labl.setText('some text')
        self.labl.adjustSize()
        
       


    def create_donutchart(self, thisDict):

        series = QPieSeries()
        series.setHoleSize(0.35)
        
        for key, value in thisDict.items():
            series.append(key, value)
        
        
        '''series.append("Protein 4.2%", 4.2)
        series.append("Fat 15.6%", 15.6)
        series.append("Other 23.8%", 23.8);
        series.append("Carbs 56.4%", 56.4);'''

        slice = QPieSlice()
        #slice = series.append("Fat 15.6%", 15.6)
        

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
        

    def handle_double_clicked(self, slice):
        i=50
        #print(slice.label(), slice.value())
        slice.setExploded()
        slice.setLabelVisible()
        
        if slice.label() in self.thisDict:
            print(slice.label());
            #print(slice.series().label());
            self.create_donutchart(self.thisDict[slice.label()])
           
            i=i+1
            print(i);
        
       


App = QApplication(sys.argv)
app = QApplication([])
window = Window()
window.show()
sys.exit(App.exec_())


