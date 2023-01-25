def showSubjectName():
	print('AI for robot system')
def showStudentYear():
	print('6310501755')
def calculator(result):
	print(result)
	
while(1):
	user_input = input()
	if user_input == 'subject':
		showSubjectName()
	elif user_input == 'year':
		showStudentYear()
	elif user_input == 'calc':
		user_input = input()
		if user_input == '+':
			user_input = int(input())
			a = user_input
			user_input = int(input())
			b = user_input
			result = a+b
			calculator(result)
		elif user_input == '-':
			user_input = int(input())
			a = user_input
			user_input = int(input())
			b = user_input
			result = a-b
			calculator(result)
		
			
			
		
