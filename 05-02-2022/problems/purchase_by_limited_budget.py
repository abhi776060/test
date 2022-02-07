def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    cost_list=[]
    for x in keyboards:
        for y in drives:
            sum=x+y
            if sum<=b:
                cost_list.append(x+y)
    try:
        act_price_cost=sorted(cost_list)[-1]
        return(act_price_cost)
    except:
        return(-1)
# getMoneySpent([40,50,60],[5,8,12],60)
# getMoneySpent([3,1],[5,2,8],10)
getMoneySpent([4],[5],5)