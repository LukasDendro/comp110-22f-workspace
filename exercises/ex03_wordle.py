"""A more structured wordle."""
__author__: str = "730565579"


def contains_char(secretword: str, userletter: str) -> bool:
    """Function will find out if a single character matches that of a character in the secret word."""
    assert len(userletter) == 1
    index = 0
    while index < len(secretword):
        if secretword[index] == userletter:
            return True
        index += 1
    return False       


def emojified(userguess: str, secretguess: str) -> str:
    """Function that evaluates each letter of user guess through the previous function and then prints an emoji box on the basis of that evaluation."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(userguess) == len(secretguess)
    result_emoji: str = ""
    index: int = 0 
    while index < len(secretguess):
        if userguess[index] == secretguess[index]:
            result_emoji += GREEN_BOX
        elif contains_char(secretguess, userguess[index]) is True:
            result_emoji += YELLOW_BOX
        elif contains_char(secretguess, userguess[index]) is False:
            result_emoji += WHITE_BOX
        index += 1
    return result_emoji


def input_guess(lensecret) -> str:
    """Evaluates whether the length of a guess matches the length of the secret word."""
    user_guess: str = input(f"Enter a {lensecret} character word: ")
    while lensecret != len(user_guess):
        user_guess = input(f"That wasn't {lensecret} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    game_loop: int = 1
    secret_word: str = "codes"
    user_guess: str = ""
    while game_loop <= 6 and user_guess != secret_word:
        print(f"=== Turn {game_loop}/6 ===")
        user_guess = input_guess((len(secret_word)))
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            print(f"You won in {game_loop}/6 turns!")
        game_loop += 1
    if game_loop > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()