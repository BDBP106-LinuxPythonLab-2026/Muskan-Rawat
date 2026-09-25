L=[1,2,1,3,4,3,5,4,6,7,6,9]
m=1 #m is an element which we are removing.
for i in L:
    if i == m:
        L.remove(i)
print(L)
