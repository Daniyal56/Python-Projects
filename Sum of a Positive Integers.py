## 13. Sum of n Positive Integers
### Write a python program to sum of the first n positive integers
#### Program Console Sample 1:
###### Enter value of n: 5
###### Sum of n Positive integers till 5 is 15



print('============================== Sum of Positive Integers ============================== ')

#Getting Input from user
number = int(input('Enter Your Number : '))

# Get it into Formulae
sum_of_integer = [(num / 2) * (2 + (num - 1))]

#Output
print(f'Sum of {number} is {sum_of_integer}')