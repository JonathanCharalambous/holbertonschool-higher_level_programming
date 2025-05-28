#!/usr/bin/env python3

class SwimMixin:
    """Mixin class to add swimming behavior."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin class to add flying behavior."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon that can swim, fly, and roar."""
    def roar(self):
        print("The dragon roars!")
