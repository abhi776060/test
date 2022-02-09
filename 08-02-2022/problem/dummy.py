# import csv

# fieldnames='abhi'

# his={'a':'a','b':'b','h':'h','i':'i'}
# with open('abhi', 'w', encoding='UTF8', newline='') as f:
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerow(his)
# print(*'o')

from os import sep


stry='python'
for i in range(len(stry)):
    print(*stry[:i],end='_')