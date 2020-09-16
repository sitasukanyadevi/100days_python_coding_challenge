import math
def prime(n):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        return n
def primesum(n):
    if(prime(n) and prime(n-2)):
        return(n-2,2)
n=int(input('enter a value'))
print(primesum(n))
