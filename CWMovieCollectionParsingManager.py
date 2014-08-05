#!/usr/bin/python

from amazonproduct import API
from CWMovieCollectionItem import CWMovieCollectionItem as MCItem
import sys
import urllib
import os.path

DEBUG = False

class CWMovieCollectionParsingManager:
	
	def __init__(self):
		self.api = API(locale='de')

	def InitAmazonApi(self, ean):
		self.root = self.api.item_lookup(ItemId=ean, IdType='EAN', SearchIndex='All', ResponseGroup='Large').Items.Item

	def Parse(self, ean):		
		self.InitAmazonApi(ean)

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
		#MCItem.Summary = self.GetSummary()
		MCItem.languages = self.GetLanguage()
		MCItem.subtitles = self.GetSubtitles()
		MCItem.audioFormat = self.GetAudioFormat()
		MCItem.plublicationDate = self.GetPublicationDate()
		MCItem.runningTime = self.GetRunningTime()

		return MCItem

	def GetRunningTime(self):
		runningTime = ''
		try:
			runningTime = self.root.ItemAttributes.RunningTime
		except:
			if DEBUG == True:
				print 'Error parsing runningtime'
				print sys.exc_info()
		return runningTime
	
	def GetPublicationDate(self):
		publicationDate = ''
		try:
			publicationDate = self.root.ItemAttributes.PublicationDate
		except:
			if DEBUG == True:
				print 'Error parsing publicationdate'
				print sys.exc_info()
		return publicationDate

	def GetAudioFormat(self):
		audioFormats = []
		try:
			for audioFormat in self.root.ItemAttributes.Languages.Language:
				try:
					audioFormats.append(audioFormat.AudioFormat)
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
			for subtitle in self.root.ItemAttributes.Languages.Language:
				if subtitle.Type == 'Subtitled':
					subtitles.append(subtitle.Name)
		except:
			if DEBUG == True:
				print 'Error parsing subtitle'
				print sys.exc_info()
		return subtitles

	def GetLanguage(self):
		languages = []
		try:
			for language in self.root.ItemAttributes.Languages.Language:
				if language.Type != 'Original':
					languages.append(language.Name)
		except:
			if DEBUG == True:
				print 'Error parsing language'
				print sys.exc_info()
		return languages

	def GetSummary(self):
		summary = ''
		try:
			summary = self.root.Offers.Offer.Promotions.Promotion.Summary
		except:
			if DEBUG == True:
				print 'Error parsing summary'
				print sys.exc_info()
		return summary

	def GetImageUrl(self, asin):
		imageUrl = ''
		try:
			imageUrl = self.root.LargeImage.URL
			if imageUrl != '' and os.path.isfile(asin + ".jpg") == False:
				urllib.urlretrieve(str(imageUrl), asin + ".jpg")
		except:
			if DEBUG == True:
				print 'Error parsing imageurl'
				print sys.exc_info()
		return imageUrl

	def GetAudienceRating(self):
		audienceRating = ''
		try:
			audienceRating = self.root.ItemAttributes.AudienceRating
		except:
			if DEBUG == True:
				print 'Error parsing audiencerating'
				print sys.exc_info()
		return audienceRating
	
	def GetStudio(self):
		studio = ''
		try:
			studio = self.root.ItemAttributes.Studio
		except:
			if DEBUG == True:
				print 'Error parsing studio: '
				print sys.exc_info()
		return studio

	def GetAsin(self):
		asin = ''
		try:
			asin = self.root.ASIN
		except:
			if DEBUG == True:
				print 'Error parsing asin: '
				print sys.exc_info()
		return asin

	def GetAmazonUrl(self):
		amazonUrl = ''
		try:
			amazonUrl = self.root.DetailPageURL
		except:
			if DEBUG == True:
				print 'Error parsing detailpageurl: '
				print sys.exc_info()
		return amazonUrl

	def GetPrice(self):
		price = ''
		try:
			price = self.root.Offers.Offer.OfferListing.Price.FormattedPrice
		except:
			if DEBUG == True:
				print 'Error parsing price: ' 
				print sys.exc_info()
		return price
	
	def GetTitle(self): 
		title = ''
		try:
			title = self.root.ItemAttributes.Title
		except:
			if DEBUG == True:
				print 'Error parsing title: ' 
				print sys.exc_info()
		return title

	def GetProductGroup(self): 
		productGroup = ''
		try:
			productGroup = self.root.ItemAttributes.ProductGroup
		except:
			if DEBUG == True:
				print 'Error parsing productgroup: ' 
				print sys.exc_info()
		return productGroup

	def GetManufacturer(self):
		manufacturer = ''
		try:
			manufacturer = self.root.ItemAttributes.Manufacturer
		except:
			if DEBUG == True:
				print 'Error parsing manufacturer: ' 
				print sys.exc_info()
		return manufacturer
		
	
	def GetDirectors(self):
		directors = []
		for director in self.root.ItemAttributes.Director:
			try:
				directors.append(director)
			except:
				if DEBUG == True:
					print 'Error parsing directors: ' 
					print sys.exc_info()		
		return directors
	
	def GetActors(self):
		actors = []
		for actor in self.root.ItemAttributes.Actor:
			try:
				actors.append(actor)
			except:
				if DEBUG == True:
					print 'Error parsing actors: '
					print sys.exc_info()
		return actors


