import os
import csv
import glob
import writeToCsvFile as writer

#############################################################
path = 'C:\Users\pavelgo\Desktop\Python Projects\ASO Report'#
os.chdir(path)												#
files = [i for i in glob.glob('*.{}'.format('csv'))]		#
#############################################################

competitors = ['Bloomberg', 'Yahoo', 'Marketwatch', 'CNBC', 'MSN']

duplicates_iOS = {}
duplicates_Android = {}

excludeKeywords_iOS = []
excludeKeywords_Android = []

def readCompetitorsKeywords():
	for file in files:
		if 'investing' in file and 'iOS' in file:
			with open(file, 'rb') as f:
				reader = csv.reader(f)
				reader.next()	
				for row in reader:
					country = row[0]
					keyword = row[1]
					ranking = row[2]
					results = row[3]	
					excludeKeywords_iOS.append(keyword)	

	for competitor in competitors:	
		for file in files:				
			if competitor in file and 'iOS' in file:
					with open(file, 'rb') as f:
						reader = csv.reader(f)
						reader.next()
						for row in reader:
							country = row[0]
							keyword = row[1]
							ranking = row[2]
							results = row[3]
							if keyword not in excludeKeywords_iOS:	
								if keyword in duplicates_iOS.keys():
									duplicates_iOS[keyword] += 1
								else:	 
									duplicates_iOS[keyword] = 1	
	for key in duplicates_iOS.keys():
		if duplicates_iOS[key] < 3:
			del duplicates_iOS[key]	
			
	print "iOS:\n", duplicates_iOS
	writer.keywordsToCompNotInvesting(duplicates_iOS, 'iOS to competitors excluding investing')			
########################### Android Section ##########################			
	for file in files:
		if 'investing' in file and 'Android' in file:
			with open(file, 'rb') as f:
				reader = csv.reader(f)
				reader.next()	
				for row in reader:
					keyword = row[1]	
					excludeKeywords_Android.append(keyword)	

	for competitor in competitors:	
		for file in files:				
			if competitor in file and 'Android' in file:
					with open(file, 'rb') as f:
						reader = csv.reader(f)
						reader.next()
						for row in reader:
							country = row[0]
							keyword = row[1]

							if keyword not in excludeKeywords_Android:	
								if keyword in duplicates_Android.keys():
									duplicates_Android[keyword] += 1
								else:	 
									duplicates_Android[keyword] = 1	
	for key in duplicates_Android.keys():
		if duplicates_Android[key] < 3:
			del duplicates_Android[key]											

	print "Android:\n", duplicates_Android	
	writer.keywordsToCompNotInvesting(duplicates_Android, 'Android to competitors excluding investing')					



def androidKeywordReader(file_name):
	thisList = []
	file_name = file_name + '.csv'
	
	with open(file_name, 'rb') as f:
		reader = csv.reader(f)
		reader.next()	
		for row in reader:
			try:
				row = ' '.join(row).strip().replace(',', '').encode('utf-8')
				if row not in thisList:
					thisList.append(row)
			except:	
				pass
			
	return thisList		


if __name__ == '__main__':
	pass