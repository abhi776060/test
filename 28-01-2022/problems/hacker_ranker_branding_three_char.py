'''
Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
Explanation 0


Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string  has at least  distinct characters.
'''
from numpy import char


def branding(str1):
    if len(str1) >= 3:
        char_accurence={}
        for x in sorted(str1):
            if x in char_accurence.keys():
                char_accurence[x]+=1
            else:
                char_accurence[x]=1
        dict1=sorted(char_accurence.items(),key=lambda x:x[1],reverse=True)
        
        print((dict(dict1[0:3])))
        
            


                
    else:
        print("length of string should be grater than 3.")
# branding('aabbbccde')
branding('google')
