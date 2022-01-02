# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import sys

number = 7
attempts = 3

while attempts > 0:
    message = input("Guess my favorite number: ")
    if int(message) == number:
        sys.exit("Congrats you are correct!!")
    elif int(message) != number:
        attempts -= 1
        print("No try again")

print("Sorry you've run out of attemmpts...")