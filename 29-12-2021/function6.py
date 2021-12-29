def factorial(func):
    if type(func) is not int:
        raise TypeError("please enter integer number")
    if func < 0:
        raise ValueError("number shouldnot be negative number")

    def inner(func):
        if func <=1:
            return 1
        return func*inner(func-1)
    return inner(func)
print(factorial(5))