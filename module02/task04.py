# Ask the user for three integer numbers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate sum, product, and average
sum_numbers = num1 + num2 + num3
product = num1 * num2 * num3
average = sum_numbers / 3

# Print the results
print(f"The sum is {sum_numbers}")
print(f"The product is {product}")
print(f"The average is {average:.2f}")
