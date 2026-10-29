# interchange the even and odd components of a list.

L=[23,32,33,44,"BDBH101","hello","python",15, 1e-10, "True","hit"]

for i in range(len(L)):
    L[i], L[i+1]= L[i+1], L[i]
    print(L)