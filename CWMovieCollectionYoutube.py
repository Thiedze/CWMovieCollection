#!/usr/bin/python

from apiclient.discovery import build
from optparse import OptionParser

class CWMovieCollectionYoutube:
	
	def __init__(self):
		self.videoUrls = []
		self.youtube = build("youtube", "v3", developerKey="AIzaSyCLc7lOZcu7kUx85WbXR9MNKNhHKJ9GjDw")

	def search(self, serachTerm):
		parser = OptionParser()
		parser.add_option("--q", dest="q", help=serachTerm, default=serachTerm)
		parser.add_option("--max-results", dest="maxResults",
    help="Max results", default=10)
		(options, args) = parser.parse_args()
		
		searchResponse = self.youtube.search().list(q=options.q, part="id,snippet", maxResults=options.maxResults).execute()

		for searchResult in searchResponse.get("items", []):
			if searchResult["id"]["kind"] == "youtube#video":
				self.videoUrls.append('https://www.youtube.com/watch?v='+searchResult["id"]["videoId"])
		
