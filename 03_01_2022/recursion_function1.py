#Write a Python program to calculate the sum of a list of numbers
'''
[2, 4, 5, 6, 7]---sum =24
'''


def Sum(list1):
        if len(list1)==1:
                return list1[0]
        else:
                return list1[0]+Sum(list1[1:])
print(Sum([2,4,5,6,7]))