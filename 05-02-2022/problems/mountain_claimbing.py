def countingValleys(steps, path):
    # Write your code here
    sea_level=0
    sea_travell=[]
    touch=0
    c=0
    for x in path:
        if x =="U":
            touch+=1
            sea_travell.append(touch)
        if x == "D":
            touch-=1
            sea_travell.append(touch)
    for x in range(len(sea_travell)):
        # print(sea_travell[x],x+1)
        try:
            if sea_travell[x] ==-1 and sea_travell[x-1] ==0 :
                c+=1
        except:
            pass
        
    return c
print(countingValleys(8,'UDDDUDUU'))