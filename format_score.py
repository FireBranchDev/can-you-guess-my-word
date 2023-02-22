import doctest

from constants import (
    CONSOLE_COLOUR_EXACT,
    CONSOLE_COLOUR_MISPLACED,
    CONSOLE_COLOUR_MISS,
    CONSOLE_COLOUR_RESET,
    EXACT,
    MISPLACED,
)


def format_score(guess, score):
    """Formats a guess with a given score as output to the terminal.
    The following is an example output (you can change it to meet your own
    creative ideas, but be sure to update these examples)
    >>> print(format_score('hello', (0,0,0,0,0)))
    H E L L O
    - - - - -
    >>> print(format_score('hello', (0,0,0,1,1)))
    H E L L O
    - - - + +
    >>> print(format_score('hello', (1,0,0,2,1)))
    H E L L O
    + - - * +
    >>> print(format_score('hello', (2,2,2,2,2)))
    H E L L O
    * * * * *
    >>> print(format_score('rhino', (1,0,0,0,2)))
    R H I N O
    + - - - *
    >>> print(format_score('moody', (0,1,0,0,0)))
    M O O D Y
    - + - - -
    >>> print(format_score('gauge', (0,2,0,2,2)))
    G A U G E
    - * - * *
    """

    guess_formatted = ""
    for letter in guess.upper():
        guess_formatted = guess_formatted + letter + " "

    guess_score_format = " "
    for result in score:
        if result == EXACT:
            guess_score_format = guess_score_format + CONSOLE_COLOUR_EXACT + "* "
        elif result == MISPLACED:
            guess_score_format = guess_score_format + CONSOLE_COLOUR_MISPLACED + "+ "
        else:
            guess_score_format = guess_score_format + CONSOLE_COLOUR_MISS + "- "

    return (
        CONSOLE_COLOUR_RESET
        + guess_formatted.strip()
        + "\n"
        + guess_score_format.strip()
        + CONSOLE_COLOUR_RESET
    ).strip()


if __name__ == "__main__":
    doctest.testmod()
