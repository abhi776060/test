'''
                d
            c       c
        b       b       b
    a       a       a       a
'''

def pattern(arg):
    for x in range(arg):
      print((' ')*(arg-x) +(' ' +chr(64+arg-x))*(x+1))
# pattern(4)


def pattern_w(arg):
    i=0
    while i< arg:
        print(((' ')*(arg-i))+((' '+chr(64+arg-i))*(i+1)))
        i+=1
pattern_w(4)

