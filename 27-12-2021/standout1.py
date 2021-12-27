#Program for array rotation
'''
[1 2 3 4 5 6] if 1times [6 1 2 3 4 5 ]
               if 2times [5 6 1 2 3 4 ] so...  on
'''
def rotate(lis,n):
    lis1=[]
    lis2=[]
    for x in range(len(lis)):
        if x >=len(lis)-n:
            lis1.append(lis[x])
        else:
            lis2.append(lis[x])
    print(lis1+lis2)
rotate([1,2,3,4,5,6],3)
