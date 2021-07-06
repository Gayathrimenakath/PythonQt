from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QApplication, QStackedWidget, QLabel, QGroupBox
import sys
import sip
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from tableView import TableView


data = {'India':['Trivandrum', 'New Delhi','Mumbai','Bangalore','Kochi'],
        'America':['Los Angeles','California','Arizona','New York', 'Boston'],
        'France':['Paris','Lyon','Marseille','Bordeaux', 'Nantes'],
        'Italy':['Milan','Rome','Genoa','Turin', 'Naples']}


sample = {
  "Alloys":{
    "Aluminium":{
        "Magnaliuim":["magnesium", "aluminium"],
        "Hydronalium":["magnesium", "manganese", "aluminium"],
        "Duralumin":["copper", "aluminium"]
       },
    "Copper":{
         "Beryllium copper":["Beryllium", "copper"],
   	 "Billon":["gold", "copper"],
         "Copper tungsten":["Tungsten","copper"],
     }
}}


sampleData = {
    "Alloys": {
        "Aluminium": 25,
        "Copper": 75
    },
    "Aluminium": {
        "Duralumin": 20,
        "Hydronalium": 30,
        "Magnaliuim": 50
    },
    "Magnaliuim": {
        "aluminium": 45,
        "magnesium": 55
    },
    "Duralumin": {
        "copper": 50,
        "aluminium": 50
    },
    "Hydronalium": {
        "manganese": 1,
        "magnesium": 12,
        "aluminium": 87
    },
    "Copper": {
        "Beryllium copper": 30,
        "Billon": 45,
        "Copper tungsten": 35
    },
    "Beryllium copper": {
        "Beryllium": 3,
        "copper": 97
    },
    "Billon": {
        "gold": 13,
        "copper": 87
    },
    "Copper tungsten": {
        "Tungsten": 40,
        "copper": 60
    }
}


class Chart(QtWidgets.QWidget):
    def __init__(self,chartKey, frame, parent=None):
        super(Chart, self).__init__(parent, QtCore.Qt.Window)  
        self.frame = frame
        self.create_chart(chartKey)
        
        
    @QtCore.pyqtSlot()
    def create_chart(self, chartKey):
        self.series = QPieSeries()
        self.series.setHoleSize(0.35)
        self.chart = QChart()
        
        print('inside chart',self.frame)
        
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
        print(self.series)
        self.series.setHoleSize(0.35)
        print('chart',key)
        
        if len(sampleData[key]) == 2:
            for key, value in sampleData[key].items():
                #print("adding series", str(key), value)
                slice_ = QPieSlice(str(key), value)
                self.series.append(slice_)
       
            self.chart.addSeries(self.series)
            #self.frame.frame.hide()
            
            #self.frame.frame.removeWidget(self.table)
            
            self.frame.frame.hide()
            self.chart.show()
        else:
            print('hi')
            
            self.table = TableView(data, 5, 4)
            
            
            if self.frame.ly.count() == 0:
                self.frame.ly.addWidget(self.table)
            
            self.frame.frame.show()
            self.chart.hide()
            #print(frame)
            print('parent', self.parent())
            
        
        


def dict_to_model(item, d):
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
    clicked = QtCore.pyqtSignal(QtCore.QModelIndex)
    def __init__(self, json_data, parent=None):
        super(Navigation, self).__init__(parent)
        self.toolbar = QtWidgets.QToolBar()
        self.toolbar.actionTriggered.connect(self.on_actionTriggered)     
        self.model =  QtGui.QStandardItemModel(self)
        dict_to_model(self.model.invisibleRootItem(), json_data)
        it = self.model.item(0, 0)
        ix = self.model.indexFromItem(it)
        root_action = self.toolbar.addAction(it.text())
        root_action.setData(QtCore.QPersistentModelIndex(ix))
        self.listview = QtWidgets.QListView()
        self.listview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listview.clicked.connect(self.on_clicked)
        self.listview.setModel(self.model)
        self.listview.setRootIndex(ix)
        self.a = 10
        
        
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        
        
        self.gridLayout.addWidget(self.listview, 0, 0, 2, 1)
        
        self.frame = QtWidgets.QFrame()
        self.chart = Chart('Alloys', self)
        
        
        
        self.ly = QtWidgets.QVBoxLayout()
        self.frame.setLayout(self.ly)
        
        #self.layout.addWidget(self.frame)
        #self.frame.hide()
        
        
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.addWidget(self.frame)
        
        self.gridLayout2 = QtWidgets.QGridLayout()
        self.gridLayout2.addWidget(self.chart.chartview)
        
        self.gridLayout.addLayout(self.gridLayout2, 0, 2, 0, 1)
        self.gridLayout.addLayout(self.gridLayout1, 0, 2, 0, 1)
        
        '''self.layout = QHBoxLayout()
        
        self.frame = QtWidgets.QFrame()
        
        self.layout.addWidget(self.listview)
        self.chart = Chart('Alloys', self.frame)
        self.layout.addWidget(self.chart.chartview)
       
        
        
        ly = QtWidgets.QVBoxLayout()
        self.frame.setLayout(ly)
        ly.addWidget(self.chart.table)
        
        self.layout.addWidget(self.frame)
        #self.frame.hide()'''
        
        self.horizontalGroupBox = QGroupBox()
        self.horizontalGroupBox.setLayout(self.gridLayout)

        

    #make the listed items clickable
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_clicked(self, index):
        print('aaaaaaaaaaaaaa', self.a)
        if not self.model.hasChildren(index):
            self.clicked.emit(index)
            return
        action = self.toolbar.addAction(index.data())
        action.setData(QtCore.QPersistentModelIndex(index))
        self.listview.setRootIndex(index)
        print(index.data())
        self.chart.addSeries(index.data())
        
        
    #make the breadcrumbs clickable in order to go back and forth
    @QtCore.pyqtSlot(QtWidgets.QAction)
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



class HomeScreen(QtCore.QObject):
    def __init__(self, a, parent=None):
        super(HomeScreen, self).__init__(parent)
        self.label1 = QLabel('Welcome to PyQt5 example')
        self.label1.setStyleSheet("border: 1px solid black;")
        self.label1.setAutoFillBackground(True)
        self.label1.setFont(QtGui.QFont("Times", 20,weight=QtGui.QFont.Bold))
        self.label1.setAlignment(Qt.AlignCenter)
       
       

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()
        self.stacked_widget.currentChanged.connect(self.set_button_state)
        self.next_button.clicked.connect(self.next_page)
        self.prev_button.clicked.connect(self.prev_page)


    def initUI(self):
        self.next_button = QPushButton('Next')
        self.prev_button = QPushButton('Previous')
        self.next_button.setEnabled(False)
        self.prev_button.setEnabled(False)
        self.stacked_widget = QStackedWidget()
        
        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.prev_button)
        hbox.addWidget(self.next_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.stacked_widget)
        vbox.addLayout(hbox)
        
        h = HomeScreen(self)
        self.insert_page(h.label1)
        
        navigation = Navigation(sample, self)
        self.insert_page(navigation.horizontalGroupBox)

        #add the toolbar to the main window
        self.toolbar = navigation.toolbar
        self.addToolBar(self.toolbar)
        
        #start with the toolbar hidden
        self.toolbar.toggleViewAction().setChecked(True)
        self.toolbar.toggleViewAction().trigger()
        
        # create main layout
        widget.setLayout(vbox)


    def set_button_state(self, index):
        self.prev_button.setEnabled(index > 0)
        n_pages = len(self.stacked_widget)
        self.next_button.setEnabled( index % n_pages < n_pages - 1)
        
        
    def insert_page(self, widget, index=-1):
        self.stacked_widget.insertWidget(index, widget)
        self.set_button_state(self.stacked_widget.currentIndex())
        

    def next_page(self):
        new_index = self.stacked_widget.currentIndex()+1
        if new_index < len(self.stacked_widget):
            self.stacked_widget.setCurrentIndex(new_index)
            self.toolbar.toggleViewAction().trigger()
            

    def prev_page(self):
        new_index = self.stacked_widget.currentIndex()-1
        if new_index >= 0:
            self.stacked_widget.setCurrentIndex(new_index)
            self.toolbar.toggleViewAction().trigger()
            

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(1000,800)
    w.show()
    sys.exit(app.exec_())
