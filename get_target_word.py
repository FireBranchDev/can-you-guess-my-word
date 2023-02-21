import doctest

from random import choice
from constants import TARGET_WORDS


def get_target_word(file_path=TARGET_WORDS, seed=None):
    """Picks a random word from a file of words

    Args:
        file_path (str): the path to the file containing the words

    Returns:
        str: a random word from the file

    How do you test that a random word chooser is choosing the correct words??
    Discuss in class!
    >>> get_target_word()
    'aback'
    >>> get_target_word()
    'zonal'
    >>> get_target_word()
    'yeast'
    >>> get_target_word()
    'wrong'
    >>> get_target_word()
    'donut'
    """
    # read words from a file and return a random word (word of the day)
    words = []

    with open(file_path, "r", encoding="utf8") as file:
        data = file.readlines()
        for word in data:
            if word not in words:
                words.append(word.strip())

    return choice(words)


if __name__ == "__main__":
    doctest.testmod()
