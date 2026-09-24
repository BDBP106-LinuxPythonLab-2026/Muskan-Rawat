word=str(input("enter a word: "))
x=(word)[::-1]
if x == word:
    print("it is a palindrome")
else:
    print("it is not a palindrome")