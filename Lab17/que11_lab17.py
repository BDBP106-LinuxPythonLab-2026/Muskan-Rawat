L=[1,1,2,4,5,5,8,4,2,1]
duplicates=[] #an empty list in which duplicate elements will append.
for i in L:
    if L.count(i) > 1 and i not in duplicates: #L.count(i) will count the elements in "i"
        duplicates.append(i) #append the duplicate or the elements which occurred more than once.
print(duplicates)