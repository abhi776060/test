'''
A A A
A A A if 3
A A A
'''
def pattern(arg):
    for x in range(arg):
        print((chr(65)+' ' )*arg)
# pattern(5)

def pattren_w(arg):
    i=0
    while i<arg:
        print((chr(65)+' ')*arg)
        i+=1
pattren_w(5)