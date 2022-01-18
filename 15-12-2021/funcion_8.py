#find the Max of three numbers

class Function:
    def __init__(self):
        pass

    def fabinacci(self, tup1):
        maxi = tup1[0]
        for x in tup1:
            if x > maxi:
                maxi = x
        return maxi
me=Function()
print(me.fabinacci((1,5,8)))