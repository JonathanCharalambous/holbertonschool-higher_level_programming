#!/usr/bin/env python3

class Fish:
    """A class representing a fish."""
    def swim(self):
        """Method to simulate swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Method to describe the fish's habitat."""
        print("The fish lives in water")

class Bird:
    def fly(self):
        """Method to simulate flying."""
        print("The bird is flying")

    def habitat(self):
        """Method to describe the bird's habitat."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """A class representing a flying fish, which can swim and fly."""
    def swim(self):
        """Override the swim method to include a message for flying fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override the fly method to include a message for flying fish."""
        print("The flying fish is soaring!")
    
    def habitat(self):
        """Override the habitat method to include a message for flying fish."""
        print("The flying fish lives in both water and air!")
