class Largest():
    def largest(self,list1):
        max_num = list1[0]
        for x in list1:
            if x > max_num :
             max_num = x
        return max_num
me=Largest()
list1=[1,2,4,2,4,9]
print(me.largest(list1))