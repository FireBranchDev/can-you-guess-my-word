from constants import GAME_STATS


def game_stats(winner):
    """
    Stores a range of game statistics including win rate, loss ratio.

    Args:
        winner (bool): did the user win or not
    """

    with open(GAME_STATS, "a+", encoding="utf8") as file:
        file.close()

    with open(GAME_STATS, "r+", encoding="utf8") as file:

        data = file.readlines()
        # There currently is already statistics update it
        if len(data) >= 1:
            rows = data[0].split(",")
            wins = int(rows[0])
            if winner:
                wins += 1

            games_played = int(rows[1]) + 1

            stats = f"{wins}, {games_played}, {wins/games_played}, beach, hello\n"

            file.truncate(0)
            file.seek(0)
            file.write(stats)
        else:
            wins = 0
            if winner:
                wins = 1

            stats = f"{wins}, {1}, {wins/1}, beach, hello\n"

            updated_file = data
            updated_file.append(stats)

            file.truncate(0)
            file.seek(0)
            file.writelines(updated_file)


if __name__ == "__main__":
    game_stats(False)
    game_stats(True)
