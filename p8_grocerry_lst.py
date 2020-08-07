import datetime
tme = datetime.datetime.now() 
print('Grocerry list')
print('Current date and time: ','{}/{}'.format(tme.month,tme.day),'   ','{}:{}'.format(tme.hour,tme.minute))
print('\n')
lst = ['Meat','Cheese']

print('You can only have five items in the list\n')
print('You currently have {} in the list'.format(lst))
item1 = input('Enter an item : ')
item2 = input('Enter another item : ')
item3 = input('Enter one more item : ')

def lst_add(i1,i2,i3):
    lst.append(i1)
    lst.append(i2)
    lst.append(i3)

lst_add(item1,item2,item3)

print('Current List has {} items'.format(len(lst)))
print(lst)
print('\n')

buyed1 = input('What did just you buy ? ')

def bought(buyed,lst):
    lst.pop(lst.index(buyed))

bought(buyed1,lst)
print('Current List has {} items'.format(len(lst)))
print(lst)
print('\n')

buyed2 = input('What more did just you buy ? ')
bought(buyed1,lst)
print('Current List has {} items'.format(len(lst)))
print(lst)
print('\n')

buyed3 = input('What else did just you buy ? ')
bought(buyed1,lst)
print('Current List has {} items'.format(len(lst)))
print(lst)
print('\n')

print('Sorry, the store is out of meat.')
item4 = input('What would you like to buy instead of meat ? ')
lst_add(item4)

print('Current List has {} items'.format(len(lst)))
print(lst)