from constants import GUESS_ATTEMPT_MSG, INVALID_GUESS_ATTEMPT_MSG, WORD_LENGTH


def ask_for_guess(valid_words=None):
    """Requests a guess from the user directly from stdout/in and ensures the
    word is valid and mets the critera.


    Args:
        valid_words : list : list of valid words

    Return:
        string : user's guess
    """
    valid_guess = False

    while not valid_guess:
        guess = input(GUESS_ATTEMPT_MSG)

        while len(guess) != WORD_LENGTH:
            print(INVALID_GUESS_ATTEMPT_MSG)
            guess = input(GUESS_ATTEMPT_MSG)

        if guess.lower() in valid_words:
            valid_guess = True
            return guess.lower()

        print(INVALID_GUESS_ATTEMPT_MSG)


if __name__ == "__main__":
    print(ask_for_guess())
