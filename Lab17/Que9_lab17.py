a=str(input("enter a word: "))
b=str(input("enter a word: "))

x=sorted(a)
y=sorted(b)

if x == y:
    print("anagrams")
else:
    print("not anagrams")