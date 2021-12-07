class AddElement:
    def __init__(self):
        self.new_set=set()
            
    def addelement(self):
        element=int(input("enter elements"))
        self.new_set.add(element)
        return self.new_set

            
              
    

me=AddElement()

print(me.addelement())