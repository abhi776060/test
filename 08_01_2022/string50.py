#split a string on the last occurrence of the delimiter
'''
The original string : i love programming very much
The splitted list at the last comma : ['i love programming very', 'much']
'''
class String:
    def __init__(self):
        pass

    def split_on_delimiter(self,str1,ch=' ',limit=0):
        limit_index_list=[]
        for x in range(len(str1)):
            if str1[x] ==ch:
                limit_index_list.append(x)
        limit_index_list.reverse()
        str2=''
        try:
            for x in range(len(str1)):
                if x == limit_index_list[limit]:
                    str2+='X'
                else:
                    str2+=str1[x]
        except:
            print("out of range")
        final_list=[]
        for x in str2.split('X'):
            final_list.append(x)
        print(final_list)


solution=String()

solution.split_on_delimiter('i love programming very much','m',2)