'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


def binary_addition(str1,str2):
   
    first=len(str1)
    second=len(str2)
    difference=abs(first-second)
    if len(str1)<len(str2):
        str3=''
        for x in range(difference):
            str3+='0'
        str1=str3+str1
        
    else:
        str3=''
        for x in range(difference):
            str3+='0'
        str2=str3+str2
    
    i=-1
    str4=''
    carry=0
    while True:
        if i==-len(str1)-1:
            break
        sum=int(str1[i])+int(str2[i])
        if sum == 2:
            str4='0'+str4
            carry=1
        else:
            a=sum+carry
            if a == 2:
                str4='0'+str4
                
            else:
                str4=str(a)+str4
        i=i-1
    
    print(str(carry)+str4)



            

binary_addition('1010','1011')