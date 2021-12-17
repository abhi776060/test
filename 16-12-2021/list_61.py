#Create a list of empty dictionaries
class List:
    def __init__(self):
        pass
    def Create(self,n):
        lis=[]
        for x in range(n):
            lis.append({})
        return lis
me=List()
print(me.Create(2))