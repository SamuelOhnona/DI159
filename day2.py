## EXERCISES XP MANDATORY BELOW

#1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 1: Create the Siamese class
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 2: Create cat instances
bengal_cat = Bengal("Tiger", 3)
chartreux_cat = Chartreux("Smokey", 5)
siamese_cat = Siamese("Luna", 2)

# Step 3: Store them in a list
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Step 4: Create Sara's pets
sara_pets = Pets(all_cats)

# Step 5: Take all cats for a walk
sara_pets.walk()


#2 

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"It's a tie between {self.name} and {other_dog.name}!"

# Creating three Dog instances
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Rocky", 4, 18)

# Testing methods
print(dog1.bark())  # Rex is barking
print(f"{dog2.name}'s running speed: {dog2.run_speed()}")  
print(dog3.fight(dog1))  
print(dog2.fight(dog3))  


#3

import random  
from dog import Dog  # Importing the Dog class from the previous file

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False  # Default value

    def train(self):
        print(self.bark())  # Call the bark method from Dog class
        self.trained = True  # Set trained to True

    def play(self, *other_dogs):
        dog_names = ", ".join(dog.name for dog in other_dogs)
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} hasn't been trained yet!")

# IN ANOTHER FILE WE HAVE TO PUT THAT : 

from pet_dog import PetDog  # Import PetDog class

# Create PetDog instances
dog1 = PetDog("Buddy", 3, 25)
dog2 = PetDog("Max", 4, 22)
dog3 = PetDog("Bella", 2, 18)

# Train one dog
dog1.train()  # Trains Buddy and makes him bark

# Play with other dogs
dog1.play(dog2, dog3)  # Buddy, Max, Bella all play together

# Try to do a trick (before training)
dog2.do_a_trick()  # Max hasn't been trained yet!

# Train Max and make him do a trick
dog2.train()
dog2.do_a_trick()  # Max performs a random trick!



#4 

class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members else []  # Initialize members as a list if not provided

    def born(self, **kwargs):
        """Adds a child to the members list and prints a congratulatory message."""
        self.members.append(kwargs)
        print(f"🎉 Congratulations! The {self.last_name} family welcomes {kwargs['name']}!")

    def is_18(self, name):
        """Returns True if the member is 18 or older, False otherwise."""
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False  # If name not found

    def family_presentation(self):
        """Prints the family's last name and details of all members."""
        print(f"\n👨‍👩‍👧‍👦 The {self.last_name} Family:")
        for member in self.members:
            print(f" - {member['name']}, {member['age']} years old, {member['gender']}, Child: {member['is_child']}")

# Create an instance of the Family class with members
my_family = Family("Smith", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

# Display the family details
my_family.family_presentation()

# Add a new baby to the family
my_family.born(name="Emma", age=0, gender="Female", is_child=True)

# Check if a family member is 18 or older
print("\nIs Michael over 18?", my_family.is_18("Michael"))  # True
print("Is Emma over 18?", my_family.is_18("Emma"))  # False

# Display updated family details
my_family.family_presentation()


#5

class TheIncredibles(Family):
    def use_power(self, name):
        """Prints the power of a family member if they are over 18, else raises an exception."""
        for member in self.members:
            if member['name'] == name:
                if member['age'] < 18:
                    raise Exception(f"{name} is not over 18 years old and cannot use their power!")
                print(f"{member['incredible_name']} uses their power: {member['power']}!")
                return
        print(f"{name} is not found in the family.")

    def incredible_presentation(self):
        """Prints the family's incredible introduction and details."""
        print("\n✨ Here is our powerful family! ✨")
        super().family_presentation()  # Call the parent class method to display members

# Create an instance of TheIncredibles class with members
incredible_family = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

# Call the incredible presentation method
incredible_family.incredible_presentation()

# Use power of a member
incredible_family.use_power("Michael")
incredible_family.use_power("Sarah")

# Add Baby Jack to the family
incredible_family.born(name="Jack", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="Baby Jack")

# Call the incredible presentation method again
incredible_family.incredible_presentation()

# Try using Baby Jack's power (should raise an exception)
try:
    incredible_family.use_power("Jack")
except Exception as e:
    print(f"⚠️ Exception: {e}")


## EXERCISES XP GOLD BELOW 

#PART I

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  # Initialisation du solde

    def deposit(self, amount):
        """Ajoute de l'argent au compte."""
        if amount <= 0:
            raise ValueError("Le montant du dépôt doit être positif.")
        self.balance += amount
        return f"Dépôt réussi. Nouveau solde : {self.balance}€"

    def withdraw(self, amount):
        """Retire de l'argent du compte."""
        if amount <= 0:
            raise ValueError("Le montant du retrait doit être positif.")
        if amount > self.balance:
            raise ValueError("Fonds insuffisants.")
        self.balance -= amount
        return f"Retrait réussi. Nouveau solde : {self.balance}€"

# Part II

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimum_balance=0):
        super().__init__(balance)  # Call the parent class constructor
        self.minimum_balance = minimum_balance  # Initialize the minimum allowed balance

    def withdraw(self, amount):
        """Withdraw money from the account while maintaining the minimum balance."""
        if amount <= 0:
            raise ValueError("The withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise ValueError("Insufficient funds to maintain the required minimum balance.")
        self.balance -= amount
        return f"Withdrawal successful. New balance: {self.balance}€"

# Test the code 

# Creating a regular bank account
account1 = BankAccount(500)
print(account1.deposit(200))  # Adds 200€ (Should display a balance of 700€)
print(account1.withdraw(100))  # Withdraws 100€ (Should display a balance of 600€)

# Creating a bank account with a minimum balance requirement
account2 = MinimumBalanceAccount(500, minimum_balance=200)
print(account2.withdraw(250))  # Should be an error (minimum balance not maintained)
print(account2.withdraw(200))  # Should work (remaining balance = 300€)

# PART III

class BankAccount:
    def __init__(self, balance=0, username="", password=""):
        """Initialize account with balance, username, and password."""
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False  # Default: not logged in

    def authenticate(self, username, password):
        """Verify the username and password to authenticate the user."""
        if self.username == username and self.password == password:
            self.authenticated = True
            return "Authentication successful!"
        else:
            raise ValueError("Invalid username or password.")

    def deposit(self, amount):
        """Deposit money only if the user is authenticated."""
        if not self.authenticated:
            raise PermissionError("You must be authenticated to perform this action.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return f"Deposit successful. New balance: {self.balance}€"

    def withdraw(self, amount):
        """Withdraw money only if the user is authenticated."""
        if not self.authenticated:
            raise PermissionError("You must be authenticated to perform this action.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return f"Withdrawal successful. New balance: {self.balance}€"

# Test the code 

# Creating a bank account with authentication
account = BankAccount(500, "john_doe", "secure123")

# Trying to deposit without authentication (should be an error)
try:
    print(account.deposit(100))
except Exception as e:
    print(e)

# Authenticating the user
print(account.authenticate("john_doe", "secure123"))

# Performing transactions after authentication
print(account.deposit(200))  # Adds 200€ (New balance: 700€)
print(account.withdraw(100))  # Withdraws 100€ (New balance: 600€)





