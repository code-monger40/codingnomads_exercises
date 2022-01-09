# plain_text = input("Enter message to encrypt: ")
# shift = input("Enter in the shift number: ")

# plain_text = plain_text.lower()
# encrypted = ""

# for char in plain_text:
#     if char.islower():
#         char_index = ord(char) - ord('a')
#         # shift the current character by key positions
#         char_shift = (char_index - shift) % 26 + ord('a')
#         c_new = chr(char_shift)
#         encrypted += c_new

# print(f"Plain text message: {plain_text}")
# print(f"Caesar cipher encrypted: {encrypted}")
# input=input('Input text here: ')
# data = list(input)
# for i, char in enumerate(data):
#     data[i] = chr((ord(char) + i) % 26)
#     output = ''.join(data)
# print(output)

result = ""

# Get the plain text that will become encrypted
message = input("\nEnter a message: ")

# Get the shift pattern (the amount of characters to shift +-)
shift = input("\nEnter a shift patter (positive or negative integer): ")

# Ensure user input is correct type...
# If the shift pattern is not an int, reject with a message.
if shift.isnumeric():
    shift = int(shift)
else:
    print(f"{shift} is not an int. Defaulting to 3!")
    shift = 3


# transverse the plain text
for i in range(len(message)):
    # Get the current character
    char = message[i]

    # Encrypt uppercase characters in plain text
    if (char.isupper()):
        # Use ord function to convert character to int representation of unicode, then back to character with chr.
        this_char = chr((ord(char) + shift - 65) % 26 + 65)
        result += this_char
    # Encrypt lowercase characters in plain text
    else:
        this_char = chr((ord(char) + shift - 97) % 26 + 97)
        result += this_char

print("Plain Text : " + message)
print("Shift pattern : " + str(shift))
print("Cipher: " + result)