def fib(n):
    a=0
    b=1
    s=a+b
    print(a,b,end=" ")
    i=2
    while i<n:
        c=a+b
        s+=c
        print(c,end=" ")
        a=b
        b=c
        i+=1
    print(b)
fib(5)
