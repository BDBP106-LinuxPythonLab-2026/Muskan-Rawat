S="        Whitespace characters from a string          "

# first split() cuts the whitespaces and separates it into a list separated by a single commas.
#join(), it takes the list which was separated by the split and joins it all together in a single string.
# " " before .join() puts this single space between each word which was earlier separated as list.

a = " ".join(S.split())
print(a)
