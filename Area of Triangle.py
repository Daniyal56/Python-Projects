## 8. Triangle area
### Write a Python program that will accept the base and height of a triangle and compute the area


print('Area of a Triangle')

# Getting User Input

base = float(input('Base : '))
print('%s cm' %base)
  
height = float(input('Height : '))
print('%s cm' %height)

 # Now getting into Formulae
Area = (base * height) / 2

 #Output

print(f'Area {Area} cm with base {base} cm & Height {height}cm ')