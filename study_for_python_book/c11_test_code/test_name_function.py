import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""测试 name_function.py"""

	def test_first_last_name(self):
		formatted_name = get_formatted_name('a', 'b')
		self.assertEqual(formatted_name, 'A B')

	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name('a', 'c', 'b')	
		self.assertEqual(formatted_name, 'A B C')	


unittest.main()		