# Write a script that takes three strings from the user
# and prints the longest string together with its length.
# 
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

# hello world greetings
message = input("Enter in a phrase: ")
message1 = input("Enter in a phrase: ")
message3 = input("Enter in a phrase: ")

if len(message) > len(message1) and len(message) > len(message3):
    print(len(message), message)
elif len(message1) > len(message) and len(message1) > len(message3):
    print(len(message1), message1)
elif len(message3) > len(message) and len(message3) > len(message1):
    print(len(message3), message3)
else:
    print("No clear max length!")

        



