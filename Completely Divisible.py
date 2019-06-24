# Write a Python program to check whether a number is completely divisible by another number. Accept two integer values form the user
# Program Console Sample Output 1:
# Enter numerator: 4
# Enter Denominator: 2
# Number 4 is Completely divisible by 2
# Program Console Sample Output 2:
# Enter numerator: 7

# Enter Denominator: 4
# Number 7 is not Completely divisible by 4

# Getting input from user

num_1 = int(input('Your first Number : '))
num_2 = int(input('Your Second Number : '))

# Coding by using def function

def function(num_1,num_2):
	if num_1 % num_2 == 0:
		print(f'{num_1} is completely divisible by {num_2}')
	elif num_1 % num_2 != 0:
		print(f'{num_1} is not completely divisible by {num_2}')
	else:
		print('Check Your Input number')

function(num_1,num_2)



