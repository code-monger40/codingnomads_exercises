# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = ""

#Find a alphabetic character using for loop
#Store letters in variable

for char in secret:
    if char.isalpha():
        solution += char

print(solution)
    
