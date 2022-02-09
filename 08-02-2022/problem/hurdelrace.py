def hurdlerace(k,height):
    max_value=max(height)
    if k<=max_value:
        max_value=max_value-k
        print(max_value)
    else:
        print(0)
# hurdlerace(1,[1,2,3,3,2])
# hurdlerace(4,[1,6,3,5,2])
hurdlerace(7,[2,5,4,5,2])