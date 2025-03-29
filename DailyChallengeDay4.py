#Challenge 1

# Accept a comma-separated sequence of words from the user
input_sequence = input("Enter a comma-separated sequence of words: ")

# Split the input string into a list of words
words_list = input_sequence.split(',')

# Use list comprehension to sort the words alphabetically
sorted_words = ','.join([word for word in sorted(words_list)])

# Print the sorted words in a comma-separated sequence
print(sorted_words)


# Challenge 2

def longest_word(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Find the longest word by comparing lengths
    longest = max(words, key=len)
    
    return longest

# Example usages:
print(longest_word("Margaret's toy is a pretty doll."))  # "Margaret's"
print(longest_word("A thing of beauty is a joy forever."))  # "forever."
print(longest_word("Forgetfulness is by all means powerless!"))  # "Forgetfulness"