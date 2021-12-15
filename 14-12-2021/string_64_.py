#Reverse a given string  Input : "Python"   Output : "nohtyP"
class String:
    def __init__(self):
        pass

    def reverse_string(self,str1):
        str2=''
        for x in str1:
            str2=x+str2
        return str2


me=String()
print(me.reverse_string('python'))
