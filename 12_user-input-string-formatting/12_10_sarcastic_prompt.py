# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

# alternating caps 
while True:
    message = input("Tell me your honest opinion: ")
    text = ""
    if message == "q":
        break
    for index, char in enumerate(message):
        if index % 2 == 0:
            text += char.upper()
        else:
            text += char.lower()
    print(text) 