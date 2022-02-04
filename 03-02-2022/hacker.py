def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%100==0 and year%4==0:
        leap=False
    elif year%4==0 and year%400==0:
        leap=True
   
        
    
    return leap
print(is_leap(1992))
# print(1992%100)
# print(1992%4)
# print(1992%400)