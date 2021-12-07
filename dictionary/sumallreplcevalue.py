class MyDictionary:
    def my_name(self,x):
        my_dictionary=x
        sum=0
        for i ,j in my_dictionary.items():
            sum+=j
        for i in my_dictionary:
            x[i]=sum
        print(my_dictionary)

x = {'key1': 1, 'key2': 3, 'key3': 2}
obj=MyDictionary()
obj.my_name(x)