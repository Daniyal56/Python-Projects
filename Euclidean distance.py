## 10. Euclidean distance
### write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
#### Program Console Sample 1:
###### Enter Co-ordinate for x1: 2
###### Enter Co-ordinate for x2: 4
###### Enter Co-ordinate for y1: 4
###### Enter Co-ordinate for y2: 4
###### Distance between points (2, 4) and (4, 4) is 2


print('-----------------------------------------Distance between two lines----------------------------------------------')

# getting input from user

x1 = int(input('Enter Co-ordinate for x1 : '))
print('%s cm' %x1)
x2 = int(input('Enter Co-ordinate for x2 : '))
print('%s cm' %x2)
y1 = int(input('Enter Co-ordinate for y1 : '))
print('%s cm' %y1)
y2 = int(input('Enter Co-ordinate for y2 : '))
print('%s cm' %y2)

#by putting in formulae

dis_1 = (x2 - x1)**2
dis_2 = (y2 - y1)**2

# Output

result = (dis_1 + dis_2) ** 1/2

print('distance between the points (x1, y1) and (x2, y2) is %s cm' %result) 