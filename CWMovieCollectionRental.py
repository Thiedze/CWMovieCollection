#!/usr/bin/python

from datetime import datetime

DEBUG = False

class CWMovieCollectionRental:
	
	def __init__(self):
		self.hirer = ''
		self.borrowed = datetime.now()
		self.restitution = ''
