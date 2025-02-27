import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts_remaining = 7

    print("Hello, welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print("Try to guess it; you have 7 attempts.")

    while attempts_remaining > 0:
        print(f"\nYou have {attempts_remaining} attempts remaining.")
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print(f"Congrats, you guessed the number in {7 - attempts_remaining + 1} attempts!")
            return

        attempts_remaining -= 1

    print(f"\nYou ran out of attempts! The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()