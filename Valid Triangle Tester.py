'''
Yang Hwi Kim
Sep.28, 2017
CSCI-UA 2-002(6162)
'''
#explain what the program is about
print('Valid Triangle Tester')

#ask the points in the grid
x1= float(input('Enter point #1 - x position: '))
y1= float(input('Enter point #1 - y postion: '))
x2= float(input('Enter point #2 - x position: '))
y2= float(input('Enter point #2 - y postion: '))
x3= float(input('Enter point #3 - x position: '))
y3= float(input('Enter point #3 - y postion: '))

#make a variable to figure out the length of three sides
side1=((x1-x2)**2+(y1-y2)**2)**0.5
side2=((x1-x3)**2+(y1-y3)**2)**0.5
side3=((x2-x3)**2+(y2-y3)**2)**0.5


#show the length of the sides in two decimal places
print('The length of each side of your test shape is: ')

print('side 1:', format(side1, '.2f'))
print('side 2:', format(side2, '.2f'))
print('side 3:', format(side3, '.2f'))

#figure out if it is not a valid triangle
if format(side1+side2, '.2f') < format(side3, '.2f'):
      print('This is not a valid triangle')
elif format(side1+side3, '.2f') < format(side2, '.2f'):
      print('This is not a valid triangle')
elif format(side3+side2, '.2f') < format(side1, '.2f'):
      print('This is not a valid triangle')
else:
    print('This is a valid triangle')

#Figure out if it is equilateral, isosceles or scalene triangles
if format(side1, '.2f')==format(side2, '.2f')==format(side3, '.2f'):
    print('This is an equilateral triangle!')
elif format(side1, '.2f')==format(side2, '.2f') or format(side1, '.2f')==format(side3, '.2f') or format(side2, '.2f')==format(side3, '.2f'):
    print('This is an isosceles triangle!')
else:
    print('This is scalene triangle!')

