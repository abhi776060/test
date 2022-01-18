def count_bits(arg):
    final_list=[]
    list1=[''.join(bin(x)) for x in range(arg+1)]
    for x in list1:
        a=x.count('1')
        final_list.append(a)

    print(final_list)

count_bits(15)