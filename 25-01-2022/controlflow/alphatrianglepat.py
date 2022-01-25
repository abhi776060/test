'''
A 
B B
C C C if 3
'''
def pattern(arg):
    for x in range(arg):
        print((chr(65+x)+' ')*(x+1))
# pattern(5)

def pattern_w(arg):
    i=0
    while i <arg:
        print((chr(65+i)+' ')*(1+i))
        i+=1
pattern_w(5)