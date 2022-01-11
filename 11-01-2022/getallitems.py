class PrintAll:
    def __init__(self):
        self.new_dict={}

    
    def print_all(self,test_dict):
        
        for i,j in test_dict.items():
            print(f'"key "{ i} "value "{ j}"items are {i}"&"{j}' )

    
test_dict = {"a" : 1, "b" : 2, "c" : 3}
me=PrintAll()
print(me.print_all(test_dict))