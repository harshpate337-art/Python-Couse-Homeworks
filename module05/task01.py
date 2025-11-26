import random

num_dice = int(input("How many dice do you want to roll? "))

total = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)
    total += roll

print(f"The sum of the dice rolls is: {total}")
