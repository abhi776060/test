
def chocolates(N, C, M):
    
    total = int(N/C)
    
    empty_wrapper = total
    
    while empty_wrapper >= M:
        
        temp = int(empty_wrapper/M)
        
        total = total + temp
        
        empty_wrapper = empty_wrapper - (temp*M) + temp
    
    return total
print(chocolates(10,2,5))