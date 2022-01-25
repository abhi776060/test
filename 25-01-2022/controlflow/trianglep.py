'''
                        1
                    2       2
                3       3       3
            4       4       4       4

'''
def pattern(arg):
    for x in range(arg):
        print((' '*(arg-x))+(str(x+1)+' ')*(x+1))
pattern(25)

def pattern_w(arg):
    i=0
    while i<arg:
        print(('  '*(arg-i))+((str(i+1)+' ')*(i+1)))
        i+=1
# pattern_w(15)