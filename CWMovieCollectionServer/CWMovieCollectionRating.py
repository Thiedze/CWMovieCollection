#!/usr/bin/python

from datetime import datetime
from CWMovieCollectionYoutube import CWMovieCollectionYoutube

DEBUG = False

class CWMovieCollectionRating:
	
	def __init__(self, title, ofdbStars):
		self.amazonStars = 0
		self.ofdbStars = ofdbStars
		self.myStars = 0
		self.hasSeen = False
		self.comment = ''
		self.trailerUrl = self.getTrailerUrl(title)
		self.addDate = datetime.now()

	def getTrailerUrl(self, title):
		Youtube = CWMovieCollectionYoutube()
		videoUrls = Youtube.search(title)

		if DEBUG == True:
			print videoUrls[0]

		return videoUrls[0]
