from logging import *

basicConfig(filename='tryblock.txt',
            filemode='a',
            format='%(asctime)s-%(levelname)s-%(message)s',
            datefmt='%d-%m-%y %H:%M:%S')
a=5
b=0
try:
    print(a/b)
except Exception as e:
    error(f"we found {e}")