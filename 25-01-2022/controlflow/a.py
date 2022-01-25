'''             *
               * *
              *   *
             * * * *
            *       *
           *         *
'''
def pattren_a(arg):
    i=0
    while i<arg:
        if i==0:
            pass
        if i== arg//2:
            print('  '*(arg//2-2)+' *'*(arg//2+1))
        print(' '*(arg-i-1)+'  *'+' '*(2*i)+' *')
        i+=1

pattren_a(10)