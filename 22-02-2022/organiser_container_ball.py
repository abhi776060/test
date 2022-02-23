def organizingContainers(container):
    Rows = []
    Cols = []

    for i in range(len(container)):
        Rows.append(sum(container[i]))
       
            
    N = [list(i) for i in zip(*container)]     
    print(N)
    for i in range(len(container)):
        Cols.append(sum(N[i]))
  
    Rows.sort()
    Cols.sort()
    if(Rows == Cols):
        print("Possible")
    else:
        print("Impossible")


# organizingContainers([[1,1],[1,1]])
# organizingContainers([[0,2],[1,1]])
organizingContainers([[1,3,2],[2,1,2],[3,3,3]])
# organizingContainers([[0,2,1],[1,1,1],[2,0,0]])

    