#convert a string in a list
'''
input: 'used to split the strings'
output: ['used', 'to', 'split', 'the', 'strings']
'''
class String:
    def __init__(self):
        pass

    def convert(self,str1):
        list1=[]
        for x in str1.split(" "):
            list1.append(x)
        print(list1)


string1=String()
string1.convert("used to split the strings")