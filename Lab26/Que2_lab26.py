import numpy as np

#(i)
array=np.array([0,1,2,3,4,5,6,7,8,9])
print(array)
array1=np.arange(0,10)
print(array1)

#(ii)
bool_array=np.ones((3,3),dtype=bool)
print(bool_array)

#(iii)
arr=np.arange(10)
print(arr)
arr=arr[arr%2 ==1]
print(arr)
arr=np.array([x for x in range(2,51) if all(x%i!=0 for i in range(2, int(x**0.5)+1))])
print(arr)


#(iv)
rg=np.random.default_rng(20)
a=rg.random((4,5))
print(a)

#(v)
a= np.arange(0,9)
b=np.array([1,1,1,1,1,1,1,1])
print(np.hstack((a,b)))

#(vi)
a=np.arange(0,101)
b=np.array([x for x in range(2,101) if all(x%i!=0 for i in range(2, int(x**0.5)+1))])
#c=np.intersect1d(a,b)
#print(c)
#print(b)
print(np.intersect1d(a,b))
#(vii)
print(np.setdiff1d(a,b))

#(viii)
#print(np.where(a==b))

#(ix)

