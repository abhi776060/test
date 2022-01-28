'''
Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =55+45+40+60=200
'''
def calculate_price():
    total_available_shoes_size=int(input("enter available shoes at your store:"))
    size_list=[]
    for x in range(total_available_shoes_size):
        size_list.append(int(input(f"enter {x+1} shoe size: " )))

    chart={}
    i=0
    while True:
        try:
            size_price=input("enter size and its price ").split(' ')
            size=int(size_price[0])
            try:
                price=int(size_price[1])
            except:
                price=0
           
            finally:
                if size in size_list :
                    if size in chart.keys() :
                        chart[size].add(price)
                    else:
                        chart[size]={price}
            i+=1
        except:
            break
    total_price=0
    for x in chart.values():
        for y in x:
            total_price+=y
    print(total_price)
    print(chart)

    
calculate_price()

