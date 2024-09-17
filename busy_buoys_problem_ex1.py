from abc import ABC, abstractmethod
import time
import random

# Base Toilet Class
class Toilet(ABC):
    def __init__(self):
        self.state = "Idle"
        self.water_level = 100  # Water percentage (for flush)
        self.toilet_paper = 100  # TP resource, 100% full

    def use_toilet(self, user):
        if self.state == "Idle":
            print(f"{user.__class__.__name__} is using the toilet.")
            self.state = "In Use"
            user.use()
            self.flush()
        else:
            print("Toilet is currently occupied.")

    @abstractmethod
    def flush(self):
        pass
    
    def check_status(self):
        print(f"Toilet Status: State={self.state}, Water={self.water_level}%, TP={self.toilet_paper}%")

# Degree of Freedom 1: Basic flushing (P)
class BasicToilet(Toilet):
    def flush(self):
        print("Flushing toilet...")
        time.sleep(1)
        self.state = "Flushing"
        self.water_level -= 10  # Basic water usage
        self.toilet_paper -= 5  # Basic TP usage
        time.sleep(1)
        self.state = "Idle"
        print("Toilet flushed and reset.")

# Degree of Freedom 2: TP constraint (P)
class ToiletWithTP(Toilet):
    def flush(self):
        print("Flushing toilet with TP constraint...")
        if self.toilet_paper <= 0:
            print("No toilet paper left!")
            return False
        time.sleep(1)
        self.water_level -= 10
        self.toilet_paper -= 5
        time.sleep(1)
        self.state = "Idle"
        print("Toilet flushed and TP used.")

# Degree of Freedom 3: Friend Preferences (P-like problem)
class ToiletWithFriends(ToiletWithTP):
    def __init__(self):
        super().__init__()
        self.friend_pairs = {}

    def assign_friend(self, sailor1, sailor2):
        self.friend_pairs[sailor1] = sailor2
        self.friend_pairs[sailor2] = sailor1

    def use_toilet(self, user):
        if user.name in self.friend_pairs:
            friend = self.friend_pairs[user.name]
            print(f"{user.name} prefers to use the toilet with {friend} nearby.")
        super().use_toilet(user)

# Degree of Freedom 4: Weight Class (NP-like problem)
class ToiletWithWeight(ToiletWithFriends):
    def __init__(self):
        super().__init__()
        self.weight_capacity = 150  # Weight limit in kg

    def use_toilet(self, user):
        if user.weight > self.weight_capacity:
            print(f"{user.name} exceeds the toilet's weight capacity!")
            return False
        super().use_toilet(user)

# Degree of Freedom 5: Optimization of resources (NP-hard-like)
class OptimizedToilet(ToiletWithWeight):
    def flush(self):
        print("Flushing with optimization...")
        if self.water_level < 20 or self.toilet_paper < 10:
            print("Low resources! Optimizing flush...")
            time.sleep(2)  # Simulating optimization
            self.water_level -= 5  # Minimized usage
            self.toilet_paper -= 2  # Minimized TP usage
        else:
            super().flush()
        self.state = "Idle"
        print("Optimized flush completed.")

# Sailor (User) Class
class Sailor(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def use(self):
        pass

# Simple Sailor who just uses the toilet
class SimpleSailor(Sailor):
    def use(self):
        print(f"{self.name} is using the toilet (P level) for basic urination.")
        time.sleep(1)
        print(f"{self.name} is done.")

# Sailor who uses toilet paper (P + TP)
class TPUser(Sailor):
    def use(self):
        print(f"{self.name} is using the toilet with TP (P + TP).")
        time.sleep(2)
        print(f"{self.name} is done.")

# Sailor with friend preferences (P + TP + Friend)
class FriendlySailor(Sailor):
    def use(self):
        print(f"{self.name} is using the toilet, checking for friends.")
        time.sleep(1)
        print(f"{self.name} is done.")

# Sailor who is filtered by weight (P + TP + Friend + Weight)
class HeavySailor(Sailor):
    def use(self):
        print(f"{self.name} is using the toilet, considering weight class.")
        time.sleep(2)
        print(f"{self.name} is done.")

# Example Simulation
def simulate_toilet_usage():
    # Toilet objects with varying complexity
    basic_toilet = BasicToilet()
    tp_toilet = ToiletWithTP()
    friend_toilet = ToiletWithFriends()
    weight_toilet = ToiletWithWeight()
    optimized_toilet = OptimizedToilet()

    # Sailor objects
    sailor1 = SimpleSailor("Sailor1", 70)
    sailor2 = TPUser("Sailor2", 75)
    sailor3 = FriendlySailor("Sailor3", 80)
    sailor4 = HeavySailor("Sailor4", 160)  # Exceeds weight class

    # Assign friends
    friend_toilet.assign_friend(sailor3.name, sailor1.name)

    # Basic toilet usage (P)
    basic_toilet.use_toilet(sailor1)
    basic_toilet.check_status()

    # TP Toilet usage (P + TP)
    tp_toilet.use_toilet(sailor2)
    tp_toilet.check_status()

    # Friend toilet usage (P + TP + Friend)
    friend_toilet.use_toilet(sailor3)
    friend_toilet.check_status()

    # Weight toilet usage (NP-like)
    weight_toilet.use_toilet(sailor4)  # Should fail due to weight
    weight_toilet.check_status()

    # Optimized toilet usage (NP-hard-like)
    optimized_toilet.use_toilet(sailor2)
    optimized_toilet.check_status()

# Simulate the scenario
simulate_toilet_usage()
