class StartsSpecyChar:
    def __init__(self,newstring):
        self.newstring=newstring
    def startswith(self,n):
        for i in self.newstring:
            if i is n:
                return True
            else:
                return False
str1='abhishek'
me=StartsSpecyChar(str1)
print(me.startswith('a'))