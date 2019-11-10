count=input('N')
sum=0
for i in range(int(count)):
    if i % 3 == 0 or i % 5 ==0:
        sum += i

print(sum)

# another way to do this is :
# sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])