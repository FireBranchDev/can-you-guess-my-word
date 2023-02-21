import doctest

from constants import EXACT


def is_correct(score):
    """Checks if the score is entirely correct and returns True if it is

    Args:
        score : tuple of ints: score from user's guess word

    Returns:
        boolean: True if the score is correct, false if not


    Examples:
    >>> is_correct((1,1,1,1,1))
    False
    >>> is_correct((2,2,2,2,1))
    False
    >>> is_correct((0,0,0,0,0))
    False
    >>> is_correct((2,2,2,2,2))
    True
    >>> is_correct((2,2,2,1,2))
    False
    >>> is_correct((1,2,1,1,2))
    False
    >>> is_correct((2,1,2,1,1))
    False
    """
    return score == (EXACT, EXACT, EXACT, EXACT, EXACT)


if __name__ == "__main__":
    doctest.testmod()
