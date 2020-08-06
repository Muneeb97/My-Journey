#enter two sides of a right triangle and get the hypotenuse and area
from math import sqrt
print('right triangle solver')
side1 = float(input('Enter the measurement of the first leg of the triangle : '))
side2 = float(input('Enter the measurement of the second leg of the triangle : '))

def calc(side1,side2):
    hyp = sqrt((side1**2) + (side2**2))
    area = (side1*side2)/2
    print('The hypotenuse of the triangle with given lengths of {} and {} is :'.format(side1,side2),hyp.__round__(3))
    print('The area of the triangle with given lengths of {} and {} is :'.format(side1,side2),area.__round__(2))

calc(side1,side2)