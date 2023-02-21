MISS = 0  # _-.: letter not found ⬜
MISPLACED = 1  # O, ?: letter in wrong place 🟨
EXACT = 2  # X, +: right letter, right place 🟩

MAX_ATTEMPTS = 6
WORD_LENGTH = 5

ALL_WORDS = "word-storage/all_words.txt"
TARGET_WORDS = "word-storage/target_words.txt"

TARGET_WORDS_TRACKER = "game/target_words_tracker.txt"
GUESS_WORDS_TRACKER = "game/guess_words_tracker.txt"
GAME_STATS = "game/game_stats.txt"

GUESS_ATTEMPT_MSG = "Please enter your guess: "
INVALID_GUESS_ATTEMPT_MSG = "Please enter in a 5 letter English word"

CONSOLE_COLOUR_EXACT = "\033[1;32m"
CONSOLE_COLOUR_MISPLACED = "\033[93m"
CONSOLE_COLOUR_MISS = "\033[97m"

CONSOLE_COLOUR_RESET = "\x1b[0m"
