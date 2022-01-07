#program to sort a string lexicographically
'''
Input :  "hello python program how are you"
Output :  are
          hello
          how
          program
          python
          you

'''

class String:
    def __init__(self):
        pass

    def lexicographically(self,str1):
        for x in sorted(str1.split(' ')):
            print(x)



solution=String()
solution.lexicographically("hello python program how are you")