'''
Created on Aug 28, 2014

@author: thiedze
'''
import urllib2

from PyQt4.Qt import QStandardItemModel, QStandardItem
import jsonpickle


HOST_IP = '127.0.0.1'
HOST_PORT = '5000'

class CWMovieCollectionGUIManager():
    

    def __init__(self, ui):
        self.ui = ui
        self.loadMovieCollection()
        
    def loadMovieCollection(self):
        json = urllib2.urlopen("http://" + HOST_IP + ":" + HOST_PORT + "/moviecollection").read()
        movieCollection = jsonpickle.decode(json)
        model = QStandardItemModel(self.ui.lvMovies)
        
        for movie in movieCollection:
            item = QStandardItem(movie['title'])
            item.setData(movie['ean'])
            model.appendRow(item)
        
        self.ui.lvMovies.setModel(model)       
        
    def addEanNumber(self):
        print(self.ui.edEanNumber.text())
        
    def changeEntry(self, index):
        print(index)