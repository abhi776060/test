'''
* * * 
* * 
*      if 3
'''
def pattern(arg):
    for x in range(arg):
        print((('*'+' ')*(arg-x)))
# pattern(5)

def pattern_w(arg):
    i=0
    while i<arg:
        print(('* ')*(arg-i))
        i+=1
pattern_w(5)