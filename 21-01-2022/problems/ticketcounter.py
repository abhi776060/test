'''
N people standing in the queue of a movie ticket counter. It is a weird counter, distributes tickets to first K people and then last K people and again first K people and so on. The task is to find the last person to get the ticket.

Example: Let N = 9, K = 3, starting queue will like {1, 2, 3, 4, 5, 6, 7, 8, 9}. After the first distribution queue will look like {4, 5, 6, 7, 8, 9}. And after the second distribution queue will look like {4, 5, 6}. The last person to get the ticket will be 6.

Input:
1. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
2. The first line of each test case contains two space-separated integers N and K.
Input:
2
9 3 {1 2 3} {4 5 6} {7 8 9}
25 7 {1 2 3 4 5 6 7} {8 9 10 11 12 13 14} {15 16 17 18 } {19 20 21 22 23 24 25}

Output:
6
15
'''
def straight(list1,num):
    list2=list1[num:]
    return list2
def forword(list1,num):
    list2=list1[:len(list1)-num]
    return list2

def find_last_person(person,ticket):
    queue=[x+1 for x in range(person)]
    list1=[]
    lenght=person//ticket
    
    for x in range(lenght):
        queue=straight(queue,ticket)
        if len(queue) >ticket:
            list1.append(queue)
        else:
            print(queue[0])
            break
        queue=forword(queue,ticket)
        if len(queue)>ticket:
            list1.append(queue)
        else:
            print(queue[-1])
            break
    
    
    
find_last_person(25,7)