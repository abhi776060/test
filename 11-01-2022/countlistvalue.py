class CountList:
    def main(self,*d):
        count = 0
        for x in d:
            for y in x.values():
                if type(y)==list:
                    for a in y:
                        count+=1
                else:
                    count+=1
        return count

me=CountList()
d = {'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],'B' : 34,'C' : 12,'D' : [7, 8, 9, 6, 4] }
print(me.main(d))


