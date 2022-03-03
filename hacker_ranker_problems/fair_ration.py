def fairRations(B):
    # Write your code here
    count=0
    try:
        for x in B:
            for i,j in enumerate(B):
                if j%2==1:
                    count+=2
                    B[i]+=1
                    B[i+1]+=1
                    break
        print(count)
    except:
        print("NO")

# fairRations([2,3,4,5,6])
fairRations([4, 5, 6, 7])