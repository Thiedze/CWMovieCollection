import sys

from PyQt4 import QtGui, QtCore

from CWMovieCollectionGUI import Ui_MainWindow
from CWMovieCollectionGUIManager import CWMovieCollectionGUIManager


class CWMovieCollectionGUI(QtGui.QMainWindow):

    def __init__(self):
        super(CWMovieCollectionGUI, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.guiManager = CWMovieCollectionGUIManager(self.ui)
        self.connectActions()
        self.show()
        
    def connectActions(self):
        QtCore.QObject.connect(self.ui.edEanNumber, QtCore.SIGNAL("returnPressed()"), self.guiManager.addEanNumber)
        QtCore.QObject.connect(self.ui.lvMovies, QtCore.SIGNAL("clicked(QModelIndex)"), self.guiManager.changeEntry)
    
        
def main():
    app = QtGui.QApplication(sys.argv)
    movieCollectionGUI = CWMovieCollectionGUI()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()