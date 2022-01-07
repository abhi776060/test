#4 Copies of last 2 chars
'''
python--
onononon
'''

class String:
    def __init__(self):
        pass

    def copies_4(self,str1):
        str2=str1[-2:]
        print(str2*4)

solution=String()
solution.copies_4('python')