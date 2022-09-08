"""EX01 - Chardle - A cute step toward Worlde."""
__author__ = "730574521"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + str(letter) + " in " + str(word))

instances_found: int = 0
if word[0] == letter:
    print(str(letter) + " found at index 0")
    instances_found = instances_found + 1
if word[1] == letter:
    print(str(letter) + " found at index 1")
    instances_found = instances_found + 1
if word[2] == letter:
    print(str(letter) + " found at index 2")
    instances_found = instances_found + 1
if word[3] == letter:
    print(str(letter) + " found at index 3")
    instances_found = instances_found + 1
if word[4] == letter:
    print(str(letter) + " found at index 4")
    instances_found = instances_found + 1

if instances_found == 0:
    print("No instances of " + str(letter) + " found in " + str(word))
if instances_found == 1:
    print("1 instance of " + str(letter) + " found in " + str(word))
if instances_found == 2:
    print("2 instances of " + str(letter) + " found in " + str(word))
if instances_found == 3:
    print("3 instances of " + str(letter) + " found in " + str(word))
if instances_found == 4:
    print("4 instances of " + str(letter) + " found in " + str(word))
if instances_found == 5:
    print("5 instances of " + str(letter) + " found in " + str(word))
