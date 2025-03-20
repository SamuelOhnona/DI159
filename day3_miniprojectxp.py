## creating a Hangman game

import random

# List of words for the game
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)  # Randomly select a word from the list

# Initialize variables
guessed_word = ['_'] * len(word)  # List to keep track of guessed letters (initially all underscores)
guessed_letters = []  # List to store guessed letters
wrong_guesses = 0  # Counter for wrong guesses
max_wrong_guesses = 6  # Maximum number of wrong guesses (head, body, arms, legs)
hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]  # Hangman body parts

# Function to display the current state of the word
def display_word():
    print("Current word: ", " ".join(guessed_word))

# Function to display the hangman state (number of wrong guesses)
def display_hangman():
    if wrong_guesses == 0:
        print("No parts yet!")
    else:
        print(f"Wrong guesses: {wrong_guesses} - {hangman_parts[wrong_guesses - 1]}")

# Game loop
while wrong_guesses < max_wrong_guesses:
    display_word()  # Show the current word with blanks or filled letters
    display_hangman()  # Show the current hangman state

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Check if the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the letter has been guessed already
    if guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'. Try again.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        # Fill in the correct positions
        for index, letter in enumerate(word):
            if letter == guess:
                guessed_word[index] = guess
        print(f"Good guess! '{guess}' is in the word.")
    else:
        # Incorrect guess, increase wrong guesses counter
        wrong_guesses += 1
        print(f"Oops! '{guess}' is not in the word.")

    # Check if the player has guessed the word completely
    if "_" not in guessed_word:
        display_word()
        print("Congratulations, you guessed the word!")
        break

# If the player has used up all wrong guesses
if wrong_guesses == max_wrong_guesses:
    print(f"Game over! The word was '{word}'.")