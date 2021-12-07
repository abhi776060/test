class Swap():
    def swap(self,my_string):
        start = my_string[0]
        end = my_string[-1]
        swapped_string = end + my_string[1:-1] + start
        return swapped_string
me=Swap()
print(me.swap("abhishek"))