''''
1111
2222
3333
4444

'''
def pattern(arg):
    for x in range(arg):
        print((str(x+1)+' ')*arg)
# pattern(5)

def pattren_w(arg):
    i=0
    while i< arg:
        print((str(i+1)+' ')*arg)
        i+=1
pattren_w(5)
