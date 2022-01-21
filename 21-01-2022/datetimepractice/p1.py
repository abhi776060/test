from datetime import *
# print(dir(datetime))
date1=datetime.now()
# print(date1)
# print(date1.year)
# print(date1.month)
# print(date1.day)
print('%A full weekday',date1.strftime("%A"))#full weekday
print('%a short word of weekday',date1.strftime("%a"))#short word of weekday
date2=datetime(1995,5,8)
print('%b month',date2.strftime("%b"))#month
print(date2.strftime("%B"))#
print('%w Weekday as a number 1-5',date2.strftime("%w"))#Weekday as a number 1-5
print('%W Weekday as a number 1-52',date2.strftime("%W"))#Weekday as a number 1-52
print('%d Day of month ',date2.strftime("%d"))#Day of month 
print('%m Month as a numbe',date1.strftime("%m"))#Month as a numbe
print('%M Minute 00-59',date1.strftime("%M"))#Minute 00-59 
print('%S Second 00-59 ',date1.strftime("%S"))#Second 00-59 
print('Microsecond',date1.strftime("%f"))#Microsecond
print('%j  Day number of year',date1.strftime("%j"))#Day number of year
print('%U Week number of year, Sunday as the first day of week, 00-53',date1.strftime("%U"))#Week number of year, Sunday as the first day of week, 00-53
print('%W Week number of year, Monday as the first day of week, 00-53',date1.strftime("%W"))#Week number of year, Monday as the first day of week, 00-53
print('%c local version of date and time',date1.strftime("%c"))#local version of date and time
print('%C century',date1.strftime("%C"))#century
print('%x local version of date ',date1.strftime("%x"))#local version of date 
print('%X local version of ',date1.strftime("%X"))#local version of  
print('%%  print %',date1.strftime("%%"))# print %
print('%G year',date1.strftime("%G"))# year
