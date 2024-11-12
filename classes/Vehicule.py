import random

class Vehicule:
    def __init__(self, immatriculation, type, is_parked=False):
        self.immatriculation = immatriculation
        self.type = type  # "voiture", "moto", etc.
        self.is_parked = is_parked
        self.entry_time = None

    @staticmethod
    def create_random_vehicule():
        immatriculation = f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}-{random.randint(100,999)}-{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
        type = random.choice(["voiture", "moto", "camion"])
        return Vehicule(immatriculation, type)
