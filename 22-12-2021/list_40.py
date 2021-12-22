#Split a list based on first character of word

class List:

    def __init__(self):
        pass

    def split(self,lis):
        dict1={}
        for x in lis:
            if x[0] not in dict1:
                dict1[x[0]]=x
            else:
                dict1[f'{x[0]}1']=x

        print(dict1)
list1=List()
lis=['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
list1.split(lis)