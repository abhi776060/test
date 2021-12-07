class TableF:        
    def table(self,dict1):
        print(f"{'name':<10}  {'age':<10}   {'course':<10}")
        for key, value in dict1.items():
            name,age,course=value
            
            print(f"{name:<10}  {age:<10}   {course:<10}")
        
        



dict1 = {1: ["abhishek", 21, 'Data Structures'],
	2: ["vishnu", 20, 'Machine Learning'],
	3: ["pavan", 21, 'OOPS with java']
	}
me=TableF()
print(me.table(dict1))
