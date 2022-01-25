def pattern(arg):
    for x in range(arg):
        print((str(arg)+' ') *arg)
# pattern(3)
def pattern_w(arg):
    i=0
    while i< arg:
        print((str(arg)+' ')*arg)
        i+=1
pattern_w(5)