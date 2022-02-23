def ip_num(s):
    str1=''
    b,c=s.split('/')
    d=''.join(x for x in b)
    y=d.split(".")
    for x in y:
        ele=int(x)
        str1=str1+'.'+str(ele)
    print('ip',str1.replace('.','',1))
    print('mark',c)
ip_num('216.08.094.000000/24')