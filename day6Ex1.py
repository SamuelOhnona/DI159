import random

def get_words_from_file(file_path="/Users/sam/Documents/DI_DATA_2025/week3/day6/words.txt"):
    """Reads words from a file and returns them as a list."""
    try:
        with open(file_path, "r") as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []

def get_random_sentence(length):
    """Generates a random sentence with the specified number of words."""
    words = get_words_from_file()
    if not words:
        return "Error: No words available to create a sentence."
    
    if not (2 <= length <= 20):
        return "Error: Sentence length must be between 2 and 20."
    
    sentence = " ".join(random.choices(words, k=length)).lower()
    return sentence

def main():
    """Runs the random sentence generator program."""
    print("Welcome to the Random Sentence Generator!")
    
    try:
        length = int(input("Enter the number of words for the sentence (2-20): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    sentence = get_random_sentence(length)
    print("Generated Sentence:", sentence)

if __name__ == "__main__":
    main()
