class AnagramChecker:
    """
    A class to check if a word is valid and find its anagrams.
    """

    def __init__(self, word_list_file='sowpods.txt'):
        """
        Initializes the class by loading the word list from the given file.
        """
        try:
            with open(word_list_file, 'r') as file:
                # Read all words, strip spaces, and store in a set for fast lookup
                self.words = {line.strip().upper() for line in file}
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find the file: {word_list_file}")

    def is_valid_word(self, word):
        """
        Checks if the given word exists in the loaded word list.
        """
        return word.upper() in self.words

    def get_anagrams(self, word):
        """
        Returns a list of anagrams of the given word from the word list.
        """
        word = word.upper()
        return [w for w in self.words if self.is_anagram(word, w) and w != word]

    def is_anagram(self, word1, word2):
        """
        Helper method to check if two words are anagrams.
        """
        return sorted(word1) == sorted(word2)