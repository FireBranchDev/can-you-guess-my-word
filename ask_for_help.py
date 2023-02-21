def ask_for_help():
    """Ask the user whether they require assistance
    Args:

    Return:
        boolean : Does the user need help or not
    """
    print("Do you need help with Can You Guess My Word?")
    answer = input("y/n: ")
    return answer.lower() == "y"
