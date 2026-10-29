import time
import math

def measure_time(func):
    def wrapper(*args, **kwargs):
        begin=time.time()
        func(*args, **kwargs)
        end=time.time()
        print("total time taken is s: ", end - begin)
    return wrapper

@measure_time
def fact(n):
    time.sleep(3)
    print(math.factorial(n))


fact(50)

