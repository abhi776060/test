def func(arg,*args):
    total_sum=arg
    new=0
    for x in args:
        new=x
    for y in new:
        total_sum+=y
    print(total_sum)
func(1,(5,6,8,9))
