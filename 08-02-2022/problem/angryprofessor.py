def angryProfessor(k, a):
    # Write your code here
    count=0
    for x in a:
        if x <=0:
            count+=1
    if k>=count:
        return "YES"
    else:
        return "NO"
print(angryProfessor(3,[-2,-1,0,1,2]))