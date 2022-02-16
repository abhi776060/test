def jumpingOnClouds(c, k):
    energy=100
    for x in range(0,len(c),k):
        if c[x] == 0:
            
            energy=energy-(k+1)
            print(x,energy)
        else:
            
            energy=energy-1
            print(x,energy)
    
# jumpingOnClouds([0,0,1,0,0,1,1,0],2)
# jumpingOnClouds([0,0,1,0],2)
