
def pickingNumbers(a):
    # Write your code here
    b=sorted(a)
    sub_arrays={}
    key=1
    for x in range(len(b)):
        try:
            first=a[x]
            second=a[x+1]
            diff=abs(first-second)
            if diff <=1:
                if not sub_arrays:
                    sub_arrays[key]=[first]
                else:
                    sub_arrays[key].append(first)
            else:
                sub_arrays[key].append(first)
                key+=1
                sub_arrays[key]=[]
        except:
            diff1=abs(a[-1]-a[-2])
            if diff1<=1:
                sub_arrays[key].append(a[-1])
            else:
                key+=1
                sub_arrays[key]=[]
    len_list=[]
    for x in sub_arrays.values():
        len_list.append(len(x))
    print((max(len_list)))
    print(sub_arrays)
    print(b)
# pickingNumbers([1,1,2,2,4,4,5,5,5])
# pickingNumbers([4,6,5,3,3,1])
pickingNumbers([1,2,2,3,1,2])