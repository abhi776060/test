'''
greeting function can pass to display function as a arguments

'''
def greeting():
    return "abhishek"

def display(func):

    def inner():
        print("the current user is", end=' ')
        print(func())
    return inner()
# display(greeting)
display(greeting)