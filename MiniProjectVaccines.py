# Part 1

class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority  # Boolean
        self.blood_type = blood_type  # 'A', 'B', 'AB', or 'O'
        self.family = []

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
            person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age > 60 or person.priority:
            # Add to the beginning without using insert
            self.humans = [person] + self.humans
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        for i in range(len(self.humans)):
            if self.humans[i] == person:
                return i
        return -1  # Not found

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        if index1 == -1 or index2 == -1:
            return False
        self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]
        return True

    def get_next(self):
        if len(self.humans) == 0:
            return None
        next_person = self.humans[0]
        self.humans = self.humans[1:]
        return next_person

    def get_next_blood_type(self, blood_type):
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                match = self.humans[i]
                self.humans = self.humans[:i] + self.humans[i+1:]
                return match
        return None

    def sort_by_age(self):
        priority = []
        older = []
        younger = []

        for person in self.humans:
            if person.priority:
                priority.append(person)
            elif person.age > 60:
                older.append(person)
            else:
                younger.append(person)

        # Combine sorted lists
        self.humans = priority + older + younger

    def rearrange_queue(self):
        if len(self.humans) < 2:
            return

        i = 0
        while i < len(self.humans) - 1:
            if any(fam in self.humans[i+1:] and self.humans[i+1] in self.humans[i].family for fam in self.humans[i].family):
                # Swap with someone later who isn't in the same family
                for j in range(i+2, len(self.humans)):
                    if self.humans[j] not in self.humans[i].family:
                        self.humans[i+1], self.humans[j] = self.humans[j], self.humans[i+1]
                        break
            i += 1

