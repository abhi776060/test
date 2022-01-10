#to display a number in left, right and center aligned of width 10

class String:
    def __init__(self):
        pass

    def disply_width(self,num):
        str2=str(num)
        str1=''
        for x in range(1,11-len(str2)):
            str1+='_'
        middle=len(str1)//2
        left_align=str2+str1
        center_align = str1[0:middle] + str2+str1[middle:]
        right_align=str1+str2
        print("left aligned num is :",left_align,)
        print("center aligned num is :",center_align)
        print("right aligned num is :",right_align)


solution=String()
solution.disply_width(15)