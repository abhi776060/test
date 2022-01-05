# Issubset and issuperset.
class Set:
    def __init__(self):
        pass

    def issubset_issuper(self,super_set,child1_set,child2_set):
        flag1="is subset"
        flag2="is super"
        for x in child1_set:
            if x in super_set:
                pass
            else:
                flag1="not subset"
        for x in child2_set:
            if x in super_set:
                pass
            else:
                flag1="not subset"
        print(flag1)
        for x in super_set:
            if x in child1_set or x in child2_set:
                pass
            else:
                flag2=" not super"
        print(flag2)

solution=Set()
solution.issubset_issuper({1,2,3,4,5,6,7,8,9},{1,2,3,4,5},{6,7,8,9})