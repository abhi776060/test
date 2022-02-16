def extraLongFactorials(n):
    # Write your code here
    fact=1
    for x in range(1,n+1):
        fact*=x
    return fact
print(extraLongFactorials(25))