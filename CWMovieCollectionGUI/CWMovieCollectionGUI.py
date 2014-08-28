# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CWMovieCollectionGUI.ui'
#
# Created: Thu Aug 28 22:41:34 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 768)
        MainWindow.setWindowTitle(_fromUtf8("Movie Collection"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.lvMovies = QtGui.QListView(self.centralWidget)
        self.lvMovies.setGeometry(QtCore.QRect(10, 40, 261, 661))
        self.lvMovies.setViewMode(QtGui.QListView.ListMode)
        self.lvMovies.setObjectName(_fromUtf8("lvMovies"))
        self.edEanNumber = QtGui.QLineEdit(self.centralWidget)
        self.edEanNumber.setGeometry(QtCore.QRect(10, 0, 261, 33))
        self.edEanNumber.setText(_fromUtf8("Enter EAN Number"))
        self.edEanNumber.setObjectName(_fromUtf8("edEanNumber"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(280, 0, 731, 701))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabDetail = QtGui.QWidget()
        self.tabDetail.setObjectName(_fromUtf8("tabDetail"))
        self.gvCover = QtGui.QGraphicsView(self.tabDetail)
        self.gvCover.setGeometry(QtCore.QRect(10, 10, 151, 181))
        self.gvCover.setFrameShape(QtGui.QFrame.StyledPanel)
        self.gvCover.setFrameShadow(QtGui.QFrame.Plain)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.gvCover.setForegroundBrush(brush)
        self.gvCover.setObjectName(_fromUtf8("gvCover"))
        self.tabWidget.addTab(self.tabDetail, _fromUtf8(""))
        self.tabRating = QtGui.QWidget()
        self.tabRating.setObjectName(_fromUtf8("tabRating"))
        self.tabWidget.addTab(self.tabRating, _fromUtf8(""))
        self.tabRental = QtGui.QWidget()
        self.tabRental.setObjectName(_fromUtf8("tabRental"))
        self.tabWidget.addTab(self.tabRental, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 27))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuCWMovieCollection = QtGui.QMenu(self.menuBar)
        self.menuCWMovieCollection.setTitle(_fromUtf8("Datei"))
        self.menuCWMovieCollection.setObjectName(_fromUtf8("menuCWMovieCollection"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setText(_fromUtf8("Exit"))
        self.actionExit.setIconText(_fromUtf8("Exit"))
        self.actionExit.setToolTip(_fromUtf8("Exit"))
        self.actionExit.setStatusTip(_fromUtf8(""))
        self.actionExit.setWhatsThis(_fromUtf8(""))
        self.actionExit.setShortcut(_fromUtf8("Ctrl+Q"))
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuCWMovieCollection.addSeparator()
        self.menuCWMovieCollection.addAction(self.actionExit)
        self.menuBar.addAction(self.menuCWMovieCollection.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDetail), _translate("MainWindow", "Detail", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRating), _translate("MainWindow", "Rating", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRental), _translate("MainWindow", "Rental", None))

