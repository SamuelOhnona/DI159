## Exercise XP Mandatory

#1

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        """String representation of the currency object"""
        return f"{self.amount} {self.currency}{'s' if self.amount > 1 else ''}"

    def __repr__(self):
        """Representation method, same as __str__ in this case"""
        return self.__str__()

    def __int__(self):
        """Returns the integer value of the amount"""
        return self.amount

    def __add__(self, other):
        """Handles addition with an integer or another Currency instance"""
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        else:
            raise TypeError("Addition is only supported between Currency and int or same Currency type")

    def __iadd__(self, other):
        """Handles in-place addition (+=)"""
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        else:
            raise TypeError("Addition is only supported between Currency and int or same Currency type")
        return self


# === TEST CASES ===
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  # '5 dollars'
print(int(c1))  # 5
print(repr(c1))  # '5 dollars'

print(c1 + 5)  # 10
print(c1 + c2)  # 15

print(c1)  # 5 dollars

c1 += 5
print(c1)  # 10 dollars

c1 += c2
print(c1)  # 20 dollars

# Uncomment the line below to see the TypeError
# print(c1 + c3)  # TypeError: Cannot add between Currency type <dollar> and <shekel>


#2 

# Cf func.py and exercise_one.py 


#3 

import random
import string

def generate_random_string(length=5):
    """Generate a random string of uppercase and lowercase letters."""
    characters = string.ascii_letters  # Contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choices(characters, k=length))

# Example usage
random_string = generate_random_string()
print(random_string)  # Example output: 'AbXyz'

#4

from datetime import datetime

def display_current_date():
    """Displays the current date in YYYY-MM-DD format."""
    current_date = datetime.now().date()  # Get today's date
    print("Current date:", current_date)

# Example usage
display_current_date()



#5

from datetime import datetime, timedelta

def time_until_new_year():
    """Displays the time remaining until January 1st."""
    now = datetime.now()
    next_new_year = datetime(now.year + 1, 1, 1)  # Next Jan 1st at midnight
    time_left = next_new_year - now

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"The 1st of January is in {days} days and {hours:02}:{minutes:02}:{seconds:02} hours.")

# Example usage
time_until_new_year()



#6 


from datetime import datetime

def minutes_lived(birthdate: str, date_format: str = "%Y-%m-%d"):
    """
    Calculates and prints the number of minutes a person has lived based on their birthdate.
    :param birthdate: The birthdate in the specified format (default: YYYY-MM-DD)
    :param date_format: The format of the birthdate string
    """
    try:
        birth_date = datetime.strptime(birthdate, date_format)
        now = datetime.now()
        
        if birth_date > now:
            print("Error: Birthdate is in the future!")
            return
        
        delta = now - birth_date
        minutes = delta.total_seconds() // 60
        print(f"You have lived approximately {int(minutes):,} minutes.")
    except ValueError:
        print("Invalid date format. Please use the correct format: YYYY-MM-DD")

# Example usage:
birthdate = "1990-01-01"  # Change this to any birthdate
time_format = "%Y-%m-%d"  # Modify if using a different format
minutes_lived(birthdate, time_format)



#7 

from datetime import datetime
from faker import Faker

fake = Faker()

users = []

def add_fake_user():
    """Generates a fake user and adds it to the users list."""
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.language_code()
    }
    users.append(user)
    print("User added:", user)

def minutes_lived(birthdate: str, date_format: str = "%Y-%m-%d"):
    """
    Calculates and prints the number of minutes a person has lived based on their birthdate.
    :param birthdate: The birthdate in the specified format (default: YYYY-MM-DD)
    :param date_format: The format of the birthdate string
    """
    try:
        birth_date = datetime.strptime(birthdate, date_format)
        now = datetime.now()
        
        if birth_date > now:
            print("Error: Birthdate is in the future!")
            return
        
        delta = now - birth_date
        minutes = delta.total_seconds() // 60
        print(f"You have lived approximately {int(minutes):,} minutes.")
    except ValueError:
        print("Invalid date format. Please use the correct format: YYYY-MM-DD")

# Example usage:
birthdate = "1990-01-01"  # Change this to any birthdate
time_format = "%Y-%m-%d"  # Modify if using a different format
minutes_lived(birthdate, time_format)

# Add a fake user
add_fake_user()



