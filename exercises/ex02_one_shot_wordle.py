"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730574521"

secret: str = "python"

length: int = len(secret)

guess: str = input(f"What is your {length}-letter guess? ")

while len(guess) != len(secret):
    guess = input(f"That was not {length} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
emoji: str = ""

while index < len(secret):
    if guess[index] == secret[index]:
        emoji += GREEN_BOX
    else:
        in_word: bool = False
        alternates: int = 0
        while not in_word and alternates < len(secret):
            if secret[alternates] == guess[index]:
                in_word = True
            else:
                alternates += 1
        if in_word:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    index += 1

print(emoji)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")