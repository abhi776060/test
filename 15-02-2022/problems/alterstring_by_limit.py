
def appendAndDelete(s, t, k):
    # Write your code here
    s_len=len(s)
    t_len=len(t)
    i=1
    str1=''
    while i<=k:
        try:
            s[:i]==t[:i]
            s_len-=1
            t_len-=1
            i+=1
        except:
            pass
        else:
            if s_len<= k:
               str1="YES"
            else:
                str1="NO"
                break
    print(str1)

appendAndDelete('hackerhappy','hackerrank',9)