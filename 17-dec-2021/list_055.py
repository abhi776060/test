#Remove key values pairs from a list of dictionaries

class List:
    def __init__(self):
        pass

    def only_values(self,dict1):
        new_list = []
        for x in dict1:
            if type(x)==dict:
                new_list.append({})
            else:
                new_list.append(x)
        print(new_list)



list1=List()
lis=[{1:1,2:2,3:3},2,5,6]
list1.only_values(lis)