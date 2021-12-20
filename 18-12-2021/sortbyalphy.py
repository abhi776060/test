class SortALpha:
    def __init__(self,new_dict):
        self.new_dict=new_dict
        
    def sort(self):
        for i, j in self.new_dict.items():
            sorted_dict ={i:sorted(j)}
            print(sorted_dict)
            
        
dict1 ={
	"L1":[87, 34, 56, 12],
	"L2":[23, 00, 30, 10],
	"L3":[1, 6, 2, 9],
	"L4":[40, 34, 21, 67]
}
me=SortALpha(dict1)
print(me.sort())

