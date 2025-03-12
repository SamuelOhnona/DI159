#CHALLENGE 1

# Ask the user for a number and a length
number = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

# Create a list of multiples of the number
multiples = [number * i for i in range(1, length + 1)] #length + 1 to stop at length

# Print the list of multiples
print("List of multiples:", multiples)


#CHALLENGE 2

# Ask the user for a string
user_input = input("Enter a string: ")

# Initialize an empty string to store the new string
new_string = ""

# Loop over the characters in the user input
for i in range(len(user_input)):
    # Add the character to new_string if it's not the same as the previous character
    if i == 0 or user_input[i] != user_input[i - 1]:
        new_string += user_input[i]

print("New string:", new_string) 

#I am sure that we can make this also with set(), but maybe we'll have a problem to store correctly the value


# HAPPY BIRTHDAY BONUS
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

print("       ___iiiii___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")
