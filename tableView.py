from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import sys


data = {'India':['Trivandrum', 'New Delhi','Mumbai','Bangalore','Kochi'],
        'America':['Los Angeles','California','Arizona','New York', 'Boston'],
        'France':['Paris','Lyon','Marseille','Bordeaux', 'Nantes'],
        'Italy':['Milan','Rome','Genoa','Turin', 'Naples']}
 
 
class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        
    def setData(self): 
        colHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            colHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(colHeaders)
        


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        lay = QtWidgets.QHBoxLayout(widget)
        
        table = TableView(data, 5, 4)
        lay.addWidget(table)

        # create main layout
        widget.setLayout(lay)

 
 
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(500,400)
    w.show()
    sys.exit(app.exec_())
    
