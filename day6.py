# EXERCISES BELLOW 

#EXERCISE XP MANDATORY 

#1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

#2

# Given family data
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# Ticket pricing function
def ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

# Calculate cost for each family member
for name, age in family.items():
    price = ticket_price(age)
    print(f"{name} has to pay: ${price}")

# Calculate total cost
total_cost = sum(ticket_price(age) for age in family.values())
print("Total cost for the family:", total_cost)

# Bonus: Asking for user input
family_input = {}
while True:
    name = input("Enter a name (or 'stop' to finish): ")
    if name.lower() == 'stop':
        break
    age = input("Enter age: ")
    if age.isdigit():
        family_input[name] = int(age)

# Calculate cost for user input
if family_input:
    for name, age in family_input.items():
        price = ticket_price(age)
        print(f"{name} has to pay: ${price}")

    total_cost_input = sum(ticket_price(age) for age in family_input.values())
    print("Total cost for the family (user input):", total_cost_input)

#3

# Step 2: Create the brand dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Step 3: Change the number of stores to 2
brand["number_stores"] = 2

# Step 4: Print a sentence explaining who Zara's clients are
print("Zara's clients are:", ", ".join(brand["type_of_clothes"]))

# Step 5: Add country_creation
brand["country_creation"] = "Spain"

# Step 6: Check and add Desigual to international competitors
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Step 7: Delete the creation date
brand.pop("creation_date")

# Step 8: Print the last international competitor
print("Last international competitor:", brand["international_competitors"][-1])

# Step 9: Print the major colors in the US
print("Major colors in the US:", ", ".join(brand["major_color"]["US"]))

# Step 10: Print the number of key-value pairs
print("Number of key-value pairs:", len(brand))

# Step 11: Print the keys of the dictionary
print("Keys in the dictionary:", list(brand.keys()))

# Step 12: Create more_on_zara dictionary
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# Step 13: Merge more_on_zara into brand
brand.update(more_on_zara)

# Step 14: Print the value of number_stores
print("Number of stores:", brand["number_stores"])


#4

# List of Disney characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1st result: Creating a dictionary where the key is the character's name and the value is its index in the list.
# We use a dictionary comprehension with enumerate to get the index and name.
disney_users_A = {user: index for index, user in enumerate(users)}
print("disney_users_A:", disney_users_A)

# 2nd result: Creating a dictionary where the key is the index and the value is the character's name.
# Again, we use enumerate but flip the key-value order.
disney_users_B = {index: user for index, user in enumerate(users)}
print("disney_users_B:", disney_users_B)

# 3rd result: Creating a dictionary where the characters are sorted alphabetically.
# We use sorted() to sort the users list alphabetically, and then enumerate the sorted list.
disney_users_C = {user: index for index, user in enumerate(sorted(users))}
print("disney_users_C:", disney_users_C)

# Only recreate the 1st result for characters whose names contain the letter "i".
# We filter the list using a list comprehension and check if "i" is in the character name (case insensitive).
disney_users_I = {user: index for index, user in enumerate([user for user in users if "i" in user.lower()])}
print("disney_users_I (names with 'i'):", disney_users_I)

# Only recreate the 1st result for characters whose names start with the letter "M" or "P".
# We filter the list for names starting with "M" or "P" (case insensitive).
disney_users_MP = {user: index for index, user in enumerate([user for user in users if user[0].lower() in ['m', 'p']])}
print("disney_users_MP (names starting with 'M' or 'P'):", disney_users_MP)

#SOLUTION OF EXERCISES XP+ IS ON OCTOPUS, SO I AM JUST ADDING OTHERS EXERCISES HERE

#EXERCISE XP GOLD

#1

# Initialize the birthdays dictionary with 5 people and their birthdays
birthdays = {
    "John": "1990/05/15",
    "Alice": "1985/08/22",
    "Bob": "1992/02/10",
    "Eve": "1987/11/30",
    "Charlie": "1995/03/25"
}

# Welcome message and instruction
print("Welcome! You can look up the birthdays of the people in the list!")

# Ask the user to input a person's name
name = input("Enter a person's name to look up their birthday: ")

# Get the birthday for the entered name
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}.")
else:
    print("Sorry, we don't have that person's birthday information.")

#2

# Initialize the birthdays dictionary
birthdays = {
    "John": "1990/05/15",
    "Alice": "1985/08/22",
    "Bob": "1992/02/10",
    "Eve": "1987/11/30",
    "Charlie": "1995/03/25"
}

# Print all names in the dictionary
print("Here are the names in the birthday list:")
for person in birthdays:
    print(person)

# Ask the user to input a person's name
name = input("Enter a person's name to look up their birthday: ")

# Get the birthday for the entered name
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}.")
else:
    print(f"Sorry, we don't have the birthday information for {name}.")

#3

# Initialize the birthdays dictionary
birthdays = {
    "John": "1990/05/15",
    "Alice": "1985/08/22",
    "Bob": "1992/02/10",
    "Eve": "1987/11/30",
    "Charlie": "1995/03/25"
}

# Ask the user to add a new birthday
new_name = input("Enter your name: ")
new_birthday = input("Enter your birthday (YYYY/MM/DD): ")

# Add the new data to the dictionary
birthdays[new_name] = new_birthday

# Print all names in the dictionary
print("Here are the names in the birthday list:")
for person in birthdays:
    print(person)

# Ask the user to input a person's name to look up their birthday
name = input("Enter a person's name to look up their birthday: ")

# Get the birthday for the entered name
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}.")
else:
    print(f"Sorry, we don't have the birthday information for {name}.")


#4

# First dictionary with fruit prices
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Print all the items and their prices
for item, price in items.items():
    print(f"The price of {item} is ${price}.")

# Second dictionary with prices and stock quantities
items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

# Calculate the total cost to buy everything in stock
total_cost = 0
for item, details in items.items():
    total_cost += details["price"] * details["stock"]

print(f"The total cost to buy everything in stock is: ${total_cost:.2f}")


#EXERCISES XP NINJA

# Given string
car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Convert the string into a list by splitting at commas
car_list = car_string.split(", ")

# Print the number of manufacturers in the list
print(f"There are {len(car_list)} manufacturers in the list.")

# Print the list of manufacturers in reverse/descending order (Z-A)
car_list_sorted_desc = sorted(car_list, reverse=True)
print("Manufacturers in reverse order (Z-A):", car_list_sorted_desc)

# Using list comprehension to find how many manufacturers have the letter 'o' in their names
count_o = len([car for car in car_list if 'o' in car.lower()])
print(f"Number of manufacturers with the letter 'o': {count_o}")


#TIMED CHALLENGE 1

# Input sentence
sentence = "You have entered a wrong domain"

# Split the sentence into a list of words
words = sentence.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed words into a sentence
reversed_sentence = " ".join(reversed_words)

# Print the output
print("Output:", reversed_sentence)


#TIMED CHALLENGE 2

# Ask the user for a number
number = int(input("Enter the number: "))

# Function to check if the number is perfect
def is_perfect(num):
    # Initialize the sum of divisors
    sum_of_divisors = 0
    
    # Loop through all numbers from 1 to num//2 (no need to go higher, as divisors can't be greater than num//2)
    for i in range(1, num // 2 + 1):
        if num % i == 0:  # If i is a divisor of num
            sum_of_divisors += i
    
    # Check if the sum of divisors is equal to the number
    return sum_of_divisors == num

# Check if the number is perfect and print the result
if is_perfect(number):
    print(True)
else:
    print(False)

