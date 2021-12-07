
class MyString():
    def chare(self,my_string):
        count={}
        for c in my_string:
            if c not in count:
                count[c]=1
            else:
                count[c]+=1    
        return count


me=MyString()
print(me.chare("abhishek"))

