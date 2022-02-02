import calendar,datetime

def dayOfProgrammer(year):
    # Write your code here
    leap=28
    if year%4==0 :
        if year%400==0:
            leap+=1
        if year%100==0:
            leap+=0
        else:
            leap+=0
    print(leap)
    day=256-(215+leap)
    # print(day)
    date1=datetime.datetime(year,9,day)
    return(date1.strftime('%d.%m.%Y'))
    

print(dayOfProgrammer(1918))

