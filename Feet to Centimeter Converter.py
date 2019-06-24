## 11. Feet to Centimeter Converter
### Write a Python program to convert height in feet to centimetres.
##### Program Console Sample 1:
###### Enter Height in Feet: 5
###### There are 152.4 Cm in 5 ft



# Getting input from User

Height = int(input(f'Enter height : ' ))
print('%s ft' %Height)

#Convert it ft to cm

user_Height = Height * 30.48

# Output
print(f'Your height is {Height} ft and {user_Height} Centimeter')


