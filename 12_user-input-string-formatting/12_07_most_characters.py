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
# longest = ["hello", "world", "greetings"]
# print(max(longest))
longest_word = ""
word_count = 0
for word in message.split():
    print(word)
        
    # print(longest_word)
    # if len(longest_word) > len(word):
        

# print(longest_word)


