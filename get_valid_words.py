import doctest

from constants import ALL_WORDS


def get_valid_words(file_path=ALL_WORDS):
    """returns a list containing all valid words.

    Args:
        file_path (str): the path to the file containing the words

    Returns:
        array of strings: a list of all the valid words

    Note to test that the file is read correctly, use:
    >>> get_valid_words()[0]
    'aahed'
    >>> get_valid_words()[-1]
    'zymic'
    >>> get_valid_words()[10:15]
    ['abamp', 'aband', 'abase', 'abash', 'abask']
    >>> get_valid_words()[30:37]
    ['abies', 'abled', 'abler', 'ables', 'ablet', 'ablow', 'abmho']
    >>> get_valid_words()[-3]
    'zygon'
    >>> get_valid_words()[5]
    'abaci'
    """
    # read words from files and return a list containing all words that can be
    # entered as guesses
    words = []

    with open(file_path, "r", encoding="utf8") as file:
        data = file.readlines()
        for word in data:
            words.append(word.strip())

    return words


if __name__ == "__main__":
    doctest.testmod()
