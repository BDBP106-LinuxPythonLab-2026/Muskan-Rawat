#filter out the odd elements of Fibonacci series for the first n terms.

def Fib():
    a=0
    b=1
    series=[]
    for i in range(0,10):
        series.append(a)
        a,b = b, a+b
    return series

fib_series=Fib()

result=list(filter(lambda F: F % 2 == 0, fib_series))
print(result)


