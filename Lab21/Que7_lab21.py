#to calculate the GC% in DNA


def analyse_dna(sequence):
    dna_seq=sequence.upper()
    def gc_content():
        A= dna_seq.count("A")
        T= dna_seq.count("T")
        G= dna_seq.count("G")
        C= dna_seq.count("C")
        AT_content= A + T
        GC_content= G + C
        total_content= A + T + G + C
        percentage=((GC_content) / total_content) * 100
        return percentage

    GC_content=gc_content()
    AT_content= 100 - GC_content
    
    if AT_content > GC_content:
       print("AT is richer")
    else:
        print("GC is richer")
    return GC_content

seq=input('enter your sequence:')
k=analyse_dna(seq)
print(k)
