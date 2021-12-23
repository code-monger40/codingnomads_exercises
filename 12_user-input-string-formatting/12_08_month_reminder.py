# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

message = input("Enter a number 1 to 12 to get the corresponding month: ")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for index, month in enumerate(months):
    if int(message) == index+1:
        print(month)
if int(message) > 12 or int(message) <= 0:
    print("Please enter a valid number!")

