'''
Given a string of length N, made up of only uppercase characters 'R' and 'G', where 'R' stands for Red and 'G' stands for Green.Find out the minimum number of characters you need to change to make the whole string of the same colour.
Input:
S="RGRGR"
Output:
2

'''
def myfun(str1):
    str2=str1.upper()
    dict1={'R':0,'G':0}
    for x in str2:
        if x =='R':
            dict1['R']+= 1
        elif x== "G":
            dict1['G']+=1
    if dict1['G'] > dict1['R'] :
        print("reqired R is ",dict1['R'])
    else:
         print("reqired G is ",dict1['G'])

myfun('rrrgrg')