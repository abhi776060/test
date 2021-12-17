#Get the depth of a dictionary

class List:
    def __init__(self):
        pass
    def depth(self,lis):
        count = 0
        for x in lis:
            string_vary=str(x)
            for y in string_vary:
                if y=='{':
                    count+=1
        return count

me=List()
lis=[{1:{}}]
print(me.depth(lis))