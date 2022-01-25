'''
                        *
                    *       *
                *       *       *
            *       *       *       *  if 4
                *       *       *
                    *       *
                        *

'''
def pattern(arg):
    for x in range(arg):
        print(" "*(arg-x)+"* "*(x+1))
    for x in range(arg-1):
        print(' '*(x+2) +'* '*(arg-x-1))
# pattern(4)


def pattern_w(arg):
    i=0
    while i< arg:
        print(' '*(arg-i)+'* '*(i+1))
        i+=1
    i=0
    while i<arg-1:
        print(' '*(i+1)+' *'*(arg-1-i))
        i+=1
pattern_w(15)