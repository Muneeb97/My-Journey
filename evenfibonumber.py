def fib():   # return sum of even terms of Fibonacci series till next term is less than 4 million
    count=0
    sum=0
    result = []
    a, b = 1,2
    #while count < n:
    while b < 4000000:

        result.append(a)
        a, b = b, a+b
        count += 1
        if a % 2 == 0:
            sum += a
       
    return sum #,result
    
print(fib())

#to get sum of even terms of fibo series upto n terms comment while b<4000000
#and uncomment other statements and add n as arguement of function and pass n, an integer to
#define number of terms





