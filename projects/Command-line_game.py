# Ask the player for their name.
end_game = True
while end_game:
    name = input("Enter your name: ")
# Display a message that greets them and introduces them to the game world.
    print(f"Greetings! {name.capitalize()}. Welcome to the game... ")
    pickup_sword = ""
# Present them with a choice between two doors.
    while True:
        door = input("You have a two doors (left or right). Pick one... ")
# If they choose the left door, they'll see an empty room.
# In both cases, they have the option to return to the previous room or interact further.
        look_choice = ""
        take_sword = ""
        fight = ""
        take_sword2 = ""
        room_1_choice = ""
        if door == "left":
            print("Room is empty...")
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
            room_1_choice = input("You can look around or go back (Type Look or Back): ")
        if room_1_choice == "back":
            continue
        if room_1_choice == "look":
            print("You found a Sword!")
            take_sword = input("Take it or leave it? (Type Take or Leave): ")
        if take_sword == "take":
            pickup_sword = "take"
            take_sword2 = input("Picked up the sword! Contine looking? (Type Look or Back): ")
        if take_sword2 == "look":
            print("Room is empty returning to the main hallway...")
            continue
        if take_sword2 == "back":
            continue
        if take_sword == "leave":
            print("Returning back to the main hallway")
            continue
# If they choose the right door, then they encounter a dragon.
        if door == "right":
# When encountering the dragon, they have the choice to fight it.
            fight = input("You've just encoutered a DRAGON! (Type leave or fight): ")
        if fight == "leave":
            continue
# If they have the sword from the other room, then they will be able to defeat it and win the game.
        if fight == "fight" and pickup_sword == "take":
            end_game = False
            print("After an extensive battle...")
            print("Congrats! YOU WON!")
            break
# If they don't have the sword, then they will be eaten by the dragon and lose the game.
        if fight == "fight":
            end_game = False
            print("Dragon just ate you...")
            print("GAME OVER!")
            break