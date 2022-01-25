'''
                                              *
                                            * *    if 3
                                          * * *
                                            * *
                                              * 
'''

def pattern(arg):
    for x in range(arg):
        print('  '*(arg-x-1)+' *'*(x+1))
    for x in range(arg-1):
        print('  '*(x+1),end=' ')
        print('* '*(arg-1-x))
# pattern(15)

def pattern_w(arg):
    i=0
    while i< arg:
        print('  '*(arg-i-1)+' *'*(i+1))
        i+=1
    i=0
    while i< arg-1:
        print('  '*(i+1)+' *'*(arg-i-1))
        i+=1
pattern_w(50)