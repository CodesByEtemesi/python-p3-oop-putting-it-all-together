class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"


if __name__ == "__main__":
    my_shoe = Shoe("Nike", 9)

    my_shoe.size = "nine"

    my_shoe.cobble()

    print("Shoe condition:", my_shoe.condition)
