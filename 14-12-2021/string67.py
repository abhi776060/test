#that accepts a string and calculate the number of digits and letters

class Strings:
    def __init__(self):
        pass
    def count_num_leter(self,str1):
        number=0
        letters=0
        for x in str1:
            if x.isdigit():
                number+=1
            else:
                letters+=1
        print('numbe:',number)
        print('letter:', letters)


me=Strings()
print(me.count_num_leter('abhi124'))