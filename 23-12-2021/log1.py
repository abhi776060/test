from logging import *

basicConfig(filename='oddeven.txt',
            filemode='a',
            format='%(asctime)s %(levelname)s-%(message)s',
            datefmt='%y-%m-%d  %H:%M:%S')
for x in range(25):
    if x%2==0:
        warning('adding even numbers')
    elif x%3==0:
        error('3 dividing numbers')
    else:
        critical("remainig numbers")