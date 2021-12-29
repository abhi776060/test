user='(1+2)+2-(5+9)'#input(" enter your expression")
print(user)
list1=[x for x in user]
print(list1)
flag=True
while flag:
    if "(" in list1:
        i=list1.index("(")
        j=0
        if ")" in list1:
            j=list1.index(")")
        list2=list1[i+1:j]
        new_elemets=0
        for x in list2:
            try:
                new_elemets+=int(x)
            except:
                pass
        list1=list1[j:]
        list1[i] = new_elemets

        if "(" not in list1:
            flag=False
print(list1)