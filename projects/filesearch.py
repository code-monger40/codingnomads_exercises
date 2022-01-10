# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

from pathlib import Path

# Specify the folder
location = input("Enter path location: ")
# Specify the file type we want to search for
file_type = input("Input file type (ie .jpeg): ")
# Convert input to Path
location = Path(location)
# rglob iterates through directory including subfolders
for folder in location.rglob("*"):
    # if the suffix is equal to the input file type specified print the results 
    if folder.suffix == file_type:
        print(folder)