## MANDATORY EXERCISES XP BELLOW


# Exercise 1

#Define the Cat class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name  # Assign the name to the object
        self.age = cat_age  # Assign the age to the object

# Create three Cat instances
cat1 = Cat("Myrtille", 3)
cat2 = Cat("Bobby", 5)
cat3 = Cat("Twister", 2)

# Function to find the oldest cat
def find_oldest_cat(cats):
    oldest = cats[0]  # Assume the first cat is the oldest
    for cat in cats:  # Loop through the list of cats
        if cat.age > oldest.age:
            oldest = cat  # Update if a cat is older
    return oldest  # Return the oldest cat

#Another solution found with gpt

# def find_oldest_cat(*cats):
#     return max(cats, key=lambda cat: cat.age)  # Get the cat with the highest age
# oldest_cat = find_oldest_cat(cat1, cat2, cat3)


# Find the oldest cat
oldest_cat = find_oldest_cat([cat1, cat2, cat3])

# Print the result
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# Exercise 2


class Dog:
    def __init__(self, name, height):
        """Initialize dog with a name and height."""
        self.name = name
        self.height = height

    def bark(self):
        """Dog barks."""
        print(f"{self.name} goes woof!")

    def jump(self):
        """Dog jumps twice its height."""
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Creating David's Dog
davids_dog = Dog("Rex", 50)
print(f"David's dog is {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

# Creating Sarah's Dog
sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog is {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Checking which dog is bigger
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print(f"The bigger dog is {sarahs_dog.name}.")


# Exercise 3

class Song:
    def __init__(self, lyrics):
        """Initialize the song with lyrics."""
        self.lyrics = lyrics

    def sing_me_a_song(self):
        """Print each lyric line separately."""
        for line in self.lyrics:
            print(line)

# Creating an instance of the Song class
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Calling the method to print lyrics
stairway.sing_me_a_song()


# Exercise 4

class Zoo:
    def __init__(self, zoo_name):
        """Initialize the zoo with a name and an empty animals list."""
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        """Add a new animal if it's not already in the list."""
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        """Print all animals in the zoo."""
        print(f"Animals in {self.name}: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        """Remove an animal from the zoo if it exists."""
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        """Sort animals alphabetically and group them by first letter."""
        self.animals.sort()  # Sort the animals alphabetically
        groups = {}  # Dictionary to store grouped animals

        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = [animal]
            else:
                groups[first_letter].append(animal)

        return groups  # Return the dictionary of grouped animals

    def get_groups(self):
        """Print each group of animals."""
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


# 🦒 Creating a Zoo instance
new_york_zoo = Zoo("New York Zoo")

# 🦁 Adding animals
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")
new_york_zoo.add_animal("Ape")

# 🐘 Displaying animals
new_york_zoo.get_animals()

# 🦓 Selling an animal
new_york_zoo.sell_animal("Giraffe")
new_york_zoo.get_animals()

# 🦜 Sorting and grouping animals
print("\nSorted and grouped animals:")
new_york_zoo.get_groups()


# EXERCISE NINJA XP 

class Phone:
    def __init__(self, phone_number):
        """Initialize the phone with a number, an empty call history, and an empty messages list."""
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        """Log and print a call between two phones."""
        call_info = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_info)
        self.call_history.append(call_info)

    def show_call_history(self):
        """Display the call history."""
        print("\n Call History:")
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, content):
        """Send a message and save it in the messages list as a dictionary."""
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)  # The recipient also receives the message

    def show_outgoing_messages(self):
        """Show messages sent by this phone."""
        print("\n Outgoing Messages:")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(f"To {msg['to']}: {msg['content']}")

    def show_incoming_messages(self):
        """Show messages received by this phone."""
        print("\n Incoming Messages:")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(f"From {msg['from']}: {msg['content']}")

    def show_messages_from(self, other_phone):
        """Show messages exchanged with a specific phone number."""
        print(f"\n Messages from {other_phone.phone_number}:")
        for msg in self.messages:
            if msg["from"] == other_phone.phone_number or msg["to"] == other_phone.phone_number:
                direction = "Sent" if msg["from"] == self.phone_number else "Received"
                print(f"{direction}: {msg['content']}")


# Creating two Phone objects
phone1 = Phone("123-456-7890")
phone2 = Phone("987-654-3210")

# Making calls
phone1.call(phone2)
phone2.call(phone1)

# Sending messages
phone1.send_message(phone2, "Hey, how are you?")
phone2.send_message(phone1, "I'm good, thanks! What about you?")
phone1.send_message(phone2, "Doing great! Let's catch up soon.")

# Displaying call history
phone1.show_call_history()
phone2.show_call_history()

# Displaying messages
phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone2.show_outgoing_messages()
phone2.show_incoming_messages()

# Displaying messages from a specific contact
phone1.show_messages_from(phone2)
phone2.show_messages_from(phone1)
