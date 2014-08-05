#!/usr/bin/python

from CWMovieCollectionItem import CWMovieCollectionItem
from CWMovieCollectionRating import CWMovieCollectionRating
from CWMovieCollectionRental import CWMovieCollectionRental

import sys
import urllib
import os.path
import xml.etree.ElementTree as ET
import urllib

from amazonproduct import API

DEBUG = False

class CWMovieCollectionParsingManager:
	
	def __init__(self):
		self.api = API(locale='de')

	def initAmazonApi(self, ean):
		self.amazon = self.api.item_lookup(ItemId=ean, IdType='EAN', SearchIndex='All', ResponseGroup='Large').Items.Item

	def initOfdbApi(self, ean):
		xmlUrl = 'http://ofdbgw.geeksphere.de/searchean/'+ean
		self.ofdb = ET.parse(urllib.urlopen(xmlUrl)).getroot()
		xmlUrl = 'http://ofdbgw.home-of-root.de/movie/'+self.ofdb.findall('resultat')[0].findall('eintrag')[0].findall('filmid')[0].text
		self.ofdb = ET.parse(urllib.urlopen(xmlUrl)).getroot()

	def Parse(self, ean):		
		self.initAmazonApi(ean)
		self.initOfdbApi(ean)

		MCItem = CWMovieCollectionItem()
		MCItem.ean = ean
		MCItem.actors = self.GetActors()
		MCItem.directors = self.GetDirectors()
		MCItem.manufacturer = self.GetManufacturer()
		MCItem.productGroup = self.GetProductGroup()
		MCItem.title = self.GetTitle()
		MCItem.price = self.GetPrice()
		MCItem.amazonUrl = self.GetAmazonUrl()
		MCItem.asin = self.GetAsin()
		MCItem.studio = self.GetStudio()
		MCItem.audienceRating = self.GetAudienceRating()
		MCItem.imageUrl = self.GetImageUrl(MCItem.asin)
		MCItem.summary = self.GetSummary()
		MCItem.languages = self.GetLanguage()
		MCItem.subtitles = self.GetSubtitles()
		MCItem.audioFormats = self.GetAudioFormat()
		MCItem.publicationDate = self.GetPublicationDate()
		MCItem.runningTime = self.GetRunningTime()
		MCItem.rating = CWMovieCollectionRating(MCItem.title,  self.GetOfdbStars())
		MCItem.rental.append(CWMovieCollectionRental())

		return MCItem

	def GetOfdbStars(self):
		ofdbStars = ''
		try:
			ofdbStars =  self.ofdb.findall('resultat')[0].findall('bewertung')[0].findall('note')[0].text
		except:
			if DEBUG == True:
				print 'Error parsing ofdbstars'
				print sys.exc_info()
		return ofdbStars

	def GetRunningTime(self):
		runningTime = ''
		try:
			runningTime = str(self.amazon.ItemAttributes.RunningTime)
		except:
			if DEBUG == True:
				print 'Error parsing runningtime'
				print sys.exc_info()
		return runningTime
	
	def GetPublicationDate(self):
		publicationDate = ''
		try:
			publicationDate = str(self.amazon.ItemAttributes.PublicationDate)
		except:
			if DEBUG == True:
				print 'Error parsing publicationdate'
				print sys.exc_info()
		return publicationDate

	def GetAudioFormat(self):
		audioFormats = []
		try:
			for audioFormat in self.amazon.ItemAttributes.Languages.Language:
				try:
					audioFormats.append(str(audioFormat.AudioFormat))
				except:
					if DEBUG == True:
						print 'No audio format found'
		except:
			if DEBUG == True:
				print 'Error parsing audioformat'
				print sys.exc_info()
		return audioFormats

	def GetSubtitles(self):
		subtitles = []
		try:
			for subtitle in self.amazon.ItemAttributes.Languages.Language:
				if subtitle.Type == 'Subtitled':
					subtitles.append(str(subtitle.Name))
		except:
			if DEBUG == True:
				print 'Error parsing subtitle'
				print sys.exc_info()
		return subtitles

	def GetLanguage(self):
		languages = []
		try:
			for language in self.amazon.ItemAttributes.Languages.Language:
				if language.Type != 'Original':
					languages.append(str(language.Name))
		except:
			if DEBUG == True:
				print 'Error parsing language'
				print sys.exc_info()
		return languages

	def GetSummary(self):
		summary = ''
		try:
			summary = self.ofdb.findall('resultat')[0].findall('beschreibung')[0].text
		except:
			if DEBUG == True:
				print 'Error parsing summary'
				print sys.exc_info()
		return summary

	def GetImageUrl(self, asin):
		imageUrl = ''
		try:
			imageUrl = str(self.amazon.LargeImage.URL)
			if imageUrl != '' and os.path.isfile(asin + ".jpg") == False:
				urllib.urlretrieve(imageUrl, asin + ".jpg")
		except:
			if DEBUG == True:
				print 'Error parsing imageurl'
				print sys.exc_info()
		return imageUrl

	def GetAudienceRating(self):
		audienceRating = ''
		try:
			audienceRating = str(self.amazon.ItemAttributes.AudienceRating)
		except:
			if DEBUG == True:
				print 'Error parsing audiencerating'
				print sys.exc_info()
		return audienceRating
	
	def GetStudio(self):
		studio = ''
		try:
			studio = str(self.amazon.ItemAttributes.Studio)
		except:
			if DEBUG == True:
				print 'Error parsing studio: '
				print sys.exc_info()
		return studio

	def GetAsin(self):
		asin = ''
		try:
			asin = str(self.amazon.ASIN)
		except:
			if DEBUG == True:
				print 'Error parsing asin: '
				print sys.exc_info()
		return asin

	def GetAmazonUrl(self):
		amazonUrl = ''
		try:
			amazonUrl = str(self.amazon.DetailPageURL)
		except:
			if DEBUG == True:
				print 'Error parsing detailpageurl: '
				print sys.exc_info()
		return amazonUrl

	def GetPrice(self):
		price = ''
		try:
			price = str(self.amazon.Offers.Offer.OfferListing.Price.FormattedPrice)
		except:
			if DEBUG == True:
				print 'Error parsing price: ' 
				print sys.exc_info()
		return price
	
	def GetTitle(self): 
		title = ''
		try:
			title = str(self.amazon.ItemAttributes.Title)
		except:
			if DEBUG == True:
				print 'Error parsing title: ' 
				print sys.exc_info()
		return title

	def GetProductGroup(self): 
		productGroup = ''
		try:
			productGroup = str(self.amazon.ItemAttributes.ProductGroup)
		except:
			if DEBUG == True:
				print 'Error parsing productgroup: ' 
				print sys.exc_info()
		return productGroup

	def GetManufacturer(self):
		manufacturer = ''
		try:
			manufacturer = str(self.amazon.ItemAttributes.Manufacturer)
		except:
			if DEBUG == True:
				print 'Error parsing manufacturer: ' 
				print sys.exc_info()
		return manufacturer
		
	
	def GetDirectors(self):
		directors = []
		for director in self.amazon.ItemAttributes.Director:
			try:
				directors.append(str(director))
			except:
				if DEBUG == True:
					print 'Error parsing directors: ' 
					print sys.exc_info()		
		return directors
	
	def GetActors(self):
		actors = []
		for actor in self.amazon.ItemAttributes.Actor:
			try:
				actors.append(str(actor))
			except:
				if DEBUG == True:
					print 'Error parsing actors: '
					print sys.exc_info()
		return actors


