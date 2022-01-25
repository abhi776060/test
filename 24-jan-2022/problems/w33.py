'''
Write a Python program to check if a given positive integer is a power of four
'''

def is_power_four(num):
    tows_list=[4**x for x in range(num)]
    if num in tows_list:
        print("true")
    else:
        print("false")
is_power_four(9)

