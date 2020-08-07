#return n terms of fibo series and calculate golden ration and check if equal to phi

num = int(input('Enter a number upto which print fibo series: '))
def fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo(n-1) + fibo(n-2))  

fibo_n = []

for i in range(num+1):  
    fibo_n.append(fibo(i))


fibo_n = fibo_n[1:]

golden = [0]

for i in range(len(fibo_n)-1):
    ratio = fibo_n[i+1]/fibo_n[i]
    golden.append(ratio.__round__(6))


for i in zip(fibo_n,golden):
    print(i)

if(golden[-1].__round__(3)==1.618):
    print('Golden Phi acheived (1.618)')