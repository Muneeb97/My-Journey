#grade sorter and drop last 2

g1 = input('Enter first grade (0-100) : ')
g2 = input('Enter second grade (0-100) : ')
g3 = input('Enter third grade (0-100) : ')
g4 = input('Enter fourth grade (0-100) : ')
print('\n')

lst = [g1,g2,g3,g4]
lst_srted = sorted(lst,reverse=True)
print('Your grades are: ',lst)
print('\n')
print('Your sorted grades in descending order are: ',lst_srted)
print('\n')

print('The lowest two of your grades will be dropped')
print('Dropped Grade : ',lst_srted[-1])
print('Dropped Grade : ',lst_srted[-2])
lst_srted.pop(-1)
lst_srted.pop(-1)
print('\n')
print('Your remaining grades are: ',lst_srted)
print('\n')
print('Your highest grade is: ',lst_srted[0] )

