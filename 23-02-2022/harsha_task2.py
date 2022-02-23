def rev(s):
    ele=s.split()
    str1=''
    for x in ele:
        y=x[::-1]
        str1=str1+" "+y
    print(str1)
rev("welcome to python")