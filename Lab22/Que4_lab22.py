
def check_positive(func):
    def wrapper():
        store=func()
        if store > 0:
            print("positive")
        elif store == 0:
            print("zero")
        else:
            print("must be positive")
    return wrapper

@check_positive
def check_sign():
    print("checking...")
    return int(input('enter a integer:'))

check_sign()
