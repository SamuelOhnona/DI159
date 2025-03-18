#Challenge 1

# Ask the user for a word
word = input("Enter a word: ")

# Initialize an empty dictionary to store the letter indexes
letter_positions = {}

# Loop through each letter and its index in the word
for index, letter in enumerate(word):
    if letter in letter_positions:
        letter_positions[letter].append(index)  # Append index if letter already exists
    else:
        letter_positions[letter] = [index]  # Create a new list with the index

# Print the resulting dictionary
print(letter_positions)

#Challenge 2

def price_to_number(price):
    return int(price.replace("$", "").replace(",", ""))

# Function to find affordable items
def affordable_items(items_purchase, wallet):
    # Convert wallet amount to a number
    wallet_amount = price_to_number(wallet)
    
    # List to store items that can be bought
    affordable = [item for item, price in items_purchase.items() if price_to_number(price) <= wallet_amount]

    # Sort the list alphabetically
    affordable.sort()

    # Return the list or "Nothing" if it's empty
    return affordable if affordable else "Nothing"

# Example cases
items_purchase1 = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}
wallet1 = "$300"
print(affordable_items(items_purchase1, wallet1))  # ➞ ["Bread", "Fertilizer", "Water"]

items_purchase2 = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}
wallet2 = "$100"
print(affordable_items(items_purchase2, wallet2))  # ➞ ["Apple", "Bananas", "Fan", "Honey", "Spoon"]

items_purchase3 = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}
wallet3 = "$1"
print(affordable_items(items_purchase3, wallet3))  # ➞ "Nothing"