#simple shiiping order system
#takes the number of orders and prints the cost

username = input("Hello, What is your username? ")
print("Hello {}, Welcome back.".format(username))
print("These are the current shipping rates: ")

rates = [5.10,5.00,4.95,4.80]

def print_shp_rates(rates):
    print("To ship 0 to 100 items:          {}".format(rates[0]))
    print("To ship 100 to 500 items:        {}".format(rates[1]))
    print("To ship 500 to 1000 items:       {}".format(rates[2]))
    print("To ship over 100 items:          {}".format(rates[3]))

print_shp_rates(rates)

item_quant = int(input("How many items would you like to ship? "))

def print_cost(item_quant,rates):
    if(item_quant >0 and item_quant <= 100):
        print("To ship {} items, the total cost will be ${} at ${} per item".format(item_quant,(item_quant*rates[0]).__round__(2),rates[0]))
    elif(item_quant >100 and item_quant <= 500):
        print("To ship {} items, the total cost will be ${} at ${} per item".format(item_quant,(item_quant*rates[1]).__round__(2),rates[1]))
    elif(item_quant >500 and item_quant <= 1000):
        print("To ship {} items, the total cost will be ${} at ${} per item".format(item_quant,(item_quant*rates[2]).__round__(2),rates[2]))
    elif(item_quant >1000):
        print("To ship {} items, the total cost will be ${} at ${} per item".format(item_quant,(item_quant*rates[3]).__round__(2),rates[3]))
    else:
        print("Invalid Quantity.")
        
        

print_cost(item_quant,rates)