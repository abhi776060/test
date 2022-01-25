'''
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false

'''
def detect(str1):
    flag=False
    for x in range(len(str1)):
        if str1[x].isupper():
            flag=True
        else:
            flag=False
            break
    print(flag)

detect('USA')