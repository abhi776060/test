def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    if p >s :
        return 0
    list1=[]
    sum=p

    while sum>=m:
        list1.append(sum)
        sum-=d
    sum1=0
    list2=[]
    i=0
    while sum1<=s:
        print(sum1+m)
        if sum1+m>s:
                break
        try:
            sum1+=list1[i]
            if sum1>s:
                break

            list2.append(list1[i])
            i+=1
        except:
            sum1+=m
            list2.append(m)
            i+=1

    print(list2)
# howManyGames(20,3,6,80)
# howManyGames(20,3,6,70)
howManyGames(100,99,81,180)