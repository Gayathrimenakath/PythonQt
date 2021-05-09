from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QApplication, QStackedWidget, QLabel
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import json

class Chart(QWidget):
    def __init__(self, chartKey, data, parent=None):
        super(Chart, self).__init__(parent)
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
            
        for key, value in self.data[key].items():
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
            self.addSeries(slice.label())
           

class HomeScreen(QtCore.QObject):
    def __init__(self, a, parent=None):
        super(HomeScreen, self).__init__(parent)
        self.centralwidget = QtWidgets.QWidget()
        #self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        #self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        #self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1 = QtWidgets.QLabel()
        self.label1.setText('Welcome to PyQt5 example')
        self.label1.setAutoFillBackground(True)
        self.label1.setFont(QtGui.QFont("Times", 20,weight=QtGui.QFont.Bold))
        self.label1.setAlignment(Qt.AlignCenter)
        
        #self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3 = QtWidgets.QLabel()
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
        #self.pushButton.clicked.connect(self.file_open)
        self.gridLayout2.addWidget(self.pushButton, 0, 2, 1, 1)
        
        self.gridLayout.addLayout(self.gridLayout2, 0, 0, 7, 2)
        self.gridLayout.addLayout(self.gridLayout1, 0, 0, 1, 2)
        #self.gridLayout.addLayout(self.gridLayout3, 4, 0, 2, 0)
        
        #MainWindow.setCentralWidget(self.centralwidget)
        
       
        #self.retranslateUi(MainWindow)
        #MainWindow.setWindowTitle( "MainWindow")
        self.label_2.setText("File Name")
        self.pushButton.setText( "Browse")
        
        
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
    
    
    def showChart(self):
        self.next_page()
        
            
    
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(514, 381)
        
        self.btn_Action = QtWidgets.QPushButton()
        self.btn_Action.setGeometry(QtCore.QRect(220, 200, 75, 23))
        self.btn_Action.setObjectName("btn_Action")
        self.gridLayout3 = QtWidgets.QGridLayout()
        self.gridLayout3.addWidget(self.btn_Action, 0, 3, 3, 3)
        #json_object = json.dumps(sampleData, indent = 4)  
        #print(json_object) 
        
        
        #self.btn_Action.setText(_translate("MainWindow", "View Chart"))
        self.btn_Action.setText("View Chart")
        
        
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.currentChanged.connect(self.set_button_state)
        self.btn_Action.clicked.connect(self.next_page)
        
        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)

        
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn_Action)
        #hbox.addWidget(self.next_button)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.stacked_widget)
        vbox.addLayout(hbox)
        
        h = HomeScreen(self)
        self.name  = None
        h.pushButton.clicked.connect(self.file_open)
        print('yes')
        self.insert_page(h.centralwidget)
        
        
        
        # create main layout
        widget.setLayout(vbox)

    #def retranslateUi(self, MainWindow):
       # _translate = QtCore.QCoreApplication.translate
        
    def file_open(self):
        print('called')
        name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', options=QtWidgets.QFileDialog.DontUseNativeDialog)
        file = open(name, 'r') 
        with file as json_file:
            text = json.load(json_file)
            #text = file.read()
            #self.lineEdit.setText(name)
            #print(text)
            chart = Chart('Alloys', text, self)
            self.insert_page(chart.chartview)
        
        
        
    def set_button_state(self, index):
        #self.prev_button.setEnabled(index > 0)
        n_pages = len(self.stacked_widget)
        self.btn_Action.setEnabled( index % n_pages < n_pages - 1)
        
        
    def insert_page(self, widget, index=-1):
        self.stacked_widget.insertWidget(index, widget)
        self.set_button_state(self.stacked_widget.currentIndex())
        

    def next_page(self):
        new_index = self.stacked_widget.currentIndex()+1
        if new_index < len(self.stacked_widget):
            self.stacked_widget.setCurrentIndex(new_index)
    


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(400,300)
    w.show()
    sys.exit(app.exec_())
