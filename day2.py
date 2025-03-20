# EXERCISES XP MANDATORY

# 1

def display_function():
    print("Hey everyone, i am actually learning data analysis at Developer institute")

display_function()

# 2

def favorite_book(title):
    print(f"My favorite book is {title}")

favorite_book("Alice in wonderlands")

#3

# Define a function that accepts a city name and a country (with a default value)
def describe_city(city, country="France"):
    print(f"{city} is in {country}")

# Call the function with different cities
describe_city("Reykjavik", "Iceland")  # Example from the instructions
describe_city("Paris")  # Uses the default country (France)
describe_city("Tokyo", "Japan")  # Another example

#4

import random  # Import the random module

# Define a function that accepts a number and compares it with a random number
def guess_number(user_number):
    if 1 <= user_number <= 100:  # Ensure the number is within the valid range
        random_number = random.randint(1, 100)  # Generate a random number between 1 and 100

        # Compare the user's number with the random number
        if user_number == random_number:
            print("🎉 Success! You guessed the correct number!")
        else:
            print(f"Fail! Your number: {user_number}, Random number: {random_number}")
    else:
        print("Please enter a number between 1 and 100.")

guess_number(42)

#5

# Define a function that accepts a shirt size and a message
def make_shirt(size="Large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is: '{text}'")

make_shirt()

# Call the function to make a medium 
make_shirt(size="Medium")

# Call the function to make a custom shirt with a different message
make_shirt(size="Small", text="Code like a Pro!")

# Bonus: Call the function using keyword arguments
make_shirt(text="Keep Calm and Code", size="XL")


#6

# List of magicians' names
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Function to print each magician's name
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# Function to modify the list by adding "the Great" to each name
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

# Call make_great() to modify the original list
make_great(magician_names)

# Call show_magicians() to verify the list has been updated
show_magicians(magician_names)


#7

import random  # Import the random module

# Function to get a random temperature based on the season
def get_random_temp(season):
    """Returns a random temperature (float) based on the given season."""
    if season == "winter":
        return round(random.uniform(-10, 16), 1)  # Winter: -10 to 16°C
    elif season == "spring":
        return round(random.uniform(5, 22), 1)   # Spring: 5 to 22°C
    elif season == "summer":
        return round(random.uniform(20, 40), 1)  # Summer: 20 to 40°C
    elif season == "autumn" or season == "fall":
        return round(random.uniform(5, 25), 1)   # Autumn/Fall: 5 to 25°C
    else:
        return round(random.uniform(-10, 40), 1) # Default: full range

# Function to determine the season based on the month
def get_season_from_month(month):
    """Returns the season based on the given month number (1-12)."""
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return None  # Invalid month

# Main function
def main():
    """Main function to run the temperature program."""
    # Ask the user for the month number and determine the season
    try:
        month = int(input("Enter the number of the month (1-12): "))
        season = get_season_from_month(month)

        if season is None:
            print("Invalid month! Please enter a number between 1 and 12.")
            return

        # Get a random temperature based on the season
        temp = get_random_temp(season)

        # Print the temperature
        print(f"The temperature right now is {temp} degrees Celsius.")

        # Provide friendly advice based on the temperature
        if temp < 0:
            print("Brrr, that’s freezing! Wear some extra layers today ❄️")
        elif 0 <= temp < 16:
            print("Quite chilly! Don’t forget your coat")
        elif 16 <= temp < 23:
            print("The weather is mild, enjoy your day!")
        elif 23 <= temp < 32:
            print("It's warm outside, stay hydrated!")
        else:
            print("It's really hot! Make sure to stay cool and drink lots of water!")

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 12.")

# Run the main function
main()


#8


# Data: List of Star Wars questions and answers
data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

# Function to run the quiz
def star_wars_quiz():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []  # List to store incorrect answers

    print("\n✨ Welcome to the Star Wars Quiz! ✨")
    
    for item in data:
        user_answer = input(f"\n{item['question']} ").strip()

        if user_answer.lower() == item['answer'].lower():  # Case insensitive comparison
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer was: {item['answer']}")
            incorrect_answers += 1
            wrong_answers.append({"question": item['question'], "your_answer": user_answer, "correct_answer": item['answer']})

    # Display results
    print("\nQuiz Results:")
    print(f"Correct Answers: {correct_answers}")
    print(f"Incorrect Answers: {incorrect_answers}")

    # Show incorrect answers
    if incorrect_answers > 0:
        print("\nHere are the questions you got wrong:")
        for mistake in wrong_answers:
            print(f"{mistake['question']}")
            print(f"  Your answer: {mistake['your_answer']}")
            print(f"  Correct answer: {mistake['correct_answer']}\n")

    # Ask the user to play again if they got more than 3 wrong
    if incorrect_answers > 3:
        retry = input("You got more than 3 wrong. Would you like to try again? (yes/no) ").strip().lower()
        if retry == "yes":
            star_wars_quiz()
        else:
            print("Thanks for playing! May the Force be with you!")

# Run the quiz
star_wars_quiz()