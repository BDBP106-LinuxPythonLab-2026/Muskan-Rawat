import re

ambiguous_dna= 'ATCG'
dna= 'ATCGCGYAATTCAC'

if re.findall(ambiguous_dna,dna):
    print("ambiguous bases are present")
else:
    print("ambiguous bases are not present")