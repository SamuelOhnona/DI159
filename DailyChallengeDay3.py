##Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.
##create a program that finds, within list_of_numbers all the pairs of number that sum to the target number


import random

# Generate a list of 20,000 random numbers between 0 and 10,000
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

# The target number we are looking for
target_number = 100

# A set to store numbers we have already seen
seen_numbers = set()

# A list to store pairs that sum up to the target number
pairs = []

# Loop through each number in the list
for number in list_of_numbers:
    # Calculate the complement (the number that, when added to the current number, gives the target number)
    complement = target_number - number
    
    # If the complement is already in the set, we found a pair
    if complement in seen_numbers:
        pairs.append((complement, number))
    
    # Add the current number to the set
    seen_numbers.add(number)

# Display the pairs found
print("Pairs that sum to", target_number, ":", pairs)