def kaprekar(n):
    d = len(str(n))
    n_sqr = str(n*n)
    right = int(n_sqr[len(n_sqr)-d:])
    left = n_sqr[:len(n_sqr)-d]
    if left == '':
        left = 0
    left = int(left)
    #print("left:", left, "right:", right)
    return left+right == n
    
def kaprekarNumbers(p, q):
    a = []
    for i in range(p, q+1):
        if kaprekar(i):
            a.append(i)
    if len(a) == 0:
        return("INVALID RANGE")
    else:
        print(' '.join(str(c) for c in a))
kaprekarNumbers(1,100)