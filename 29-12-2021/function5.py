def outer_function(func):
    def inner():
        print(f"hai {func}")
    return inner()
outer_function("abhishek")