'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

def spiralMatrixPrint( arr):
    
    top = 0
    bottom = len(arr)-1
    left = 0
    right = len(arr[0] )- 1

    
    dir = 0
    
    while (top <= bottom and left <=right):    
        if dir ==0:
            for i in range(left,right+1): 
                print (arr[top][i], end=" ")

            
            top +=1
            dir = 1

        elif dir ==1:
            for i in range(top,bottom+1):
                print (arr[i][right], end=" ")

            
            right -=1 
            dir = 2
            
        elif dir ==2:
            for i in range(right,left-1,-1): 
                print (arr[bottom][i], end=" ")

            
            bottom -=1
            dir = 3
            
        elif dir ==3:
            for i in range(bottom,top-1,-1):
                print (arr[i][left], end=" ")
            
            left +=1
            dir = 0

array = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]

spiralMatrixPrint(array)