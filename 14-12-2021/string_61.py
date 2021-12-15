#remove duplicate characters of a given string geeksforjeeks geeksfor
class String:
    def __init__(self):
        pass

    def remove_duplicates(self,str1):
        str2=''
        for x in str1:
            if x not in str2:
                str2+=x
        return str2
me=String()
print(me.remove_duplicates('geeksforgeeks'))
