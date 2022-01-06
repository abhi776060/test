my_list=list()
print('printing empty list :',my_list)

my_list1=[]
print('another way of printing empty list :',my_list1)

print("start the iterating process: ")
my_list2=[1,2,3,4]
for i in my_list2:
    print("iterating from list2",i)
print("end of for loop")

print(" iterating by range function")
for x in range(5):
    print("elements from range function :",x)
print(" end of range function iteration ")

print(" ===============list converting to list iterator ====")
list1=[1,2,3,4]
iterate=list1.__iter__()
print(type(iterate),'type of iterate object')
try:

    print("using next 1 iteration:",iterate.__next__())
    print("using next 2 iteration:",iterate.__next__())
    print("using next 3 iteration:",iterate.__next__())
    print("using next 4 iteration:",iterate.__next__())
    print("using next 5 iteration:",iterate.__next__())
    print("using next 6 iteration:",iterate.__next__())
except:
    print("iteration completed")

