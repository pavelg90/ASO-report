import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def checkForCustomBaloon(driver):
	try:
		customBaloon = driver.find_element_by_xpath('//*[@id="walkme-balloon-3166601"]/div/div[1]/div[4]/div[2]/div/button/span')
		customBaloon.click()
	except:
		pass	

def waitUntilVisible(driver, xpath, name=False):
	counter = 0
	if not name:
		for loop in xrange(5):
			try:
				if not driver.find_element_by_xpath(xpath):
					time.sleep(3)
				elif driver.find_element_by_xpath(xpath):
					return True
					break
				else:
					False
				try:
					checkForCustomBaloon(driver)
				except:
					pass	
			except:
				try:
					if not driver.find_element_by_xpath(xpath):
						time.sleep(3)
					elif driver.find_element_by_xpath(xpath):
						return True
						break
					else:
						False
					try:
						checkForCustomBaloon(driver)
					except:
						pass	
				except:
					return False	
	else:
		for loop in xrange(5):
			try:
				if not driver.find_element_by_link_text(xpath):
					time.sleep(3)
				elif driver.find_element_by_link_text(xpath):
					return True
					break
				else:
					False
				try:
					checkForCustomBaloon(driver)
				except:
					pass	
			except:
				try:
					if not driver.find_element_by_link_text(xpath):
						time.sleep(3)
					elif driver.find_element_by_link_text(xpath):
						return True
						break
					else:
						False
					try:
						checkForCustomBaloon(driver)
					except:
						pass	
				except:
					return False						
	return False	

def parseFeaturedCollections(driver, file_name):
	time.sleep(2.5)
	try:	
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
		driver.execute_script("window.scrollTo(0, 0")
		time.sleep(2)
	except:
		try:
			driver.execute_script("window.scrollTo(0, 0")
			time.sleep(2)
		except:
			time.sleep(2)

	htmlSource = driver.page_source
	soup = BeautifulSoup(htmlSource,'html.parser')	

	waitUntilVisible(driver, '//*[@id="aa-app"]/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[3]/table/tbody/tr[1]/td/div/section/img')
	try:
		headings = [th.get_text() for th in soup.find("tr").find_all("th")]
	except:
		time.sleep(1.5)
		headings = [th.get_text() for th in soup.find("tr").find_all("th")]
	
	country = headings[1]
	device = headings[2]
	position = headings[5]
	featuredVisibility = headings[len(headings) - 1]
	headings = [country, device, position, featuredVisibility]
	
	dataset = []
	dataset.append(headings)

	for row in soup.find_all('tr'):
		countryName = " ".join([text.get_text() for text in row.find_all('td', {'class': 'country_flag_with_text'})]).strip().replace(',', '').encode('utf-8')
		deviceType = [text.get_text() for text in row.find_all('td', {'class': 'tbl-col-text'})]
		positionValue = " ".join([text.get_text() for text in row.find_all('span', {'class': ' '})]).strip().replace(',', '').encode('utf-8')
		featuredVisibilityValue = " ".join([text.get_text() for text in row.find_all('td', {'class': 'percentage-with-bar tbl-col-percentage-with-bar'})]).strip().replace(',', '').encode('utf-8')
		this_row = [countryName, deviceType, positionValue, featuredVisibilityValue]
		if countryName != '' and positionValue != '' and deviceType != '':
			this_row[1] = deviceType[0].strip().replace(',', '').encode('utf-8')

			if this_row not in dataset:
				dataset.append(this_row)
	writeToCsvFile.featuredCollectionsWriter(dataset, file_name)	

			



def parseTable(driver):	
	time.sleep(3)
	htmlSource = driver.page_source
	soup = BeautifulSoup(htmlSource,'html.parser')

	try:
		headings = [th.get_text() for th in soup.find("tr").find_all("th")]
	except:
		time.sleep(1.5)
		headings = [th.get_text() for th in soup.find("tr").find_all("th")]
	
	datasets = []
	datasets.append(headings)
	counter = 0
	for row in soup.find_all("tr"):
		rowNumber = " ".join([a.get_text().encode('utf-8').replace(chr(10), '') for a in row.find_all('span', {'class': ' '})])
		tempdatasets = []
		for td in row.find_all("td"):
			if counter > 0:
				appName = " ".join([a.get_text().encode('utf-8').replace(chr(10), '') for a in td.find_all('a', {'class': 'app-link'})])
				companyName = " ".join([a.get_text().encode('utf-8').replace(chr(10), '') for a in td.find_all('a', {'class': 'company-link'})])
				change = " ".join([a.get_text().encode('utf-8').replace(chr(10), '') for a in td.find_all('span', {'class': 'var change_same'})])
				if appName != '' and companyName != '':
					tempdatasets.append([appName, companyName, change])
			counter += 1
		if tempdatasets != []:
			tempdatasets.insert(0, rowNumber)
			datasets.append(tempdatasets)
	return datasets

def parseKeywords(driver):
	time.sleep(4)
	countriesName = []
	returnDict = {}


	waitUntilVisible(driver, '//*[@id="aa-app"]/div/div[1]/div/div[2]/a[1]')
	openCountriesMenue = driver.find_element_by_xpath('//*[@id="aa-app"]/div/div[1]/div/div[2]/a[1]')
	
	try:
		openCountriesMenue.click()
	except:
		time.sleep(1.5)
		openCountriesMenue.click()

	time.sleep(3)	
	
	htmlSource = driver.page_source
	soup = BeautifulSoup(htmlSource,'html.parser')

	countriesFromMenue = soup.find('div', {'class': 'x-clear picker-option-box'})
	for countryLink in countriesFromMenue.find_all('a', {'class': 'ng-scope picker-option-button indicators-0'}):
		countriesName.append(countryLink.get_text().strip())

	openCountriesMenue.click()	

	counter = 0
	for country in countriesName:	
		time.sleep(3)
		waitUntilVisible(driver, '//*[@id="aa-app"]/div/div[1]/div/div[2]/a[1]')
		openCountriesMenue.click()
		waitUntilVisible(driver, country, name=True)
		argentinaLink = driver.find_element_by_link_text(country)
		argentinaLink.click()
		
		htmlSource = driver.page_source
		soup = BeautifulSoup(htmlSource,'html.parser')
		'''
		try:
			headings = [span.get_text() for span in soup.find("tr").find_all("span", {'class': 'column-header-container'})]
		except:
			time.sleep(2.5)
			headings = [span.get_text() for span in soup.find("tr").find_all("span", {'class': 'column-header-container'})]
		for a in headings:
			if a == '' or a == ' ':
				headings.remove(a)	

		headings = headings[0:3]	
		'''
		datasets = []

		#datasets.append(headings)    ###################

		for row in soup.find_all("tr"):
			if row.find('td', {'class': 'link2 tbl-col-link2'}):
				topKeywords = row.find('a')
				topKeywords = topKeywords.get_text().replace(',', '').encode('utf-8')
			if row.find('td', {'class': 'rank-num tbl-col-rank-with-change--rank '}):	
				ranking = row.find('span', {'class': 'number'})
				ranking = ranking.get_text().replace(',', '').encode('utf-8')
			if row.find('td', {'class': ' number tbl-col-number'}):	
				results = row.find('span', {'class': ' '})
				results = results.get_text().replace(',', '').encode('utf-8')

				datasets.append([topKeywords, ranking, results])
		returnDict[country] = datasets		
		time.sleep(1)
		print returnDict, '\n'
		if counter >= 2:
			break
		counter += 1
		
	return returnDict	
	
		



def parseRatings(driver):	
	time.sleep(3)
	htmlSource = driver.page_source
	soup = BeautifulSoup(htmlSource,'html.parser')

	headers = []
	currVers_rankings = []
	allVers_rankings = []

	try:
		for h3 in soup.find_all('h3', {'class': 'country-title'}):
			h3 = h3.get_text().encode('utf-8').replace(chr(10), '').replace('  ', '')
			updateIndex = h3.find('Update')
			h3 = h3[0:updateIndex]
			headers.append(h3)
	except:
		print "can't get_text()"

	for currVersion in soup.find_all('div', {'class': 'current-version rating-bars-wrapper'}):
		currentVersion = currVersion.find('div', {'class': 'rating-title'})
		currentVersion =  currentVersion.get_text()

		if currVersion.find('div', {'class': 'rating-number'}):
			rating = currVersion.find('div', {'class': 'rating-number'})
			rating = rating.get_text()

			raters = currVersion.find('div', {'class': 'rating-count'})
			raters = raters.get_text()
		else:
			rating = 'No Rating'
			raters = "No Raters"	
		currVers_rankings.append([currentVersion, rating, raters])
	
	for currVersion in soup.find_all('div', {'class': 'all-versions rating-bars-wrapper'}):	
		currentVersion = currVersion.find('div', {'class': 'rating-title'})
		currentVersion =  currentVersion.get_text()

		if currVersion.find('div', {'class': 'rating-number'}):
			rating = currVersion.find('div', {'class': 'rating-number'})
			rating = rating.get_text()

			raters = currVersion.find('div', {'class': 'rating-count'})
			raters = raters.get_text()
		else:
			rating = 'No Rating'
			raters = "No Raters"

		allVers_rankings.append([currentVersion, rating, raters])	
	
	ratingsByCountry = {}

	for row in xrange(len(headers)):
		ratingsByCountry[headers[row]] = [currVers_rankings[row], allVers_rankings[row]]
	print ratingsByCountry
	return ratingsByCountry	


def credentials_and_submit(driver):
	usernameText ="Lonny@investing.com"
	passwordText = "56tyghbn"

	driver.find_element_by_xpath('//*[@id="login-button"]/button').click()
	
	time.sleep(3)

	username = driver.find_element_by_xpath('//*[@id="email"]')
	password = driver.find_element_by_xpath('//*[@id="password"]')

	username.send_keys(usernameText)
	password.send_keys(passwordText)

	driver.find_element_by_xpath('//*[@id="submit"]').click()


#################################      Navigation    #############################################################
def navigateTo_TopCharts(driver):
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="sub-container-aside"]/nav/div/div/div[1]/div[4]/ul/li[4]/a/span').click()	

def selectStore(driver, store):
	apple = '//*[@id="aa-app"]/ul/li[1]/a'
	android = '//*[@id="aa-app"]/ul/li[4]/a'
	
	if store == "apple":
		driver.find_element_by_xpath(apple).click()
	else:	
		driver.find_element_by_xpath(android).click()
	time.sleep(3)	

def selectCategory(driver, platform):
	if platform == 'android':	
		time.sleep(2)
		category = driver.find_element_by_xpath('//*[@id="aa-app"]/div/div/div[1]/div[1]/div/div[2]/a[1]').click()
		time.sleep(1.5)
		subCategory = driver.find_element_by_xpath('//*[@id="aa-app"]/div/div/div[2]/div[1]/ul[1]/li[2]/a[2]').click()
		time.sleep(1.5)
		finance = driver.find_element_by_xpath('//*[@id="aa-app"]/div/div/div[2]/div[1]/ul[2]/li[13]/a').click()
	# iPhone:
	else:	
		time.sleep(2)
		category = driver.find_element_by_xpath('//*[@id="aa-app"]/div/div/div[1]/div[1]/div/div[3]/a[1]').click()
		time.sleep(1.5)
		finance = driver.find_element_by_xpath('//*[@id="aa-app"]/div/div/div[2]/div[1]/ul/li[7]/a').click()
	
################################# !      Navigation      ! ########################################################

def investing_iOSApp(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/ios/app/investingcom-stocks-forex/details/")


def investing_AndroidApp(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/google-play/app/20600001500856/details/")	

def goTo_iOSRatings(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/ios/app/investingcom-stocks-forex/ratings/?countries=AR,AU,AT,BE,BR,CA,CL,CN,CZ,DK,EG,FI,FR,DE,GR,HK,IN,ID,IE,IL,IT,JP,KW,MY,MX,NL,NZ,NO,PH,PL,PT,RU,SA,SG,ZA,KR,ES,SE,CH,TW,TH,TR,AE,GB,US,VN")

def goTo_iOSKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/ios/app/investingcom-stocks-forex/keywords/#countries=US&device=iphone&start_date=2017-01-04&end_date=2017-04-02")	

def goTo_AndroidKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/google-play/app/com.fusionmedia.investing/keywords/#countries=US&device=&start_date=2017-01-05&end_date=2017-04-03")


def goTo_BloombergAndroidKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/google-play/app/20600002105754/keywords/#countries=ES&device=&start_date=2017-01-09&end_date=2017-04-07")


def goTo_BloombergiOSKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/ios/app/bloomberg-business/keywords/#countries=ES&device=iphone&start_date=2017-01-09&end_date=2017-04-07")

def goTo_YahooiOSKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/ios/app/yahoo-finance-real-time-stocks/keywords/#countries=ES&device=iphone&start_date=2017-01-09&end_date=2017-04-08")

def goTo_YahooAndroidKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/google-play/app/com.yahoo.mobile.client.android.finance/keywords/#countries=ES&device=&start_date=2017-01-09&end_date=2017-04-08")

def	goTo_MarketWatchiOSKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/ios/app/336693422/keywords/#countries=ES&device=iphone&start_date=2017-01-09&end_date=2017-04-08")

def	goTo_MarketWatchAndroidKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/google-play/app/com.marketwatch/keywords/#countries=ES&device=&start_date=2017-01-09&end_date=2017-04-08")

def goTo_CNBCiOSKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/ios/app/cnbc-business-news-finance/keywords/#countries=ES&device=iphone&start_date=2017-01-09&end_date=2017-04-08")

def	goTo_CNBCAndroidKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/google-play/app/com.cnbc.client/keywords/#countries=ES&device=&start_date=2017-01-09&end_date=2017-04-08")

def goTo_MSNiOSKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/ios/app/msn-money/keywords/#countries=ES&device=iphone&start_date=2017-01-09&end_date=2017-04-08")

def	goTo_MSNAndroidKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/google-play/app/com.microsoft.amp.apps.bingfinance/keywords/#countries=ES&device=&start_date=2017-01-09&end_date=2017-04-08")

def goTo_iOSFeaturedCollections(driver):
	time.sleep(2)
	driver.get('https://www.appannie.com/apps/ios/app/investingcom-stocks-forex/featured/?account_id=164862&report=daily-features&country=ALL&chart_type=frequency&date=2017-04-17&category=all-categories%3Efinance&metrics=position,reach')
	time.sleep(3)
	openDevices = driver.find_element_by_xpath('//*[@id="aa-app"]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/a[1]')
	openDevices.click()
	time.sleep(0.5)
	openDevices = driver.find_element_by_xpath('//*[@id="sub-container"]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/ul/li[1]/a')
	openDevices.click()
	time.sleep(0.5)

def goTo_AndroidFeaturedCollections(driver):
	time.sleep(2)
	driver.get('https://www.appannie.com/apps/google-play/app/com.fusionmedia.investing/featured/?account_id=81676&report=daily-features&date=2017-04-18&country=ALL&metrics=position,reach&category=all-category%3Efinance')
	time.sleep(0.5)	

def appAnnieCrawler():
	url = "https://www.appannie.com/"

	driver = webdriver.Firefox()
	driver.get(url)
	
	credentials_and_submit(driver)

# ----------- Android Featured Collections ---------------- #
	goTo_AndroidFeaturedCollections(driver)
	androidFeaturedCollections = parseFeaturedCollections(driver, 'Android Featured Collections All Devices')
# !!!!!!!!!!! Android Featured Collections !!!!!!!!!!!!!!!! #


'''
# ----------- iOS Featured Collections ---------------- #
	goTo_iOSFeaturedCollections(driver)
	iosFeaturedCollections = parseFeaturedCollections(driver, 'iOS Featured Collections All Devices')
# !!!!!!!!!!! iOS Featured Collections !!!!!!!!!!!!!!!! #


# ----------- Ratings ---------------- #	
	goTo_iOSRatings(driver)
	iosRatingsByCountry = parseRatings(driver)
	writeToCsvFile.iOSRatingsWriter(iosRatingsByCountry, 'iOS Ratings by Country')
# !!!!!!!!!!!! Ratings !!!!!!!!!!!!!!!! #


# ----------- Leading Keywords to Investing.com ---------------- #
	goTo_iOSKeywords(driver)
	iOSKeywordsByCountry = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(iOSKeywordsByCountry, 'Leading Keywords investing iOS')

	goTo_AndroidKeywords(driver)
	androidKeywordsByCountry = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(androidKeywordsByCountry, 'Leading Keywords investing Android')
# !!!!!!!!!!!! Leading Keywords to Investing.com !!!!!!!!!!!!!!! #


# ----------- Leading Keywords to Bloomberg -------------------- #
	goTo_BloombergiOSKeywords(driver)
	bloombergKeyByCountryiOS = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(bloombergKeyByCountryiOS, 'Leading Keywords Bloomberg iOS')	

	goTo_BloombergAndroidKeywords(driver)
	bloombergKeyByCountryAndroid = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(bloombergKeyByCountryAndroid, 'Leading Keywords Bloomberg Android')
# !!!!!!!!!!!! Leading Keywords to Bloomberg !!!!!!!!!!!!!!!!!!!! #



# ----------- Leading Keywords to Yahoo Finance ----------------- #
	goTo_YahooiOSKeywords(driver)
	YahooKeyByCountryiOS = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(YahooKeyByCountryiOS, 'Leading Keywords Yahoo Finance iOS')	

	goTo_YahooAndroidKeywords(driver)
	YahooKeyByCountryAndroid = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(YahooKeyByCountryAndroid, 'Leading Keywords Yahoo Finance Android')
# !!!!!!!!!!!! Leading Keywords to Yahoo Finance !!!!!!!!!!!!!!!! #



# ----------- Leading Keywords to MarketWatch  ----------------- #
	goTo_MarketWatchiOSKeywords(driver)
	MarketWatchKeyByCountryiOS = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(MarketWatchKeyByCountryiOS, 'Leading Keywords MarketWatch iOS')	

	goTo_MarketWatchAndroidKeywords(driver)
	MarketWatchKeyByCountryAndroid = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(MarketWatchKeyByCountryAndroid, 'Leading Keywords MarketWatch Android')
# !!!!!!!!!!!! Leading Keywords to MarketWatch !!!!!!!!!!!!!!!!! #



# ----------- Leading Keywords to CNBC  ----------------- #
	goTo_CNBCiOSKeywords(driver)
	CNBCKeyByCountryiOS = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(CNBCKeyByCountryiOS, 'Leading Keywords CNBC iOS')	

	goTo_CNBCAndroidKeywords(driver)
	CNBCKeyByCountryAndroid = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(CNBCKeyByCountryAndroid, 'Leading Keywords CNBC Android')
# !!!!!!!!!!!! Lading Keywords to CNBC !!!!!!!!!!!!!!!!! #



# ----------- Leading Keywords to MSN Money ----------------- #
	goTo_MSNiOSKeywords(driver)
	MSNKeyByCountryiOS = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(MSNKeyByCountryiOS, 'Leading Keywords MSN iOS')	

	goTo_MSNAndroidKeywords(driver)
	MSNKeyByCountryAndroid = parseKeywords(driver)
	writeToCsvFile.leadingKeywordsWriter(MSNKeyByCountryAndroid, 'Leading Keywords MSN Android')
# !!!!!!!!!!!! Lading Keywords to MSN Money !!!!!!!!!!!!!!!!! #
'''


if __name__ == '__main__':
	pass