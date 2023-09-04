class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self._condition = "New"

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("Size must be an integer")

    def get_size(self):
        return self._size
    
    size = property(get_size, set_size)

    def cobble(self):
        if self._condition == "Worn":
            print("Your shoe has been cobbled and is as good as new!")
            self._condition = "New"
        else:
            print("Your shoe is already in a new condition.")

    def wear(self):
        if self._condition == "New":
            print("You've worn your shoe. It's no longer in a new condition.")
            self._condition = "Worn"
        else:
            print("Your shoe is already worn.")

    def get_condition(self):
        return self._condition
    
    condition = property(get_condition)

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Size: {self.size}")
        print(f"Condition: {self.condition}")

# Example usage:
shoe1 = Shoe("Nike", 10)
shoe1.display_info()

shoe1.wear()
shoe1.display_info()

shoe1.cobble()
shoe1.display_info()

shoe1.wear()
shoe1.display_info()
