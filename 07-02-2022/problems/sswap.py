def swap_case(s):
    case_change=[]
    for i in range(len(s)):
        if (s[i].isupper())==True:
            case_change.append(s[i].lower())
        elif (s[i].islower()==True):
            case_change.append(s[i].upper())
        else:
            case_change.append(s[i])    
        stri=''
    return stri.join(case_change)
print(swap_case('abhiShek'))