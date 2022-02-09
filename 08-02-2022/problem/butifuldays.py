def reverse(a):
    b=str(a)[::-1]
    c=int(b)
    return c

def beautifulDays(i, j, k):
    # Write your code here
    count=0
    for x in range(i,j+1):
        # print(x)
        sum=str(abs(x-reverse(x))/k)
        if sum[-1]=='0':
            count+=1
    print(count)
    

beautifulDays(20,23,6)
        