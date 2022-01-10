#reverse words in a string
'''
i love programming very much
much very programming love i
'''
class String:
    def __init__(self):
        pass

    def reverse_word(self,str1):
        list1=[]
        for x in str1.split():
            list1.append(x)
        str2 = ''
        for x in list1:
            str2=x + ' ' + str2
        print(str2)

solution=String()
solution.reverse_word('i love programming very much')