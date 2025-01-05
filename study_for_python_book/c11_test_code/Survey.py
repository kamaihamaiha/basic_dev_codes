class AnoymousSurvey():
	"""收集匿名调查问卷的答案"""
	def __init__(self, question):
		self.question = question
		self.responses = []

	def show_question(self):
		print(self.question)


	def store_response(self, response):
		self.responses.append(response)

	def show_results(self):
		"""显示收集到的所有答案"""
		print("Survey results:")
		for response in self.responses:
			print('- ' + response)				