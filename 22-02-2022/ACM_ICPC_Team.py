def check(a,b):
    flag=True
    for x in range(len(a)):
        new1=a[x]
        new2=b[x]
       
        if new1=='0' and new2=='0':
            flag=False
            break
    return flag


def acmTeam(topic):
    # Write your code here
    topic_len={x+1:topic[x] for x in range(len(topic))}
    combinations_list=[]
    count=0
    for x in range(1,len(topic_len)+1):
        for y in range(x+1,len(topic_len)+1):
            if x !=y:
                combinations_list.append((x,y))
    for x in combinations_list:
        i=x[0]
        j=x[1]
        var=check(topic_len[i],topic_len[j])
       
        if var:
            count+=1
        
    print(len(topic_len[1]),count)
# acmTeam(['10101','11110','00010'])
acmTeam(['10101','11100','11010','00101'])
