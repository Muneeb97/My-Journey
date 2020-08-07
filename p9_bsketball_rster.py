#enter name of five players for positions and injure one on random and replace with another
import random

def data_input():
    p1 = input('Enter Point Guard: ')
    p2 = input('Enter Shooting Guard: ')
    p3 = input('Enter Small Forward: ')
    p4 = input('Enter Power Forward: ')
    p5 = input('Center: ')

    lst_pst = ['Point Guard','Shooting Guard','Small Forward','Power Forward','Center']
    nme_lst = [p1,p2,p3,p4,p5]
    return(lst_pst,nme_lst)

def current_team(lst_pst,nme_lst): 
    print('Your starting {} are: '.format(len(lst_pst)))
    for i in range(len(lst_pst)):
        print('{}: '.format(lst_pst[i]),nme_lst[i])
    print('\n')

def remove_injured(lst_pst,nme_lst):
    to_rmve = random.randint(0,4)
    rmve = nme_lst[to_rmve]
    print('Oh no! Your {}, {} is injured!'.format(lst_pst[to_rmve],rmve))
    rmve_index = nme_lst.index(rmve)
    player_injured = nme_lst.pop(rmve_index)
    position_injured = lst_pst.pop(rmve_index)
    return(rmve_index,rmve,player_injured,position_injured)

def replace_injured(lst_pst,nme_lst,rmve_index,position_injured):
    print('Your team only has 4 players')
    add_player = input("Who will take {}'s position? ".format(rmve))
    nme_lst.insert(rmve_index,add_player)
    lst_pst.insert(rmve_index,position_injured)
    print('\n')
    return(add_player)

lst_pst,nme_lst = data_input()

current_team(lst_pst,nme_lst)

rmve_index,rmve,player_injured,position_injured =remove_injured(lst_pst,nme_lst)

current_team(lst_pst,nme_lst)

add_player = replace_injured(lst_pst,nme_lst,rmve_index,position_injured)

print('Good Luck to {}'.format(add_player))
print('\n')

current_team(lst_pst,nme_lst)




