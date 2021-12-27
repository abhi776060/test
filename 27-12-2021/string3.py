#Reverse words in a given String in Python
'''
Input : str = geeks quiz practice code
Output : str = code practice quiz geeks
'''
class String:
    def __init__(self):
        pass

    def reverse(self,lis):
        lis1=lis.split(" ")
        str1=''
        for x in lis1:
            str1=x+" " + str1
        print(str1)


string=String()
string.reverse('geeks quiz practice code')