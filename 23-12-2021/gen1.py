def topten():
    return 10

top=topten()
print(top)

def topfive():
    for x in range(10):
        yield x

top1=topfive()
# print(top1)#same
print(iter(top1))
# for x in top1:
#     print(x)
print(next(top1))

print(next(top1))
print(next(top1))