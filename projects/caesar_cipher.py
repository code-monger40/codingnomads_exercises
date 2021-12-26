message = input("Enter message to encrypt: ")
shift = input("Enter in the shift number: ")

# shift_num = 7
# result = ""

# alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# cipher = "XYZABCDEFGHIJKLMNOPQRSTUVW"

message = message.lower()
int(shift)
data = list(message)
print(data)
for index, char in enumerate(data):
    data[index] = chr((ord(char) + shift) % 26)
    output = ''.join(data)
print(output)

# print(message - shift % 26)

# for index, letter in enumerate(alphabet):
#     result += index + shift_num

# print(result)

# input=raw_input('Input text here: ')
#     data = list(input)
#     for i, char in enumerate(data):
#         data[i] = chr((ord(char) + shift) % 26)
#     output = ''.join(data)
#     return output