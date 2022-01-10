list1=[]
for x in range(1,101):
    list1.append(x)
list2=[]
for x in range(0,len(list1),5):
    j=x+5
    list2.append(list1[x:j])
print(list2)



