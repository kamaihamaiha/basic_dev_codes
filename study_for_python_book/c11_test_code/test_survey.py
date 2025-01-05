import unittest

from Survey import AnoymousSurvey

class TestAnoymousSurvey(unittest.TestCase):

	def setUp(self):
		"""这个函数先运行，然后才会运行 test 开头的函数"""
		question = "what language did you first lean to speak?"
		self.my_survey = AnoymousSurvey(question)
		self.my_responses = ['English', 'Spanish', 'Mandarin']

	def test_store_sigle_response(self):
		"""测试单个答案是否被妥善存储"""
		
		self.my_survey.store_response('English')

		self.assertIn('English', self.my_survey.responses)


	def test_store_three_response(self):
		"""测试三个答案是否被妥善存储"""		
		for my_response in self.my_responses:
			self.my_survey.store_response(my_response)

		for my_response in self.my_responses:
			self.assertIn(my_response, self.my_survey.responses)	



unittest.main()		
