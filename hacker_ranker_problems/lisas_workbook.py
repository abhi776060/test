


def workbook(n, k, arr):
    # Write your code here
    unordered_book=[]
    for x in arr:
        for y in range(x):
            unordered_book.append(y+1)
    book={}
    page=0
    count=0
    for x in unordered_book:
        
        if x ==1:
           
            page+=1
            count=0
        count+=1
        # print(x,page)
        if count ==k+1:
            page+=1
            count=1
        if count<=k:
            if page not in book:
                book[page]=[x]
            else:
                book[page].append(x)
    cal=0
    for key, val in book.items():
        if key in val:
            cal+=1
    print(cal)
workbook(5,3,[4, 2, 6, 1, 10])
# workbook(5,5,[3,8,15,11,14,1,9,2,24,31])