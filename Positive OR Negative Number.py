# Write a Python program to check if a number is positive, negative or zero
# Program Console Sample Output 1:
# Enter Number: -1
# Negative Number Entered
# Program Console Sample Output 2:
# Integer: 3
# Positive Number Entered
# Program Console Sample Output 3:
# Integer: 0
# Zero Entered


user_input = int(input("Enter your number to check it's positive OR negative : "))

def function(user_input):
	if user_input > 0:
		print(f'Your number {user_input} is Positive Number')
	elif user_input < 0:
		print(f'Your number {user_input} Negative Number')
	else:
		print(f'You entered {user_input}')

function(user_input)
