import re



txt = "The rain in Spain"
# x = re.search("Spain$", txt)#treu
# x = re.search("^The", txt)#true
x = re.search("^The.*Spain$",txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


'''
[] --- a set of a characters '[a-m]'
\ ---- escape special character '\d'
.    any char     'he..o'
^  starts with   '^hello"
$ ends with     "world$'
*  Zero or more occurences  'he.*o'



'''
import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("in", txt)
print(x)


import re

txt = "The rain in Spain"

#Check if "Spain/Portugal" is in the string:

x = re.findall("Spain", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")