import re
dna_seq= 'ATCGCGAATTCAC'
pattern= 'GAATTC'

if re.findall(pattern,dna_seq):
    print("DNA contain an EcoR1 restriction site")
else:
    print("DNA contain an EcoR1 restriction site")