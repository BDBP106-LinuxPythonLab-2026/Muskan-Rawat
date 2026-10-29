
def count_calls(func):
    count=0

    def wrapper():
        nonlocal count
        func()
        count+=1
        print("the function called",count,"times")
    return wrapper

@count_calls
def say_hi():
    print("hi!")

say_hi()
say_hi()
say_hi()
