#check if a string contains all letters of the alphabet

class String:
    def __init__(self):
        pass

    def check_string(self,str1):
        alpha_list=[chr(x) for x in range(97,97+26)]
        flag='all character are present'
        for x in alpha_list:
            if x in str1:
                pass
            else:
                flag='some of characters are missing'
        print(flag)


solution=String()
solution.check_string("abcdefghijkmnopqrstuvwxyz")