class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name  # Using underscores to indicate a private attribute
        self._last_name = last_name
        self._age = age

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer.")
        self._age = value

    def greet(self):
        return f"Hello, my name is {self.full_name} and I am {self.age} years old."


# Instantiate objects
person1 = Person("Hakim", "Blinder", 30)
person2 = Person("Muserian", "Smith", 25)

# Access attributes and methods
print(person1.full_name)  # Output: Hakim Blinder
print(person2.age)        # Output: 25

# Try to set an invalid age
try:
    person1.age = "thirty"
except ValueError as e:
    print(e)  # Output: Age must be a non-negative integer.

# Set a valid age
person1.age = 35
print(person1.age)  # Output: 35

# Call the greet method
# Output: Hello, my name is Muserian Smith and I am 25 years old.
print(person2.greet())
