# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

string = input("Enter a word or a phrase: ")
letter = input("Enter a letter: ")

if letter in string:
    print(string.index(letter))
else:
    print("Index not found!")