from constants import GUESS_ATTEMPT_MSG, INVALID_GUESS_ATTEMPT_MSG, WORD_LENGTH


def ask_for_guess(valid_words: list[str]) -> str:
    """Prompts the player for a guess.

    Ensures player's guess to met the word requirements.

    Args:
        valid_words: A list of valid words.

    Returns:
        The user's guess.

    """
    guess = input(GUESS_ATTEMPT_MSG)
    while guess.lower() not in valid_words or len(guess) != WORD_LENGTH:
        print(INVALID_GUESS_ATTEMPT_MSG)
        guess = input(GUESS_ATTEMPT_MSG)
    else:
        return guess


if __name__ == "__main__":
    valid_words = ["beach", "flare", "value", "hello"]
    print(ask_for_guess(valid_words))
