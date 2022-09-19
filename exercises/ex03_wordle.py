"""Structured Wordle."""
__author__ = "730574521"


def contains_char(searched_through: str, searched_for: str) -> bool:
    """Returns whether or not the single character is contained in the multiple character string."""
    assert len(searched_for) == 1
    index: int = 0
    while index < len(searched_through):
        if searched_through[index] == searched_for[0]:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emoji comparing the guessed word to the secret word using the contains_char function."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emojis: str = ""
    while i < len(secret):
        contained: bool = contains_char(secret, guess[i])
        if contained == True:
            if guess[i] == secret[i]:
                emojis += GREEN_BOX
            else:
                emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        i += 1
    return emojis


def input_guess(expected_length: int) -> str:
    """Returns whether or not the guess is the expected length."""
    guess: str = input(f"Enter a {str(expected_length)} char word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {str(expected_length)} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn_number: int = 1
    guess: str = ""
    while turn_number < 7 and guess != secret:
        print(f"=== Turn {str(turn_number)}/6 ===")
        guess: str = input_guess(len(secret))
        emojis: str = emojified(guess, secret)
        print(str(emojis))
        if guess == secret:
            print(f"You won in {str(turn_number)}/6 turns!")
        if guess != secret and turn_number == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turn_number += 1


if __name__ == "__main__":
    main()