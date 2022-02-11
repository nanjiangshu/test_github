#!/usr/bin/env python

"""A test python code"""


class App1:
    """ simple arithmetic calculation
    """
    def __init__(self, a=1, b=2):
        self.var_a = a
        self.var_b = b

    def plus(self):
        """return a + b"""
        c = self.var_a + self.var_b
        print(f"{__name__}: {self.var_a} + {self.var_b} = {c}")

    def multiplication(self):
        """return a * b"""
        c = self.var_a * self.var_b
        print(f"{__name__}: {self.var_a} * {self.var_b} = {c}")
