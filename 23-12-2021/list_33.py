#Generate all sublists

from itertools import combinations

class List:
    def __init__(self):
        pass
    def sub_lists(self,my_list):
        subs = []
        for i in range(0, len(my_list)+1):
            temp = [list(x) for x in combinations(my_list, i)]
            # print(temp)
            if len(temp)>0:
                subs.extend(temp)
        print(subs)

list1=List()
l1 = [10, 20, 30, 40]
list1.sub_lists(l1)

