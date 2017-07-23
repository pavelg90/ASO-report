from datetime import datetime
import csv

currentTime = " " + str(datetime.now()).replace("-", "").replace(":", "").replace(".", "")


def leadingKeywordsWriter(write_this, file_name):
	global currentTime
	file_name = file_name + ' ' + currentTime
	header = ['Country', 'Top Keywords', 'Ranking', 'Results']

	with open(file_name + '.csv', 'ab') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
		writer.writerow(header)
		
		try:
			for key in write_this.keys():
				for row in write_this[key]:
					rowToWrite = [a.replace('"', '') for a in row]
					rowToWrite.insert(0, key)
					writer.writerow(rowToWrite)
		except:		
				print "\nSomething went wrong. Here's the last operation: "
				print write_this
		f.close()


def keywordsToCompNotInvesting(write_this, file_name):
	currentTime = " " + str(datetime.now()).replace("-", "").replace(":", "").replace(".", "")		
	
	file_name = file_name + ' ' + currentTime
	header = ['keywords', 'Importance']

	with open(file_name + '.csv', 'ab') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
		writer.writerow(header)
		
		try:
			for key in write_this.keys():
				
				rowToWrite = [key, write_this[key]]
				writer.writerow(rowToWrite)
		except:		
			print "\nSomething went wrong. Here's the last operation: "
			print write_this
		f.close()

def iOSRatingsWriter(write_this, file_name):
	currentTime = " " + str(datetime.now()).replace("-", "").replace(":", "").replace(".", "")			

	file_name = file_name + ' ' + currentTime
	header = ['Country Name', 'Current Ver Avg. Rating', 'Current Ver # of Raters', 'All Ver Avg. Rating', 'All Ver # of Raters',]

	with open(file_name + '.csv', 'ab') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
		writer.writerow(header)
		
		try:
			for country in write_this.keys():
				tempRow = []
				tempRow.append(country)
				for row in write_this[country]:
					average = row[1].replace(',', '')
					numOfRaters = row[2].replace(',', '')
					tempRow.append(average)	
					tempRow.append(numOfRaters)	
				
				writer.writerow(tempRow)
		except:		
			print "\nSomething went wrong. Here's the last operation: "
			print write_this
		f.close()

def featuredCollectionsWriter(write_this, file_name):
	currentTime = " " + str(datetime.now()).replace("-", "").replace(":", "").replace(".", "")			

	file_name = file_name + ' ' + currentTime

	with open(file_name + '.csv', 'ab') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
		try:
			for row in write_this:
				writer.writerow(row)
		except:		
			print "\nSomething went wrong. Here's the last operation: "
			print write_this
		f.close()

def crashReportWriter(write_this, file_name):
	currentTime = " " + str(datetime.now()).replace("-", "").replace(":", "").replace(".", "")			

	file_name = file_name + ' ' + currentTime
	header = ['App Version', 'Crashes']

	with open(file_name + '.csv', 'ab') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
		writer.writerow(header)
		
		try:
			for row in write_this:
				writer.writerow(row)
		except:		
			print "\nSomething went wrong. Here's the last operation: "
			print write_this
		f.close()

def rankingsByCountryByCategory(write_this, file_name):
	currentTime = " " + str(datetime.now()).replace("-", "").replace(":", "").replace(".", "")			
	file_name = file_name + ' ' + currentTime

	with open(file_name + '.csv', 'ab') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
		try:
			for row in write_this:
				writer.writerow(row)
		except:		
			print "\nSomething went wrong. Here's the last operation: "
			print write_this
			f.close()			


if __name__ == '__main__':
	pass	