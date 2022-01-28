'''
Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206
Explainaton:
picking 5 from the 1st list, 9 from the 2nd list  10 from 3rd list (5*5+9*9+10*10)=206
'''

def maximize():
    range_width=input("enter range :").split(' ')
    range_list=[x for x in range(int(range_width[0]),int(range_width[1])+1)]
    first_list=sorted(list(map(lambda x: int(x),input("1st list :").split(' '))),reverse=True)
    second_list=sorted(list(map(lambda x: int(x),input("2 nd list :").split(' '))),reverse=True)
    third_list=sorted(list(map(lambda x: int(x),input("3rd list :").split(' '))),reverse=True )
    print(first_list,second_list,third_list)
    first=0
    for x in first_list:
        if x in range_list:
            first+=x
            break
    second=0
    for x in second_list:
        if x in range_list:
            second+=x
            break
    third=0
    for x in third_list:
        if x in range_list:
            third+=x
            break

    sum_all=(first**2+second**2+third**2)%1000
    print(sum_all)

    
maximize()
