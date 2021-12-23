'''

123------321
-123--------(-321)



'''

a=123
b=str(123)
print(a)
c=''
for x in b:
    c=x+c
sign=-1 if a <0 else 1

print(sign*int(c))