
# kilometers to drive
# liters-per-kilometer usage of the car
# price per liter of fuel

drive = input("Enter the miles of the trip: ")
mpg = input("Enter the miles per gallon of the car: ")
price_gallon = int(drive)/int(mpg)

print(f"Price per mile:${price_gallon}")
