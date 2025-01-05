from Survey import AnoymousSurvey

# 定义一个问题
question = 'What language did you first lean to speak?'
my_survey = AnoymousSurvey(question)

# 显示问题
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)	

print("Thank you to everyone who participated in the survey!")
my_survey.show_results()
