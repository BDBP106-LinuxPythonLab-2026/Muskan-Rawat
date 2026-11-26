import re

dna= 'ATCGCGAATTCAC'
pattern= 'GGACC|GGTCC'

if re.search(pattern,dna):
    print("Dna has an AvaII recognition site")
else:
    print("No Dna has an AvaII recognition site")