import writeToCsvFile as writer


def averageAppRankByCountryBy(dictionary, file_name):
	categories = dictionary['response']['header']['categories']
	types_main = dictionary['response']['header']['types']
	countries = dictionary['response']['header']['stores']

	headers = ['Country']
	for k, v in categories.iteritems():
		for key in types_main.keys():
			headers.append(v + ' - ' + key)		

	tempDict = dictionary['response']['data']

	for a in tempDict.keys():
		tempDict[countries[a]] = tempDict.pop(a)
	
	for a in tempDict.keys():
		for b in tempDict[a].keys():
			tempDict[a][categories[b]] = tempDict[a].pop(b)
		
	calculatedDict = {}	
	tempList = []
		
	for country in tempDict.keys():
		for category in tempDict[country].keys():
			for types in tempDict[country][category].keys():
				rank = 0.0
				divider = 0.0
				write_this = {}
				for day in tempDict[country][category][types]:
					
					write_this['Country'] = country
					write_this['Category'] = category
					write_this['Type'] = types

					divider += 1
					rank += int(day['rank'])
				rank = rank / divider
				write_this['Avg. Rank'] = rank
				tempList.append(write_this)
	

	return_this = []
	countries_used = []
	return_this.append(headers)
	for a in tempList:
		
		country = a['Country']
		category = a['Category']
		types = a['Type']
		rank = str(round(a['Avg. Rank'], 2))
		colIndex = headers.index(category + ' - ' + types)
		line = []

		if country not in countries_used:
			line.append(country)
			for i in xrange(len(headers)):
				if i > 0:
					if i == colIndex:
						line.append(rank)
					else:
						line.append('')	
			countries_used.append(country)			
		elif country in countries_used:
			rowIndex = 0
			for i in return_this:
				if country in i:
					rowIndex = return_this.index(i)	
			return_this[rowIndex][colIndex] = rank				
		

		return_this.append(line)
	return_this = [x for x in return_this if x != []]	
	writer.rankingsByCountryByCategory(return_this, file_name)	





if __name__ == '__main__':
	pass