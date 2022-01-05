#Use of frozensets

set1=frozenset({1,2,3,4,5,6})
#set1.add(5)
print(set1)
'''
    set1.add(5)
AttributeError: 'frozenset' object has no attribute 'add'

'''
set1.remove(5)
'''
set1.remove(5)
AttributeError: 'frozenset' object has no attribute 'remove'
'''