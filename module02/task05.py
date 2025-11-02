# Ask the user for input in medieval units
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Conversion factors
LOTS_IN_POUND = 32
POUNDS_IN_TALENT = 20
GRAMS_IN_LOT = 13.3

# Convert everything to lots first
total_lots = (talents * POUNDS_IN_TALENT * LOTS_IN_POUND) + (pounds * LOTS_IN_POUND) + lots

# Convert lots to grams
total_grams = total_lots * GRAMS_IN_LOT

# Convert grams to kilograms and remaining grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

# Print the result
print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")
