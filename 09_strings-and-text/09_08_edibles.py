# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

item1 = s[5:13]
item2 = s[25:32]
item3 = s[57:67]
item4 = s[68:-1]

print(item1)
print(item2)
print(item3)
print(item4)