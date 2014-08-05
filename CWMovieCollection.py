#!/usr/bin/python

from flask import Flask, Response
import jsonpickle

from CWMovieCollectionLoadSaveManager import CWMovieCollectionLoadSaveManager
from CWMovieCollectionParsingManager import CWMovieCollectionParsingManager

DEBUG = False

'''
MovieCollection = []

dvd = ParsingManager.Parse('4010232049841')
MovieCollection.append(dvd)

#MovieCollection.append(dvd)

#LoadSaveManager.SaveMovieCollection(MovieCollection)
#MovieCollection = LoadSaveManager.LoadMovieCollection()

for dvd in MovieCollection:
	print '============================================='
	print dvd.rental[0].borrowed
	
	print dvd.title
	print dvd.price
	print dvd.directors
	print dvd.actors
	print dvd.productGroup
	print dvd.manufacturer
	print dvd.amazonUrl
	print dvd.asin
	print dvd.studio
	print dvd.audienceRating
	print dvd.imageUrl
	print dvd.summary
	print dvd.languages
	print dvd.subtitles
	print dvd.audioFormats
	print dvd.publicationDate
	print dvd.runningTime
	print '=============================================
'''

if DEBUG == True:
	print 'Start flask'

LoadSaveManager = CWMovieCollectionLoadSaveManager()
ParsingManager = CWMovieCollectionParsingManager()

app = Flask(__name__)

@app.route('/<ean>', methods=['GET', 'POST'])
def parse(ean):
	if request.method == 'GET':
		if DEBUG == True:
			print 'GET: ' + ean

		for dvd in MovieCollection:
			if dvd.ean == ean:
				resp = jsonpickle.encode(dvd)
				break
	
	elif request.method == 'POST':
		if DEBUG == True:
			print 'POST: ' + ean

		dvd = ParsingManager.Parse(ean)
		MovieCollection.append(dvd)
		resp = jsonpickle.encode(dvd)
	
	return resp

@app.route('/moviecollection', methods=['GET'])
def moviecollection():
	if DEBUG == True:
		print 'GET: moviecollection'

	return jsonpickle.encode(MovieCollection)


if __name__ == '__main__':
	if DEBUG == True:
		print 'Load Movie Collection'
	MovieCollection = LoadSaveManager.LoadMovieCollection()
	
	app.debug = DEBUG
	app.run()

	if DEBUG == True:
		print 'Save Movie Collection'
	LoadSaveManager.SaveMovieCollection(MovieCollection)


