list1=[1,2,3,4,5]
iterator=list1.__iter__()
while True:
    try:
        print(iterator.__next__())
    except:
        break
print("finished")


#by using usr defind function

def iterate(sequence):
    my_list=sequence.__iter__()
    for x in range(len(sequence)):
        print(my_list.__next__())

iterate([1,2,3,4])