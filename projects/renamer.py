# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

import pathlib

#Enter the location you want to move
location = input("Enter file location: ")
location = pathlib.Path(location)
# Make the folder where pics are getting moved too
new_location = pathlib.Path("\\Users\\P3036391\\Desktop\\Brand_New_Folder")
# Checks if folder already exists or not 
new_location.mkdir(exist_ok=True)

# Iterate through input
for file in location.iterdir():
    # Contidtional is siffix ends with .png
    if file.suffix == ".png":
        # New variable creates a new path for each file
        new_filepath = new_location.joinpath(file.name)
        # Moves each file to the new path
        file.replace(new_filepath)