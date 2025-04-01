import string
from collections import Counter
import os

#Part 1
class Text:
    """Class for analyzing a given text."""
    def __init__(self, text):
        self.text = text.lower()
    
    def word_frequency(self, word):
        """Returns the frequency of a given word in the text."""
        words = self.text.split()
        count = words.count(word.lower())
        return count if count > 0 else "Word not found in text."
    
    def most_common_word(self):
        """Returns the most common word in the text."""
        words = self.text.split()
        counter = Counter(words)
        return counter.most_common(1)[0][0] if counter else "No words in text."
    
    def unique_words(self):
        """Returns a list of all unique words in the text."""
        words = set(self.text.split())
        return list(words)
 #Part 2   
    @classmethod 
    def from_file(cls):
        """Creates a Text instance from a file."""
        file_path = "/Users/sam/Documents/DI_DATA_2025/week3/DailyChallengeDay6/the_stranger.txt"
        if not os.path.exists(file_path):
            print("Error: File not found.")
            return None
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
            return cls(text)
        except FileNotFoundError:
            print("Error: File not found.")
            return None
# Prime 
class TextModification(Text):
    """Class for modifying and cleaning text."""
    def remove_punctuation(self):
        """Returns the text without punctuation."""
        return self.text.translate(str.maketrans('', '', string.punctuation))
    
    def remove_stopwords(self):
        """Returns the text without common English stop-words."""
        stopwords = set("""
            a an and are as at be but by for if in into is it no not of on or such that the their then there these they this to was will with
        """.split())
        words = [word for word in self.text.split() if word not in stopwords]
        return " ".join(words)
    
    def remove_special_characters(self):
        """Returns the text without special characters."""
        return ''.join(e for e in self.text if e.isalnum() or e.isspace())

# Example Usage
text_instance = Text("A good book would sometimes cost as much as a good house.")
print("Word frequency of 'good':", text_instance.word_frequency("good"))
print("Most common word:", text_instance.most_common_word())
print("Unique words:", text_instance.unique_words())

text_file_instance = Text.from_file()
if text_file_instance:
    print("Most common word in file:", text_file_instance.most_common_word())