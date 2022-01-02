# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user
print("Let's play hangman! Guess the following word...")
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input
# Allow only single-character alphabetic input
hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word = "district"
blanks = len(word) * ["_ "]
tries = 6
wrong_letters = []
hangman = [""]
print("".join(blanks))

print(type(blanks))

# for i in hangman_pics[l]:
#     print()

while len(wrong_letters) != tries:
    word = "district"
    guess = input("\nGuess a letter: ")
    if len(guess) != 1 and guess.isalpha():
        print("Please only input one alphabetic character")
    if guess not in word:
        wrong_letters.append(guess)
        print(hangman_pics[len(wrong_letters)])
    for index, letter in enumerate(word):
        if letter != "_" and guess == letter:
            blanks[index] = letter
    wins = True
    for strings in blanks:
      if "_" in strings:
        wins = False
    if wins == True:
      print("\nYOU WON!")
      print(f"{word}")
      break

    print("".join(blanks))

if len(wrong_letters) == tries:
  print("\nGame over...")

# Create a counter for how many tries a user has
    
            
# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it
