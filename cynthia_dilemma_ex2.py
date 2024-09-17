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

# Degree of Freedom 1: Urinos (Basic flushing, P-like)
class UrinosToilet(Toilet):
    def flush(self):
        print("Urinos flushing toilet...")
        time.sleep(1)
        self.state = "Flushing"
        self.water_level -= 10  # Basic water usage
        self.toilet_paper -= 5  # Basic TP usage
        time.sleep(1)
        self.state = "Idle"
        print("Toilet flushed and reset.")

# Degree of Freedom 2: Skatos (TP constraint, P + TP)
class SkatosToilet(Toilet):
    def flush(self):
        print("Skatos flushing toilet with TP constraint...")
        if self.toilet_paper <= 0:
            print("No toilet paper left!")
            return False
        time.sleep(1)
        self.water_level -= 10
        self.toilet_paper -= 5
        time.sleep(1)
        self.state = "Idle"
        print("Toilet flushed and TP used.")

# Degree of Freedom 3: Cynthos (P + TP + Friend constraint)
class CynthosToilet(SkatosToilet):
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

# Degree of Freedom 4: Feathers (P + TP + Friend + Weight constraint, NP-like)
class FeathersToilet(CynthosToilet):
    def __init__(self):
        super().__init__()
        self.weight_capacity = 150  # Weight limit in kg

    def use_toilet(self, user):
        if user.weight > self.weight_capacity:
            print(f"{user.name} exceeds the toilet's weight capacity!")
            return False
        super().use_toilet(user)

# Degree of Freedom 5: Anchors (Impossible, unsolvable)
class AnchorsToilet(FeathersToilet):
    def use_toilet(self, user):
        print(f"{user.name} tries to use the toilet, but...")
        print("This problem is computationally impossible (Anchors level), cannot compute!")
        return False

# Sailor (User) Classes
class Sailor(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def use(self):
        pass

# Sailor using Urinos-level toilet (P level)
class UrinosSailor(Sailor):
    def use(self):
        print(f"{self.name} is using the Urinos-level toilet.")
        time.sleep(1)
        print(f"{self.name} is done.")

# Sailor using Skatos-level toilet (P + TP)
class SkatosSailor(Sailor):
    def use(self):
        print(f"{self.name} is using the Skatos-level toilet with TP.")
        time.sleep(1)
        print(f"{self.name} is done.")

# Sailor using Cynthos-level toilet (P + TP + Friend)
class CynthosSailor(Sailor):
    def use(self):
        print(f"{self.name} is using the Cynthos-level toilet, checking for friends.")
        time.sleep(1)
        print(f"{self.name} is done.")

# Sailor using Feathers-level toilet (P + TP + Friend + Weight)
class FeathersSailor(Sailor):
    def use(self):
        print(f"{self.name} is using the Feathers-level toilet, considering weight class.")
        time.sleep(1)
        print(f"{self.name} is done.")

# Sailor encountering Anchors-level toilet (Impossible task)
class AnchorsSailor(Sailor):
    def use(self):
        print(f"{self.name} attempts an impossible task at the Anchors level.")
        time.sleep(1)
        print(f"{self.name} is stuck in the computational abyss...")

# Example Simulation
def simulate_toilet_usage():
    # Toilet objects for different levels of complexity
    urinos_toilet = UrinosToilet()
    skatos_toilet = SkatosToilet()
    cynthos_toilet = CynthosToilet()
    feathers_toilet = FeathersToilet()
    anchors_toilet = AnchorsToilet()

    # Sailor objects for different complexity levels
    sailor1 = UrinosSailor("Sailor1", 70)
    sailor2 = SkatosSailor("Sailor2", 75)
    sailor3 = CynthosSailor("Sailor3", 80)
    sailor4 = FeathersSailor("Sailor4", 160)  # Exceeds weight class
    sailor5 = AnchorsSailor("Sailor5", 90)  # Impossible task

    # Assign friends for Cynthos-level toilet
    cynthos_toilet.assign_friend(sailor3.name, sailor1.name)

    # Urinos-level toilet usage (P)
    print("\n--- Urinos-Level (P) ---")
    urinos_toilet.use_toilet(sailor1)
    urinos_toilet.check_status()

    # Skatos-level toilet usage (P + TP)
    print("\n--- Skatos-Level (P + TP) ---")
    skatos_toilet.use_toilet(sailor2)
    skatos_toilet.check_status()

    # Cynthos-level toilet usage (P + TP + Friend)
    print("\n--- Cynthos-Level (P + TP + Friend) ---")
    cynthos_toilet.use_toilet(sailor3)
    cynthos_toilet.check_status()

    # Feathers-level toilet usage (NP-like, weight constraint)
    print("\n--- Feathers-Level (NP-like, Weight Constraint) ---")
    feathers_toilet.use_toilet(sailor4)  # Should fail due to weight
    feathers_toilet.check_status()

    # Anchors-level toilet usage (Impossible task)
    print("\n--- Anchors-Level (Impossible Task) ---")
    anchors_toilet.use_toilet(sailor5)  # Impossible task
    anchors_toilet.check_status()

# Simulate the scenario
simulate_toilet_usage()
