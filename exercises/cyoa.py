"""Choose your own adventure program."""
__author__ = "730565579"

import random
THUMBS_UP = "\U0001F44D"
THUMBS_DOWN = "\U0001F44E"

player: str = ""
streak: int = 0
end: int = 0
points: int = 0


def main() -> None:
    """Mainframe of the function, two main functions game() and greet() are called here."""
    global points
    points = 0 
    greet()
    while end != 1:
        game()


def greet() -> None:
    """Greets the player and asks for their name which stores in a global variable."""
    global player
    print("Welcome to the coin flipping game!")
    player = input("What is your name? ")


def game() -> None:
    """Asks player for input and the decision to go three seperate ways."""
    global streak
    global end
    p_input: int = int(input(f"{player}, enter 1 for heads, 2 for tails, or any other number to end the game: "))
    coin: int = random.randint(1, 2)
    if p_input != 1 and p_input != 2:
        print(f"Game over, Goodbye {player}")
        print(f"You had a highscore of {streak}!")
        end = 1
    elif coin == 1:
        heads(p_input)
    elif coin == 2:
        tails(p_input)
        

def tails(input: int) -> None:
    """Determines whether the player got it right if its tails."""
    global points
    if input == 2:
        points += 1
        print(f"{player}, you guessed tails and were correct {THUMBS_UP}! You have guessed {points} times in a row!")
    else: 
        print(f"{player}, it wasn't heads {THUMBS_DOWN}! Your guessing streak has been set to 0.")
        points = streak_counter(points)


def heads(input: int) -> None:
    """Determines whther the player got it right if its tails."""
    global points
    if input == 1:
        points += 1
        print(f"{player}, you guessed heads and were correct {THUMBS_UP}! You have guessed {points} times in a row!")
    else: 
        print(f"{player}, it wasn't tails {THUMBS_DOWN}! Your guessing streak has been set to 0.")
        points = streak_counter(points)


def streak_counter(points: int) -> int:
    """Keeps the players highscore based off of whther the points variable is greater than the previous highscore."""
    global streak
    if points > streak:
        streak = points
        print(f"{player}, you have a new highscore of {streak} in a row!")
    else: 
        print(f"{player} you were {streak - points} tries away from beating your highscore!")
    points = 0
    return points


if __name__ == "__main__":
    main()