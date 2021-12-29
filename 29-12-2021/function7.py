def outer(number):
    def inner():
        return number+5
    return inner()
print(outer(5))
