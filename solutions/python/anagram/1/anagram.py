def find_anagrams(word: str, candidates: list[str]):
    """Finds anagrams from a given word in a list of words

    :param word: str - the word to find anagrams of
    :param candidates: list[str] - list of potential anagrams
    :return: list[str] - list of anagrams
    """
    word_lower = word.lower()
    sorted_word = sorted(word_lower)
    anagrams: list[str] = []

    for candidate in candidates:
        candidate_lower = candidate.lower()

        if candidate_lower == word_lower:
            continue
        if sorted(candidate_lower) == sorted_word:
            anagrams.append(candidate)

    return anagrams
