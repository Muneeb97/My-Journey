import cmath
print('Quadratic equation solver ax^2 + bx + c')

def quad_solve():
    a = int(input('Give a: '))
    b = int(input('Give b: '))
    c = int(input('Give c: '))

    #b*2 minus 4ac whole underoot
    b_c = (b**2) - (4*a*c)

    # minus b plus/minus b*2 minus 4ac whole underoot divided by 2
    sol1 = (- b + cmath.sqrt(b_c)) / (2*a)
    sol2 = (- b - cmath.sqrt(b_c)) / (2*a)
    print('\n')
    print('sol of quadratic equation: {}x^2 + {}x + {} is: '.format(a,b,c))
    print('Solution#1: ',sol1)
    print('Solution#2: ',sol2)
    print('\n')

count = int(input('Enter number of times you want to use quadratic solver: '))

for i in range(1,count+1):
    print('Solving Equation# {}'.format(i))
    quad_solve()