from constants import GUESS_ATTEMPT_MSG, INVALID_GUESS_ATTEMPT_MSG, WORD_LENGTH


def ask_for_guess(valid_words: list[str]) -> str | None:
    """Requests a guess from the user directly from stdout/in and ensures the
    word is valid and mets the critera.


    Args:
        valid_words : list : list of valid words

    Return:
        string : user's guess
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
