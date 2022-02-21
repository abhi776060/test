def repeatedString(s, n):
    # Write your code here
    m=n//len(s)
    new_updated_str=s*(m+1)
    print(new_updated_str)
    list1=[]
    for index in range(n):
        list1.append(new_updated_str[index])
    accurences=list1.count('a')
    print(accurences)
# repeatedString('''a''',1000000000000)
# repeatedString('aba',10)
