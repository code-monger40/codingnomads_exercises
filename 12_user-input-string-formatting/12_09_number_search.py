# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

number = 52
while True:
    message = input("Enter a number between 0 and 1,000,000,000: ")
    if int(message) != number:
        print("Try again")
    if int(message) == number:
        print(f"Number was: {number}")
        break