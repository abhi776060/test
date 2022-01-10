#strip a set of characters from a string
'''
Original String:
The quick brown fox jumps over the lazy dog.
After stripping a,e,i,o,u
Th qck brwn fx jmps vr th lzy dg.
'''
class String:
    def __init__(self):
        pass

    def strip_on_vowel(self,str1):
        vowel_list=['a','e','i','o','u']
        str2=''
        for x in str1:
            if x in vowel_list:
                pass
            else:
                str2+=x
        print(str2)

solution=String()
solution.strip_on_vowel('The quick brown fox jumps over the lazy dog.')