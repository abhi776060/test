def jumpingOnClouds(c):
    # Write your code here
    n=len(c)
    ans = 0
    i = 0
    while i < n - 1:
        print(i)
        if i + 2 >= n or c[i + 2] == 1:
            i = i + 1
            ans = ans + 1
        else:
            i = i + 2
            ans = ans + 1
    print(ans)
jumpingOnClouds([0,0,0,0,1,0,0,1,1,0])