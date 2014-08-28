#!/usr/bin/python

from apiclient.discovery import build
from optparse import OptionParser
import ConfigParser

class CWMovieCollectionYoutube:

	def __init__(self):
		Config = ConfigParser.ConfigParser()
		Config.read("MovieCollection.ini")
		self.youtube = build("youtube", "v3", developerKey=Config.get("Youtube" ,"developerKey"))

	def search(self, searchTerm):
		searchTerm = searchTerm + 'trailer hd'
		parser = OptionParser()
		parser.add_option("--q", dest="q", help=searchTerm, default=searchTerm)
		parser.add_option("--max-results", dest="maxResults",
    help="Max results", default=10)
		(options, args) = parser.parse_args()
		
		searchResponse = self.youtube.search().list(q=options.q, part="id,snippet", maxResults=options.maxResults).execute()
		
		videoUrls = []

		for searchResult in searchResponse.get("items", []):
			if searchResult["id"]["kind"] == "youtube#video":
				videoUrls.append('https://www.youtube.com/watch?v='+searchResult["id"]["videoId"])
		return videoUrls

		
