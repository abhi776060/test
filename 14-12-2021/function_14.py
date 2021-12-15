#accepts a string and calculate the number of upper case letters and lower case letters

class Function:
    def __init__(self):
        pass
    def count_u_l(self,str1):
        upper=0
        lower=0
        for x in str1:
            if x.isupper():
                upper+=1
            else:
                lower+=1
        return 'upper cases are ;',upper ,'lowers are  ;',lower
me=Function()
print(me.count_u_l('AbHiShEks'))