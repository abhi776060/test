cache={i:i for i in range(12)}
def solve(i):
    global cache
    if i not in cache:
        cache[i] = max(solve(i//2)+solve(i//3)+solve(i//4), i)
    return cache[i]
while True:
    try:
        n=int(input(' enter number'))
    except:break
    print(solve(n))