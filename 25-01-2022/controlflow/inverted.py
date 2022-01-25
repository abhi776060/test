'''
1 2 3 4 5
1 2 3 4
1 2 3               
1 2
1
'''

def pattern(arg):
    for x in range(arg):
        for y in range(arg-x):
            print((y+1),end=' ')
        print()
pattern(5)

def pattern_w(arg):
    i=0
    while i<arg:
        j=0
        while j<arg-i:
            print(j+1,end=' ')
            j+=1
        print()
        i+=1
pattern_w(5)


