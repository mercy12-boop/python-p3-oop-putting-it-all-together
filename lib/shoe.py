#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self.condition = "Old"  # Assuming shoes start in an "Old" condition

    @property
    def brand(self):
        return self._brand

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
