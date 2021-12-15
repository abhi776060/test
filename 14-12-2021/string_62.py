#remove leading zeros from an IP address Input :001.200.001.004  Output : 1.200.1.4
class String:
    def __init__(self):
        pass

    def sum_of_digit(self,str1):
        sum_digi=0
        lis1=[]
        for x in str1:
            if x.isdigit():
                lis1.append(x)
        for x in lis1:
            sum_digi+=int(x)
        return sum_digi
me=String()
print(me.sum_of_digit('abhi185dgdh789'))
