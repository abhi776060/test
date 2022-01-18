'''
Problem Statement: Little Robert likes mathematics. Today his teacher has given him two integers and asked to find out how many integers can divide both the numbers. Would you like to help him in completing his school assignment?
Input Formatting: Thre is two integers, a and b as input to the program.

Output Formatting: Print the number of common factors of a and b. Both the input value should be in a range of 1 to 10^12.

Example:

Input: 10 15
Output: 2
Explanation: The common factors of 10 and 15 are 1 and 5. So the answer will be 2.
'''
data  = input('enter two integer numbers')
li = data.split()
   
a = int(li[0])
b = int(li[1])
   
def gcd(a, b):
    if (a == 0): 
        return b
    return gcd(b%a, a)#8/4-2, 4
   
if (a>0 and a<(10**12+1) and b>=1 and b<(10**12+1)):
    count = 1
    for i in range(2, gcd(a, b)+1):
        if a%i==0 and b%i==0:
            count = count+1
    print(count)