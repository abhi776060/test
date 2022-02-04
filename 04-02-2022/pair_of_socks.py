def sockMerchant(n, ar):
    # Write your code here
    item_collections={}
    for x in ar:
        if x in item_collections:
            item_collections[x].append(x)
        else:
            item_collections[x]=[x]
    count=0
    # print(item_collections)
    for x in item_collections.values():      
            count+=len(x)//2
    return count
print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))