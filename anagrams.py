from anagram_checker import AnagramChecker

def get_user_input():
    """
    Gets a single valid word from the user. Ensures that:
    - Only one word is entered
    - Only alphabetic characters are used
    - Whitespace is stripped
    """
    while True:
        user_input = input("Enter a word (or type 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            return None  # Exit condition
        
        if ' ' in user_input:
            print("Error: Please enter only one word.")
            continue
        
        if not user_input.isalpha():
            print("Error: Only alphabetic characters are allowed.")
            continue

        return user_input

def main():
    """
    Main function to run the anagram checker program.
    """
    checker = AnagramChecker()  # Create an instance of AnagramChecker
    
    while True:
        print("\n=== ANAGRAM CHECKER ===")
        user_word = get_user_input()
        
        if user_word is None:
            print("Goodbye!")
            break  # Exit the program
        
        user_word = user_word.upper()
        
        if not checker.is_valid_word(user_word):
            print(f"Sorry, '{user_word}' is not a valid English word.")
            continue
        
        anagrams = checker.get_anagrams(user_word)
        
        print(f"\nYOUR WORD: \"{user_word}\"")
        print("This is a valid English word.")
        print(f"Anagrams for your word: {', '.join(anagrams) if anagrams else 'None'}")

if __name__ == "__main__":
    main()