def magic_square_test(my_matrix):
    iSize = len(my_matrix[0])
    sum_list = []
    
    #Horizontal Part:
    sum_list.extend([sum (lines) for lines in my_matrix])   

    #Vertical Part:
    for col in range(iSize):
        sum_list.append(sum(row[col] for row in my_matrix))
    
    #Diagonals Part
    result1 = 0
    for i in range(0,iSize):
        result1 +=my_matrix[i][i]
    sum_list.append(result1)  
    
    result2 = 0
    for i in range(iSize-1,-1,-1):
        result2 +=my_matrix[i][i]
    sum_list.append(result2)

    if len(set(sum_list))>1:
        return False
    return True
a=[[4,5,8],
[2,4,1],
[1,9,7]]

print(magic_square_test(a))