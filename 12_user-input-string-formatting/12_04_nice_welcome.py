# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

while True:
    name = input("Please enter your name: ")
    if " " in name:
        firstname = name.split()
        print(f"Hold there {firstname[0].capitalize()}... I only wanted your first name!")
    else:
        print(f"Welcome {name.capitalize()} personally to my new script")