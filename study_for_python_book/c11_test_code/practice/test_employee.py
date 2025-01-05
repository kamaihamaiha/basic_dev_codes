import unittest

from employee import Employee

class TestSalary(unittest.TestCase):

	def setUp(self):
		self.init_salary = 60000
		self.m_employee = Employee('Tim', self.init_salary)

	def test_give_default_rise(self):
		self.m_employee.give_rise()
		self.assertEqual(self.m_employee.annual_salary, self.init_salary + 5000)	

	def test_give_custom_rise(self):
		self.m_employee.give_rise(6000)		
		self.assertEqual(self.m_employee.annual_salary, self.init_salary + 6000)		


unittest.main()		