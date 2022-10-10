"""A quiz that determines how big of a Kanye West fan a user is."""
__author__: "730574521"

from random import randint

points: int = 0
player: str = ""
GRINNING_EMOJI: str = "\U0001F60A"
TONGUE_EMOJI: str = "\U0001F61D"
CONFUSED_EMOJI: str = "\U0001F914"
HAPPY_EMOJI: str = "\U0001F604"


def main() -> None:
    """Entrypoint of the program."""
    greet()
    choice: int = 0
    global points
    global TONGUE_EMOJI
    global HAPPY_EMOJI
    print("To start, choose your first path.")
    print("Choice 1: Easy level - guess a number 1-10")
    print("Choice 2: Hard level - guess a number 1-100")
    print("Choice 3: Quit game.")
    choice = int(input("What is your choice? Write only the integer (1, 2, or 3) of the path you choose. "))
    if choice == 1:
        easy()
    if choice == 2:
        points = hard(points)
    if choice == 3:
        print(f"You have ended the game, {player}. You have collected {points} points. Have a nice day!{HAPPY_EMOJI}")
        quit()
    # Game loop
    i: int = 0
    while i < 1:
        print(f"Good job, {player}. You have collected {points} points{TONGUE_EMOJI}.")
        print("If you would like to play the easy level, type '1'.")
        print("If you would like to play the hard level, type '2'.")
        print("If you would like to quit, type '3'.")
        choice = int(input("What is your choice? "))
        if choice == 1:
            easy()
        if choice == 2:
            points = hard(points)
        if choice == 3:
            print(f"You have ended the game, {player}. You have collected {points} points. Have a nice day!{HAPPY_EMOJI}")
            i += 1


def greet() -> None:
    """Welcomes the player and asks for their name."""
    global player
    global GRINNING_EMOJI
    print(f"Welcome to the random number guessing game{GRINNING_EMOJI}!")
    print("In this game, you will be challenged with seeing how many numbers you can guess in a row.")
    player = input("What is your name? ")


def easy() -> None:
    """Allows a player to guess a randomly generated integer between 1 and 10."""
    global points
    global player
    global CONFUSED_EMOJI
    guess: int = 0
    print("You have selected the easy level. Guess a number between 1-10.")
    guess = int(input(f"What is your guess, {player}? "))
    secret: int = randint(1, 10)
    i: int = 0
    while i < 1:
        if guess != secret:
            guess = int(input(f"Your guess was incorrect{CONFUSED_EMOJI}, {player}. Try again: "))
            points -= 1
        else:
            if guess == secret:
                points += 10
                i += 1


def hard(x: int) -> int:
    """Allows a player to guess a randomly generated integer between 1 and 100."""
    global player
    global points
    global CONFUSED_EMOJI
    guess: int = 0
    print("You have selected the hard level. Guess a number between 1-100.")
    guess = int(input(f"What is your guess, {player}? "))
    secret: int = randint(1, 100)
    i: int = 0
    while i < 1:
        if guess != secret:
            guess = int(input(f"Your guess was incorrect{CONFUSED_EMOJI}, {player}. Try again: "))
            points -= 1
        else:
            if guess == secret:
                points += 100
                i += 1
                return points


if __name__ == "__main__":
    main()