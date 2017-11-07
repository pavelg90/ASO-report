import time
import sys
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def investing_iOSApp(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/ios/app/investingcom-stocks-forex/details/")

def investing_AndroidApp(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/google-play/app/20600001500856/details/")	

def goTo_iOSKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/ios/app/investingcom-stocks-forex/keywords/#countries=US&device=iphone&start_date=2017-01-04&end_date=2017-04-02")	

def goTo_AndroidKeywords(driver):
	time.sleep(2)
	driver.get("https://www.appannie.com/apps/google-play/app/com.fusionmedia.investing/keywords/#countries=US&device=&start_date=2017-01-05&end_date=2017-04-03")	

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

def credentials_and_submit(driver):
	usernameText ="***************"
	passwordText = "*************"

	driver.find_element_by_xpath('//*[@id="login-button"]/button').click()
	
	time.sleep(3)

	username = driver.find_element_by_xpath('//*[@id="email"]')
	password = driver.find_element_by_xpath('//*[@id="password"]')

	username.send_keys(usernameText)
	password.send_keys(passwordText)

	driver.find_element_by_xpath('//*[@id="submit"]').click()

def checkForCustomBaloon(driver):
	try:
		customBaloon = driver.find_element_by_xpath('//*[@id="walkme-balloon-3166601"]/div/div[1]/div[4]/div[2]/div/button/span')
		customBaloon.click()
	except:
		pass

def parseKeywords(driver, keywords, platform, countries):

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
		if country not in countries and country == 'United Kingdom' or country == 'United States':	
			time.sleep(3)
			waitUntilVisible(driver, '//*[@id="aa-app"]/div/div[1]/div/div[2]/a[1]')
			openCountriesMenue.click()
			waitUntilVisible(driver, country, name=True)
			countryLink = driver.find_element_by_link_text(country)
			countryLink.click()
			time.sleep(1)
			
			for i in xrange(5):
				#try:
				print keywords
				for keyword in keywords:
					time.sleep(0.3)
					addnewKeywords = driver.find_element_by_xpath('//*[@id="aa-app"]/div/div[2]/div/div[2]/div[2]/div/form/span[1]/input')
					time.sleep(0.3)
					addnewKeywords.clear()
					addnewKeywords.send_keys(keyword)
					time.sleep(0.3)
					addnewKeywords = driver.find_element_by_xpath('//*[@id="aa-app"]/div/div[2]/div/div[2]/div[2]/div/form/span[1]/button')
					addnewKeywords.click()
					time.sleep(0.3)
				break
				#except:
#					time.sleep(0.2)			

			time.sleep(1)


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
	###################################################################
	###################################################################
	###################################################################
	###################################################################
			datasets = []
			for row in soup.find_all("tr"):
				try:	
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
				except:
					pass

			returnDict[country] = datasets		
			time.sleep(1)
			break

	return returnDict		

###################################################################
###################################################################
###################################################################
###################################################################				



def appAnnieCrawler(countries, keywords, platform):
	tempdict = {}
	if countries != {}:
		for country in countries:

			url = "https://www.appannie.com/"

			driver = webdriver.Firefox()
			driver.get(url)
			credentials_and_submit(driver)
			
			if platform == 'Android':
				goTo_AndroidKeywords(driver)
				keywordsDict = parseKeywords(driver, keywords, platform, countries)
				tempdict.update(keywordsDict)
			else:
				goTo_iOSKeywords(driver)	
			driver.delete_all_cookies()
			driver.quit()			
	else:
		url = "https://www.appannie.com/"
		driver = webdriver.Firefox()
		driver.get(url)
		credentials_and_submit(driver)
		
		if platform == 'Android':
			goTo_AndroidKeywords(driver)
			keywordsDict = parseKeywords(driver, keywords, platform, countries)
			tempdict.update(keywordsDict)
		else:
			goTo_iOSKeywords(driver)	
		driver.delete_all_cookies()	
		driver.quit()	
		
	

	return tempdict	
	

if __name__ == '__main__':
	pass
