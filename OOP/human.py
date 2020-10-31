class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0


    @property
    def age(self):
        return f"{self.first} is {self._age} years old"



person = Human("Victoria", "Rossi", 34)
print(person.first, person.last, person.age)