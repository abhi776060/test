
def repeatedString(s, n):
    # Write your code here
    
    x,y = divmod(n,len(s))
    return s[:y].count("a")*(x+1) + s[y:].count("a")*x
print(repeatedString('aba',10))