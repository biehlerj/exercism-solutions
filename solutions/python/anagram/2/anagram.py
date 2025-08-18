def find_anagrams(word: str, candidates: list[str]):
    """Finds anagrams from a given word in a list of words

    :param word: str - the word to find anagrams of
    :param candidates: list[str] - list of potential anagrams
    :return: list[str] - list of anagrams
    """
    return [
        candidate
        for candidate in candidates
        if candidate.casefold() != word.casefold()
        and sorted(candidate.casefold()) == sorted(word.casefold())
    ]
