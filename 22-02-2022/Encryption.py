from math import ceil,floor,sqrt

def encryption(s):
    b=len(s)
    s=s.replace(' ','')
    length=sqrt(len(s))
    lower=floor(length)
    upper=ceil(length)
    difference=(upper*upper)-len(s)
    str1=' '*difference
    s+=str1

    if lower == upper:
        upper+=1

    list1=[]
    start=0
    end=upper

    while end <=len(s):
        list1.append(s[start:end])
        start=end
        end+=upper

    str2=''
    for x in range(len(list1)):
        for y in range(len(list1)):
            str2+=list1[y][x]
        str2+=' '

    str3=str2.replace("  "," ")
    print(str3,list1,upper,lower,s)


s='if man was meant to stay on the ground god would have given us roots'
s1='haveaniceday'
s2='feedthedog'
s3='chillout'
encryption(s3)