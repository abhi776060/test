def minimumDistances(a):
    # Write your code here
    list1=[]
    for x in range(len(a)):
        for y in range(x+1,len(a)):
            if a[x]==a[y]:
                sub=y-x
                list1.append(sub)
    if list1:
        print(min(list1))
    else:
        print(-1)


# minimumDistances([3,2,1,2,3])
minimumDistances([7, 1, 3, 4, 1, 7])