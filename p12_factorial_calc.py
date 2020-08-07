import math
print('Factorial Calc')
num = int(input('give number to finda factorial of: '))

print('The mathematical relationship of the factorial of {} is: '.format(num))
print('{}! = '.format(num),end="")

factorial = 1
fact_lst = []
for i in range(1,num + 1):
       factorial = factorial*i
       fact_lst.append(i)
       print(str(i)+' * ',end="")
print('\n')

print('Factorial calculated using math library=> ',end="")
print(math.factorial(num))

print('Factorial calculated using algorithm:=>',end="")
print(factorial)

if(math.factorial(num) == factorial):
    print('Both methods give the same answer!')

