# Find the minimal nucleotide from a range of sequence DNA.
# https://www.youtube.com/watch?v=HYi4S11FvKE
def solution(S: str, P: list, Q: list) -> list:
    dna_values = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    result = []
    for i in range(len(P)):
        dna_slice = (S[P[i]: Q[i] + 1])
        if 'A' in dna_slice:
            result.append(dna_values['A'])
        elif 'C' in dna_slice:
            result.append(dna_values['C'])
        elif 'G' in dna_slice:
            result.append(dna_values['G'])
        elif 'T' in dna_slice:
            result.append(dna_values['T'])
    return result

