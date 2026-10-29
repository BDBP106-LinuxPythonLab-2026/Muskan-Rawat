
def greet_decorator(func):
    def wrapper():
        print("this is before calling the function")
        func()
        print("this is after calling the function")
    return wrapper

@greet_decorator
def message():
    print("This is my first attempt at using decorator")

message()