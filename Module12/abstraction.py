"""
Program:  abstract.py
Author:  Ty Hobbs
Last Day Modified:  11/12/2019

The purpose of the program is to demonstrate the use of abstract classes in Python.
"""

from abc import ABC, abstractmethod

class Rider(ABC):
    """
    A abstract class
    """
    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def rider(self):
        pass


class Motorcycle(Rider):
    """
    Motorcycle class
    """
    def ride(self):
        return "Engine powered, not enclosed"

    def rider(self):
        return "1 or 2"

class Bicycle(Rider):
    """Bicycle Class"""
    def ride(self):
        return "Human powered, not enclosed"

    def rider(self):
        return "1 or 2 if tandem or a daredevil"

class Car(Rider):
    """Car Class"""
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


