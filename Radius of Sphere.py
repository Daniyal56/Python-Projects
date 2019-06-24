# Program Console Output:
# Enter Radius of Sphere: 1
# Volume of the Sphere with Radius 1 is 4.18

print('Check Radius of the Sphere')

# first we get the value of radius and pie
user_input = int(input('Radius of Circle > '))

# Now we have values of pie and radius now close in a formulae
Volume = (4/3)*(22/7)*(user_input*user_input*user_input)

print(f'Voulme of the sphere is {Volume} with the given radius{user_input}')
