class RemoveKeySpace:
    def __init__(self,new_dict):
        self.new_dict=new_dict

    def remove(self):
        remover={ x.translate({32:None}): y for x, y in self.new_dict.items()}
        return remover,

Product_list = {'key 01' : 'DBMS', 'key 02' : 'OS',
				'k e y 3 ': 'Soft Computing'}
me=RemoveKeySpace(Product_list)
print(me.remove())

