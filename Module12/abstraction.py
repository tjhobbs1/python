"""
Program:  abstract.py
Author:  Ty Hobbs
Last Day Modified:  11/12/2019

The purpose of the program is to demonstrate the use of abstract classes in Python.
"""

from abc import ABC, abstractmethod

class Rider(ABC):
    """
    An abstract class called Rider
    """
    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def rider(self):
        pass


class Motorcycle(Rider):
    """
    Motorcycle subclass
    """
    def ride(self):
        return "Engine powered, not enclosed"

    def rider(self):
        return "1 or 2"

class Bicycle(Rider):
    """Bicycle subclass"""
    def ride(self):
        return "Human powered, not enclosed"

    def rider(self):
        return "1 or 2 if tandem or a daredevil"

class Car(Rider):
    """Car subclass"""
    def ride(self):
        return "Engine powered, enclosed"

    def rider(self):
        return "1 plus comfortably"

# Instantiate the Objects
car = Car()
bike = Bicycle()
motorcycle = Motorcycle()

# Call the methods
print(bike.ride())
print(bike.rider())
print(motorcycle.ride())
print(motorcycle.rider())
print(car.ride())
print(car.rider())


