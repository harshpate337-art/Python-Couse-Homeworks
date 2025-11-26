numbers = []

while True:
    user_input = input("Enter a number (leave blank to stop): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

numbers.sort(reverse=True)

top_five = numbers[:5]

print("Five greatest numbers (largest to smallest):")
for num in top_five:
    print(num)
