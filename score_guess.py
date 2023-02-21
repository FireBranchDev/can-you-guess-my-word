import doctest

from constants import MISS, MISPLACED, EXACT


def score_guess(guess_word, target_word):
    """given two strings of equal length, returns a tuple of ints representing
    the score of the guess
    against the target word (MISS, MISPLACED, or EXACT)
    Here are some example (will run as doctest):

    Args:
        guess_word : string : word guessed
        target_word : string : word randomly chosen

    Returns:
        (int, int, int, int, int) : Used to carry the result
            of the user's guess.

    >>> score_guess('hello', 'hello')
    (2, 2, 2, 2, 2)
    >>> score_guess('drain', 'float')
    (0, 0, 1, 0, 0)
    >>> score_guess('hello', 'spams')
    (0, 0, 0, 0, 0)

    Try and pass the first few tests in the doctest before passing these tests.
    >>> score_guess('gauge', 'range')
    (0, 2, 0, 2, 2)
    >>> score_guess('melee', 'erect')
    (0, 1, 0, 1, 0)
    >>> score_guess('array', 'spray')
    (0, 0, 2, 2, 2)
    >>> score_guess('train', 'tenor')
    (2, 1, 0, 0, 1)
    >>> score_guess('hello', 'rhino')
    (1, 0, 0, 0, 2)
    >>> score_guess('moody', 'rhino')
    (0, 1, 0, 0, 0)
    >>> score_guess('zebra', 'zonal')
    (2, 0, 0, 0, 1)

    >>> score_guess('hello', 'hello')
    (2, 2, 2, 2, 2)
    >>> score_guess('hello', 'looks')
    (0, 0, 1, 0, 1)
    >>> score_guess('hello', 'rainy')
    (0, 0, 0, 0, 0)
    >>> score_guess('melee', 'erect')
    (0, 1, 0, 1, 0)
    >>> score_guess('papal', 'earth')
    (0, 2, 0, 0, 0)
    >>> score_guess('duded', 'caddy')
    (1, 0, 2, 0, 0)
    """
    # You must use this convention as test automation will be validating your
    #  scorer
    letters_remaining = {}
    score_location = {}
    score_result = []

    # count how many times a letter appears in the target word
    for letter in target_word:
        letters_remaining[letter] = letters_remaining.get(letter, 0) + 1

    for letter in guess_word:
        score_location[letter] = []

    for letter_position, letter in enumerate(guess_word):
        if letter in target_word:
            if letters_remaining[letter] > 0:
                while letters_remaining[letter] > 0:
                    if letter == target_word[letter_position]:
                        score_result.append(EXACT)
                        score_location[letter].append((letter_position, EXACT))
                        letters_remaining[letter] -= 1
                        break
                    score_result.append(MISPLACED)
                    score_location[letter].append((letter_position, MISPLACED))
                    letters_remaining[letter] -= 1
                    break
            elif letter == target_word[letter_position]:
                score_result.append(EXACT)
                score_location[letter].append((letter_position, EXACT))

                for item in score_location.items():
                    if item[0] == letter:
                        for k in item[1]:
                            if k[0] == letter_position:
                                break
                            score_result[k[0]] = MISS
            else:
                score_result.append(MISS)
                score_location[letter].append((letter_position, MISS))
        else:
            score_result.append(MISS)
            score_location[letter].append((letter_position, MISS))

    return tuple(score_result)


if __name__ == "__main__":
    doctest.testmod()
