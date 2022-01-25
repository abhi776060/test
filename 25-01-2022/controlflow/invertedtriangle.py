'''
A B C D
 A B C
  A B
   A  IF 4

'''
def pattern(arg):
    for x in range(arg):
        print(" "*x,end='')
        for y in range(arg-x):
            print((chr(65+y)),end=' ')
        print()

# pattern(4)

def pattern_w(arg):
    i=0
    while i <arg:
        print(' '*i,end='')
        j=0
        while j<arg-i:
            print(chr(65+j),end=' ')
            j+=1
        print()
        i+=1
pattern_w(5)