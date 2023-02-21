from os import mkdir, path

from constants import GUESS_WORDS_TRACKER


def track_guess_words(guess_word):
    """
    Creates a file in order to track the number of times the guess word appears

    Args:
        guess_word (str): guess_word to be tracked
    """

    # Create game folder
    if not path.exists("./game"):
        mkdir("./game")

    # Create the file if it doesn't exist
    with open(GUESS_WORDS_TRACKER, "a+", encoding="utf8") as file:
        file.close()

    guess_words = []
    # Get a list of guess words that have statistics
    with open(GUESS_WORDS_TRACKER, "r", encoding="utf8") as file:
        data = file.readlines()
        data.sort()
        for column in data:
            rows = column.split(",")
            guess_words.append(rows[0])

        file.close()

    guess_words.sort()

    # Add the guess word if it doesn't exist
    if guess_word not in guess_words:
        with open(GUESS_WORDS_TRACKER, "r+", encoding="utf8") as file:
            data = file.readlines()
            data.sort()

            new_guess_stat = f"{guess_word}, 1\n"
            data.append(new_guess_stat)

            data.sort()

            file.truncate(0)
            file.seek(0)

            file.writelines(data)
            file.close()

        return

    # Find the relevant guess words and increment the counter
    with open(GUESS_WORDS_TRACKER, "r+", encoding="utf8") as file:
        data = file.readlines()

        data.sort()

        for index, column in enumerate(data):
            rows = column.split(",")
            if rows[0] == guess_word:
                file.truncate(0)
                file.seek(0)
                updated_target_stat = f"{guess_word}, {int(rows[1]) + 1}\n"
                data[index] = updated_target_stat

        data.sort()

        file.writelines(data)
        file.close()


if __name__ == "__main__":
    track_guess_words("beach")
