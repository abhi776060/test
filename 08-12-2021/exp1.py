'''
#syntax error
x= 10
if x>5:
    raise Exception(f'x should not be exceed 5, but you entered{x}')
'''
'''
while True print('hello world')
'''
#exceptions errors
'''
10/0 #ZerodivisionError
'''
'''
4+name #Name error
'''
'''
'2'+2 #Type error
'''
'''
while True:#value error
    try:
        x=int(input("enter a numbeer"))
        break
    except ValueError:
        print('thata was a valid number')
'''
'''
class A(Exception):
    pass
a=A()
#print(a.o)#AttributeError
try:
    print(a.o)
except :
    print("Attribute error occred")
'''
'''
print(k)
try:
  print(k)
except:#NameError
  print("An exception occurred")
'''
'''
try:
  print(x)
except NameError:#Name error handling 
  print("Variable x is not defined")
except:
  print("Something else went wrong")
finally:
    print("bye")
'''
''''
try:
  f=open('textfile1.txt','r')
  print(f.read())
except:
  print("enter a valid file name")
finally:
  print("bye")
'''
'''
x = 'j'
if not type(x) is int:#how to handle raised error and raise comments for that
  raise TypeError("Only integers are allowed")
'''
username = input("Enter username:")
prin
