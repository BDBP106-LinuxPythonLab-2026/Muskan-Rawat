L=[1,1,1,2,3,3,6,5,5,5,8,7,3,9]
k=2
new_L=[]
for i in L:
    if L.count(i) > k:
        new_L.append(i)
print(new_L)