#!/usr/bin/python

from CWMovieCollectionRental import CWMovieCollectionRental

DEBUG = False

class CWMovieCollectionItem:

	def __init__(self):
		self.ean = ''
		self.actors = []
		self.directors = []
		self.manufacturer = ''
		self.productGroup = ''
		self.title = ''
		self.price = ''
		self.amazonUrl = ''
		self.asin = ''
		self.studio = ''
		self.audienceRating = ''
		self.imageUrl = ''
		self.summary = ''
		self.languages = []
		self.subtitles = []
		self.audioFormats = []
		self.publicationDate = ''
		self.rental = [CWMovieCollectionRental()]
		self.rating = None
