from ask_for_guess import ask_for_guess
from ask_for_help import ask_for_help
from constants import ALL_WORDS, MAX_ATTEMPTS, TARGET_WORDS
from format_score import format_score
from game_stats import game_stats
from get_target_word import get_target_word
from get_valid_words import get_valid_words
from help import help
from is_correct import is_correct
from score_guess import score_guess
from track_guess_words import track_guess_words
from track_target_words import track_target_words


def play():
    """Code that controls the interactive game play"""
    target_word = get_target_word(TARGET_WORDS)
    valid_words = get_valid_words(ALL_WORDS)
    attempts = 0

    if ask_for_help():
        help()

    while attempts < MAX_ATTEMPTS:
        print(f"Attempts remaining {MAX_ATTEMPTS - attempts}")
        guess = ask_for_guess(valid_words)

        track_guess_words(guess)

        score = score_guess(guess, target_word)

        attempts += 1

        print("Result of your guess:")
        print(format_score(guess, score))

        if is_correct(score):
            winner_output = f"Winner: word guessed in {attempts} attempts"
            game_stats(winner=True)
            track_target_words(target_word)
            print(winner_output)
            break

    if attempts == MAX_ATTEMPTS:
        game_stats(winner=False)
        track_target_words(target_word)
        print(f"The word was {target_word}.")
