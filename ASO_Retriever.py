import sys
from datetime import date, timedelta
import multiprocessing
import appLyzerParser as apiParser
import appLyzerAPI as appAPI
import playGoogleRetrieval
import appAnnieRetriever
import appAnnieListingChecker
import readFromCsvFile as reader
import itunesConnectRetriever as iConnect

start_date = (date.today()-timedelta(days=30)).isoformat() 
current_date = current_date = date.today().isoformat() 


def playGoogleAPI():
	goog = playGoogleRetrieval	
	
	url = "https://play.google.com/apps/publish/"


def appAnnie():
	#############################################
	# Retrieve from App Annie:
	#############################################
	#annieStart = appAnnieRetriever.appAnnieCrawler()
	#reader.readCompetitorsKeywords()

	#iOSListingChecker = 
	androidkeywordList = reader.androidKeywordReader('Listing keyword rankings - Android')
	#print androidkeywordList
	countries = {}
	

	for i in xrange(900):
		tempDict = appAnnieListingChecker.appAnnieCrawler(countries, androidkeywordList, 'Android')
		if 'United Kingdom' in countries.keys() and 'United States' in countries.keys():
			break
		else:		
			countries.update(tempDict)
		del tempDict
	print countries	


	#############################################
	#############################################
	# Retrieve from iTunes:
	#############################################
	#itunesStart = iConnect.iTunesConnectCrawler()





if __name__ == '__main__':
	
	#appAnnie()

	androidAppRatings = appAPI.appRank('Play', 'Android', 'com.fusionmedia.investing', start_date, current_date)
	apiParser.averageAppRankByCountryBy(androidAppRatings, 'Android Ratings By Country By Cat')

	iosAppRatings = appAPI.appRank('iOS', 'iPhone', '909998122', start_date, current_date)
	apiParser.averageAppRankByCountryBy(iosAppRatings, 'iOS Ratings By Country By Cat')

	#playGoogleAPI()


