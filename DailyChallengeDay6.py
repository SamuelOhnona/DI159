class Farm:
    def __init__(self, name):
        """Initialize the farm with a name and an empty dictionary for animals."""
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        """Add animals to the farm. If the animal already exists, increase its count."""
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        """Return a formatted string with the farm name and all animals."""
        info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            info += f"{animal.ljust(10)} : {count}\n"
        info += "\n   E-I-E-I-O!"
        return info

    def get_animal_types(self):
        """Return a sorted list of animal types."""
        return sorted(self.animals.keys())

    def get_short_info(self):
        """Return a short sentence about the farm's animals."""
        animal_types = self.get_animal_types()
        formatted_animals = [animal + "s" if self.animals[animal] > 1 else animal for animal in animal_types]
        return f"{self.name}’s farm has {', '.join(formatted_animals[:-1])} and {formatted_animals[-1]}."


# Creating the farm
macdonald = Farm("McDonald")

# Adding animals
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')  # This should increase the sheep count to 2
macdonald.add_animal('goat', 12)

# Displaying farm info
print(macdonald.get_info())

# Displaying sorted animal types
print("\nSorted animal types:", macdonald.get_animal_types())

# Displaying short info
print(macdonald.get_short_info())