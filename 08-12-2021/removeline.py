class RemoveLine:
    def __init__(self,str1):
        self.str1=str1
    def removenewline(self):
        str2=''
        list1=[]
        for x in self.str1:
            if x == '\n':
                pass
            else:
                list1.append(x)
        list2=list1[1:len(list1)-1]
        str3=''
        for i in list2:
            str3+=i
        return str3   
        
str1="\n Starbucks has the best coffee \n"
me=RemoveLine(str1)
print(me.removenewline())
print("good bye")
