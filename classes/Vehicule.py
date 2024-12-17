import random
from dataclasses import dataclass
import datetime

@dataclass
class Vehicule:
    """
    Classe représentant un véhicule.
    """
    immatriculation: str
    type: str  # "voiture", "moto", etc.
    is_parked: bool = False
    entry_time: datetime = None

    @staticmethod
    def create_random_vehicule():
        immatriculation = f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}-{random.randint(100,999)}-{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
        type = random.choice(["voiture", "moto", "camion"])
        return Vehicule(immatriculation, type)
