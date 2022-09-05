"""EX02 - One Shot Wordle - Another step towards Wordle."""
__author__ = "730565579"
secret_word: str = "computer"
user_guess: str = input(f"What is your {len(secret_word)} letter guess? ")
while len(user_guess) != len(secret_word):
    user_guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")

index_guess: int = 0 
result_emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while index_guess < len(secret_word):
    if user_guess[index_guess] == secret_word[index_guess]:
        result_emoji += GREEN_BOX
    else:
        char_exists: bool = False
        secret_index: int = 0
        while char_exists == False and secret_index < len(secret_word):
            if user_guess[index_guess] == secret_word[secret_index]:
                char_exists = True
            else:
                secret_index += 1
        if char_exists == True:
            result_emoji += YELLOW_BOX
        else:
            result_emoji += WHITE_BOX
    index_guess += 1

print(result_emoji)
if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

