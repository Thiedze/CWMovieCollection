#!/usr/bin/python

from CWMovieCollectionLoadSaveManager import CWMovieCollectionLoadSaveManager
from CWMovieCollectionParsingManager import CWMovieCollectionParsingManager
from CWMovieCollectionYoutube import CWMovieCollectionYoutube

LoadSaveManager = CWMovieCollectionLoadSaveManager()
ParsingManager = CWMovieCollectionParsingManager()
Youtube = CWMovieCollectionYoutube()

Youtube.search('psy')

for url in Youtube.videoUrls:
	print url

MovieCollection = []

dvd = ParsingManager.Parse('4010232049841')
MovieCollection.append(dvd)

MovieCollection.append(dvd)

LoadSaveManager.SaveMovieCollection(MovieCollection)
#MovieCollection = LoadSaveManager.LoadMovieCollection()

'''for dvd in MovieCollection:
	print '============================================='
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
	print '============================================='
'''
#item = api.item_lookup(ItemId='', IdType='EAN', SearchIndex='All', ResponseGroup='Large').Items.Item

#ASIN = item.ASIN
#print ASIN

#for act in item.ItemAttributes.Actor:
#	try:
#		print act
#	except:
#		print 'Error'


#print item.LargeImage.URL

#print item.Offers.Offer.OfferListing.Price.FormattedPrice
