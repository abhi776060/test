class List():
    def longer_word(self,list1):
        list2=[len(str(x)) for x in list1]
        list3=[x for x in sorted(list2)]
        i=list3[-1]
        list4=[]
        for x in list1:
            if len(str(x))==i:
                list4.append((x))
        return list4
me=List()

list1=['abhi',12345546,'#####']

print(me.longer_word(list1))
