import time
import re
import writeToCsvFile as writer
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



def parseCrashTable(driver):
	
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
	
	dataset = [['', ''], ['', ''], ['', ''], ['', ''], [u'3.4.1 (iOS)', u'   3.4.1 (iOS)  57,335  '], [u'3.4 (iOS)', u'   3.4 (iOS)  13,471  '], [u'3.3.3 (iOS)', u'   3.3.3 (iOS)  3,952  '], [u'3.2.5 (iOS)', u'   3.2.5 (iOS)  1,870  '], [u'2.6.1 (iOS)', u'   2.6.1 (iOS)  895  '], [u'2.7.5 (iOS)', u'   2.7.5 (iOS)  868  '], [u'3.3 (iOS)', u'   3.3 (iOS)  498  '], [u'2.7.1 (iOS)', u'   2.7.1 (iOS)  464  '], [u'2.8.2 (iOS)', u'   2.8.2 (iOS)  228  '], [u'3.2 (iOS)', u'   3.2 (iOS)  223  '], [u'3.0 (iOS)', u'   3.0 (iOS)  170  '], [u'3.1.0 (iOS)', u'   3.1.0 (iOS)  140  '], [u'2.1 (iOS)', u'   2.1 (iOS)  139  '], [u'2.5 (iOS)', u'   2.5 (iOS)  131  '], [u'3.3.2 (iOS)', u'   3.3.2 (iOS)  97  '], [u'2.9.1 (iOS)', u'   2.9.1 (iOS)  55  '], [u'2.8.1 (iOS)', u'   2.8.1 (iOS)  51  '], [u'2.3 (iOS)', u'   2.3 (iOS)  47  '], [u'2.8 (iOS)', u'   2.8 (iOS)  14  '], [u'2.9 (iOS)', u'   2.9 (iOS)  13  '], [u'2.9.2 (iOS)', u'   2.9.2 (iOS)  13  '], [u'2.4 (iOS)', u'   2.4 (iOS)  4  '], [u'2.0.1 (iOS)', u'   2.0.1 (iOS)  2  '], [u'1.0 (iOS)', u'   1.0 (iOS)  0  '], [u'1.0.1 (iOS)', u'   1.0.1 (iOS)  0  '], [u'1.1.0 (iOS)', u'   1.1.0 (iOS)  0  '], [u'1.2.0 (iOS)', u'   1.2.0 (iOS)  0  '], [u'1.3.0 (iOS)', u'   1.3.0 (iOS)  0  '], [u'1.3.1 (iOS)', u'   1.3.1 (iOS)  0  '], [u'1.4.0 (iOS)', u'   1.4.0 (iOS)  0  '], [u'1.4.1 (iOS)', u'   1.4.1 (iOS)  0  '], [u'1.5 (iOS)', u'   1.5 (iOS)  0  '], [u'1.5.1 (iOS)', u'   1.5.1 (iOS)  0  '], [u'1.6 (iOS)', u'   1.6 (iOS)  0  '], [u'1.6.1 (iOS)', u'   1.6.1 (iOS)  0  '], [u'2.0 (iOS)', u'   2.0 (iOS)  0  '], [u'2.1.1 (iOS)', u'   2.1.1 (iOS)  0  '], [u'2.1.2 (iOS)', u'   2.1.2 (iOS)  0  '], [u'2.2 (iOS)', u'   2.2 (iOS)  0  '], [u'2.6 (iOS)', u'   2.6 (iOS)  0  '], [u'2.7 (iOS)', u'   2.7 (iOS)  0  ']]
	
	for row in soup.find_all('tr'):
		appVersion = " ".join([text.get_text() for text in row.find_all('td', {'class': 'ng-scope ng-binding linkable'})])
		crashes = " ".join([text.get_text() for text in row.find_all('td', {'class': 'ng-scope'})])
		this_row = [appVersion, crashes]
		dataset.append(this_row)
	
	tempDataset = []
	for row in dataset:
		tempRow = []
		for item in row:
			item = item.replace('(iOS)', '').replace(',', '')
			if item != '':
				tempRow.append(item)
		if tempRow != []:
			tempDataset.append(tempRow)
	
	for row in tempDataset:
		version = row[0]
		crashes = row[1].replace(version, '').strip().replace(' ', '')
		tempDataset[tempDataset.index(row)] = [version, crashes]


	writer.crashReportWriter(tempDataset, 'iOS Crashes')	
	





def frame_switch(driver, xpath):
	driver.switch_to.frame(driver.find_element_by_xpath(xpath))

def waitUntilVisible(driver, xpath):
	for loop in xrange(50):
		try:
			if driver.find_element_by_xpath(xpath):
				return True
		except:
			time.sleep(0.2)			

def credentials_and_submit(driver):
	usernameText = "apps@investing.com"
	passwordText = "Tihj7X9b#"
	
	time.sleep(3)
	driver.refresh()
	time.sleep(2)
	waitUntilVisible(driver, '//*[@id="appleId"]')

	frame_switch(driver, '//*[@id="aid-auth-widget-iFrame"]')

	username = driver.find_element_by_xpath('//*[@id="appleId"]')
	password = driver.find_element_by_xpath('//*[@id="pwd"]')

	username.send_keys(usernameText)
	password.send_keys(passwordText)

	time.sleep(1.5)
	driver.find_element_by_xpath('//*[@id="sign-in"]').click()

def goToCrashesByVersion(driver):
	time.sleep(3)
	url = 'https://analytics.itunes.apple.com/#/metrics?interval=r&datesel=d30&zoom=day&measure=crashes&type=line&app=909998122&view_by=3'
	driver.get(url)
	checkUrl = driver.current_url
	for counter in xrange(5):
		if checkUrl != url:
			driver.get(url)
			time.sleep(1.5)
		else:
			break	
	time.sleep(1.5)


def iTunesConnectCrawler():
	url = 'https://analytics.itunes.apple.com/#/overview?interval=r&datesel=d30&pmeasure=units&tmeasure=units&app=909998122'
	
	driver = webdriver.Firefox()
	driver.get(url)

	credentials_and_submit(driver)
	goToCrashesByVersion(driver)
	parseCrashTable(driver)












if __name__ == '__main__':
	pass