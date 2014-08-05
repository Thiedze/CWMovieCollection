#!/usr/bin/python

import pickle

DEBUG = True

FILENAME = 'MovieCollection.dat'

class CWMovieCollectionLoadSaveManager:

	def LoadMovieCollection(self):
		ListOfMCItems = []
		try:
			with open(FILENAME) as f:
				ListOfMCItems = pickle.load(f)
			return ListOfMCItems
		except:
			if DEBUG == True:
				print 'Error on loading movie collection'
				print sys.exc_info()

	def SaveMovieCollection(self, ListOfMCItems):
		try:
			with open(FILENAME, 'wb') as f:
				for item in ListOfMCItems:
					pickle.dump(item, f)
		except:
			if DEBUG == True:
				print 'Error on saving movie collection'	
				print sys.exc_info()
		
