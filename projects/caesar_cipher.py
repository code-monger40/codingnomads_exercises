plain_text = input("Enter message to encrypt: ")
shift = input("Enter in the shift number: ")

plain_text = plain_text.lower()
encrypted = ""

for char in plain_text:
    if char.islower():
        char_index = ord(char) - ord('a')
        # shift the current character by key positions
        char_shift = (char_index - shift) % 26 + ord('a')
        c_new = chr(char_shift)
        encrypted += c_new

print(f"Plain text message: {plain_text}")
print(f"Caesar cipher encrypted: {encrypted}")
# input=input('Input text here: ')
# data = list(input)
# for i, char in enumerate(data):
#     data[i] = chr((ord(char) + i) % 26)
#     output = ''.join(data)
# print(output)