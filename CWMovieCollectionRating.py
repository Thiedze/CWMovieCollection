#!/usr/bin/python

from datetime import datetime

DEBUG = False

class CWMovieCollectionRating:
	
	def __init__(self):
		self.amazonStars = 0
		self.ofdbStars = 0
		self.myStars = 0
		self.hasSeen = False
		self.comment = ''
		self.trailerUrl = ''
		self.addDate = datetime.now()
