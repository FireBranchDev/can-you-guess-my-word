from constants import (
    CONSOLE_COLOUR_EXACT,
    CONSOLE_COLOUR_MISPLACED,
    CONSOLE_COLOUR_RESET,
    MAX_ATTEMPTS,
    WORD_LENGTH,
)


def help():
    """Provides help for the game"""

    print(
        "\nCan You Guess My Word is a console based game developed to test the users\n"
        + f"ability of guessing a {WORD_LENGTH} letter word within "
        + f"{MAX_ATTEMPTS} attempts.\n"
        + f'if the letter is in the correct spot it would have a {CONSOLE_COLOUR_EXACT}"*"{CONSOLE_COLOUR_RESET}\n'
        + "and if the letter is in the word...\n"
        + f'but not in the right spot it would have a {CONSOLE_COLOUR_MISPLACED}"+"{CONSOLE_COLOUR_RESET}\n'
        + 'and if the letter is not present it would have a "-".\n'
    )
