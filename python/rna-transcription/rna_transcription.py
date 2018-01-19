def to_rna(dna_strand):
    transDict = {'G': 'C', 'C': 'G','T': 'A', 'A': 'U'}
    output = []
    for i in dna_strand:
        try:
            output.append(transDict[i])
        except:
            raise ValueError("Not a DNA String")
    return ''.join([i for i in output])