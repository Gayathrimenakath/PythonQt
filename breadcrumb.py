from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt


data = {"books":{
    "Science Fiction":{
      "Issac Asimov":{
        "1950":["The Caves of Steel", "The Naked Sun", "Pebble in the Sky", "The Stars, Like Dust"],
        "1980":["The Robots of Dawn", "Robots and Empire", "Prelude to Foundation", "Forward the Foundation"],
        "1990":["Robot Visions", "The Positronic Man"]
      },
      "Arthur C. Clarke":{
        "1950":["Islands in the Sky", "Prelude to Space", "The Sands of Mars", "The Deep Range"], 
        "1970":["Imperial Earth", "Rendezvous with Rama ", "The Fountains of Paradise"],
        "1980":["2010: Odyssey Two", "The Songs of Distant Earth", "2061: Odyssey Three", "The Sentinel "]
      }
    },
    "Romance":{
      "Jane Austen":{
        "1810":["Sense and Sensibility ", "Pride and Prejudice", "Mansfield Park", "Emma"],
      },
      "Nicholas Sparks":{
        "1990":["The Notebook", "Message In A Bottle", "A Walk To Remember"],
        "2000":["Dear John", "The Lucky One", "The Choice", "The Last Song"],
        "2010":["The Best Of Me", "Safe Haven", "The Longest Ride"]
     }
   },
   "Crime Fiction":{
      "Agatha christie":{
        "1920":["The Mysterious Affair at Styles", "The Murder of Roger Ackroyd", "The Mystery of the Blue Train", "The Man in the Brown Suit"],
        "1930":["Peril at End House", "Three Act Tragedy", "The A.B.C. Murders", "Murder on the Orient Express"],
        "1940":["One, Two, Buckle My Shoe", "Sparkling Cyanide", "Crooked House", "The Moving Finger "]
      },
      "Arthur Conan Doyle":{
        "1880":["A Physiologist's Wife", "A Midshipman's Story", "An Exciting Christmas Eve", "The Bravoes of Market Drayton"], 
        "1890":["The Adventure of the Gloria Scott", "The Adventure of the Cardboard Box", "The Adventure of the Musgrave Ritual", "The Adventure of the Final Problem"],
        "1900":["The Adventure of the Empty House", "The Adventure of the Norwood Builder", "The Adventure of Charles Augustus Milverton", "The Adventure of the Abbey Grange"]
      }
    }  
}}

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
        

    #make the listed items clickable
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_clicked(self, index):
        if not self.model.hasChildren(index):
            self.clicked.emit(index)
            return
        action = self.toolbar.addAction(index.data())
        action.setData(QtCore.QPersistentModelIndex(index))
        self.listview.setRootIndex(index)
        print(index.data())
        #Chart(index.data())
        
    #make the breadcrumbs clickable in order to go back and forth
    @QtCore.pyqtSlot(QtWidgets.QAction)
    def on_actionTriggered(self, action):
        ix = action.data()
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

        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        navigation = Navigation(data, self)
        navigation.clicked.connect(self.on_clicked)

        self.addToolBar(navigation.toolbar)

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        lay = QtWidgets.QHBoxLayout(widget)
        lay.addWidget(navigation.listview)
        
        

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_clicked(self, index):
        print(index.data())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
