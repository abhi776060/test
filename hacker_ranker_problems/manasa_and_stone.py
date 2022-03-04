def stones(n, a, b):
    print(*sorted(set(x * a + (n - 1 - x) * b for x in range(n))))
# stones(2,2,3)
# stones(3,1,2)
stones(4,10,100)