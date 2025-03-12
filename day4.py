#Mandatory Exercises Bellow

#Exercises XP
#1

my_fav_numbers = {3, 7, 21} # Create a set with your favorite numbers

my_fav_numbers.add(42) # Add two new numbers to the set
my_fav_numbers.add(99)

my_fav_numbers.remove(max(my_fav_numbers))  # Removes the highest number
friend_fav_numbers = {5, 8, 15} # Create a set with your friend's favorite numbers
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers) # Concatenate both sets into a new variable
print("My favorite numbers:", my_fav_numbers) # Print results
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)

#2
#Tuple has not attribute .add, tuples ar immutable in Pyhton
my_tuple = (1, 2, 3)
temp_list = list(my_tuple)  # Convert tuple to list
temp_list.append(4)  # Modify the list
my_tuple = tuple(temp_list)  # Convert back to tuple
print(my_tuple)  # Output: (1, 2, 3, 4)

#3

basket = ["Banana", "Apples", "Oranges", "Blueberries"] # Initial list
basket.remove("Banana") # Remove "Banana"
basket.remove("Blueberries") # Remove "Blueberries"
basket.append("Kiwi") # Add "Kiwi" to the end of the list
basket.insert(0, "Apples") # Add "Apples" to the beginning of the list
apple_count = basket.count("Apples") # Count how many apples are in the basket
print("Number of Apples:", apple_count)
basket.clear() # Empty the basket
print(basket) 

#4
#A float is a number that has a decimal point, like 3.14 or 2.0.
numbers = [x / 2 for x in range(3, 11)]  # Generates [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(numbers)

#another way with while 
numbers = []
x = 1.5
while x <= 5:
    numbers.append(x)
    x += 0.5

print(numbers)

#5
for num in range(1, 21):  # range(1, 21) includes 1 to 20
    print(num)

for i in range(0, 20, 2):  # Even indices 
    print(numbers[i])

#6

my_name = "Samuel"

while True:  # Infinite loop
    user_name = input("Enter your name: ")  # Ask for user input
    if user_name == my_name:  # Check if the name matches
        print("Hello, Samuel! You've entered the correct name.")
        break  # Exit the loop
    else:
        print("That's not the right name. Try again!")

#7

fav_fruits = input("Enter your favorite fruit(s) (separated by spaces): ").lower().split() # Ask the user for their favorite fruits (space-separated)

chosen_fruit = input("Enter a fruit name: ").lower() # Ask the user for any fruit name

if chosen_fruit in fav_fruits: # Check if the chosen fruit is in the favorite fruits list
    print("You chose one of your favorite fruits!")
else:
    print("You chose a new fruit.")

#8
toppings = []
base_price = 10  # Base price of pizza
topping_price = 2.5  # Price per topping
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ").strip().lower()
    
    if topping == "quit":  # Exit condition
        break
    
    toppings.append(topping)  # Add topping to list
    print(f"Adding {topping} to your pizza! 🍕")

total_price = base_price + (len(toppings) * topping_price) # Calculate total price

print("Your pizza will have the following toppings:")
print(", ".join(toppings) if toppings else "No extra toppings.")
print(f"Total price: ${total_price:.2f}") #I had to use AI to understand this part, was difficult to make it run properly. 

#9

total_cost = 0

num_people = int(input("How many people are in your family? ")) # Ask the number of family members

for i in range(num_people):
    age = int(input(f"Enter the age of family member {i+1}: "))
    
    if age < 3:  # Determine ticket price based on age
        print("Ticket is free for this person! 🎟️")
    elif 3 <= age <= 12:
        print("Ticket price: $10 🎟️")
        total_cost += 10
    else:
        print("Ticket price: $15 🎟️")
        total_cost += 15

print(f"\nTotal cost for the family: ${total_cost}") # Print total cost

teenagers = ["Sam", "Abby", "Salomé", "Simon", "John"] # List of teenagers coming to the movie

allowed_teens = teenagers.copy() # Copy the list to modify it safely
for teen in teenagers: # Ask each teenager for their age
    age = int(input(f"{teen}, enter your age: "))

    
    if 16 <= age <= 21: # Remove restricted ages (16-21)
        print(f"Sorry {teen}, you cannot watch this movie")
        allowed_teens.remove(teen)

print("\nFinal list of teenagers allowed to watch the movie:") # Print final list of allowed teenagers
print(allowed_teens if allowed_teens else "No one is allowed.")

#10

sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", 
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"
]

print("Sorry, we have run out of Pastrami sandwiches.")

while "Pastrami sandwich" in sandwich_orders: 
    sandwich_orders.remove("Pastrami sandwich") #remove Pastrami

finished_sandwiches = [] # Create an empty list to store finished sandwiches

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Take the first sandwich
    print(f"I made your {current_sandwich.lower()}")  # Inform the customer
    finished_sandwiches.append(current_sandwich)  # Move to finished list

# Print final summary
print("\nAll sandwiches have been made! Here is what we prepared:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")


#Exercises XP GOLD

#1

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

#2 

# Loop from 1500 to 2500 and prints all multiples of 5 and 7
for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)

#3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name: ")
if user_name in names:
    index = names.index(user_name)
    print(f"The first occurrence of your name is at index: {index}")
else:
    print("Your name is not in the list.")

#4

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
greatest_num = max(num1, num2, num3)
print(f"The greatest number is: {greatest_num}")

#5

alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    if letter in "aeiouy":
        print(f"{letter.upper()} is a vowel.")
    else:
        print(f"{letter.upper()} is a consonant.")

#6

words = []
for i in range(7):
    word = input(f"Enter word {i+1}: ")
    words.append(word)
letter = input("Enter a single character: ")
for word in words:
    # Check if the letter exists in the word
    if letter in word:
        print(f"The first occurrence of '{letter}' in '{word}' is at index {word.index(letter)}.")
    else:
        print(f"The letter '{letter}' is not in the word '{word}'.")

#7

# Create a list of numbers from 1 to 1 million
numbers = list(range(1, 1000001))
print(f"Min value: {min(numbers)}")
print(f"Max value: {max(numbers)}")
total_sum = sum(numbers)
print(f"Sum of all numbers: {total_sum}") #it was very quick...

#8

input_numbers = input("Enter a sequence of comma-separated numbers: ") # Accept a sequence of comma-separated numbers from the user
numbers_list = [int(num) for num in input_numbers.split(',')] # Convert the input string into a list of numbers (by splitting and converting to integers)
numbers_tuple = tuple(numbers_list)
print("List:", numbers_list)
print("Tuple:", numbers_tuple)

#9

import random

#counter for wins and losses
games_won = 0
games_lost = 0

while True:
    user_guess = int(input("Guess a number between 1 and 9 (or enter 0 to quit): "))

    if user_guess == 0:
        break

    random_number = random.randint(1, 9)

    if user_guess == random_number:
        print("Winner!")
        games_won += 1
    else:
        print(f"Better luck next time! The correct number was {random_number}.")
        games_lost += 1

print(f"\nTotal Games Won: {games_won}")
print(f"Total Games Lost: {games_lost}")


# Exercises XP Ninja

#1 

import math #I found that we have to import math to use .sqrt function

C = 50
H = 30
input_numbers = input("Enter a comma-separated list of numbers: ")
numbers = input_numbers.split(',')
results = []
for num in numbers:
    D = int(num)
    Q = math.sqrt((2 * C * D) / H)
    results.append(str(int(Q)))  # Convert the result to an integer and append to the results list
print(",".join(results))


# I didn't had time to do all the ninja exercises

