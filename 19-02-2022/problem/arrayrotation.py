def circularArrayRotation(a, k, queries):
    # Write your code here
    new_a=a
    i=0
    for x in range(k):
        new_a=list(new_a[len(new_a)-1:])+new_a[:len(new_a)-1]
        i+=1
        if k ==i:
            for x in queries:
                yield new_a[x]
circularArrayRotation([1,2,3],2,[0,1,2])