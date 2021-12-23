# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

phrase = input("Enter a word or a phrase: ")
symbol = input("Enter a symbol: ")

first_char = ""
for char in phrase:
    if char == phrase[0]:
        symbol_phrase = phrase.replace(char, symbol)

print(symbol_phrase)