#Length of first 3 chars

'''
ipy       ---ipy
python    ---pyt
py        ---py
'''
class String:
    def __init__(self):
        pass

    def first_3char(self,str1):
        str2=''
        if len(str1) <= 3:
            print(str1)
        else:
            print(str1[:3])

solution=String()
solution.first_3char('python')