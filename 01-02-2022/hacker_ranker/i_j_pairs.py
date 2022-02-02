def divisibleSumPairs( k, ar):
    # Write your code here
    ar=sorted(ar)
    count=0
    for x in range(len(ar)):
        for y in range(x+1,len(ar)):
            str1=ar[x]+ar[y]
            # print(ar[x],ar[y])
            if ar[y]>=ar[x] and (str1%k)==0:
                count+=1
                # print('ff',ar[x],ar[y])
            
    return (count)

# print(divisibleSumPairs(2,[5 ,9 ,10 ,7 ,4]))
# print(divisibleSumPairs(5,[1 ,2 ,3 ,4 ,5,6]))
print(divisibleSumPairs(3,[2, 8, 6, 8, 4]))#3
