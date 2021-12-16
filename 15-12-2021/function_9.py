#fibonacci series
class Function:
    def __init__(self):
        pass
    def fabinacci(self,n):
        first_num = 0
        second_num = 1
        print(first_num)
        print(second_num)
        for i in range(3,n+1):
            third_num = first_num + second_num
            print(third_num)
            first_num=second_num
            second_num=third_num
me=Function()
print(me.fabinacci(10))