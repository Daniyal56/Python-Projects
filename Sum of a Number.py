## 14. Digits Sum of a Number
### Write a Python program to calculate the sum of the digits in an integer
#### Program Console Sample 1:
##### Enter a number: 15
###### Sum of 1 + 5 is 6
#### Program Console Sample 2:
##### Enter a number: 1234
###### Sum of 1 + 2 + 3 + 4 is 10

print('=========================================== Digits Sum Of Number =========================================== ')

#getting user input

user_input = (input('Enter Number : '))

sum_of_number = 0

for i in user_input:
	sum_of_number += int(i)
	
print(f'Sum Of Number {user_input} is {sum_of_number}')