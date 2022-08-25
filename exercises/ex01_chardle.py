"""EX01 - Chardle - A cute step towards Wordle!"""
__author__ = "730565579"
user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
user_letter: str = input("Enter a single character: ")
if len(user_letter) != 1:
    print("Error: Character must be a single character")
    exit()
num_letter: int = 0
print("Searching for " + user_letter + " in " + user_word)
if user_letter == user_word[0]:
    print(user_letter + " found at index 0")
    num_letter = num_letter + 1
if user_letter == user_word[1]:
    print(user_letter + " found at index 1")
    num_letter = num_letter + 1
if user_letter == user_word[2]:
    print(user_letter + " found at index 2")
    num_letter = num_letter + 1
if user_letter == user_word[3]:
    print(user_letter + " found at index 3")
    num_letter = num_letter + 1
if user_letter == user_word[4]:
    print(user_letter + " found at index 4")
    num_letter = num_letter + 1
if num_letter > 0:
    if num_letter == 1:
       print(str(num_letter) + " instance of " + user_letter + " found in " + user_word)
    else:
       print(str(num_letter) + " instances of " + user_letter + " found in " + user_word)
else:
    print("No instances of " + user_letter + " found in " + user_word)
