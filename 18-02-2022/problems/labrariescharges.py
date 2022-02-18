def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if d1<d2 and m1==m2 and y1==y2:
        return 0
    elif d1>d2 and m1==m2 and y1==y2:
        diff=d1-d2
        return 15 *diff
    elif m1>m2 and y1==y2:
        diff=m1-m2
        return 500 * diff
    elif y1>y2:
        diff=y1-y2
        return 10000*diff
    else:
        return 0
print(libraryFine(6,6,2015,9,6,2016))
# print(libraryFine(14,7,2018,5,7,2018))
# print(libraryFine(9,6,2015,6,6,2015))