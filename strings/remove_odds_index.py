class OddRemove():
    def odd_values_string(self,mystring):
        result = "" 
        for i in range(len(mystring)):
            if i % 2 == 0:
                result = result + mystring[i]
        return result
me=OddRemove()
print(me.odd_values_string("abhishek"))