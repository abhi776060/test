'''
Write a Python program to check if a given positive integer is a power of two
'''

def is_power_two(num):
    tows_list=[2**x for x in range(num)]
    if num in tows_list:
        print("true")
    else:
        print("false")
is_power_two(7)