def jumpingOnClouds(c, k):
    actual_c=c*2
    energy=100

    for x in range(0,len(c)+1,k):
        print(actual_c[x])
        if actual_c[x]==0:
            energy=energy-k-1
        if actual_c[x]==1:
            energy=energy
    print(energy)


# jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0],2)
jumpingOnClouds([0, 0,1,0],2)