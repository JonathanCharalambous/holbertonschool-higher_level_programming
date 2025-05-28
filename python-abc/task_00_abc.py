from abc import ABC, abstractmethod
"""
This module defines an abstract base class 
for animals and concrete implementations for Dog and Cat.
"""

class Animal(ABC):
    """Abstract base class for animals."""
    @abstractmethod
    def sound(self):
        """Abstract sound function for an animal class."""
        pass

class Dog(Animal):
    """Concrete implementation of Animal for dogs."""
    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"

class Cat(Animal):
    """Concrete implementation of Animal for cats."""
    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
