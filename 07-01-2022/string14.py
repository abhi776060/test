#Sort unique words alphanumerically
'''
Input comma separated sequence of words red, black, pink, green
 black, green, pink, red
'''

class String:
    def __init__(self):
        pass

    def sort_by_alphanumerical(self,str1):
        str2=''
        for x in sorted(str1.split(',')):
            str2+=x+','
        print(str2)

solution=String()
solution.sort_by_alphanumerical(' red, black, pink, green')