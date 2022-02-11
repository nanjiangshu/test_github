#!/usr/bin/env python
"""A test python code"""
import math


class App2:
    """simple math"""
    def __init__(self, x=10):
        self.x = x

    def sin(self):
        """sin"""
        c = math.sin(self.x)
        print(f"{__name__}: sin({self.x}) = {c}")

    def cos(self):
        """cos"""
        c = math.cos(self.x)
        print(f"{__name__}: cos({self.x}) = {c}")

    def tan(self):
        """tan"""
        c = math.tan(self.x)
        print(f"{__name__}: tan({self.x}) = {c}")

    def pow10(self):
        """power of 10"""
        c = math.pow(10, self.x)
        print(f"{__name__}: pow10({self.x}) = {c}")

    def pow16(self):
        """power of 16"""
        c = math.pow(16, self.x)
        print(f"{__name__}: pow16({self.x}) = {c}")
