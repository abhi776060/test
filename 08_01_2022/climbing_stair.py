'''
1-1
2-1+1  2
3- 1+1+1  1+2  2+1
4 1+1+1+1  1+1+2  1+2+1  2+1+1  2+2
5 1+1+1+1+1  1+2+1+1 1+2+2  2+1+1+1 2+2+1

'''


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def countWays(s):
    return fib(s + 1)

s = 5
print("Number of ways = ",)
print(countWays(s))
