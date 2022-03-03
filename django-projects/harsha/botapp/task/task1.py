
def check(str1):
    f=0
    for x in str1:
        if x =="(" and f!=-1:
            f+=1
        elif x==")"  :
                f-=1

    if f == 0:
        return True
    else:
        return False
print('()','-->',check('()'))
print(')(()))','-->',check(')(()))'))
print('(','-->',check('('))
print('(())((()())())','-->',check('(())((()())())'))
print(') test','-->',check(') test'))
print('hi())(','-->',check('hi())('))
print('(hello))','-->',check('(hello))'))
print('hello','-->',check('hello'))
print('(hell(0))','-->',check('(hell(0))'))

