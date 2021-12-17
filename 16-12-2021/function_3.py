#print prime numbers
class Function:
    def __init__(self):
        pass
    def prime(self,num):
        flag = False
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    flag = True
                    break
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
me=Function()
print(me.prime(6))