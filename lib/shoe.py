#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color
        self.is_worn = False

    def wear(self):
        if not self.is_worn:
            self.is_worn = True
            return "Shoe is now worn"
        else:
            return "Shoe is already worn"

    def take_off(self):
        if self.is_worn:
            self.is_worn = False
            return "Shoe is taken off"
        else:
            return "Shoe is not currently worn"

    def is_clean(self):
        return not self.is_worn
