#function to check whether a string is a pangram or not

class Function:
    def __init__(self):
        pass
    def pangram(self,str1):
        alphabets='abcdefghijklmnopqrstuvwxyz'
        for x in alphabets:
            if x not in str1.lower():
                return False
        return True

me=Function()
#str1='The quick brown fox jumps over the lazy dog'
str1="marry had a little limb"
print(me.pangram(str1))