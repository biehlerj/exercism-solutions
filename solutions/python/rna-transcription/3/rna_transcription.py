CONVERSION_STR = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand: str):
    """Provide the RNA complement given the DNA sequence

    :param dna_strand: str - the DNA sequence
    :return: str - the RNA sequence

    v3 uses translate() with maketrans()
    """

    return dna_strand.translate(CONVERSION_STR)
