def sum_of_digits(n):
    sum=0
    for i in range(1,n):
        rem=n%10
        sum+=rem
        n//=10
    return sum
n=int(input("enter a value:"))
print(sum_of_digits(n))



