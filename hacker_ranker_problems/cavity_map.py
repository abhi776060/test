def cavityMap(grid):
    # Write your code here
    for i in range(len(grid)):
        for j in range(len(grid[i])-2):
            ele1,ele2,ele3=grid[i][j:j+3]
            if ele1 <ele2 and ele3<ele2 and ele1>ele3:
            #   print(grid[i][:j+1]+"X"+grid[i][j+2:])
                grid[i]=grid[i][:j+1]+"X"+grid[i][j+2:]
              
              

    print(grid)
# cavityMap(['989','191','111'])
cavityMap(['1112','1912','1892','1234'])

