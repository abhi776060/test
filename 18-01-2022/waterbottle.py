


def water(fill,empty):
    count=fill
    filled_list=['x' for x in range(count)]
    empty_list=[filled_list[x:x+empty] for x in range(0,len(filled_list),empty)]
    for x in empty_list:
        if len(x)== empty:
            count+=1
    print(count)


water(100001,2) 