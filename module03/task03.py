# Hemoglobin level checker

# Ask for biological gender and hemoglobin level
gender = input("Enter your biological gender (male/female): ").lower()
hemoglobin = float(input("Enter your hemoglobin level (g/L): "))

# Check and print the result based on gender
if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin level is low.")
    elif hemoglobin <= 155:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin level is low.")
    elif hemoglobin <= 167:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
else:
    print("Invalid input for gender. Please enter 'male' or 'female'.")
