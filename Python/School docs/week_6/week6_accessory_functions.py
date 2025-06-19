
import random

def create_random_genome(genome_size: int, gc_percent: float) -> str:
    '''
    Generates a random genomic DNA sequence of a specified size and GC content.

    Parameters:
    -----------
    genome_size : int
        The desired length of the genomic sequence (must be a positive integer).
    gc_percent : float
        The GC content as a decimal (e.g., 0.4 for 40% GC content).
        Must be between 0 and 1 (inclusive).

    Returns:
    --------
    str
        A string containing the random genomic DNA sequence.

    Raises:
    -------
    ValueError
        If genome_size is not a positive integer or gc_percent is not between 0 and 1.

    Example:
    --------
    >>> create_random_genome(10, 0.5)
    'ATGCGTACGA'

    >>> create_random_genome(20, 0.3)
    'AATGTTTAAGGTTATATTGA'
    
    Notes:
    ------
    - The generated sequence will contain only 'A', 'T', 'G', and 'C'.
    - The GC content of the sequence may slightly vary due to random generation but will be close to the specified percentage.

    '''
    
    if genome_size <= 0:
        raise ValueError("Genome size must be a positive integer.")
    if not (0 <= gc_percent <= 1):
        raise ValueError("GC percent must be a float between 0 and 1 (inclusive).")
    
    # Calculate the number of G/C and A/T bases
    gc_count = int(genome_size * gc_percent)
    at_count = genome_size - gc_count
    
    # Create lists of G/C and A/T bases
    gc_bases = ['G', 'C']
    at_bases = ['A', 'T']
    
    # Randomly generate GC and AT sequences
    gc_sequence = random.choices(gc_bases, k=gc_count)
    at_sequence = random.choices(at_bases, k=at_count)
    
    # Combine and shuffle the sequences
    genome_sequence = gc_sequence + at_sequence
    random.shuffle(genome_sequence)
    
    # Return the final genomic sequence as a string
    return ''.join(genome_sequence)
