#find the first non-repeating character in given string
'''
madam--d
'''
class String:
    def __init__(self):
        pass

    def non_repeating(self,str1,accurence=0):
        input_list=[]
        extra_list=[]
        for x in str1:
            if x  not in input_list:
                input_list.append(x)
            else:
                extra_list.append(x)
        final_list=[]
        for x in input_list:
            if x in extra_list:
                pass
            else:
                final_list.append(x)
        print(final_list[accurence])
solution=String()
solution.non_repeating('madam')