# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

message = input("Enter a word or a phrase: ")

vowels = "aeiou"
a = 0
e = 0
i = 0
o = 0
u = 0
for vowel in message:
    if vowel == "a":
        a += 1
    elif vowel == "e":
        e += 1
    elif vowel == "i":
        i += 1
    elif vowel == "o":
        o += 1
    elif vowel == "u":
        u += 1
    
if a == 0:
    pass
else:
    print(f"a vowel total was {a}")
if e == 0:
    pass
else:
    print(f"e vowel total was {e}")
if i == 0:
    pass
else:
    print(f"i vowel total was {i}")
if o == 0:
    pass
else:
    print(f"o vowel total was {o}")
if u == 0:
    pass
else:
    print(f"u vowel total was {u}")