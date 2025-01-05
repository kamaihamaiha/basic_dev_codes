def city_country(city, country, population = 0):
	if population:
		return (city + ', ' + country).title() + ' - population=' + str(population)
	else:	
		return (city + ', ' + country).title()