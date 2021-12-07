'''
#finding lenght of string
def fun_for_len(my_string):
    lenght_of_string=0
    for x in my_string:
        lenght_of_string+=1
    print("lenght of string: ",lenght_of_string)
fun_for_len("abhishek")

'''
class StringLenght():
    def Len(self,my_string):
        len_of_string=0
        for i in my_string:
            len_of_string+=1
    
        return len_of_string
me=StringLenght()
print(me.Len("abhishek"))