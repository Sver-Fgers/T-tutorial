def reverse_complement_DNA(input_DNA):
    '''
    This function takes a DNA sequence as input and returns the reverse complement of the DNA sequence.
    '''
    # Define the dictionary of complementary bases
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    input_DNA = input_DNA.upper()
    # Reverse the input DNA sequence
    reverse_DNA = input_DNA[::-1]
    # Generate the reverse complement DNA sequence
    reverse_complement_DNA = ''.join([complement_dict[base] for base in reverse_DNA])
    return reverse_complement_DNA

def gc_content_DNA(input_DNA):
    '''
    This function takes a DNA sequence as input and returns the GC content of the DNA sequence.
    '''
    input_DNA = input_DNA.upper()
    # Count the number of G and C bases in the DNA sequence
    gc_count = input_DNA.count('G') + input_DNA.count('C')
    # Calculate the GC content of the DNA sequence
    gc_content = gc_count / len(input_DNA)
    return gc_content

def transcribe_DNA_to_RNA(input_DNA):
    '''
    This function takes a DNA sequence as input and returns
    the RNA sequence transcribed from the DNA sequence.
    '''
    # Replace T with U to transcribe DNA to RNA
    return input_DNA.replace('T', 'U')

def translate_RNA_to_protein(input_sequence):
    '''
    This function takes an RNA sequence as input and returns the protein sequence translated from the RNA sequence.
    '''
    if 'U' not in input_sequence:
        if 'T' in input_sequence:
            print ('Input sequence is DNA, not RNA. Transcribing DNA to RNA...')
            input_sequence = transcribe_DNA_to_RNA(input_sequence)
    # Define the dictionary of codons and corresponding amino acids
    codon_dict = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    # Translate the RNA sequence to protein
    protein = ''
    for i in range(0, len(input_sequence), 3):
        codon = input_sequence[i:i+3]
        protein += codon_dict[codon]
    return protein
