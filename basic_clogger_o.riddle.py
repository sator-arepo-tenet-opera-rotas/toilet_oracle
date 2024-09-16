import time
import random
from abc import ABC, abstractmethod

class Toilet:
    def __init__(self):
        self.state = "Idle"  # Initial state of the toilet is idle
        self.water_level = 100  # Percentage, 100 means fully refilled
        self.cleanliness = 100  # Cleanliness level, 100 means fully clean

    def use_toilet(self, user):
        if self.state == "Idle":
            print(f"{user.__class__.__name__} is using the toilet.")
            self.state = "In Use"
            user.use()  # Invoke the specific usage pattern of the user
            self.state = "Flushing"
            self.flush()
        else:
            print("Toilet is not available right now!")

    def flush(self):
        print("Flushing the toilet...")
        self.cleanliness -= random.randint(1, 10)  # Dirtiness varies
        self.water_level -= random.randint(5, 15)  # Water decreases by random amount
        time.sleep(2)  # Simulate the time it takes to flush
        print("Flushing complete!")
        self.refill()

    def refill(self):
        self.state = "Refilling"
        print("Refilling the tank...")
        time.sleep(2)
        self.water_level = 100  # Refill the water to 100%
        print("Toilet is refilled.")
        self.state = "Idle"

    def check_status(self):
        print(f"Toilet Status: State={self.state}, Water Level={self.water_level}%, Cleanliness={self.cleanliness}%")

# Abstract Base Class for User
class User(ABC):
    @abstractmethod
    def use(self):
        """Abstract method to be implemented by sitters and standers"""
        pass

class Sitter(User):
    def use(self):
        print("Sitter is sitting and using the toilet...")
        time.sleep(3)  # Simulate the time it takes to sit and use
        print("Sitter is done.")

class Stander(User):
    def use(self):
        print("Stander is standing and using the toilet...")
        time.sleep(1)  # Simulate a quicker use case for standing
        print("Stander is done.")

# Example of the simulation

# Create the toilet object
toilet = Toilet()

# Create users
sitter = Sitter()
stander = Stander()

# Check initial status
toilet.check_status()

# Sitter uses the toilet
toilet.use_toilet(sitter)
toilet.check_status()

# Stander uses the toilet
toilet.use_toilet(stander)
toilet.check_status()

# Simulate another user trying to use the toilet while it's busy
toilet.use_toilet(sitter)
