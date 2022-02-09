def designer_viewr(h,word):
    alpha_dict={}
    alpha=97
    for x in h:
        alpha_dict[chr(alpha)]=int(x)
        alpha+=1
    all_hieght=[]
    for x in word.lower():
        all_hieght.append(alpha_dict[x])
    sum=(max(all_hieght)*len(all_hieght))
    print(sum)

al='1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'.split()
designer_viewr(al,'abc')



