


def timeInWords(h, m):
    # Write your code 
    hour={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty'}
    m1=m
    m2=0
    if m>20 and m<60:
        str1=str(m)
        m1,m2=(m//10)*10,int(str1[1])


    if m==0 and m<=59 and h <=24:
        return(f"{hour[h]} o' clock")
    elif m==1 and m<=14 and h <=24:
        return(f"{hour[m1]} minute past {hour[h]}")
    elif m>1 and m<=14 and h <=24:
        return(f"{hour[m1]} minutes past {hour[h]}")
    elif m==15 and m<=29 and h <=24:
        return(f"quarter past {hour[h]}")
    elif m>15 and m<=29 and h <=24:
        return(f"{hour[m1]} {hour[m2]} minutes past {hour[h]}")
    elif m==30:
        return(f"half past {hour[h]}")
    elif m>30 and m<=44 and h <=24:
        a=60-(m1+m2)
        str2=str(a)
        m3,m4=(a//10)*10,int(str2[1])
        return(f"{hour[m3]} {hour[m4]} minutes to {hour[h+1]}")
    elif m==45:
        return(f"quarter to {hour[h+1]}")
    elif m>45 and m<=59 and h <=24:
        a=60-(m1+m2)
        str2=str(a)
        m3,m4=(a//10)*10,int(str2[1])
        return(f"{hour[m3+m4]} minutes to {hour[h+1]}")
print(timeInWords(7,29))