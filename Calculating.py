## 9. Calculate Interest
### Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
#### Program Console Sample 1:
##### Please enter principal amount: 10000
###### Please Enter Rate of interest in %: 0.1
###### Enter number of years for investment: 5
###### After 5 years your principal amount 10000 over an interest rate of 0.1 % will be 16105.1

print('-------------------------------------Calculate Interest------------------------------------------')

# Getting Input from User

principal_amount = int(input('Enter your amount in PKR: '))
print('%s PKR' %principal_amount)
rate_of_interest = float(input('Enter the rate of interest : '))
print('%s PKR' %rate_of_interest)
years_for_investment = int(input('Enter number of years for investment : '))
print('%s years' %years_for_investment)
value = principal_amount * (1 + 10/100) ** years_for_investment

print(f'The value will be after 5 years is {value} PKR')
