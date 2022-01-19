import re

txt = "That will be 59.0 dollars"


x = re.findall("\d", txt)
print(x)
