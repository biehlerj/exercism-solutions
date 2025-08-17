CONVERSION_DICT = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand: str):
    """Provide the RNA complement given the DNA sequence

    :param dna_strand: str - the DNA sequence
    :return: str - the RNA sequence
    """

    rna_strand = ""

    for nucleotide in dna_strand:
        if nucleotide in CONVERSION_DICT:
            rna_strand += CONVERSION_DICT[nucleotide]

    return rna_strand
