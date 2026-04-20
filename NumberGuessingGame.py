import random

print("===== Number Guessing Game =====")

while True:
    number = random.randint(1, 100)
    attempts = 0

    print("\n I have selected a number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You guessed it in", attempts, "attempts.")
            break

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break