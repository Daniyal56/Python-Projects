## 6. Check if number is Even or Odd
### Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
#### Program Console Output 1:
##### Enter Number: 4
###### 4 is Even
#### Program Console Output 2:
##### Enter Number: 9
###### 9 is Odd

print('Check Even OR Odd Number')

# getting input from user
num = int(input('Your Number : '))

# Check number by using if condition
if num % 2 == 0:
	print(f'{num} is Even Number')
else:
	print(f'{num} is Odd Number')