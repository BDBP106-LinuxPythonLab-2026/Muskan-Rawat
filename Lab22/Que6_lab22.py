
import time
import math
def measure_time(func):
    def wrapper(*args,**kwargs):
        begin=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print("the time taken for the code to run is: ", end - begin)
        return result
    return wrapper

@measure_time
def population_growth(initial,rate,Time):
    def exponential_growth():

        formula= initial * math.pow((1+rate),Time)
        return formula
    a=exponential_growth()
    print(a)
    return a

initial=int(input('enter the initial population: '))
rate=int(input('enter the rate at which the population increased: '))
Time=int(input('enter the time: '))
k=population_growth(initial,rate,Time)
print('The population is equal to: ',k)


