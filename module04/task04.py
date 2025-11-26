import random

secret_number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct! You guessed the number!")
        break
