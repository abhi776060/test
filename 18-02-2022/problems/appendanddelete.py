def appendAndDelete(s, t, k):
    # Write your code here
    max_str=s if len(s) >len(t) else t
    actual_s=''
    actual_t=''
    for x in range(len(max_str)):
        if s[:x]==t[:x]:
            actual_s=s[x:]
            actual_t=t[x:]
        else :
            break
    acutal_value=k-len(actual_t)
    s1=len(actual_s)
    t1=len(actual_t)
    if s1+t1>k:
        print("No")
    elif s1+t1==k:
        print("Yes")
    elif (len(s)+len(t))-k<=0:
        print("Yes")
    elif abs((len(s)+len(t))-k)%2==0:
        print("Yes")
    else:
        print("No")
# appendAndDelete('abhishek','abhi',9)
# appendAndDelete('hackerhappy','hackerrank',9)
# appendAndDelete('aba','aba',7)
# appendAndDelete('ashley','ash',2)
appendAndDelete('y','yu',2)

