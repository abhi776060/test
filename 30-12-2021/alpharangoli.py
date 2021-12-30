def display(n):
    alpha=[chr(x) for x in range(97,97+n)]
    for x in range(n,0,-1):
        for y in range(x-1):
            print(" ",end=' ')
        for z in range(n-x+1):
            print(alpha[z],end=' ')
        for a in range((n-x)-1,-1,-1):
            print(alpha[a],end=' ')

        print()


display(26)