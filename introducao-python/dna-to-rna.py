def dna_to_rna(dna):
    return dna.replace('T', 'U')
    
dna_to_rna2 = lambda dna: dna.replace('T', 'U')
print(dna_to_rna2('GACT'))