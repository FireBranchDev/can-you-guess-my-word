from constants import TARGET_WORDS_TRACKER


def track_target_words(target_word):
    """
    Creates a file in order to track the number of times the target word appears

    Args:
        target_word (str): target_word to be tracked
    """
    # Create the file if it doesn't exist
    with open(TARGET_WORDS_TRACKER, "a+", encoding="utf8") as file:
        file.close()

    target_words = []
    # Get a list of target words that have statistics
    with open(TARGET_WORDS_TRACKER, "r", encoding="utf8") as file:
        data = file.readlines()
        for column in data:
            rows = column.split(",")
            target_words.append(rows[0])

        file.close()

    # Add the target word if it doesn't exist
    if target_word not in target_words:
        with open(TARGET_WORDS_TRACKER, "r+", encoding="utf8") as file:
            data = file.readlines()
            data.sort()

            new_target_stat = f"{target_word}, 1\n"
            data.append(new_target_stat)

            data.sort()

            file.truncate(0)
            file.seek(0)

            file.writelines(data)
            file.close()

        return

    target_words.sort()

    # Find the relevant target words and increment the counter
    with open(TARGET_WORDS_TRACKER, "r+", encoding="utf8") as file:
        data = file.readlines()
        data.sort()

        for index, column in enumerate(data):
            rows = column.split(",")
            if rows[0] == target_word:
                file.truncate(0)
                file.seek(0)
                updated_target_stat = f"{target_word}, {int(rows[1]) + 1}\n"
                data[index] = updated_target_stat

        data.sort()

        file.writelines(data)
        file.close()


if __name__ == "__main__":
    track_target_words("catch")
