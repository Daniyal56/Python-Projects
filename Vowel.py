## 7. Vowel Tester
### Write a Python program to test whether a passed letter is a vowel or not
#### Program Console Output 1:
##### Enter a character: A
###### Letter A is Vowel
#### Program Console Output 2:
##### Enter a character: e
###### Letter e is Vowel
#### Program Console Output 2:
##### Enter a character: N
###### Letter N is not Vowel

print('Get to Know about Vowels')

# Getting user input
alpha = str(input('Enter Alphabets : ').lower())

#Now check vowels by using if condition

if (alpha=='a' or alpha=='e' or alpha=='i' or alpha=='o' or alpha=='u'):
	print(f' Letter {alpha} is Vowel')
else:
	print(f'Letter {alpha} is not Vowel')


