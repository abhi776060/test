'''
A
A B
A B C 
A B C D 
A B C D E
A B C D
A B C 
A B
A
'''
def pattern(arg):
    for x in range(arg):
        for y in range(x+1):
            print(chr(65+y),end=' ')
        print()
    for x in range(arg-1):
        for y in range(arg-x-1):
            print(chr(65+y),end=' ')
        print()
# pattern(5)


def pattern_w(arg):
    i=0
    while i<arg:
        j=0
        while j<i+1:
            print(chr(65+j),end=' ')
            j+=1
        print()
        i+=1
    i=0
    while i<arg-1:
        j=0
        while j<arg-i-1:
            print(chr(65+j),end=' ')
            j+=1
        print()
        i+=1
pattern_w(5)
