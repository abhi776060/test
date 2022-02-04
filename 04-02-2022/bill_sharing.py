def bonAppetit(bill, k, b):
    # Write your code here
    '''
    anna   brian 
    [2,4,6]  k=6   
    anna 2+4/2=3 
    total= 2+4+6/2=6
    bill-- array cost of each item
    k--anna doesn't eat
    b -- anna contributed money
    '''
    del bill[k]
    total_cost=0
    for x in bill:
        total_cost+=x
    equal_share=total_cost//2
    difference=abs(b-equal_share)
    if difference==0:
        print('Bon Appetit')
    else:
        print(difference)
bonAppetit([3,10,2,9],1,12)