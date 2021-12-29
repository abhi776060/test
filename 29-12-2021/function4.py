def outer_func():
    def inner_func():
        print("hai, abhishek!")
    return inner_func()
outer_func()