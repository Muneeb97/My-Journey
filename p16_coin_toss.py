from secrets import randbelow

n_num = int(input("Enter the number of times you want to flip a coin: "))
toss_result_ht = []
toss_result_oz = []


#randomint
#0 is tails & 1 is heads
for i in range(n_num):
    one_zero = randbelow(2)
    if(one_zero == 0):
        #print("TAILS")
        toss_result_ht.append("tails")
        toss_result_oz.append(one_zero)
    else:
        #print("HEADS")
        toss_result_ht.append("heads")
        toss_result_oz.append(one_zero)
    if(toss_result_oz.count(0) == toss_result_oz.count(1)):
        print("equal at {} coin toss".format(i))



print("The Cummulative Result is: ")
print("SIDE         COUNTS          PERCENTAGE")
print("HEADS        {}/{}           {}%".format(toss_result_oz.count(1),n_num,(toss_result_oz.count(1)*100)/n_num))
print("TAILS        {}/{}           {}%".format(toss_result_oz.count(0),n_num,(toss_result_oz.count(0)*100)/n_num))


#print("The percentage of HEADS is: ",((toss_result_oz.count(1)*100)/n_num))
#print("The percentage of HEADS is: ",((toss_result_oz.count(0)*100)/n_num))
#print(toss_result_oz.count(0))
#print(toss_result_oz.count(1))




