CONVERSION_DICT = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand: str):
    """Provide the RNA complement given the DNA sequence

    :param dna_strand: str - the DNA sequence
    :return: str - the RNA sequence

    v2 uses dictionary with lookup in one line
    """

    return "".join(CONVERSION_DICT[nucleotide] for nucleotide in dna_strand)
