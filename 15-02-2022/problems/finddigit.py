def findDigits(n):
    # Write your code here
    count=0
    
    for x in str(n):
        try:
            if n%int(x)==0:
                count+=1
        except:
            pass
    return count
# print(findDigits(124))
# print(findDigits(111))
# print(findDigits(10))
print(findDigits(1012))