import random

print("=== Guess the Number Game ===")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
        break