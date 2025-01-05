import unittest

from city_functions import city_country

class CityTestCase(unittest.TestCase):

	def test_city_country(self):
		format_city = city_country('Tokyo', 'Japan')
		self.assertEqual(format_city, 'Tokyo, Japan')

	def test_city_country_population(self):
		format_city_population = city_country('santiago', 'chile', 5000000)
		self.assertEqual(format_city_population, 'Santiago, Chile - population=5000000')	

unittest.main()