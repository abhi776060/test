#Computes the result of x raised to the power of n.
def exp(base,top):
    if top == 0:
        return 1
    else:
        return base * exp(base,top-1)
print(exp(2,2))

def fast_exp(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_exp(x*x, n/2)
    else:
        return x * fast_exp(x, n-1)
print(fast_exp(4,8))