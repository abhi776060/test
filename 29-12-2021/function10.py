user='(1+2)+2-(5+9)'#input(" enter your expression")
operration=["(",")","*","/","+","-"]
def add(*a):
    b=0
    for x in a:
        b+=x
    return b

def sub(*a):
    b = 0
    for x in a:
        b=x-b
    return b

def mul(*a):
    b = 1
    for x in a:
        b *= x
    return b

def div(*a):
    b = 1
    for x in a:
        b /= x
    return b

def brackets(str1):
    for x in str1:
        i=j=0
        if "(" in str1:
            i=str1.index("(")
            if ")" in str1:
                j=str1.index(")")
        str2=str1[i+1:j]
        if "+" in str2:
            list1=str2.split("+")
            list1=tuple(map(int,list1))
            a=add(*list1)
            return a
        if "-" in str2:
            list1=str2.split("-")
            list1=tuple(map(int,list1))
            a=sub(*list1)
            return a
        if "*" in str2:
            list1=str2.split("*")
            list1=tuple(map(int,list1))
            a=mul(*list1)
            return a
        if "/" in str2:
            list1=str2.split("-")
            list1=tuple(map(int,list1))
            a=div(*list1)
            return a
# print(brackets(user))
flag=True
while flag:
    for x in user:
        i = 0
        j=0
        if "(" in user:
            i = user.index("(")
            if ")" in user:
                j = user.index(")")
        str2 = user[i:j+1]
        new = brackets(str2)
        user=str(new)+user[j+1:]
        print(user)
        brackets(user)
        print(user)
        flag=False