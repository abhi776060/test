'''
Write a Python program to check if a given positive integer is a power of three
'''

def is_power_three(num):
    tows_list=[3**x for x in range(num)]
    if num in tows_list:
        print("true")
    else:
        print("false")
is_power_three(9)