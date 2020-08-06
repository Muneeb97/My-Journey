#multiplaction/exponent table
number = float(input('Enter a number you want the exponent/multiplication table of :'))

def mult(number):
    print('Multiplication Table')
    for i in range(1,10):
        mult = (number * i).__round__(2)
        print('{} * {} = '.format(number,i),mult)
    print('\n')

def expo(number):
    print('Exponential Table')
    for i in range(1,10):
        mult = (number ** i).__round__(2)
        print('{} ** {} = '.format(number,i),mult)
    print('\n')

mult(number)
expo(number)