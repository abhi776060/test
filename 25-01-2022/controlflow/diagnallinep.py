'''
                *
            *       *
        *               *
    *                       *

'''

def pattern(arg):
    for x in range(arg):
        if x ==0:
            print(" "*(arg)+"    *")
        print(" "*(arg-x+1)+'  *'+' '*(2*x+1)+' *')
# pattern(15)

def pattern(arg):
    i=0
    while i<arg:
        if i == 0:
            print(' '*(arg)+'   *')
        print(' '*(arg-i+1)+' *'+' '*(2*i+1)+' *')
        i+=1
pattern(10)