'''
a= sequence of integers = a[i],a[j],a[k] is beautiful when i<j<k
means a[j]-a[i]=a[k]-a[j]=d
d= increment of units 
a=[2,2,3,4,5] d=1


'''
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    n=len(arr)
    triplets = 0
    for i in range(n-2):
        for j in range(i + 1, n-1):
            if arr[j] - arr[i] == d:
                foundTrip = False
                for k in range(j + 1, n):
                    if arr[k] - arr[j] == d:
                        triplets += 1
                        foundTrip = True
                        break
                if foundTrip == True:
                    break
                
    print(triplets)

beautifulTriplets(1,[2,2,3,4,5])


