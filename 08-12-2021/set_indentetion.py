class SetIndentation:
    def __init__(self,str1):
        self.str1=str1
    def indentation(self,n):
        list1=[]
        
        for i in range(n):
            list1.append(" ")
        for j in self.str1:
            list1.append(j)
        str2=''
        for x in list1:
            str2+=x
        return str2
str1="well come to python"
print(str1)
me=SetIndentation(str1)
print(me.indentation(10))