import datetime
def dayOfProgrammer(year):
    centure_year=[x for x in range(1700,1917,100)]
    sec_centure_year=[x for x in range(2100,2701,100)]

    flag=False
    if year%4==0 or year%400==0:
        if year  in centure_year:
            print('0')
            flag=False
        if year in sec_centure_year:
            flag=False
        else:
            print('1')
            flag=True
      
    else:
        print('2')
        flag=False
    
    if not flag:
        return ('13.09.{}'.format(year))
    else:
        return ('12.09.{}'.format(year))

    

print(dayOfProgrammer(2200))




