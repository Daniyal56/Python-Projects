#    Copy string n times
#    Write a Python program to get a string which is n (non-negative integer) copies of a given string.
#    Program Console Output:
#    Enter String: Hi
#    How many copies of String you need: 4
#    4 Copies of Hi are HiHiHiHi

greeting = str(input('Enter Variable : '))
no_of_times = int(input('Enter No. of times you need to print'))
print(greeting * no_of_times)