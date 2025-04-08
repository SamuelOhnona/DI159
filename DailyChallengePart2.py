import random

class Card:
    """Represents a single playing card with a suit and a value."""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    """Represents a deck of 52 playing cards."""
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        """Initializes the deck with 52 cards."""
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
    
    def shuffle(self):
        """Shuffles the deck randomly."""
        if len(self.cards) != 52:
            raise ValueError("Cannot shuffle: Deck is incomplete!")
        random.shuffle(self.cards)
    
    def deal(self):
        """Deals a single card from the deck. Removes it from the deck."""
        if not self.cards:
            raise ValueError("No cards left in the deck!")
        return self.cards.pop()

# Example Usage
deck = Deck()
deck.shuffle()
print(deck.deal())  # Deals a random card