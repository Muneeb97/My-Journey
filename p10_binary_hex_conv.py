#convert numbers to binary and hex upto a certain number
print('decimal to binary/hex converter')
num1 = int(input('To which number shall values be converted: '))
lst_b = []
lst_h = []
for i in range(1,num1+1):
    #print(i,'  ',bin(i))
    lst_b.append(bin(i))
for i in range(1,num1+1):
    #print(i,'  ',hex(i))
    lst_h.append(hex(i))
r1 = int(input('what decimal value would you like to start: '))
r2 = int(input('what decimal value would you like to end: '))

for i in range(r1,r2+1):
    print(i,' ',lst_b[i-1],' ',lst_h[i-1])