import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


apiKey = 'f5573e4abc09f92b69b8969bca7e9fbf'

def connetcToAPI():
	global apiKey
	url = 'https://api.applyzer.com/key:' + apiKey + '/function:appinfo/appid:909998122'
	response = requests.get(url)
	return response.json()

def analysisTopPublishers(market, device, storeid, categoryid):
	#	market : ios/mac/play
	#	device : iphone/ipad/mac/appletv/android
	#	storeid : integer
	#	categoryid : integer
	# 	response: {"data": {"type (string)":{"seller", "count", "percentage"}}, "header":{"date":"SQL Date"}
	global apiKey
	url = 'https://api.applyzer.com/key:' + apiKey + '/function:analysistoppublishers/storeid:'+ storeid + '/categoryid:' + categoryid + '/market:' + market + '/device:' + device
	response = requests.get(url)	
	return response.json()

def appkeywordrank(market, device, appid, storeid, date):
	#	appid : string
	#	Market : iOS/Mac/Play
	#	Device : iPhone/iPad/Mac/AppleTV/Android
	#	Date : SQL YYYY-MM-DD
	#	storeid : integer
	# 	response: {"data": {"keyword":{"storeid":"rank"}}}
	global apiKey
	url = 'https://api.applyzer.com/key:' + apiKey + '/function:appkeywordrank/market:' + market + '/device:' + device + '/date:' + date + '/appid:' + appid + '/storeid:' + storeid
	response = requests.get(url)
	return response.json()

def appkeywordranktoday(market, device, appid):
	#	market : ios/mac/play
	#	device : iphone/ipad/mac/appletv/sticker/android
	#	appid : string
	#	storeid : integer
	#	keyword : string
	#	response: {"data": {"keyword":{"storeid":"rank"}}}
	global apiKey
	url = 'https://api.applyzer.com/key:' + apiKey + '/function:appkeywordranktoday/market:' + market + '/device:' + device + '/appid:' + appid
	response = requests.get(url)
	return response.json()

def appRank(market, device, appid, startDate, endDate):
	#	appid : string
	#	Market : iOS/Mac/Play
	#	Device : iPhone/iPad/Mac/AppleTV/Android/Sticker
	#	startDate : SQL YYYY-MM-DD
	#	endDate : SQL YYYY-MM-DD
	#	{"data": {"storeid":{"categoryid":{"type (string)":{"rank", "date"}}}}}
	global apiKey
	url = 'https://api.applyzer.com/key:' + apiKey + '/function:apprank/market:' + market + '/device:' + device + '/startdate:' + startDate + '/enddate:' + endDate + '/appid:' + appid
	response = requests.get(url)
	return response.json()

def categoryList(market):
	#	market : ios/mac/play
	#	{"data": {"id","name"}}
	global apiKey
	url = 'https://api.applyzer.com/key:' + apiKey + '/function:categorylist/market:' + market
	response = requests.get(url)
	return response.json()

def countryList(market):
	#	market : ios/mac/play
	#	{"data": {"id","name","play","code"}}
	global apiKey
	url = 'https://api.applyzer.com/key:' + apiKey + '/function:countrylist/market:' + market
	response = requests.get(url)
	return response.json()





if __name__ == '__main__':
	pass
