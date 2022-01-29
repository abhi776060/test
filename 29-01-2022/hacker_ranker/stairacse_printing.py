def staircase(n):
    # Write your code here
    for x in range(n):
        print(' '*(n-1-x)+'#'*(x+1))
staircase(6)
