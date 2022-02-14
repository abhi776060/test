def permutationEquation(p):
    # Write your code here
    dict1={}
    for x in range(len(p)):
        dict1[x+1]=p[x]
    for x in range(1,len(dict1)+1):
        for key,val in dict1.items():
            if x == val:
                for key1,val1 in dict1.items():
                    if key==val1:
                        print(key1)

    
                


# permutationEquation([2,3,1])
permutationEquation([4,3,5,1,2])