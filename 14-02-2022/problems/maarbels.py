n=int(input('enter a number'))
for i in range(n):
    n,b=map(int,input().split())
    r1=1
    for i in range(1,b):
        r1=r1*(n-b+i)//(i)
    print(int(r1))