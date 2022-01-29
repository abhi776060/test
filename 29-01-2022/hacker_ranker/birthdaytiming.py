def timeConversion(s):
    # Write your code here
    str1=s[len(s)-2:]
    num=int(s[:2])
    result=''
    if str1=='AM':
        
        if num >= 12:
            
            a=num-12
            
            res=str(a)+s[2:len(s)-2]
            print(res)
            if len(res)==len(s):
                result=res
            else:
                result='0'+res

            
            
        else:
            result=s[:len(s)-2] 
            
            
    elif str1=='PM':
        
        if num < 12:
            a=num+12
            result=str(a)+s[2:len(s)-2]
           
        else:
            
            result=s[:len(s)-2]
    print(result)
timeConversion('04:59:59AM')
