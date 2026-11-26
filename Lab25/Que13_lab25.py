import re


dna= 'ACTNGCATRGCTACGATSCGAWTCG'


x= re.split(r'[^ATCG]', dna)  #ATGC with ^ is a negation(NOT) operator so it will print those bases which are not ATGC.
#basically ^(NOT)ATGC.
print(x)